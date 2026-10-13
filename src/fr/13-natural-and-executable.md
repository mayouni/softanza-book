---
id: natural-and-executable
part: 3
number: 13
title: "Naturel, et exécutable : deux directions, une seule discipline"
spine: false
narrations: [stznatural-vs-ring-naturallib.md, stz-near-natural-language-programming.md, stznatural-narration.md, stz-bridging-minds-and-code.md]
site: [natural]
guards: [nnl_narrated, multilingual_pack_narrated, semantic_resolver_narrated, question_narrated, literate_templates_narrated, truthchain_narrated, interrogative_narrated]
stage:
  built: "les deux directions : des chaînes où l'humain est l'analyseur, et des phrases où c'est la machine ; cinq paquets de langue comme données et un sixième ajouté à l'exécution ; des refus avec raisons des deux côtés ; des cadres de question ; une chaîne de vérité mince ; du code naturel comme données dans les documents et les gabarits"
  designed: "une grammaire qui tient un modèle au lexique ; une garde qui vérifie qu'aucun socket ne s'ouvre pendant une exécution naturelle ; le plan émis comme une chaîne ; les exemples des articles épinglés comme fixtures"
  absent: "toute machine qui juge la grammaire d'une chaîne ; l'ajami, le zarma et le peul ; une couche naturelle fermée jusqu'en bas ; un dictionnaire protégé de la dérive de la documentation dont il est lu ; les promesses des anciens articles, dont plusieurs ne tournent pas"
status: draft
rulings: ["12.2", "12.6", "12.27", "12.30"]
research: research/ch13.md
---

Dans ce chapitre, je fais tourner les deux directions du langage naturel dans la bibliothèque : la chaîne, où vous êtes l'analyseur, et la phrase, où c'est la bibliothèque. J'imprime les refus des deux côtés, cinq paquets de langue comme données et un sixième ajouté à l'exécution, et le compte de ce que chaque paquet sait dire. Je dis ce que j'ai refusé, les marqueurs de référence et la chaîne non grammaticale entre autres, et où le tribunal propre du dictionnaire échoue à ce commit. Le principe tient en une phrase. Une phrase s'exécute parce que chacun de ses mots est dans un dictionnaire que la bibliothèque possède, et ce que la bibliothèque ne connaît pas, elle le refuse, avec la raison.

## 1. Le concept, tel que le terrain le tient

Dans le langage courant du terrain, « programmer en langage naturel » veut dire une seule chose : demander du code à un modèle, ou lui demander de faire la tâche, dans un prompt. Les outils sont des assistants de discussion et des compléteurs de code, d'un usage large depuis 2021 environ. Ce sur quoi la phrase s'exécute, c'est la conjecture du modèle. La même phrase peut donner un code différent d'un jour à l'autre, le modèle a besoin d'un réseau ou d'un runtime local, et une personne lit le résultat pour savoir ce qui a été compris. Le chapitre 11 l'a dit, et j'y renvoie.

Des pratiques plus anciennes existent, et le dossier les nomme. Inform 7, un langage dont les programmes sont des phrases anglaises, compilées d'un bloc, avec un modèle du monde et un moyen de dire *il* d'une phrase à l'autre. AppleScript, proche de l'anglais et difficile à écrire, parce que sa naturalité était en surface et non dans un modèle sémantique. Les langages naturels contrôlés, dont le dispositif le plus fort, dit le commentaire de la bibliothèque elle-même, est de montrer ce qui peut être dit ensuite. Une lecture de session du 30 août 2026 est qu'Inform 7 est un compilateur de texte entier avec contexte référentiel, et non un répartiteur de commandes. (Connaissance générale pour les dates, pas une étude du dossier.)

Aucun d'eux n'est ce que le dossier revendique. La revendication est le contraire du prompt : une phrase s'exécute parce que chacun de ses mots est dans un lexique fermé, défini comme données, associé à un verbe que la bibliothèque documente. Tout le reste est refusé avec la raison. Et elle a deux directions, que la revue de conception de la bibliothèque met en tableau. Dans la première, la machine est l'analyseur. Dans la seconde, c'est l'humain.

## 2. Le premier principe

**Une phrase s'exécute parce que chacun de ses mots est dans un dictionnaire que la bibliothèque possède. Ce que la bibliothèque ne connaît pas, elle le refuse, avec la raison.**

