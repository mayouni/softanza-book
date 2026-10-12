---
id: the-engine-beneath
part: 5
number: 27
title: "Le moteur sous-jacent : trois couches, un moteur, Haro"
spine: false
narrations: [stz-engine-senses-narration.md, stz-vs-qt-unicode-narration.md, stz-emulating-the-whole-solution-narration.md, stz-honest-stopwatch-narration.md]
site: [architecture]
guards: [engine_is_optimised_narrated, engine_senses_narrated, wasm_narrated, threat_model_narrated]
stage:
  built: "trois couches choisies par le fichier d'entrée qu'on charge, chacune incluant celle du dessous et aucune celle du dessus ; la règle de dépendance tenue aux chargements ; un moteur de quatre-vingt-neuf bibliothèques, en Zig, construit en mode optimisé sûr, avec le propre décompte du moteur de ce qu'il expose ; Haro comme charte ratifiée et un spike dont les tribunaux tournent sur le nouveau runtime et sur l'ancien"
  designed: "la couche base héritant de la couche noyau ; la couche max comme couche construite ; un tribunal qui vérifie les couches contre leur contrat ; une couche choisie par une déclaration que le compilateur honore ; les autres faces de Haro sur un même graphe de programme ; un chargeur pour un domaine de la base ; le dépôt autonome du moteur et sa ligne de commande ; le pont polyglotte du moteur, qui est celui du chapitre 16"
  absent: "une couche noyau légère qui exécute ses chaînes ; un moteur Linux ou macOS en service ; une passe mesurée de la bibliothèque sur le nouveau runtime sous Linux ; un exécutable `haro` ; Haro exécutant la bibliothèque ; un exécutable unique sans dépendance ; un décompte de tests du moteur que je puisse imprimer"
status: draft
rulings: ["12.10", "12.11", "12.15", "12.21", "12.28", "12.29"]
research: research/ch27.md
---

Dans ce chapitre, je charge les trois couches de la bibliothèque, un fichier d'entrée à la fois, et je compte ce que chacune contient. Je lis le moteur en dessous, ses quatre-vingt-neuf bibliothèques et les fonctions qu'il enregistre, et je laisse le tribunal dire s'il est optimisé. Je pose les décisions, que l'avenir est Haro et que chaque fonctionnalité est implémentée une fois, dans le moteur, et j'imprime les lignes où un pair rapide est encore en tête. Le principe tient au-dessus de tout cela : la surface est la promesse, et le runtime est la partie qu'on mesure, et qu'on n'affirme jamais.

## 1. Le concept, tel que le terrain le tient

Une plateforme dans une seule base de code se dessine comme une pile avec une seule règle : une couche interne ne sait rien d'une couche externe. Le pair le plus net, dans les mots de l'étude, est celui des trois crates de Rust pour trois profondeurs d'hôte, choisies par la cible. (Connaissance générale pour le terrain : Rust impose la règle par son compilateur.) Softanza le tient par des fichiers d'entrée, et la section 7 dit ce que cela coûte.

L'habitude du terrain pour un moteur est une bibliothèque native avec une interface C simple, enveloppée finement par chaque langage. SQLite est l'exemple courant : une bibliothèque C, des liaisons dans presque tous les langages. Le dossier énonce la même conception pour son moteur : les clients de langage sont de fins ponts qui ajoutent syntaxe et paradigmes, et jamais de calcul. (Connaissance générale pour le terrain, bien établie.)

Et le terrain a fait, à plusieurs reprises, une troisième chose : un langage garde sa surface et ses bibliothèques et change la machine en dessous. L'exemple propre du dossier est un descendant typé de Lua. Un autre est l'implémentation alternative de Python. (Connaissance générale pour le terrain, bien établie.) Les deux enseignent la même chose que le dossier enseigne : la surface est la promesse, et le runtime est la partie qu'il faut mesurer.

## 2. Le premier principe

**Chaque fonctionnalité est implémentée une fois, dans le moteur. La surface est la promesse, et le runtime est la partie qu'on mesure, et qu'on n'affirme jamais.**

La première phrase est la règle de conception de l'architecture du moteur, dans un document de session : chaque fonctionnalité est implémentée une fois, dans le moteur. Les clients de langage sont de fins ponts qui ajoutent syntaxe et paradigmes, jamais de calcul. Le chapitre 4 a raconté la décision de l'auteur qui en découle, que j'ai refusé le calcul dans les faces. La seconde phrase est le cahier des charges du runtime en dessous : performance et portabilité, mesurées, jamais affirmées.

