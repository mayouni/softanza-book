---
id: functions-as-linguistic-expressions-and-scope
part: 2
number: 8
title: Les fonctions comme expressions linguistiques, et la portée
spine: false
narrations: [stz-functions-as-linguistic-expressions.md, stz-function-forms-narration.md, stz-system-dev-to-deploy-narration.md]
site: [craft, innovations]
guards: [00_regex_narrated, 972_narration_viz-finding_a_recurring_substring, full_scope_model_narrated, system_scope_model_narrated, delivery_narrated]
stage:
  built: "quatorze des vingt-deux formes, certaines avec d'autres exemples que ceux de l'article, et trois autres sous une autre forme ; la bibliothèque qui lit un nom comme une phrase ; la portée dans les verbes de l'expression régulière, dans le système et dans le placement d'un déploiement"
  designed: "les formes déclarées une fois comme données et générées, en Haro ; le paradigme de portée pour le temps, les unités, la mémoire et le style"
  absent: "cinq formes : partielle, future, libre, par défaut et multilingue ; la concurrence comme portée : un plan sans code"
status: draft
rulings: ["12.3", "12.13", "12.19", "12.21"]
research: research/ch08.md
figures:
  - "fourteen forms run as shown, three in another shape, five do not run: a tally made on 8 October 2026 at stzlib 93d7a39bd, form by form, in research/ch08.md section 4.1"
---

Dans ce chapitre, je lis le nom d'une fonction comme la bibliothèque le lit : une phrase dont les préfixes, les suffixes et les paramètres sont une grammaire. Je parcours les formes d'un nom qui tournent, et je compte les cinq qui ne tournent pas. Puis je passe à la portée : le même verbe, trois verdicts, avec le cadre dans le verbe et non dans un drapeau posé plus tôt. Je dis ce que la conception de Haro garde des formes, ce qu'elle refuse, et ce que le tribunal prouve. Le principe est celui-ci : le nom d'une fonction est une phrase, et ses préfixes, ses suffixes et ses paramètres sont une grammaire que la bibliothèque peut lire.

## 1. Le concept, tel que le terrain le tient

Sur le terrain, le nom d'une fonction est une étiquette. Il suit une convention, camel case ou snake case, et il vous dit à peu près ce que fait la fonction ; les détails sont dans la signature et la documentation. Un nom ne porte pas de grammaire. Les outils voisins ne parlent que de structure. Python et Swift offrent l'argument nommé, pour qu'un appel puisse dire quel paramètre est lequel. L'interface fluide enchaîne les appels pour qu'une ligne se lise comme une phrase, et la surcharge donne à un seul nom plusieurs signatures.

Et quand le terrain veut qu'une fonction se comporte autrement dans un autre contexte, il change son sens par un drapeau posé ailleurs. Le drapeau est un mode, une locale, une variable d'environnement. Le nom de la fonction ne vous dit pas dans quel cadre elle va s'exécuter.

## 2. Le premier principe

**Le nom d'une fonction est une phrase, et ses préfixes, ses suffixes et ses paramètres sont une grammaire que la bibliothèque peut lire.** L'article qui a le premier avancé cette thèse dit, dans les mots que cite l'étude de ses racines, qu'elle a été obtenue « without machine learning or NLP systems ». Elle l'a été par des conventions de nommage qui encodent le sens, un ordre des paramètres qui épouse la parole, des formes souples et des valeurs par défaut intelligentes.

## 3. La forme Softanza

Regardez un nom comme la bibliothèque le regarde. `FindNextSTCS` : trouver le suivant, à partir d'une position de départ, avec un drapeau de casse. `RemoveManyCS` : retirer, plusieurs choses, un drapeau de casse. Chaque suffixe est petit et ne veut dire qu'une chose, et, dans ces noms, l'ordre des suffixes est l'ordre des paramètres. Ici le premier nom trouve. Que laisse le second quand il retire toutes les occurrences de trois lettres, quelle que soit leur casse ? Exécutez-le :

```haro
o1 = new stzString("123456789HARO")
? o1.FindNextSTCS("haro", 5, FALSE)
#--> 10
o2 = new stzString("SOOooooFFfffTANNnnnZA")
o2.RemoveManyCS([ "o", "f", "n" ], FALSE)
? o2.Content()
#--> STAZA
```