La ligne de thèse de l'étude pour la page qu'elle a demandée, et le chapeau de la page du site du 8 octobre 2026, le disent. Pour la seconde direction, la thèse de la revue de conception : dans le langage quasi naturel, l'humain est l'analyseur. Et la devise plus ancienne, que le chapitre 5 porte : ce que vous pensez est ce que vous écrivez.

## 3. La forme Softanza

Je commence par la seconde direction, parce qu'elle est la plus ancienne.

### L'humain est l'analyseur

Une chaîne quasi naturelle est une phrase dont chaque maillon est un vrai appel. La phrase est « le mot haro est un mot latin en minuscules, d'une longueur de 4 lettres et avec seulement 2 voyelles ». Quand elle est fausse, que dit la chaîne ? Exécutez-la :

```haro
? TheWordQ("haro").IsAQ([ :Lowercase, :Latin, :Word ]).WithQ().ALengthQ().OfQ(4).UnitQ(:Letters).AndQ().OnlyQ(2).VowelNB()
#--> TRUE
? TheWordQ("haro").IsAQ([ :Lowercase, :Latin, :Word ]).WithQ().ALengthQ().OfQ(4).UnitQ(:Letters).AndQ().OnlyQ(1).VowelNB()
#--> FALSE
? Why()
#--> no: expected exactly 1, found 2
```

La chaîne répond `no: expected exactly 1, found 2`. Les mots de degré sont des dispositifs, et la raison est conservée. Le bloc la lit avec le `Why()` de la console ; celui de la chaîne est `WhyCheckFailed()` :

```haro
? Q("AnnIE").AtLeast(2).VowelNB()
#--> TRUE
? Q("AnnIE").AtMost(2).VowelNB()
#--> FALSE
? Why()
#--> no: expected atmost 2, found 3
```

La chaîne refuse ce que son sujet ne peut pas faire. Elle parle le même lexique que la direction de la machine : un mot français fonctionne dans une chaîne. Et un mot mal orthographié est refusé avec le mot le plus proche. C'est « un lexique, deux directions » en trois lignes :

```haro
try
	Q(5).VowelNB()
catch
	? cCatchError
done
#--> NNL: a stznumber cannot count 'numberofvowels' -- and neither can the chain subject.
? Q("haro").IsAQ(:String).IfSo("majuscule").Content()
#--> HARO
try
	Q("haro").IsAQ(:String).IfSo("uppercse")
catch
	? cCatchError
done
#--> NNL: this stzstring does not understand 'uppercse'. Did you mean 'uppercase'?
```

Une chaîne se ramifie sur sa propre vérité, et un ordinal est un mot :

```haro
? Q("haro").IsAQ(:String).IfSo(:Uppercase).Otherwise(:Reverse).Content()
#--> HARO
? Q("hello").IsAQ(:Number).IfSo(:Reverse).Otherwise(:Uppercase).Content()
#--> HELLO
? Q("hello brave world").TheNth(2, :Words)
#--> brave
```

Les questions fonctionnent de la même manière. Un mot de force ouvre un cadre, un mot et une méthode. Une question de confirmation se termine par « or not ». Que garde la session quand l'une répond oui et l'autre non ? Elle garde chaque réponse et les replie, comme une narration :

```haro
? @@( WhatQ().TheQ().VowelsQ().OfQ("AnnIE").Is() )
#--> [ "A", "I", "E" ]
? HowManyQ().WordsQ().Of("hello brave world")
#--> 3
ClearAnswers()
? IsQ().TheQ().LengthQ().OfQ("Haro").TheSameAsQ().TheQ().LengthQ().OfQ("Ruby").OrNot()
#--> 1
? Why()
#--> yes: 4 is the same as 4
? IsQ().TheQ().LengthQ().OfQ("Haro").TheSameAsQ().TheQ().LengthQ().OfQ("softanza").OrNot()
#--> 0
? Why()
#--> no: 4 is not the same as 8
? @@( AnswersSoFar() )
#--> [ 1, 0 ]
? AllYesSoFar()
#--> FALSE
? AnyYesSoFar()
#--> TRUE
```

La session a gardé `[ 1, 0 ]` et l'a repliée : tout oui vaut `FALSE`, au moins un oui vaut `TRUE`.

### La machine est l'analyseur

Maintenant l'autre direction. La phrase est une chaîne de caractères, et la bibliothèque la lit. Le même verdict peut venir d'une narration de questions et d'une chaîne de vérité. Avec quelle certitude la chaîne de vérité répond-elle, et pourquoi ? Exécutez-la :