Et la définition qui gouverne les dépendances du moteur, que le chapitre 4 énonce déjà : la souveraineté est de n'avoir rien qu'un autre puisse retirer. Dans les mots de la vision, elle n'a jamais voulu dire que chaque ligne est de nous.

## 3. La forme Softanza

Trois affirmations, et un bloc pour chacune de ce qu'un bloc peut prouver. Je vous dis d'abord ce qu'un bloc ne peut pas prouver, parce que cela compte. La règle de dépendance des couches, qu'aucun fichier noyau ne charge base et qu'aucun fichier base ne charge max, demande un balayage d'environ huit cent soixante-dix lignes de chargement. Seule une garde pourrait le porter, et il n'en existe aucune. J'ai fait le balayage avec un script à moi, et la section 7 en donne le résultat.

### Une couche est le fichier qu'on charge

Combien de classes chaque fichier d'entrée charge-t-il ? Trois fichiers d'entrée, trois processus neufs. Chacun imprime combien de classes il contient, et si `stkList`, `stzList` et `stzListXT` existent. Le bloc lance des processus enfants, parce que le processus de ce chapitre a déjà chargé la plus grande couche, et que seul un enfant peut montrer le noyau seul :

```haro
cAsk = 'aC = ringvm_classesList()' + nl +
       '? "" + len(aC) + " " + (find(aC, "stklist", 1) > 0) + " " + (find(aC, "stzlist", 1) > 0) + " " + (find(aC, "stzlistxt", 1) > 0)' + nl
aEntries = [ "core/stkLib.ring", "stzLib.ring", "max/stxLib.ring" ]
for i = 1 to 3
    write("layer" + i + ".ring", 'load "../../../' + aEntries[i] + '"' + nl + cAsk)
    ? trim(systemcmd("ring layer" + i + ".ring"))
    remove("layer" + i + ".ring")
next
#--> 17 1 0 0
#--> 674 1 1 0
#--> 714 1 1 1
```

Le noyau contient 17 classes, dix au préfixe `stk` et sept à `stzCore`, et aucune classe de base. La base en contient 674 et aucune classe max. Max en contient 714. Chaque couche inclut celle du dessous et aucune celle du dessus : noyau dans base dans max, chargées par le bas. Un chargement du seul fichier d'entrée du noyau prend environ un dixième de seconde sur cette machine, et un chargement de la base prend entre trois et huit secondes, en exécutions uniques le 9 octobre 2026. Mes notes consignent ces temps, et aucun bloc ne les montre.

Le contrat dit que la base s'appuie sur le noyau, par héritage ou par délégation. Que disent les classes ? `ringvm_classesList()` renvoie, pour chaque classe, son nom, son identifiant et son parent :

```haro
aClasses = ringvm_classesList()
? ParentOf("stkString")
#--> stzcorestring
? ParentOf("stzString")
#--> stzobject
? ParentOf("stzList")
#--> stzobject
? ParentOf("stzListXT")
#--> stzlist

func ParentOf(cClass)
    n = find(aClasses, lower(cClass), 1)
    if n = 0  return "(not loaded)" ok
    return aClasses[n][3]
```

`stzString` hérite de `stzObject`, et non de `stkString` ! Le noyau porte une hiérarchie parallèle, dans laquelle `stkString` hérite de `stzCoreString`. Max s'appuie bien sur la base : `stzListXT` hérite de `stzList`. Exactement deux classes de la base héritent d'une classe du noyau, `stzSciNumber` et `stzPointer`, et une délègue, dans une ligne de `stzPointer`. Ce sont deux sur environ six cent soixante-dix-sept. Le contrat n'est pas rempli, et il ne l'est pas de la manière dont le chapitre 4 posait la question. Je l'imprime comme une dette.

Et la troisième couche par son préfixe. Dans le processus de la plus grande couche, combien de classes commencent par `stk`, combien par `stz`, et combien par `stx` ?

```haro
nStk = 0  nStz = 0  nStx = 0
aClasses = ringvm_classesList()
for aClass in aClasses
    cPrefix = left(aClass[1], 3)
    if cPrefix = "stk"  nStk++
    but cPrefix = "stz"  nStz++
    but cPrefix = "stx"  nStx++
    ok
next
? @@([ nStk, nStz, nStx ])
#--> [ 10, 693, 0 ]
```