L'article promettait `SOFTANZA` sur la deuxième ligne. L'exécution imprime `STAZA` ! Le code a raison et l'article a tort : un retrait qui ne se soucie pas de la casse retire aussi les majuscules. J'imprime l'exécution.

La bibliothèque se contente-t-elle de suivre cette grammaire, ou la lit-elle ? Son analyseur de noms, `_StzParseName`, est un assistant interne que nulle garde ne couvre. La voie publique est `ExplainMethod`, qui explique une méthode dans ces termes :

```haro
? @@( _StzParseName("FindNextSTCS") )
#--> [ "find next", [ "case-sensitive", "from-position", "active" ] ]
? @@( _StzParseName("RemoveManyCS") )
#--> [ "remove", [ "case-sensitive", "plural", "active" ] ]
? StzSelfDocQ("stzString").ExplainMethod("RemoveMany")
#--> RemoveMany -- Remove every occurrence of each given substring (mutating).
#-->   (plural form -- applies the operation to many items at once)
#-->   reads as: remove -- over many values at once
```

Elle la lit. Voilà la thèse rendue mécanique : la grammaire est dans le code et pas seulement dans l'article. La ligne imprimée `reads as: remove -- over many values at once` est la lecture que l'analyseur fait de `RemoveMany`. L'analyseur décode les préfixes et les suffixes, les mots « except » et « is not », et la voix : un nom qui finit en `ed` est passif.

Je vais maintenant parcourir les formes. Le chapitre 5 en a montré quatre : l'active, la passive, la fluide et le paramètre nommé. Voici les autres, celles qui tournent.

**Z et ZZ** disent si une position arrive comme un nombre ou comme une section. Un suffixe, et la réponse change de forme :

```haro
o1 = new stzString("haro php haro ruby haro")
? @@( o1.FindZ("haro") )
#--> [ 1, 10, 20 ]
? @@( o1.FindZZ("haro") )
#--> [ [ 1, 4 ], [ 10, 13 ], [ 20, 23 ] ]
o2 = new stzString("SOFTANZA")
? @@( o2.FirstHalfZ() )
#--> [ "SOFT", 1 ]
? @@( o2.FirstHalfZZ() )
#--> [ "SOFT", [ 1, 4 ] ]
```

**Le préfixe viz** change la sorte de réponse : un dessin. La position est montrée sous le texte, et une option peut la numéroter :

```haro
o1 = new stzString("fjharoljharodjharog")
? o1.vizFind("haro")
#--> fjharoljharodjharog
#--> --^-----^-----^----
? o1.vizFindXT("haro", [ :Numbered = TRUE ])
#--> fjharoljharodjharog
#--> --^-----^-----^----
#-->   3     9     15
```

**Le pluriel** étend un verbe à plusieurs choses sans boucle, et **la forme d'exception** ne garde que ce que vous nommez. L'exemple de l'article pour la seconde, `RemoveNonLettersExcept`, n'existe pas. La forme existe, sous d'autres noms :

```haro
o1 = new stzString("__H~~~AR***O__")
? @@( o1.FindMany([ "~", "*" ]) )
#--> [ 4, 5, 6, 9, 10, 11 ]
o1.RemoveMany([ "_", "~", "*" ])
? o1.Content()
#--> HARO
o2 = new stzString("--Haro--&__Softanza__")
o2.RemoveAllExcept([ "Haro", "&", "Softanza" ])
? o2.Content()
#--> Haro&Softanza
```

**Le négatif** est un mot dans le nom, pas un NOT autour de l'appel :

```haro
? Q("*").IsNotLetter()
#--> TRUE
o3 = new stzList([ "R", "I", "N", "G" ])
? o3.IsNotAString()
#--> TRUE
? o3.DoesNotContain("♥")
#--> TRUE
```

**La forme profonde** répond par un chemin, une liste d'indices qui va aussi profond que les données, et la même famille remplace et retire à cette profondeur :

```haro
o1 = new stzList([ "you", "other", [ "other", "you", [ "you" ], "other" ], "other", "you" ])
? @@( o1.DeepFind("you") )
#--> [ [ 1 ], [ 3, 2 ], [ 3, 3, 1 ], [ 5 ] ]
o1.DeepReplace("you", :By = "♥")
? @@( o1.Content() )
#--> [ "♥", "other", [ "other", "♥", [ "♥" ], "other" ], "other", "♥" ]
```