```haro
oT = Naturally("Create a string with 'haro' Is it lowercase ? Does it contain 'r' ?")
? @@( oT.Answers() )
#--> [ 1, 1 ]
? oT.AllYes()
#--> TRUE
? oT.Understood()
#--> create a string with haro -> ask: is lowercase -> ask: contains
? TruthOf("haro").IsA(:Lowercase).AndIsA(:Latin).AndContaining("r").Holds()
#--> TRUE
? Why()
#--> yes: "haro" is lowercase and is latin and containing "r"
? Certainty()
#--> 1
? Evidentially()
#--> certainly
```

Elle répond `certainly`, et dit pourquoi : `yes: "haro" is lowercase and is latin and containing "r"`.

Le paragraphe entier est compilé en code avant que rien ne s'exécute, et le code est lisible. C'est le compte rendu même de la bibliothèque sur la raison d'être de la couche :

```haro
o1 = Naturally("Create a string with 'test.data' Replace '.' with '_' Uppercase it")
? o1.Result()
#--> TEST_DATA
? o1.Code()
#--> oStr = StzStringQ("test.data")
#    oStr.Replace(".", "_")
#    oStr.Uppercase()
#    @result = oStr.Content()
```

Le même sens en haoussa aboutit-il au même code ? Le haoussa est écrit ici sans la lettre crochetée, comme le paquet la lit aujourd'hui, pour une raison que donne le chapitre 11. Exécutez, et chaque programme redit ce qu'il a compris, dans ses propres mots :

```haro
oE = Naturally("Make a string with 'hello niger' inside Spacify it and uppercase it")
oH = NaturallyIn("hausa", "Yi rubutu da dauke 'hello niger' a ciki Raba shi kuma maida shi")
? oE.Code() = oH.Code()
#--> TRUE
? oH.Understood()
#--> yi rubutu dauke hello niger -> raba -> maida
? oE.Understood()
#--> create a string with hello niger -> spacify -> uppercase
```

La comparaison répond `TRUE` : un seul code pour deux langues !

Le dictionnaire de phrases n'est pas le seul vocabulaire. Où va un mot qu'il ne tient pas ? Il est cherché dans le vocabulaire propre de la bibliothèque, ici les balises de documentation du verbe de mise en majuscules. Une valeur entre guillemets est une donnée, et jamais un verbe. Un mot inconnu en position de valeur reste un littéral :

```haro
? Naturally("Create a string with 'softanza' Capitals it").Result()
#--> SOFTANZA
? Naturally("Create a string with 'capitals' Uppercase it").Result()
#--> CAPITALS
? Naturally("Create a string with 'a-sep-b' Replace sep with '_'").Result()
#--> a-_-b
```

La troisième ligne est aussi une limite : elle a imprimé `a-_-b`. Le mot `sep` n'était dans aucun dictionnaire, et il a servi de texte à remplacer. Un mot qu'elle ne connaît pas est un littéral.

**Cinq langues comme données.** Le dictionnaire est indexé par sens, et le mot de chaque langue aboutit à un seul identifiant. Un mot français, un mot arabe et un mot turc aboutissent-ils au même ? Exécutez :

```haro
? StzResolveSemanticInLang("fr", "doublons")
#--> METHOD_REMOVEDUPLICATES
? StzResolveSemanticInLang("ar", "تكرارات")
#--> METHOD_REMOVEDUPLICATES
? StzResolveSemanticInLang("tr", "tekrarları")
#--> METHOD_REMOVEDUPLICATES
? StzResolveSemantic("removeduplicates")
#--> METHOD_REMOVEDUPLICATES
```

Les langues suivent leur propre grammaire, et ce ne sont pas des traductions mot à mot. Le turc met le verbe en dernier, avec les paramètres avant lui. L'arabe, avec ses marques de voyelles et sa lettre doublée, est dépouillé par le paquet ; le suffixe du verbe est le « le » masculin pour un texte. Le français élide :

```haro
? NaturallyIn("tr", "'a.b' ile bir metin oluştur '.' yerine '_' koy").Result()
#--> a_b
? NaturallyIn("tr", "'haro' ile bir metin oluştur ve tersine çevir").Result()
#--> orah
? NaturallyIn("ar", "أنشئ نصا بـ 'haro' ثم اقلبه").Result()
#--> orah
? NaturallyIn("ar", "أنشئ نصًا بـ 'haro' ثمّ اقلِبْه").Result()
#--> orah
? NaturallyIn("ar", "أنشئ نصا بـ 'haro' ثم اقلبه").Understood()
#--> أنشئ سلسلة بـ haro -> اعكس
? NaturallyIn("fr", "Crée une chaine avec 'haro' et mets la à l'envers").Result()
#--> orah
```