Dix, six cent quatre-vingt-treize, et aucune. Les quarante classes que max ajoute à la base portent toutes le préfixe de la base. Les trente-deux classes au troisième préfixe existent, toutes dans un seul répertoire, et aucun fichier d'entrée ne les charge. La section 7 le redit.

### Un moteur

Les couches sont réelles au niveau du binaire. Le fichier de construction déclare les domaines du noyau et les domaines de la base et construit une bibliothèque par domaine, dans une boucle. Ce bloc lit ce fichier, et l'affirmation porte sur ce fichier :

```haro
$cEngineDir = "../../../engine"
cBuild = read($cEngineDir + "/build.zig")
n1 = substr(cBuild, "const core_domains")
n2 = substr(cBuild, "const base_domains")
n3 = substr(cBuild, "fn addSpeech")
? Q(substr(cBuild, n1, n2 - n1)).NumberOfOccurrence('.name = "stk_')
#--> 4
? Q(substr(cBuild, n2, n3 - n2)).NumberOfOccurrence('.name = "stz_')
#--> 85
? Q(cBuild).NumberOfOccurrence('stx_')
#--> 0
```

Quatre bibliothèques noyau, quatre-vingt-cinq bibliothèques base, et aucune bibliothèque pour la troisième couche : quatre-vingt-neuf en tout. Le repère `fn addSpeech` est la première fonction après les deux tables, une frontière en texte brut, arbitraire mais visible. Un tribunal des couches ferait une analyse correcte, et je le range parmi les demandes. L'étude dit quatre-vingt-six domaines de base à ce commit et j'en lis quatre-vingt-cinq.

Le moteur dit à la bibliothèque ce qu'il est. Sa version est une constante. Combien de fonctions distinctes enregistre-t-il dans la machine virtuelle une fois chargé ?

```haro
? StzEngineEmbedVersionString()
#--> 0.8.0
aAll = ringvm_cfunctionslist()
aNames = []
for cName in aAll
    if left(lower(cName), 9) = "stzengine"  aNames + lower(cName)  ok
next
? len( Q(aNames).DuplicatesRemoved() )
#--> 2786
```

Deux mille sept cent quatre-vingt-six fonctions distinctes du moteur, la vue propre de la bibliothèque, prise à l'exécution. Le même appel renvoie plus d'entrées, puisque celles de la machine virtuelle elle-même sont incluses, et plusieurs noms apparaissent plus d'une fois ; je n'ai pas cherché pourquoi. J'ai d'abord assigné la liste à une variable, parce que l'appel est réévalué à chaque tour d'une boucle, et j'ai arrêté deux exécutions qui avaient grossi jusqu'à des gigaoctets avant que je l'apprenne. Le décompte bouge avec le moteur construit.

Il y a trois décomptes de trois choses différentes, et le chapitre dit lequel il imprime. Le premier est le décompte vu de la bibliothèque à l'exécution : les 2 786 ci-dessus. Le deuxième est le décompte vu de n'importe quel hôte par l'interface C. Un script à moi a lu les tables d'export des quatre-vingt-neuf bibliothèques le 9 octobre 2026 et y a trouvé 1 710 symboles nommés, dont quatre-vingt-neuf sont le crochet du chargeur, donc 1 621 fonctions. Le troisième est le décompte dans les sources Zig, comme noms d'enregistrement : 2 703 littéraux distincts. Le site dit 752 et 2 652, au commit 010743cce tel que la page le lit au 9 octobre 2026, et les constantes typées de la bibliothèque disent 1 513, datées du 16 juin 2026. Je ne peux reproduire 752 par aucune méthode que j'ai essayée. N'imprimez qu'un décompte que la construction lit, avec sa méthode et sa date.

**Le moteur fait le travail.** Que fait le `upper` de l'hôte de l'eszett allemand, et qu'en fait la mise en correspondance de casse du moteur, sa propre table au-dessus d'une bibliothèque embarquée ? Une seconde bibliothèque embarquée extrait les radicaux des mots. Ce sont deux des dix-neuf :

```haro
? upper("Straße")
#--> STRAßE
? Q("Straße").Uppercased()
#--> STRASSE
? @@( Q("running runs ran").StemmedWords() )
#--> [ "run", "run", "ran" ]
```

L'hôte laisse l'eszett tranquille, et le moteur écrit SS ! La première ligne montre le comportement de l'hôte. Si le `upper` de Haro devient du Unicode complet, la promesse change.