**La forme immuable**, QC, exécute toute la chaîne sur une copie. Après cette chaîne, que contient l'original ?

```haro
o1 = new stzString("haxxrxo")
? o1.RemoveQC("x").UppercaseQ().Spacified()
#--> H A R O
? o1.Content()
#--> haxxrxo
```

La chaîne a imprimé `H A R O`, et l'original contient encore `haxxrxo` !

**La forme mal orthographiée** est acceptée, avec une note sur ce qui la soutient. Une faute d'orthographe dans un nom fonctionne :

```haro
? Q("   Haro ").WithoutSapces()
#--> Haro
```

L'article dit que la bibliothèque reconnaît et corrige les fautes de frappe mineures, et que l'intelligence réside dans la bibliothèque elle-même. Le code montre comment la forme fonctionne : `WithoutSapces` fonctionne parce que cette orthographe a été écrite à la main comme un alias. Une autre faute, `WithoutSpces`, échoue. La forme est donc réelle, et dans ce que j'ai suivi c'est une liste d'alias déclarés ; le moteur de correction que décrit l'article ne fait pas partie de ce que j'ai suivi. Je n'ai pas suivi tous les fichiers qui parlent de correction ; un message de la classe objet ne fait que suggérer un nom, avec « Did you mean ».

Voici maintenant la moitié du chapitre qui concerne la portée. Le même défaut apparaît partout en programmation : un comportement gouverné par un cadre invisible. Je tiens cela pour une vue, non pour un résultat ; ce qui la soutient ici, ce sont trois instances : les verbes de l'expression régulière, le système et le placement d'un déploiement. Une fonction fait une chose ici et une autre là, et rien dans son nom ne dit dans quel cadre elle se trouve. La réponse, en quatre gestes, est le paradigme que j'appelle la programmation orientée portée. Nommer le cadre caché. En faire un petit ensemble fermé de portées nommées. Choisir la portée à l'endroit de l'appel, dans le verbe, et pas dans un drapeau posé plus tôt. Et donner à la bibliothèque la portée pour raisonner, une prise sémantique et pas un commentaire.

Il est né dans les expressions régulières, où le cadre est la part du texte qu'un motif doit couvrir. Le même motif, le même texte, trois verbes : que répond chacun ?

```haro
cText = "First: Line1" + nl + "Second: Line2" + nl + "Third: Line3"
o1 = new stzRegex("^Second:.*$")
? o1.Match(cText)
#--> FALSE
? o1.MatchFirst(cText)
#--> FALSE
? o1.MatchLine(cText)
#--> TRUE
```

`Match` répond `FALSE` : il demande si le motif couvre la valeur entière. `MatchFirst` répond `FALSE` aussi : il demande si le motif apparaît quelque part, avec les ancres de ligne désactivées. `MatchLine` répond `TRUE` : il fait que `^` et `$` s'accrochent à chaque ligne. Le cadre est dans le verbe. Il y a aussi une portée de mot, qui fournit les limites de mot pour que vous ne les écriviez pas. Elle réécrit pour de bon le motif de son objet, c'est pourquoi la deuxième instance est un nouvel objet avec le même motif. Le même motif répond-il pareil sous `MatchFirst` et sous `MatchWord` ?

```haro
o2 = new stzRegex("pre\w+")
? o2.MatchFirst("compress")
#--> TRUE
o3 = new stzRegex("pre\w+")
? o3.MatchWord("compress")
#--> FALSE
```

Le même motif répond `TRUE` sous `MatchFirst` et `FALSE` sous `MatchWord` !

La deuxième instance est le système. Le code d'une fonctionnalité s'écrit dans une portée nommée, et le même verbe reçoit un verdict différent dans chacune. La portée peut faire se comporter un portable comme un appareil qu'il n'a pas, ou refuser ce que la cible interdit. Ici, une solution avec un backend sur un serveur Linux et un firmware sur une petite carte. Que répond chaque système quand on lui demande le même verbe, `Spawn` ? Exécutez-le :