Trois langues, trois grammaires, une seule réponse : `orah`. L'arabe redit ce qu'il a compris, dans ses propres mots : `أنشئ سلسلة بـ haro -> اعكس`.

Aucun lecteur natif n'a lu ces phrases. Elles sont calquées sur celles de la garde, avec « haro » à la place du mot d'essai de la garde, et l'inversion turque d'une chaîne de caractères est la variante du livre de l'inversion de liste de la garde. Je ne sais pas qu'un locuteur les ait lues. Le dossier ne tient aucune lecture, par un locuteur, des phrases arabes, turques, françaises ou swahilies, comme il n'en tient aucune pour le haoussa du chapitre 11. Elles sont imprimées comme des phrases calquées sur celles de la bibliothèque, non lues.

Une langue peut-elle être un bloc de données ? Voici le swahili, ajouté à l'exécution, dans les mots propres de la garde :

```haro
StzAddNaturalLanguage([
	:code = "sw",
	:name = "swahili",
	:script = "latin",
	:ignored_words = [ "na", "ya", "kwa", "hii" ],
	:semantic_mappings = [
		[:natural = "unda",   :semantic = "CREATE_OBJECT"],
		[:natural = "orodha", :semantic = "OBJECT_LIST"],
		[:natural = "na",     :semantic = "VALUE_INDICATOR"],
		[:natural = "panga",  :semantic = "METHOD_SORT"]
	],
	:phrases = [
		[:semantic = "METHOD_REMOVEDUPLICATES", :words = "ondoa nakala, futa nakala"]
	]
])
? StzHasLanguagePack("sw")
#--> TRUE
osw = NaturallyIn("sw", "Unda orodha na [ 9, 4, 9 ] ondoa nakala")
? @@( osw.Result() )
#--> [ 9, 4 ]
? osw.Understood()
#--> unda orodha na [ 9, 4, 9 ] -> ondoa nakala
```

Quatre correspondances, une locution, et la sixième langue répond `[ 9, 4 ]` !

Le code naturel est aussi une donnée. Les blocs délimités d'un document s'exécutent, et un gabarit se remplit :

```haro
cDoc = "This tutorial explains deduplication." + nl +
	"#<" + nl +
	"Create a list with [ 3, 1, 3 ] and remove its duplicates" + nl +
	"#>" + nl +
	"The end."
? len( StzNaturalBlocks(cDoc) )
#--> 1
? @@( NaturallyFromDoc(cDoc)[1].Result() )
#--> [ 3, 1 ]
cT = "Create a list with {#1} and remove its duplicates"
? @@( NaturallyWith(cT, [ [ 5, 3, 5 ] ]).Result() )
#--> [ 5, 3 ]
? @@( NaturallyWith(cT, [ [ 9, 9, 4 ] ]).Result() )
#--> [ 9, 4 ]
```

**Ce que les paquets savent dire.** Combien chaque paquet sait-il dire ? La bibliothèque a une fonction pour cela, et aucune garde n'imprime ses chiffres. Je compte par rapport à vingt-cinq sens de référence, qui sont les sens structurels et chaque méthode et modificateur que nomme un paquet livré. Ce ne sont pas les milliers de verbes que la bibliothèque a fait croître :

```haro
for cLang in [ "en", "ha", "fr", "ar", "tr" ]
	aC = StzPackCoverage(cLang)
	? cLang + " " + aC[:covered] + " of " + aC[:total]
next
#--> en 23 of 25
#    ha 9 of 25
#    fr 25 of 25
#    ar 16 of 25
#    tr 10 of 25
? StzHasNeuralModel()
#--> FALSE
```

Le paquet haoussa parle neuf des vingt-cinq sens : `ha 9 of 25` ! Et aucun modèle n'est chargé. La couche a un secours facultatif par plongement, quand rien de lexical n'a été trouvé et qu'un modèle est chargé. À ce commit aucun ne l'est, et aucun n'est nécessaire. Je dis donc « aucun modèle n'est chargé », et non « ne touche jamais un modèle ».

### Du schéma de 2020 aux trois ères