Et le moteur est optimisé. Le mode par défaut de la construction est optimisé et sûr, depuis le commit 1fdc2eda5, que le journal git de la bibliothèque date du 26 juillet 2026. Les fichiers épinglés portent le commit et non la date. Jusque-là, chaque bibliothèque que la bibliothèque avait jamais chargée était compilée sans aucune optimisation, et cela clôt la question que le chapitre 22 avait laissée ouverte sur le mode de construction. Une garde lit le temps, puisqu'elle ne peut pas lire un drapeau. Vingt sommes sur deux millions de doubles qui vivent dans le moteur doivent finir en moins d'un dixième de seconde, et être justes :

```haro
oBuf = StzNumBufferOfSizeQ(2000000)
oBuf.RangeFrom(1, 1)
nT0 = clock()
for k = 1 to 20
    nSum = oBuf.Sum()
next
? (clock() - nT0) / clockspersecond() < 0.10
#--> 1
? nSum
#--> 2000001000000
oBuf.Free()
```

Le bloc n'imprime que le booléen, parce qu'un temps n'est pas une promesse. Sur trois exécutions les 8 et 9 octobre 2026, les temps écoulés ont été de 0,02, 0,04 et 0,03 seconde, tirés de mes notes et absents du relevé d'exécution. La table propre de la garde dit 0,14 pour le mode non optimisé et 0,04 pour l'optimisé. La garde elle-même a tourné le 8 octobre : sept assertions dans le fichier, six atteintes ici, six réussies ; la septième est sur une branche else qu'on n'atteint pas quand l'analyseur est construit.

### Ce qui l'exécute

Le runtime sous chaque bloc de ce livre est l'ancien langage hôte, version 1.27, l'oracle contre lequel le nouveau runtime est jugé. Haro n'exécute pas la bibliothèque :

```haro
? version()
#--> 1.27
```

Sous un futur runtime la promesse change, comme la ligne de preuve le dit.

## 4. La décision, et ce que j'ai refusé

**J'ai décidé que l'avenir est Haro, et non l'ancien langage hôte.** Mes mots du 7 octobre 2026, dans la citation de l'étude, les crochets de moi : l'avenir est Haro, pas [l'ancien langage], et le site doit être clair là-dessus. La face de Haro pour l'ancien langage ne sera maintenue que pour que le code déjà écrit continue de fonctionner. Ce qui n'est pas porté, c'est le runtime de ce langage et sa gouvernance. La première décision, le 28 août, était qu'il n'est pas porté du tout ; il a été remplacé deux jours après, comme l'amendement de la vision le dit.

**J'ai décidé que la réécriture est un renommage.** Le code des articles, au nom de Haro, est le même que la face de l'ancien langage. La charte le mesure de même : les étapes propres de Haro exécutent le même texte, identique à l'octet sur le nouveau compilateur et sur l'oracle.

**J'ai décidé que Haro est le langage des langages.** L'en-tête de la charte cite ma note du 1er octobre 2026. La charte a été ratifiée ce jour-là, avec mon « go with your recommendations » sur sept décisions. Ses amendements du 4 octobre répondent à dix-neuf des questions du compas, et la version reste ratifiée jusqu'à ce que j'aie lu sa section 15.

**J'ai décidé que la surface est conservée.** Sa surface aujourd'hui est celle que le compilateur compile. La bibliothèque est sa spécification de compatibilité. Les autres surfaces sont des faces sur un même graphe de programme : chaque syntaxe est une face, pour qu'un agent à l'aise avec l'ancien langage, avec Python ou avec JavaScript écrive du Haro. Parmi elles seule la première face existe. Une face en forme de Python est une orthographe, pas du Python.

**J'ai retiré l'ancien cadre, sans repli.** Moteur seul : pas de repli, pas de drapeaux de fonctionnalité, pas de dépendance à Qt. Le statut du 12 juin 2026 dit qu'il n'en reste aucun. J'ai vérifié : aucun fichier chargé ne charge une bibliothèque Qt, et deux extensions externes sont chargées par leur nom : une extension zip, que la base charge, et une de cryptographie, dans un répertoire qu'aucun fichier d'entrée ne charge.

**J'ai ordonné le retrait des extensions propres du langage.** Ma directive du 13 juin 2026 : s'assurer qu'aucune extension externe n'est requise, et que des alternatives du moteur les remplacent. La bibliothèque en charge encore une, une extension zip, comme l'entrée ci-dessus le dit.

**J'ai mis le moteur en Zig, sans dépendance à une bibliothèque,** comme l'étude rapporte ma demande. C'est qualifié par la définition de la souveraineté du dossier lui-même : dix-neuf bibliothèques embarquées, chacune avec un enregistrement.