```haro
oSol = new stzPlatformProfile("my-iot-product")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oSol.WithApp(:firmware, :ESP32)
oBack = oSol.App(:backend).System()
oFirm = oSol.App(:firmware).System()
? oBack.Spawn("worker")
#--> native
? oFirm.ReadPin(4)
#--> rehearsed
try
	oFirm.Spawn("worker")
catch
	? cCatchError
done
#--> scope 'esp32' (espidf) forbids 'process' -- spawn 'worker'. This target has no such capability.
```

Le même verbe, `Spawn`, a deux verdicts ! Le serveur répond `native` ; la carte répond `scope 'esp32' (espidf) forbids 'process'`. C'est la portée qui décide, pas l'opération. Et le portable n'a pas de broche à lire, alors la portée répond `rehearsed`. C'est le cinquième geste : quand les capacités d'une portée diffèrent de celles de l'hôte, la bibliothèque comble l'écart, dans les deux sens. Deux systèmes déclarés peuvent être comparés comme des données, avec un ensemble fermé de capacités :

```haro
oEsp = DeclareSystem("esp32-firmware")
oEsp.SetOSName(:rtos)
oEsp.SetCapabilityList([ :gpio, :network, :clock, :threads ])
oBox = DeclareSystem("laptop")
oBox.SetOSName(:windows)
oBox.SetCapabilityList([ :filesystem, :process, :network, :clock, :threads ])
? @@( oBox.Forbids(oEsp) )
#--> [ "filesystem", "process" ]
? @@( oBox.Requires(oEsp) )
#--> [ "gpio" ]
```

L'exécution a imprimé `[ "filesystem", "process" ]` pour ce que le portable peut faire et que la carte ne peut pas, et `[ "gpio" ]` pour ce dont la carte a besoin et que le portable n'a pas. C'est la deuxième instance. La troisième est le déploiement : la cible est le cadre, et la portée décide de ne pas livrer ce que la cible fait déjà bien ; le chapitre 4 en a montré le plan. La quatrième est la concurrence, et c'est un plan.

La conception vient ensuite, avec ce que Haro garde de ces formes et ce qu'il refuse.

## 4. La décision, et ce que j'ai refusé

**Dans la conception de Haro, le principe 7 fait des formes une grammaire que le langage possède.** Elle est conçue et non construite : les formes sont déclarées une fois, et le compilateur générerait et vérifierait chaque famille. La forme passive ne peut pas muter ; un verbe avec Q renvoie l'objet ; l'ordre des suffixes est l'ordre des paramètres ; un W prend un littéral analysé à la compilation. Le prototype ne juge que des noms : il ne lit pas les corps et ne juge pas l'ordre des suffixes. Sa première mesure est la classe chaîne de la bibliothèque : parmi ses 595 orthographes livrées des verbes find, replace et remove, 584 s'accordent avec la déclaration et 11 non. J'ai dit au chapitre 5 ce que Haro a refusé comme grammaire : la forme mal orthographiée, l'ordre libre des paramètres et les noms de méthodes par langue. Voici ce que cela veut dire pour ce chapitre : cinq formes ne tournent pas.

**La forme future a été écourtée exprès.** L'en-tête du fichier de code naturel la date du 10 juillet 2026 : la file globale d'actions différées est partie, et ses enveloppes FQ et FFQ avaient déjà disparu. La raison est écrite dans la conception : le langage naturel exige de bâtir tout le modèle de calcul avant d'exécuter, et le plan de jetons du moteur le fait désormais. C'est un plan du moteur naturel et plus un suffixe.

**La forme conditionnelle a changé de mécanisme.** La narration dit qu'elle ne passe plus par `eval()` mais par un petit langage textuel que le moteur compile, et que l'ancienne forme étendue, WXT, est maintenant un alias obsolète de W.

**Pour la portée, le document de conception refuse le courant flottant.** Le code d'une fonctionnalité n'est jamais écrit contre un « système courant » ambiant. Il nomme sa portée. Et pour la concurrence le document consigne deux refus avant qu'il y ait le moindre code. L'un est une méthode par opération qui étale le cadre sur de nombreux verbes, comme `DoubleEachConcurrently`. L'autre est un mode posé plus tôt. Ce mode est l'antimodèle contre lequel ce paradigme a été fondé. Il refuse aussi une portée qu'aucun hôte ne peut exécuter. Sa première idée pour la concurrence était un vocabulaire de fils d'exécution, et le langage en dessous n'a pas de fils.