La bibliothèque nomme trois ères, dans un document de conception du 10 juillet 2026. La première est le langage quasi naturel, le premier paradigme. La deuxième est la programmation naturelle : abaisser le langage vers le code, avec du texte libre, et un objet par bloc. La troisième, de 2026, est un lexique partagé par l'exécution et la documentation, des paquets multilingues avec morphologie, et `Understood()`. J'appelle la troisième *le lexique partagé*. Le titre même de la vision pour elle emploie un mot que ce livre n'emploie pas.

Voici les dates, telles que le dossier les donne. Mon schéma stratégique porte les années 2020 à 2025, partagé le 13 septembre 2026 ; sa bande Narrations se lit « langage naturel exécutable ». Le diaporama de 2022 a été exporté le 20 septembre 2022, et sa diapositive 2 dit d'exprimer la pensée dans un langage naturel exécutable. Le dépôt de la bibliothèque commence le 12 mars 2022, et son historique ne peut pas dater 2020 ni 2021. Les fichiers quasi naturels et le moteur à son chemin actuel ont été commités pour la première fois entre le 16 et le 19 septembre 2025. Le 30 octobre 2025, les langues sont devenues de la configuration. Le 2 novembre 2025, l'entrée par chaîne de caractères a remplacé la capture par accolades. Le 9 juillet 2026, le lexique a été unifié à partir des balises de documentation. Le 10 juillet 2026, les deux documents de conception ont été écrits, et l'audit de quinze exemples canoniques a trouvé que quatre tournaient, et que deux d'entre eux répondaient correctement. La page phare du site est du 8 octobre 2026. (Les dates git viennent du dépôt propre de la bibliothèque, que l'instantané n'a pas. Les dates des commits y ont été vérifiées le 9 octobre 2026, et les commits cités sont des ancêtres de l'épinglage.)

La plus ancienne diapositive que le dossier date est donc la diapositive fondatrice du diaporama de 2022, exporté le 20 septembre 2022. L'année 2020 est la première année de mon schéma stratégique, partagé le 13 septembre 2026 ; le dossier ne tient aucune diapositive de 2020.

Vient maintenant la décision, et ce que j'ai refusé.

## 4. La décision, et ce que j'ai refusé

**Je l'ai construite sans modèle, comme un dictionnaire.** La conception dit que tout ce qui est dans le dossier naturel attaque un seul mur : l'écart sémantique entre une intention humaine et son exécution. La thèse du langage quasi naturel, dans cette revue : zéro NLP, zéro ML, vitesse native, déterminisme complet, et le programmeur aux commandes. La couche a livré sans bruit une quatrième promesse que les anciens documents n'avaient jamais osé faire : la responsabilité.

**J'ai décidé de deux directions, une seule discipline.** Le tableau de la revue a cinq lignes. Qui analyse : une machine avec un lexique, ou l'humain. L'ambiguïté : refusée bruyamment, ou impossible par construction. Le vocabulaire : borné par les paquets, ou non borné. La compréhension : vérifiée par la machine, ou par une lecture humaine. Le public : des experts du domaine et des agents, ou des programmeurs. Les deux finissent au même endroit : une suite déterministe d'opérations sémantiques.

**J'ai refusé les marqueurs de référence.** Le 10 juillet 2026, j'ai rejeté la famille de suffixes qui marquaient une référence. Le chiffre a été inversé par son propre inventeur, de mémoire, il dupliquait des sens, et le langage lui-même ne marque jamais la référence ainsi. C'est mon point de vue sur le langage, non un résultat. Plus de deux cent soixante méthodes ont été retirées. Le chapitre 11 le raconte en deux phrases.

**J'ai refusé la chaîne non grammaticale.** La chaîne est la phrase, et une chaîne non grammaticale qui s'exécute est un bogue. Je tiens cela pour une vue, non pour un résultat. La doctrine est tenue par la lecture à voix haute, non par une machine, et j'en montre la preuve plus bas.

**J'ai refusé la négation en préfixe.** La négation vit dans les formes négatives, dans les comparateurs antonymes et dans le fermeur de question `OrNot()`. La question de confirmation ci-dessus est cette décision en train de tourner.

**J'ai refusé la tolérance silencieuse.** L'ancienne tolérance aux fautes de frappe a été remplacée par l'explication de tout : le refus avec le mot le plus proche, ci-dessus.

**J'ai refusé le contexte global.** Deux chaînes entremêlées se contaminaient, et la correction a mis le contexte sur la chaîne. Le `Why()` à l'échelle du processus reste comme commodité pour la console et les tests. Les globales survivent comme adaptateurs de repli : une ancienne méthode hors de la couche naturelle qui construit un nouvel objet y retombe encore.

**J'ai refusé le langage de balisage.** Les annotations qui donnaient à la machine ce qu'elle ne pouvait pas inférer gouvernaient en obligeant l'humain à annoter. Le système gouverne par le dialogue. Deux graines ont été gardées comme portes minces, et ce sont le document et le gabarit ci-dessus.

**J'ai refusé un interpréteur de commandes pour des récits, et la capture par accolades.** Dans mes propres mots dans l'article : il est conçu pour des commandes, pas pour des récits. Et un objet par bloc. La forme chaîne de caractères a remplacé la forme à accolades, parce que le code naturel est devenu un type de données de première classe, stockable, versionnable et cherchable. La règle depuis assouplie : un programme peut nommer des objets et passer de l'un à l'autre.

**J'ai refusé la gouvernance à l'intérieur de la couche naturelle.** J'ai sorti cette portée de la bibliothèque le 12 juillet 2026, et le code a été retiré.

**J'ai refusé le langage naturel comme moyen de déclarer.** Il demande, et ne déclare jamais.

Le tribunal vient ensuite, et l'une de ses gardes échoue.

## 5. Le tribunal

`nnl_narrated` prouve la phrase phare, la surface générée de noms, les mots de degré, le mode conditionnel, la référence ordinale, le refus qui rend compte de lui-même, la doctrine de grammaticalité, le contexte sur la chaîne, et le temps du discours. `multilingual_pack_narrated` prouve les paquets comme données, des programmes en français, en arabe et en turc qui s'exécutent, le retrait d'affixes vérifié, une langue ajoutée à l'exécution, et `Understood()` rendu dans la langue du programme. `question_narrated` prouve les cadres de question et qu'un cadre sans aspect est refusé. `literate_templates_narrated`, les documents et les gabarits. `truthchain_narrated` et `interrogative_narrated`, les verdicts repliés.

`semantic_resolver_narrated` est la garde qui devrait protéger le dictionnaire, et à ce commit elle échoue. Un chercheur l'a lancée deux fois le 8 octobre 2026 et, chaque fois, elle s'est arrêtée sur une erreur : trois assertions ont échoué, et l'exécution s'est terminée après la vingt-neuvième. Dans cette exécution, le mot « caps », que la garde affirme, s'est résolu en une méthode pour les bornes, et « mirrored » ne s'est résolu en rien. La raison est celle de la conception elle-même : le vocabulaire est lu dans les balises de documentation de la bibliothèque, plus dix-sept opérations écrites à la main, portées par réflexion à environ trois mille. Une modification de la documentation change donc le sens d'un mot. La bibliothèque refuse honnêtement dans le second cas : dans cette exécution, `Unresolved()` a nommé le mot et `UnderstoodAll()` a imprimé 0. Le tribunal du dictionnaire a échoué sur le dictionnaire, et le chapitre 11, le chapitre 22 et le chapitre 2 nomment cette garde.

Un chercheur a lancé une fois chacune les autres gardes nommées ci-dessus le 8 octobre 2026, et dans cette exécution elles ont passé toutes leurs assertions ; les données propres du livre n'en tiennent que les décomptes. Les appels d'assertion écrits dans les sept gardes nommées ci-dessus totalisent 269.

## 6. Le terrain, et où il mène

Le terrain mène en largeur de formulation. Un modèle accepte n'importe quelle formulation dans n'importe quelle langue, et le dictionnaire accepte ce que les paquets nomment. Mesuré plus haut : le paquet haoussa couvre neuf des vingt-cinq sens, le turc dix, l'arabe seize, l'anglais vingt-trois (les deux qui lui manquent, l'anglais les atteint par le vocabulaire développé par réflexion), le français vingt-cinq. Et la couche de phrases n'agit que sur trois classes : les chaînes de caractères, les listes et les nombres. Les objets du domaine d'un client n'en font pas partie ; le domaine passe par le graphe de connaissance.

Le terrain mène en sémantique de programme entier. Inform 7 compile un monde entier. Ici un programme est une suite d'opérations sur un objet vivant.

Le terrain mène sur l'éditeur. Dans l'exécution d'un chercheur, la fonction de suggestion a répondu neuf suites possibles pour une phrase à moitié écrite, et le code attribue au terrain des langages contrôlés l'idée. Il n'y a pas ici d'éditeur qui les montre pendant que vous tapez.

Et il y a une perte du côté de la bibliothèque elle-même. `Understood()` imprime les verbes et non leurs arguments : le bloc de la section 3 imprime `contains` et non le « r » demandé. Dans l'exécution d'un chercheur, `Replace` s'est imprimé `replace`, et `Add 3 to it` s'est imprimé `add` alors que le résultat était 8. Un lecteur qui vérifie la lecture de la machine ne voit pas de 3. Cela nuance l'affirmation du chapitre 11 selon laquelle une personne peut vérifier ce que la machine a compris.

Là où est le gain, avec la perte à côté : la même phrase donne la même réponse, avec une raison, dans la langue de l'utilisateur, et conçue pour s'exécuter hors ligne, ce qu'aucune garde ne mesure. La perte est que la langue de l'utilisateur doit être dans un paquet, et qu'un mot extérieur est un littéral ou un refus. Le dossier dit que le cas gagnant est le travail réglementé ou souverain : une instruction qui s'exécute localement et peut être auditée au mot près.

La section suivante dit où le chapitre s'arrête.

## 7. La limite

Une chaîne non grammaticale s'exécute. La seconde chaîne ci-dessous se lit « which a length of 4 », ce qui n'est pas de l'anglais. Quelque chose la juge-t-il ? Exécutez les deux :

```haro
? TheWordQ("haro").IsAQ(:Word).WhichQ().HasQ().ALengthQ().Of(4)
#--> TRUE
? TheWordQ("haro").IsAQ(:Word).WhichQ().ALengthQ().Of(4)
#--> TRUE
```

Les deux répondent `TRUE` : rien n'a jugé la seconde ! La doctrine est que relire une chaîne, c'est la lire à voix haute comme de l'anglais. C'est le travail de l'humain.

Le descripteur d'une chaîne atteint-il le code hôte ? Oui. `IsAXT` construit une chaîne de caractères et l'évalue, de sorte qu'une fonction définie par le programme et nommée dans la chaîne a imprimé `host code ran`. C'est le résidu que l'étude du dossier et le chapitre 6 nomment :

```haro
? Q("haro").IsAXT([ "String('x') and HostRan() and @isString" ])
#--> host code ran
#    TRUE

func HostRan()
	? "host code ran"
	return 1
```

Et un mot de l'ancienne ère est signalé, et jamais deviné. Le mode permissif exécute quand même le reste, et le mode strict refuse. La suggestion offerte, `addn`, est mauvaise :

```haro
o = Naturally("Create a string with 'softanza' Spacify it and_ Uppercase it")
? o.Result()
#--> S O F T A N Z A
? o.UnderstoodAll()
#--> FALSE
? @@( o.Unresolved() )
#--> [ [ "and_", "addn" ] ]
try
	NaturallyStrict("Create a string with 'softanza' Spacify it and_ Uppercase it")
catch
	? cCatchError
done
#--> Strict natural mode: not understood: 'and_' (did you mean 'addn'?)
```

**Plusieurs chaînes des anciens articles ne tournent plus.** La phrase de l'article sur le pont qui porte `IsAMQ` demande un marqueur que j'ai retiré par ma décision du 10 juillet 2026. Plusieurs chaînes de l'article quasi naturel ne tournent pas à ce commit : `InLowercase()` lève une erreur faute d'objet ; `LettersNB`, `BeforeQ` et `TheirQ().FirstCharQ()` ne sont pas définis ; et la forme à accolades `Naturally() { ... }` lève une erreur pour trop peu de paramètres. La chaîne de l'article sur le pont avec `ReplaceLowercaseCharsQ` n'est pas définie non plus. Un chercheur a lancé douze chaînes de l'article quasi naturel le 8 octobre 2026, et huit fonctionnent. Dans l'exécution de ce chercheur, le paragraphe de l'article sur le pont tournait encore en mode permissif, et imprimait deux boîtes imbriquées autour de « NOTHING SOFTANZA » au lieu de la seule qu'il promet. La machine l'a dit, puisque `UnderstoodAll()` vaut faux et que le mot non résolu est nommé (le bloc ci-dessus montre les deux), mais un lecteur doit le demander.

Ce qui est construit : les deux directions ; cinq paquets comme données et un sixième à l'exécution ; des refus avec raisons des deux côtés ; les cadres de question, la chaîne de vérité mince, le registre évidentiel ; le code naturel comme données. Le dossier contient treize fichiers et environ douze mille lignes dans douze classes, d'après `wc` et `grep` le 8 octobre 2026.

Ce qui est conçu : le plan d'une narration émis comme une chaîne exécutable, de sorte que les chaînes gagnent `Understood()` gratuitement. Une grammaire émise pour le lexique naturel, de sorte qu'un modèle ne puisse produire que des phrases que la couche exécute : j'ai cherché dans le dossier, et aucun émetteur de grammaire ne le touche. Une garde qui échoue si un socket s'ouvre pendant une exécution naturelle, qui n'existe pas. Un chiffre de couverture par paquet imprimé par une garde. Et les exemples des articles épinglés comme fixtures.

Ce qui est absent : le haoussa en écriture ajami, le zarma et le peul. Une couche naturelle fermée jusqu'en bas : une liste simple dans une phrase naturelle atteint le code hôte, ce que le chapitre 11 imprime, et un descripteur atteint le code hôte, ci-dessus. Toute machine qui juge la grammaire d'une chaîne. La lettre haoussa standard, que le paquet stocke brisée. Un dictionnaire protégé de la dérive. Le dossier ne tient pas non plus de récit, ni de date, du plaidoyer de l'auteur auprès du projet de l'ancien langage hôte pour que la programmation naturelle devienne une préoccupation première. Il ne tient pas davantage une phrase de lui sur ce ton dont le livre puisse citer la source. Il ne tient qu'un mémo privé du 30 août 2026, qui donne son jugement sur la forme naturelle livrée par ce langage. Le mémo est marqué privé : le livre ne le cite pas et n'attribue aucune expression à l'auteur.

## 8. Six portes

**Le programmeur.** Écrivez la chaîne comme la phrase et lisez-la à voix haute. La bibliothèque refuse ce que son sujet ne peut pas faire, et dit pourquoi. Vous êtes l'analyseur, donc la phrase n'est grammaticale que dans la mesure où vous l'êtes.

**L'analyste.** Une exigence peut être un paragraphe qui s'exécute, avec une paraphrase qui revient. Aujourd'hui elle agit sur des chaînes de caractères, des listes et des nombres, donc les mots de domaine de l'analyste vont dans un fichier de connaissance (chapitre 14), pas ici.

**Le concepteur.** Le ton d'un concepteur est dans les refus : un message nomme le mot et le mot le plus proche. Le dossier n'a pas de preuve propre au concepteur pour ce chapitre, et je garde la ligne courte.

**Le décideur.** Demandez à toute affirmation de « langage naturel » ce qu'elle fait d'un mot qu'elle ne connaît pas. Ici elle le signale, le refuse en mode strict, ou le prend comme littéral, et dit lequel. Elle est conçue pour s'exécuter hors ligne, sans clé. L'affirmation d'absence de réseau n'est pas encore mesurée.

**Le formateur.** Un apprenant écrit en haoussa, en français, en arabe ou en turc, et le programme redit ce qu'il a compris dans la même langue. Le paquet haoussa parle neuf des vingt-cinq sens, et aucun relecteur n'a lu les éditions du cours dans d'autres langues.

**L'agent.** Parlez le lexique. Utilisez le mode strict et une liste d'autorisation (chapitre 11). Attendez-vous à un refus avec une raison. Votre phrase est une proposition. Une grammaire qui vous tiendrait au lexique est conçue et non construite.

## 9. Exercice

Prenez une phrase que vous dites d'un mot de votre propre langue : qu'il est en minuscules, qu'il a une longueur donnée, et un nombre donné de voyelles. Écrivez-la deux fois avant de rien exécuter. D'abord comme une chaîne quasi naturelle, où vous êtes l'analyseur. Ensuite comme une phrase `Naturally`, où c'est la bibliothèque. Sous chacune, écrivez la ligne que vous vous attendez à voir imprimée.

```haro exercise
# 1. as a chain, where you are the parser:
# 2. as a Naturally sentence, where the library is:
```

Exécutez ensuite les deux. Puis changez un mot de la chaîne, et un mot de la phrase, en un mot que le dictionnaire ne tient pas. Quelle direction vous l'a dit ? Laquelle avez-vous dû vous le dire vous-même ? Dans une direction la machine vous le dit, et dans l'autre vous devez vous le dire vous-même. Si une promesse se rompt, ne la changez pas : expliquez d'abord la sortie.

Le chapitre suivant porte sur la programmation de la connaissance, où les mots de domaine de l'analyste ont été envoyés. Son principe est qu'un système est un fichier, et qu'y ajouter une ligne fait que le système sait davantage, sans rien coder ni entraîner. Ici une phrase demande, et ne déclare jamais.