**J'ai laissé tout aller dans base.** Ma phrase, comme l'étude la rapporte : sous la pression du temps, tout est allé dans base, en attendant le bon moment pour refactoriser à nouveau. D'après mon décompte plus bas, base représente quatre-vingt-treize pour cent des lignes.

**J'ai choisi l'optimisation sûre.** Ni le mode le plus rapide, ni le non optimisé. Je tiens pour une vue, non pour un résultat, qu'une panique propre vaut mieux qu'une corruption silencieuse de la mémoire, et qu'ici cela ne coûte rien.

**J'ai refusé une affirmation phare qui ne se reproduit pas.** Le mémo du 13 septembre 2026 dit que l'affirmation à retirer est que le runtime bat le pair rapide, au présent, sur x64. Le chapitre 22 a raconté le refus, et la section 6 imprime les lignes.

**J'ai refusé un pourcentage.** Le chiffre est de moi, et il ne devrait pas être imprimé sans la garde qui le produit. Les chapitres 31 et 33 le disent.

**Je n'ai aucune phrase sur la façon dont une couche est choisie en Haro.** L'étude propose seulement qu'en Haro, le choix de la couche soit une déclaration que le compilateur honore. La charte n'a aucun texte sur noyau, base et max. La base héritant du noyau est le contrat tel que conçu, avec le mot d'étape conçu. Le code ne le respecte pas aujourd'hui, comme l'imprime la section 3, et le compte rendu du livre est ce que fait le code : deux implémentations sur un seul moteur. Et en Haro, une couche est choisie aujourd'hui par le fichier qu'on charge. Une déclaration que le compilateur honore est la proposition de l'étude, et elle est conçue.

## 5. Le tribunal

`engine_is_optimised_narrated` prouve que le moteur est compilé avec optimisation : vingt sommes sur deux millions de doubles en moins d'un dixième de seconde, et la bonne réponse. Elle prouve qu'un indice de 99 et un indice de 0 sont refusés et le tampon intact, et que l'analyseur embarqué que le mode optimisé avait cassé répond maintenant. Je l'ai exécutée : six des sept assertions du fichier ont été atteintes, et six ont réussi. `engine_senses_narrated` prouve que le moteur donne au processus cinq sens : la mémoire, son pic, la mémoire du système, le temps du processeur, et une série bornée. Je l'ai exécutée : trente-six sur trente-six, et l'exécution s'arrête ensuite avec "STOPPED!" par conception. `wasm_narrated` prouve que l'entrée du moteur pour le navigateur exporte son interface choisie et que la construction a une cible pour elle, et elle construit un sous-ensemble et affirme qu'il est plus petit. Je ne l'ai pas exécutée, parce qu'elle appelle une construction de la chaîne d'outils. `threat_model_narrated` lit le modèle de menaces et vérifie que chaque ligne de garantie nomme une preuve et que chaque fichier de garde nommé existe. Les lignes G11, les harnais de fuzzing, et G25, la nomenclature de composants avec ses empreintes, concernent le moteur.

Ce qui n'existe pas : **aucune garde ne juge les couches.** Aucun fichier sous les répertoires de test ne charge le fichier d'entrée d'une couche ni ne lit le contrat. Il y a 529 gardes narrées dans base, et aucune dans noyau ou dans max. L'étude dit 517 à un endroit et 387 à un autre, et le site 501 ; je n'imprime que ce que la construction lit. Et aucune garde ne juge les décomptes du moteur : les nombres qu'imprime la commande d'état en ligne de commande du moteur sont des constantes typées datées du 16 juin 2026.

## 6. Le terrain, et où il mène

**La vitesse.** Le runtime en dessous contre un runtime de script rapide du terrain, le 13 septembre 2026. La méthode est celle du mémo : six paires de noyaux de calcul écrits à neuf, même algorithme et mêmes tailles des deux côtés, chaque côté dans son idiome rapide, sommes de contrôle entre langages vérifiées avant tout nombre. Les minima sont pris sur trois répétitions internes et deux exécutions de processus, le nouveau compilateur construit pour la vitesse, le pair en interpréteur seul sans JIT, sous Windows, x64. Le pair est en tête sur chaque ligne :

| ligne | le runtime en dessous (min ms) | le pair (min ms) | le pair est en tête de |
|---|---:|---:|---:|
| sieve | 128 | 74,5 | 1,72 |
| matmul | 349 | 185,6 | 1,88 |
| fib | 57 | 50,2 | 1,14 |
| mergesort | 376 | 206,7 | 1,82 |
| binsearch | 536 | 513,1 | 1,04 |
| bytescan | 53 | 37,5 | 1,41 |