**J'ai refusé de livrer tout le moteur en périphérie.** La règle de placement est : ne livrer que ce qui est critique et soit propre à Softanza, soit faible sur la cible. Une cible qui excelle déjà dans une chose n'en reçoit rien.

Voici maintenant le tribunal, et les gardes qui prouvent chacune de ces affirmations.

## 5. Le tribunal

`00_regex_narrated` prouve les verbes `Match` et `MatchFirst` : `Match` ancre, `MatchFirst` cherche, Z rend les positions et ne les imprime pas. Elle n'affirme rien pour `MatchLine` et `MatchWord` : les blocs plus haut les montrent, et seuls des blocs classiques, qui ne sont pas des gardes, les couvrent. `972_narration_viz-finding_a_recurring_substring` prouve la réponse dessinée. `full_scope_model_narrated` prouve la portée du système, avec ses trois verdicts. `system_scope_model_narrated` prouve l'ensemble fermé de capacités ; l'une de ses assertions est une limite de temps, et, lors d'une exécution de sonde sous charge que `data/` n'enregistre pas, elle n'a pas tenu. Je l'imprime à côté de la preuve. `delivery_narrated` prouve le plan de placement.

Où le terrain fait mieux vient ensuite.

## 6. Le terrain, et où il mène

Le terrain mène en convention. Un nom qui est une étiquette est plus facile à enseigner et plus facile à taper. La grammaire de ce chapitre doit s'apprendre, et certaines de ses formes sont rarement utilisées.

Le terrain mène en garantie. Les arguments nommés de Python sont vérifiés à l'appel, et les étiquettes de Swift par le compilateur, pour chaque fonction, dès le premier jour. Les formes d'ici sont jugées par le prototype de Haro, sur les noms et non sur les corps, et par l'analyseur propre de la bibliothèque, et seulement dans les noms qui les suivent.

Sur la portée, le terrain mène en maturité. La pratique la plus proche est le contexte explicite : l'habitude de Go de passer un contexte à chaque appel, un objet de locale qui porte un cadre. Elles sont plus anciennes et plus largement employées. Ce que ce paradigme ajoute, c'est que le cadre fait partie d'un petit ensemble fermé, choisi dans le verbe, et que la bibliothèque peut raisonner avec lui.

Enfin, la limite, avec ce qui est construit, ce qui est conçu et ce qui est absent.

## 7. La limite

Ce qui est construit : quatorze des vingt-deux formes d'un nom tournent, certaines avec d'autres exemples que ceux de l'article, et trois autres tournent sous une autre forme. La bibliothèque lit un nom comme une phrase. Et la portée tourne dans les verbes de l'expression régulière, dans le système et dans le placement d'un déploiement. L'article compte vingt-trois sections : les vingt-deux formes d'un nom, et « small functions », qui sont des fonctions et non une forme de nom. Le nombre du livre est vingt-deux, les formes d'un nom.

Ce qui est conçu : les formes de Haro comme données, avec des familles générées ; et le paradigme de portée pour le temps, les unités, la mémoire et le style, comme lignes d'un tableau.

Ce qui est absent, et la page doit dire chacune avec ce qui existe à côté :

- **Partielle**, `@Removed`, n'est que dans l'archive : l'appel n'est pas défini.
- **Future**, `BeforeQ`, a été écourtée exprès, comme je l'ai dit.
- **Libre**, le suffixe qui laisse un appel donner ses paramètres dans n'importe quel ordre et n'importe quel sous-ensemble : il n'y en a aucune définition hors de l'archive. L'analyseur propre de la bibliothèque connaît le nom `FX` et pas `FF`. Les deux narrations qui la racontent emploient deux noms, et le code n'a ni l'un ni l'autre.
- **Par défaut**, `dftRange` et `infRange` : non définis ; le commentaire de la bibliothèque appelle la forme informante pas encore construite.
- **Multilingue**, une méthode nommée en français ou en arabe : absente de la bibliothèque vivante. Les noms existent dans l'archive. Ce qui s'en approche le plus aujourd'hui, ce sont les paquets de langue du chapitre 11.
- Les trois qui tournent sous une autre forme. La forme d'exception existe, mais l'exemple de l'article n'existe pas. L'ordre libre ne fonctionne que pour le premier ordre : dans ma sonde du 8 octobre, l'appel permuté a terminé le programme avec un statut de un et n'a rien imprimé. Et la forme d'énoncé est à moitié en place : la moitié « All » fonctionne, et la moitié « No » est l'étape suivante. Le propre test classique de la bibliothèque promet vrai sur deux de ses quatre lignes « No », et l'exécution imprime faux sur les quatre.