Les mots du mémo : le pair est en tête sur chaque ligne, fib et binsearch sont des quasi-égalités, et rien n'est pire que 2x. ARM n'est pas mesuré. La victoire que le mémo garde : à moins de 2x sur chaque ligne, ce qu'aucune version de l'ancien runtime n'a jamais été.

**L'affirmation phare est encore vivante dans les notes propres du dépôt.** Comme je l'ai lu le 9 octobre 2026, le cahier des charges du dépôt propre du runtime et ses notes disent encore que le spike bat les pairs sur chaque ligne. La correction est portée dans un autre dépôt du domaine de projets et dans le mémo, et, dans le dossier propre du runtime, seulement pour sa configuration de version candidate, dans une section des notes. Le mémo l'a demandée. Le mémo du 13 septembre 2026 retire l'affirmation, et les six lignes ci-dessus sont les siennes, bien que les notes du dépôt portent encore l'ancienne affirmation. Je ne nomme aucun pair, et je le décris comme le fait le chapitre 22 : un runtime de script rapide du terrain.

**La mémoire.** Le même jour la note dit : résidente, exécutant la bibliothèque, ce matin 733 mégaoctets, maintenant 149, et l'ancien runtime 139. Une perte de dix contre l'ancien runtime, après une chute de 584. Une victoire et une perte dans une même note.

**La compatibilité, le 5 octobre 2026.** La suite large de la bibliothèque a été exécutée sur un instantané. La note consigne la parité des assertions sur chacune de celles que l'ancien runtime passe, que la plupart des programmes s'accordent sur chaque ligne stable, et que dix-neuf lignes diffèrent par nature. La note ne dit pas Windows dans cette entrée, et la passe Linux est listée comme prochaine étape. Ce sont des notes de session d'une branche privée, et aucun nombre de moi. Je les imprime, datés du 5 octobre 2026, avec le mot d'étape en construction : 8 540 assertions sur 8 540 à parité, 1 253 tests sur 1 253 qui portent des assertions, et 3 425 programmes sur 5 112 identiques sur chaque ligne stable. Il y en a 1 267 de plus, identiques sauf sur la ligne qui imprime le temps écoulé, et 19 lignes diffèrent par nature : 13 impriment davantage, 5 sont refusées ou lèvent une erreur, une écrit une ligne sur la sortie d'erreur. Ce sont les décomptes de la note, et je n'en ai exécuté aucun.

**La plateforme.** Construite et exécutée sous Windows aujourd'hui. Une construction Linux de quatre-vingt-cinq des quatre-vingt-neuf modules existe sur une branche de travail ; le site dit qu'elle est en construction. Un programme entier avec son moteur dans un seul fichier, sans dépendance, est absent.

**Le moteur contre le terrain.** La ligne du modèle de menaces pour le fuzzing le dit elle-même : pas de fuzzing planifié ni guidé par la couverture, pas d'intégration continue et des commits non signés, différés par l'auteur pour la phase de développement. Les bibliothèques natives maintenues du terrain ont du fuzzing continu et des versions signées. Et la perte du chapitre 22, inchangée : pas de collation par locale, et pas de fuseaux horaires.

## 7. La limite

**La couche légère ne tourne pas.** La classe chaîne du noyau appelle des noms de moteur qu'aucune bibliothèque du moteur n'enregistre :

```haro
o = new stkString("abc")
? o.Content()
#--> Error (R3) : Calling Function without definition: stkenginestringfrom
```

Le runtime répond : `Error (R3) : Calling Function without definition: stkenginestringfrom`. Dans un processus du noyau seul, la bibliothèque noyau du moteur enregistre cinq cent trente-quatre fonctions sous les noms de la base et aucune sous les noms du noyau, un décompte de mes notes qu'aucun bloc ne montre. Donc `stkString` et `stkChar` ne trouvent rien. L'étude le range comme point ouvert du noyau et du moteur. `stkList` tourne, ce que le chapitre 4 a montré, et le chargement de dix-sept classes en un dixième de seconde est réel.

**La couche légère n'est pas légère au niveau du binaire, pour les chaînes.** Par taille de fichier, sur la construction du 5 octobre 2026, la bibliothèque chaîne du noyau fait 22 355 968 octets et celle de la base 22 362 624. Les données en lecture seule font 20,8 mégaoctets dans les deux ; je n'ai pas diagnostiqué ce qu'elles contiennent. Les quatre bibliothèques noyau totalisent 24,1 mégaoctets sur les 122,4 des quatre-vingt-neuf bibliothèques. Les bibliothèques noyau pour les dates, les fichiers et la locale diffèrent de leurs jumeaux de la base de moins d'un pour cent.

**La règle de dépendance tient aux chargements, avec une exception à un appel.** J'ai analysé chaque chargement de chaque fichier non test, non archive du noyau, de la base et de max, 871 lignes, et résolu chacun. Le noyau ne charge, hors de son propre répertoire, que la face du moteur ; la base charge le noyau et le moteur ; aucun fichier sous la base ne charge quoi que ce soit sous max ou future ; max charge la base. Mais `FindMin`, dans la liste de nombres du noyau, appelle une fonction qui n'est définie que dans la base. Dans un processus du noyau seul, `FindMin([4,2,9])` répond 2, et `FindMin("not a list")` lève "Calling Function without definition". Dans un processus de base il lève l'erreur voulue. J'ai trouvé une instance par une recherche de noms de la base dans le noyau, et je n'ai pas cherché d'autres.

**Sur un disque sensible à la casse, le fichier d'entrée du noyau ne charge pas.** Sa deuxième ligne charge un fichier par un nom dans la mauvaise casse. Mon balayage trouve vingt tels chargements dans des fichiers non test à ce commit ; la session du runtime en a compté cinquante-cinq avec les tests, le 8 octobre 2026. Le livre est construit sous Windows, qui le cache.

**La troisième couche est écrite et non câblée.** Ses trente-deux classes sont toutes dans un seul répertoire, et aucun fichier d'entrée ne les charge. La première d'entre elles fonctionne chargée à la main ; je l'ai exécuté et je ne le montre pas, une chaîne de onze caractères comptée par elle, et je n'ai essayé aucune des trente et une autres. Une couche de bibliothèque pour elles dans le moteur n'existe pas.

Ce qui est construit : une couche est un répertoire, un préfixe et un fichier d'entrée. J'ai compté le 9 octobre 2026 à ce commit, par fichiers avec l'extension, en excluant les répertoires de test et d'archive. Noyau, 27 fichiers et 6 366 lignes ; base, 984 fichiers et 519 579 ; max, 115 et 31 292 ; et un répertoire de l'avenir, 51 fichiers et 6 356. La base représente 93,2 pour cent des lignes des trois couches. Le moteur : quatre-vingt-neuf bibliothèques issues des sources Zig, 401 fichiers source, 179 985 lignes, et 2 464 tests déclarés, que je n'ai pas exécutés. La chaîne d'outils est Zig 0.15.2 d'après le propre commentaire du fichier de construction. Dix-neuf bibliothèques embarquées, chacune avec un enregistrement de composant, version, source, licence et empreinte. Les lacunes propres du dossier : une empreinte d'archive est consignée pour neuf des dix-neuf, et trois n'ont pas de version.

Ce qui est conçu : la couche base héritant de la couche noyau. Les sept domaines partagés sont implémentés deux fois sur le même moteur. Max comme couche construite. Un chargeur pour un domaine de la base. Un tribunal qui vérifie les couches contre leur contrat. Le dépôt autonome du moteur et sa ligne de commande, que l'architecture liste comme une phase. Le pont polyglotte du moteur, qui est celui du chapitre 16.

Ce qui est absent : un moteur Linux et macOS en service ; une passe mesurée de la bibliothèque sur le nouveau runtime sous Linux ; un exécutable unique sans dépendance ; un décompte de tests du moteur que je puisse imprimer.

### Haro

Je dis ce qui est construit, ce qui est conçu, et ce qui est absent, tel que le dossier l'a au 9 octobre 2026.

**Construit, comme une charte, une famille de grammaires et une garde.** La charte, version 0.2, ratifiée le 1er octobre 2026. Un spike de dix-neuf échelons, entre le 1er et le 4 octobre, chacun un document de grammaire avec des fixtures. Sa garde a rapporté un succès de l'exécution entière le 5 octobre, et ses tribunaux sont des programmes qui tournent à l'identique à l'octet sur le nouveau compilateur et sur l'ancien runtime officiel. Le nouveau compilateur met aussi en forme et exporte les fichiers de la bibliothèque : sur environ six mille, presque tous impriment les octets de la référence, et quelques dizaines sont refusés par les deux. Une première tranche d'un graphe du code a été construite le 5 octobre.