Du côté de la portée : les verbes de l'expression régulière diffèrent du tableau de conception en deux endroits. `MatchLine` laisse un point traverser une ligne, là où le tableau dit qu'il reste dans une seule, et `MatchOneSegment`, que le tableau propose pour le cas paresseux, n'est pas défini. La portée du système est construite, et le document de conception l'appelle encore conçue : le dossier se contredit lui-même. Le document de conception de la portée, version 1.2 du 16 août 2026, est cité ici comme le texte du document. Le dossier ne dit pas qui l'a écrit, et je ne l'imprime pas comme mien. Le document de fondation du système, du 20 juillet 2026, dit que la fondation est implémentée. Lors d'une exécution de sonde que `data/` n'enregistre pas, 61 des 62 assertions de sa garde narrée ont passé, et la seule assertion qui n'a pas tenu était une limite de temps. Je dis ce que le code fait : la portée du système est construite, avec ce résultat imprimé à côté, et le mot « conçue » du document de conception est celui du document, périmé. Et la concurrence est un plan du dossier sans code : le mot `Concurrently` n'a aucune définition.

## 8. Six portes

**Le programmeur.** Lisez un nom comme une phrase : ses suffixes sont ses paramètres, dans l'ordre.

**L'analyste.** Une position peut arriver comme un nombre ou comme une section ; un nom dit laquelle.

**Le concepteur.** Le préfixe change la sorte de réponse : viz la dessine.

**Le décideur.** Une portée est choisie dans le verbe, donc le cadre est visible là où l'appel est fait, et une revue peut le voir.

**Le formateur.** La bibliothèque analyse un nom en sa phrase, de sorte qu'un apprenant peut lui demander ce que dit une méthode.

**L'agent.** Écrivez la portée dans le verbe. Un appel qui nomme une portée n'est pas déplacé dans un autre cadre par un drapeau posé ailleurs.

## 9. Exercice

Prenez un verbe d'une bibliothèque que vous utilisez et qui se comporte autrement dans deux cadres : un mode, une locale, une cible. Dites en une phrase quel est le cadre caché. Puis écrivez, comme vous voudriez qu'ils soient, deux noms pour le même acte dans les deux cadres, avec le cadre dans le verbe. Avant de rien exécuter dans Softanza, prenez `Match` et `MatchLine` sur un texte de trois lignes et écrivez ce que chacun imprime pour un motif qui s'ancre au début.

Exécutez-le. Si vos deux noms ne diffèrent que par un drapeau, vous n'avez pas encore déplacé le cadre dans le verbe.

Je vous laisse celui-ci, exprès. À la section 3, l'article promettait `SOFTANZA` à partir d'un retrait, et l'exécution a imprimé `STAZA`. Voici ce bloc avec un seul changement, le dernier argument de l'appel :

```haro exercise
o2 = new stzString("SOOooooFFfffTANNnnnZA")
o2.RemoveManyCS([ "o", "f", "n" ], TRUE)
? o2.Content()
```

Exécutez-le. Mettez ce qu'il imprime à côté de ce que l'article promettait et à côté de ce que la première exécution a imprimé. La section 3 dit pourquoi la première exécution n'a pas donné la ligne de l'article ; je n'imprime pas ce que celui-ci donne. Quand vous l'aurez résolu, vous saurez ce que le drapeau de casse décide dans un retrait, et s'il suffit à lui seul à tenir la promesse de l'article.

Le chapitre 9 passe aux motifs de pensée. Il présente le Softanzuter, une représentation computationnelle d'une machine pensante. Il est fondé sur un ou plusieurs Regexuters, qui reconnaissent des motifs de pensée et y réagissent. Avec lui viennent Reaxis et les moteurs.