**Ce qu'est Haro aujourd'hui, en une phrase que le dossier soutient :** une charte ratifiée et un spike dont les tribunaux tournent sur le nouveau runtime et sur l'ancien, sur la surface dans laquelle la bibliothèque est écrite. Il n'y a pas d'exécutable `haro`. Le répertoire des binaires contient le compilateur et deux autres. Les tribunaux forgés ne chargent aucune bibliothèque. **Haro n'exécute pas la bibliothèque.** La vision du 27 septembre disait que Haro n'existe pas et que la ligne Linux du nouveau runtime n'est pas mesurée. La première moitié est périmée, puisqu'une charte et un spike existent. La seconde moitié reste vraie de la suite large sous Linux.

**Conçu :** les trois altitudes, déclarant, déclaré, et calculant ; l'alphabet de six lettres, cinq forgées entières dans le spike ; le raffinement comme surface d'écriture ; d'autres faces sur un même graphe de programme. Ces faces arrivent comme imprimeurs avant d'arriver comme analyseurs, et jamais comme sémantique. Les verbes `haro forge`, `check`, `refine`, `run`, `project` et `narrate` sont une recommandation, et non un programme.

**Le runtime en dessous, tel que le dossier le date.** Son cahier des charges : une machine à registres et un compilateur du source de l'ancien langage vers son bytecode, exécutant les programmes existants. Environ trois cent mille lignes de Softanza sont sa spécification de compatibilité. Sa face publique : la branche principale est publique et intacte ; le travail vit sur une branche poussée vers un dépôt distant privé seulement. Son dernier commit à ma lecture date du 8 octobre 2026, à 22 h 26. Le mot d'étape est de moi, et c'est « en construction ».

## 8. Six portes

**Le programmeur.** Vous choisissez votre profondeur par le fichier que vous chargez, et vous pouvez le prouver en trois processus neufs. La couche légère n'exécute pas ses chaînes aujourd'hui : prenez la base. Lisez le décompte du moteur comme la bibliothèque le voit, et non comme une page le tape.

**L'analyste.** Trois nombres pour « quelle est la taille du moteur », et trois méthodes. Demandez laquelle un fournisseur veut dire. La bibliothèque noyau a la taille de celle de la base pour les chaînes.

**Le concepteur.** Une couche est une décision sur ce que vous livrez, et non sur le goût. Au niveau du binaire, le noyau et la base ont une bibliothèque par domaine et la troisième couche n'en a aucune ; le sous-ensemble web, que les chapitres 4 et 24 montrent, est un sous-ensemble et non une couche.

**Le décideur.** Les deux questions du chapitre 4, plus deux. Ce qui l'exécute : la version 1.27 aujourd'hui, avec le remplaçant en construction. Ce que le remplaçant a perdu : chaque ligne contre un pair rapide, de 1,04 à 1,88 fois, et dix mégaoctets de mémoire face à l'ancien. C'est mon point de vue : un dossier qui imprime sa perte est le seul genre à croire.

**Le formateur.** Enseignez la règle de dépendance en faisant charger le noyau seul à l'apprenant et prédire, puis compter. Enseignez « mesuré, jamais affirmé » avec le mémo du 13 septembre 2026.

**L'agent.** Vous pouvez compter vous-même les fonctions du moteur. Ne répétez pas un décompte d'une page, et n'écrivez pas une boucle directement sur la liste des classes. Dites au lecteur dans quelle couche vit une classe par sa chaîne de parents, et non par son préfixe.

## 9. Exercice

Avant d'exécuter quoi que ce soit, écrivez trois nombres : combien de classes chaque fichier d'entrée chargera, et lesquelles de `stkList`, `stzList` et `stzListXT` chacun contient.

```haro exercise
# core/stkLib.ring, stzLib.ring, max/stxLib.ring: write your three predictions here,
# then load each entry in its own process and count with ringvm_classesList().
```

Puis choisissez n'importe quelle classe de la bibliothèque, prédisez son parent, et lisez-le avec la chaîne de parents. Écrivez la ligne que votre prédiction a ratée. Un apprenant qui devine que `stzString` hérite de `stkString` est en bonne compagnie : le contrat le dit, et la bibliothèque non. Je ne dis pas lequel des 17, 674 ou 714 est lequel.

Le chapitre suivant quitte le moteur pour un restaurant à Lyon, et pour la phrase que le projet y a enseignée : livrer petit, vite et utile, et laisser les fondations mûrir en parallèle sans jamais bloquer une livraison.
