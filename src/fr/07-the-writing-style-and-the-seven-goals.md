---
id: the-writing-style-and-the-seven-goals
part: 2
number: 7
title: Le style d'écriture, et les sept buts
spine: false
narrations: [stz-functions-as-linguistic-expressions.md, stz-conditional-code-narration.md, stzlist-in-strings-narration.md, stzstring-vizfind-narration.md, stz-function-forms-narration.md]
site: [craft, principles]
guards: [coderule_narrated, 602_l_function, 59_use_of_the_l_small_function, 527_identifying_lists_inside_a_string, 48_replacebymany, 483_w_and_wf_forms_in_conditional_code, 28_numberofoccurrenceofcharleftside, 646_content, 972_narration_viz-finding_a_recurring_substring, testoor_promises_narrated]
stage:
  built: "les quatorze règles de la maison de la bibliothèque comme un tribunal sur son propre code ; la promesse jugée comme une affirmation ; les petits langages des intervalles, des listes et des conditions dans des chaînes ; l'emplacement du code ; le préfixe viz ; les alternatives et les paramètres nommés dans n'importe quel ordre, en partie"
  designed: "un tribunal qui juge le style d'un programme écrit avec la bibliothèque ; un tribunal qui lit les buts ; la grammaire d'écriture déclarée en Haro ; la forme classique d'un bloc de test comme forme unique"
  absent: "toute machine qui juge le style du code que vous écrivez aujourd'hui ; l'écriture dans n'importe quelle langue humaine du nom d'une fonction ; la phrase quasi naturelle telle que le diaporama l'écrivait ; le code fondé sur eval sur le nom d'un paramètre"
status: draft
rulings: ["12.2", "12.14", "12.16", "12.17", "12.21"]
research: research/ch07.md
---

Dans ce chapitre, je prends le reste du style d'écriture, comme une grammaire de quatorze règles. J'imprime l'état où chaque règle se trouve au commit sur lequel ce livre s'exécute, un bloc là où elle s'exécute et une limite là où elle ne s'exécute pas. Sous la grammaire je mets les sept buts, j'en montre trois dans des blocs et je laisse à l'étude les quatre que je n'ai pas exécutés. J'imprime le tribunal de la maison, les quatorze règles que la bibliothèque tient sur son propre code, et je dis ce qu'il ne lit pas : le code d'un programme écrit avec la bibliothèque. Le principe est celui du chapitre 5, et je ne l'argumente pas de nouveau : ce que vous pensez est ce que vous écrivez.

## 1. Le concept, tel que le terrain le tient

Le mot *style* veut dire deux choses dans le terrain, et je dois dire laquelle j'entends.

Le premier est le style comme mise en page, imposé par un outil. Le guide de style de Python date de 2001, le formateur de Go de 2009, et tout projet exécute un linter avant un commit. Ils jugent la forme d'une ligne : espaces, majuscules, longueur, noms inutilisés. Ils y sont bons, et ils tournent par défaut. Ils ne disent rien de savoir si une ligne suit l'ordre dans lequel son auteur raisonnait.

Le second est le petit langage à l'intérieur du langage. Les programmeurs écrivent déjà de petits langages dans des chaînes, et personne n'appelle cela un style : une expression régulière, un texte SQL, une chaîne de format telle que `"%5.2f"`. Chacun est une notation séparée, avec son propre outil, apprise à part.

Pour les buts, le terrain dit *attributs de qualité*. La norme ISO de qualité logicielle, de 2011, en liste huit, et les méthodes d'architecture les classent avant qu'un système soit dessiné. (Connaissance générale, non une étude du dossier.) Les sept buts de ce chapitre sont une autre liste, choisie pour un autre usage. Ils ne disent pas ce qu'un produit promet à ses utilisateurs. Ils disent ce qu'une fonctionnalité doit servir pour être admise dans une seule bibliothèque.

## 2. Le premier principe

**Ce que vous pensez est ce que vous écrivez.** C'est la phrase du chapitre 5, tirée du schéma de 2020, et je ne l'argumente pas de nouveau. Le chapitre 5 a pris cinq règles du style. Ce chapitre prend le reste, comme une grammaire, puis les buts sous lesquels la grammaire a été conçue.

Pour les buts, le point est celui de l'auteur, tel que l'étude le rapporte, et non une citation datée. Une architecture logicielle orientée par les buts est la seule façon pour un architecte de maîtriser un projet de cette taille.

## 3. La forme Softanza

L'étude du dossier a écrit le style en quatorze règles, dans sa décision 12.16, à partir de la lecture du code. Ce sont des lectures du code, énoncées comme des règles, et non une norme que quelqu'un a signée. Les voici avec l'état où chacune se trouve au commit sur lequel ce livre s'exécute. Je mets la table d'abord parce qu'elle montre quelles règles portent un bloc et lesquelles portent une limite.

| # | Règle | État à ce commit |
|---|---|---|
| 1 | Une valeur est élevée à son objet par `Q()` ou un élévateur typé | s'exécute ; chapitre 5 |
| 2 | Une scène est un bloc d'accolades sur un seul objet | s'exécute ; chapitre 5 |
| 3 | Chaque ligne imprimée porte sa réponse sous `#-->` | jugé par une machine ; chapitre 5 |
| 4 | Un paramètre est nommé, et le nom se lit comme de l'anglais | s'exécute ; chapitre 5, et ici dans n'importe quel ordre |
| 5 | Une chaîne reflète l'ordre de la pensée, une étape par ligne | s'exécute ; chapitre 5 |
| 6 | La forme du verbe dit ce qui arrive | s'exécute ; chapitres 5 et 8 |
| 7 | Les suffixes et les préfixes sont petits et veulent dire une seule chose chacun | en partie : `CS`, `XT`, `viz` s'exécutent ; les familles `FF`, `dft` et `inf` du diaporama ne sont pas définies |
| 8 | Une fonction a des alternatives pour la façon dont une personne la dit | en partie |
| 9 | Précision plutôt que généralité, quand cela ne coûte rien | en partie |
| 10 | Le code voyage à l'intérieur d'un argument comme une petite chaîne | l'emplacement s'exécute ; le `@` sur le nom d'un paramètre est retiré |
| 11 | De petits langages littéraux vivent dans des chaînes | s'exécute sous une forme ; la forme à accolades lève une erreur |
| 12 | Une phrase peut être quasi naturelle | pas de ce chapitre ; aucune des trois formes du diaporama ne s'est exécutée telle qu'écrite |
| 13 | Une fonction peut être nommée dans n'importe quelle langue humaine | ne s'exécute pas |
| 14 | Un commentaire parle avant le code, dans la voix du maître | s'exécute |

La règle 11 d'abord, parce que c'est la plus étrange. Le langage hôte compte en entiers et coupe les décimales. Que garde un intervalle écrit à l'intérieur d'une chaîne ? Les commentaires ci-dessous parlent avant le code, dans la voix du maître, ce qui est la règle 14. Exécutez-le :

```haro
# The host's own range counts in integers: the decimals are cut. Softanza reads
# a small language inside a string, and keeps the decimals, the numbered words,
# and the letters of any script:
? @@( 1.02 : 3.08 )
#--> [ 1, 2, 3 ]
? @@( L("1.02:1.05") )
#--> [ 1.02, 1.03, 1.04, 1.05 ]
? @@( L('"♥1" : "♥3"') )
#--> [ "♥1", "♥2", "♥3" ]
? @@( L(' "ا" : "ج" ') )
#--> [ "ا", "ب", "ة", "ت", "ث", "ج" ]
```

L'hôte répond `[ 1, 2, 3 ]` à `1.02 : 3.08`. La chaîne répond `[ 1.02, 1.03, 1.04, 1.05 ]` : Softanza lit un petit langage d'intervalles à l'intérieur de la chaîne et garde les décimales, les mots numérotés et les lettres de n'importe quelle écriture. Le langage d'intervalles est un argument comme un autre. Il donne les remplacements pour chaque occurrence, dans l'ordre, et la forme étendue reboucle la palette quand les occurrences la dépassent en nombre :

```haro
o1 = new stzString("haro php ruby haro python haro")
o1.ReplaceByMany("haro", L('"♥1" : "♥3"'))
? o1.Content()
#--> ♥1 php ruby ♥2 python ♥3
o2 = new stzString("haro php ruby haro python haro ruby haro")
o2.ReplaceByManyXT("haro", L('"♥1" : "♥3"'))
? o2.Content()
#--> ♥1 php ruby ♥2 python ♥3 ruby ♥1
```

Une liste peut aussi être portée comme une chaîne dans sa forme courte, reconnue, convertie entre les formes et réévaluée :

```haro
? StzStringQ('1:3').IsListInString()
#--> TRUE
? @@( StzStringQ('[1,2,3]').ToListInShortForm() )
#--> "1 : 3"
? @@( StzStringQ(' "A":"C" ').ToList() )
#--> [ "A", "B", "C" ]
```

Règle 10 : le code voyage à l'intérieur d'un argument comme une petite chaîne avec un espace réservé, `@char` pour les caractères d'une chaîne et `@item` pour les éléments d'une liste. Le chapitre 6 a montré l'emplacement sur une liste. Ici il est sur une chaîne, où il trouve et retire par une règle et non par une boucle :

```haro
o1 = new stzString("SOooooFTAaaannnNZA")
? @@( o1.FindW('{ Q(@char).IsUppercase() }') )
#--> [ 1, 2, 7, 8, 9, 16, 17, 18 ]
o1.RemoveW('{ Q(@char).IsLowercase() }')
? o1.Content()
#--> SOFTANZA
```

Le diaporama de 2022 écrit le même appel avec un emplacement nommé, `:Where = '...'`, et cette forme lève une erreur sur une chaîne à ce commit. Je ne la montre pas. Le même diaporama met un `@` à la fin du nom d'un paramètre, `:With@`, pour marquer que sa valeur est du code à évaluer. Cette forme est retirée. L'en-tête d'une garde le dit : les formes fondées sur eval sont retirées. Le diaporama lui-même marque la forme « TODO ». Le code voyage maintenant dans l'emplacement comme une chaîne bornée que le moteur évalue, ou comme une fonction.

Règle 8 : le même acte peut se dire en deux ordres de mots, avec le nom du conteneur, ou avec le côté épelé de quatre façons. Chaque paire est un seul acte, avec deux définitions. La propre narration de la bibliothèque appelle la première avec deux arguments et elle lève une erreur ; les gardes passent la position de départ, et le bloc aussi :

```haro
o1 = new stzList([ 1, 2, "♥", 4, 5, "♥", "♥" ])
? o1.FindNthNext(2, "♥", :StartingAt = 1)
#--> 6
? o1.FindNextNth(2, "♥", :StartingAt = 1)
#--> 6
? Q("---haro").NumberOfOccurrenceOfCharLeftSide("-")
#--> 3
? Q("---haro").HowManyOccurrenceOfCharStartSide("-")
#--> 3
o2 = new stzList([ "C", "B", "A" ])
o2.SwapItems(:AtPositions = 1, :And = 3)
? @@( o2.Content() )
#--> [ "A", "B", "C" ]
```

Le diaporama promettait davantage. Une famille de cinq noms en `CharsRemoved`, pour retirer des caractères aux bouts, est nommée dans le diaporama. Deux sont définis, `LeadingCharsRemoved` et `TrailingCharsRemoved`. Trois ne le sont pas : `LeadingAndTrailingCharsRemoved`, `TrailingAndLeadingCharsRemoved` et `RepeatedCharsRemoved`. `RemoveLeadingAndTrailingChars` est défini, et n'est pas l'un des cinq.

Règle 9 : la précision plutôt que la généralité. Le nom précis dit ce qui est compté. Les caractères d'une chaîne sont comptés par `NumberOfChars`, et `Size()` est la longueur en octets de l'hôte. Les deux réponses diffèrent-elles sur un mot arabe ? Exécutez-le :

```haro
? Q("سلام").NumberOfChars()
#--> 4
? Q("سلام").NumberOfBytes()
#--> 8
? Q("سلام").Size()
#--> 8
o1 = new stzList([ "tea", "rice", "fish", "salt" ])
? o1.ContainsBoth("tea", "fish")
#--> TRUE
? o1.ContainsAll([ "tea", "oil" ])
#--> FALSE
```

L'exécution répond `4` à l'un et `8` à l'autre, sur un mot de quatre lettres ! La propre ligne de documentation de la bibliothèque pour `NumberOfChars` liste *size* parmi ses mots alternatifs. L'exécution montre que `Size()` ne veut pas dire cela. Je le liste parmi les demandes.

Règle 7 : un préfixe `viz` montre la réponse sous le mot, et le suffixe `XT` ajoute les positions comme des nombres :

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

La narration et le diaporama écrivent `vizFindAll` sur une chaîne. Il n'y existe pas à ce commit, et `vizFind` si. Une liste a son propre `VizFindAll`.

### Les buts

Sous la grammaire il y a sept buts, écrits dans le diaporama de 2022 comme une matrice de trente-trois fonctionnalités. La décision 12.14 de l'étude les lit comme le squelette architectural de la bibliothèque : une fonctionnalité qui n'en sert aucun est refusée, et un but sans fonctionnalité est un écart. Le résumé de l'étude est la lecture d'une session et non un texte de la bibliothèque, et aucun document de la bibliothèque n'énonce la règle en ces mots. Le plus proche est le document de conception du moteur : le moteur doit permettre les sept.

Je ne listerai pas les sept comme une table de slogans. Voici ce qui s'exécute de trois d'entre eux.

**Flexibilité : l'ordre des paramètres nommés est libre.** Deux appels, avec les paramètres dans deux ordres, sont le même appel :

```haro
o1 = new stzString("----@@--@@-------@@----@@---")
o1.ReplaceNextNthOccurrence(2, :Of = "@@", :StartingAt = 12, :With = "##")
? o1.Content()
#--> ----@@--@@-------@@----##---
o2 = new stzString("----@@--@@-------@@----@@---")
o2.ReplaceNextNthOccurrence(2, :With = "##", :StartingAt = 12, :Of = "@@")
? o2.Content()
#--> ----@@--@@-------@@----##---
```

Une tension doit être dite avec. La conception de Haro refuse les paramètres à ordre libre comme grammaire, et la bibliothèque les garde. Deux faits sont vrais aujourd'hui. Le bloc ci-dessus les exécute, donc ils sont dans la bibliothèque. La grammaire à laquelle une machine est tenue les laisse de côté, par le principe de Haro. Que la bibliothèque les garde au-delà de cette grammaire ou les retire, c'est une décision que le dossier ne tient pas, et je ne la prends pas ici : ils sont gardés, et ils ne sont pas de la grammaire.

**Cohérence : un vocabulaire à travers une chaîne et une liste.** Le même verbe répond sur les deux :

```haro
? @@( StzStringQ("hello").FindAllCS("L", :CaseSensitive = 0) )
#--> [ 3, 4 ]
? @@( StzListOfStringsQ([ "h", "e", "l", "l", "o" ]).FindAllCS("L", :CaseSensitive = 0) )
#--> [ 3, 4 ]
? Q("").IsEmpty()
#--> TRUE
? Q([]).IsEmpty()
#--> TRUE
```

La perte à côté, du même groupe de diapositives : le conseil du diaporama d'employer le mot-clé Item avec tout type énumérable ne tient pas. `NumberOfItems()` sur une chaîne lève une erreur, et sur une liste il répond.

**Maniabilité : un échec qui dit où, quoi, pourquoi, et que faire.** La bibliothèque lève une erreur en quatre champs. Je n'imprime pas son message, parce que, dans l'exécution de recherche, sa première ligne portait un numéro de ligne de la bibliothèque, et un numéro de ligne n'est pas une promesse.

Les quatre autres buts (l'expressivité, la fiabilité, les métaphores humaines et les abstractions pratiques) je les laisse aux tables de l'étude. Je ne les ai pas exécutés pour ce chapitre, et je ne décrirai pas d'après le diaporama ce que je n'ai pas exécuté.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé un style qu'on aurait changé quand l'IA est devenue l'outil d'écriture principal.** L'étude rapporte la déception de l'auteur en ces termes, et le chapitre 5 la raconte. Le code d'implémentation que l'IA a écrit est accepté comme bon. Ce qui est exigé, c'est que chaque ligne qu'un programmeur, humain ou agent, est prié d'écrire avec Softanza embrasse le style historique.

**J'ai refusé un but qui ne vit que dans un document.** Les sept buts sont écrits dans un document de conception et dans des balises qu'aucun tribunal ne lit. La trouvaille de l'étude est qu'il n'y a de tribunal sur aucun des deux.

**J'ai refusé de cacher le coût du style.** L'étude a mesuré des marqueurs par millier de lignes. Les gardes narrées, les fichiers de test écrits pour être lus comme des articles, portent la promesse `#-->` à moins d'une ligne par millier, et un appel à la fonction d'aide d'assertion à quatre-vingt-cinq. Les tests numérotés plus anciens portent la promesse à cinquante-deux. Le code de la bibliothèque porte la promesse à moins de deux. Le style a survécu là où l'auteur écrivait pour un lecteur, et s'est amenuisé là où l'IA écrivait pour d'autres. Un marqueur est une lecture du texte, non un jugement du code ; l'étude le dit elle-même.

**J'ai refusé de recompter les balises comme les miennes.** Les formes des fonctions sont marquées dans le code par des info-balises, dans des commentaires qui commencent par `#<` et un `@`, appliquées à la main. L'étude y lit le vocabulaire, au niveau des fonctionnalités, de deux buts, l'expressivité et la flexibilité, et en a compté 6 090. J'ai recompté le 8 octobre 2026, avec la commande du fichier de recherche, et j'en ai trouvé 6 126, avec 89 orthographes. Mais 1 360 d'entre elles se trouvent hors des dossiers d'archive, et 4 766 dans les dossiers d'archive. Donc la phrase « appliquées à la main en 6 090 points » est, à ce commit, surtout une phrase sur l'archive. Aucune garde ne les lit : la couche de réflexion lit le nom d'une méthode, avec une grammaire, et non sa balise.

**J'ai refusé le décompte comme un compte de réussites.** L'étude compte trente-trois fonctionnalités : vingt-quatre construites, quatre transformées avec le projet, deux qui ont changé de forme, une partielle, une archivée, une seulement un nom. L'arithmétique tient. Mais c'est un compte de noms trouvés, et une définition trouvée n'est pas un test qui passe. Plusieurs des fonctionnalités sont nommées dans le diaporama et ne sont pas définies dans le code de la bibliothèque, l'archive mise à part. Ce sont les familles `FF` et `FX` pour les sections, les familles `dft` et `inf` pour les défauts et les infinis, `WalkFF` et `AddWalkerFF`, et le `Check` sur une liste. Ce dernier est le vérificateur du diaporama, qui répond 1 ou 0 pour chaque élément. Deux sont définies et répondent à tort sur certains exemples du diaporama : `Yield`, qui devrait donner le résultat d'une expression pour chaque élément, et `Perform`, qui devrait appliquer une action à chaque élément. J'imprime le décompte, et j'imprime ses pertes avec lui. Le diaporama dit aussi « 7 causes racines de la complexité de la programmation », à côté des sept buts. Aucune diapositive ne liste ces sept causes, et aucun autre fichier du dossier ne les nomme : le chapitre n'en nomme aucune et ne les met pas en correspondance avec les buts, une par une.

## 5. Le tribunal

`coderule_narrated` prouve qu'une règle de la maison est une règle sur le graphe du code ; que le code planté est trouvé par son nom ; que le code propre passe ; et que la bibliothèque en liste quatorze. `testoor_promises_narrated` prouve que la promesse `#-->` est jugée comme l'affirmation d'un arrêt : tenue, divergente, non atteinte ou non jugée. `602_l_function` et `59_use_of_the_l_small_function` prouvent le langage d'intervalles. `527_identifying_lists_inside_a_string` prouve les listes hébergées dans des chaînes. `48_replacebymany` prouve que les remplacements se font dans l'ordre. `483_w_and_wf_forms_in_conditional_code` prouve la condition dans une chaîne, en deux écritures du même balayage. `28_numberofoccurrenceofcharleftside` prouve les noms alternatifs en arabe comme en latin, et porte une note disant que la promesse de l'archive était fausse et que l'implémentation fait autorité. `646_content` prouve les paramètres nommés. `972_narration_viz-finding_a_recurring_substring` prouve la visite viz.

Voici le tribunal de la maison lui-même, les quatorze règles de la bibliothèque et non les quatorze du style. La coïncidence numérique est une coïncidence. Que répond-il à une faute d'orthographe plantée, et à une écriture plantée sur une constante ? Exécutez-le :

```haro
? @@( StzCodeRuleNames() )
#--> [ "no-len-method", "q-returns-object", "no-aggressive-verbs", "engine-first", "q-has-plain-twin", "no-case-collision", "dead-knob", "setter-resets-on-reject", "setter-only-moves-one-way", "misspelled-name", "library-prints", "empty-method-body", "writes-a-mutable-constant", "value-called-as-function" ]
cOne = "class Inbox" + nl + "def Recieve(x)" + nl + "	return x" + nl
? StzCheckCode(cOne)[1][:rule]
#--> misspelled_name
? StzCodeIsClean(cOne)
#--> TRUE
cTwo = "class Inbox" + nl + "def Count()" + nl + "	nl = 3" + nl + "	return nl" + nl
? StzCheckCode(cTwo)[1][:rule]
#--> writes_a_mutable_constant
? StzCodeIsClean(cTwo)
#--> FALSE
```

La faute d'orthographe est trouvée par son nom, `misspelled_name`, et le code reste propre, `TRUE`, parce que c'est un avertissement. L'écriture sur une constante est trouvée par son nom, `writes_a_mutable_constant`, et le code est refusé, `FALSE`, parce que c'est une erreur.

Un détail d'orthographe, pour l'annexe B : la liste des noms emploie des traits d'union, et le constat de huit des quatorze revient avec des soulignés. Le bloc montre ce que l'exécution a imprimé.

Ce que le tribunal ne lit pas, c'est le code d'un programme écrit avec la bibliothèque. Aucune des quatorze règles de la maison n'est une règle d'écriture.

## 6. Le terrain, et où il mène

Le terrain mène en application par défaut. Un formateur s'exécute à chaque commit. Pour le code qu'un programmeur écrit avec Softanza, l'application aujourd'hui est nulle, et le chapitre 5 le dit.

Le terrain mène en ayant ses buts quelque part où un lecteur regarde d'abord. Les sept buts sont dans un document de conception et dans des balises qu'aucun tribunal ne lit, et les notes de fonctionnement du dépôt propre de la bibliothèque n'en nomment aucun. Le récit d'un lecteur IA de la bibliothèque dit que soixante documents de paradigme pourraient aisément être soixante idées déconnectées. L'étude y lit un signe que la discipline est dans le code et écrite nulle part où un lecteur regarderait d'abord. C'est un document de session, et non un témoin indépendant.

Le site a montré un jour un dialecte réduit : ses blocs n'avaient ni paramètre nommé ni scène. Il a depuis mis les quatorze règles sur sa page Craft et les règles comme données. Je n'ai pas remesuré les blocs du site après cela.

Là où je pense que le style se distingue, c'est que chaque règle sert une étape de pensée, et que chaque étape a une forme écrite (étude 12.17). La forme du verbe est un contrat sur l'objet. Et la promesse sous la ligne est l'exemple, le test et la documentation à la fois. La matrice de 2022 a servi de squelette à un architecte pour environ trois cent mille lignes écrites à la main.

## 7. La limite

Ce qui est construit : les quatorze règles de la maison de la bibliothèque comme un tribunal sur son propre code, exécutées dans le bloc ci-dessus ; la promesse jugée par une machine ; les petits langages, l'emplacement, le préfixe. Et les fonctionnalités qui s'exécutent (`CS`, `XT`, `ZZ`, `viz`, les paramètres nommés, le même verbe sur une chaîne et une liste).

Ce qui est conçu :

- **Un tribunal qui juge le style d'un programme écrit avec la bibliothèque.** C'est une spécification dans l'étude : les quatorze règles comme règles de la maison sur le graphe d'un extrait. Ses exemples sont un argument positionnel là où un argument nommé existe, ou une ligne imprimée sans promesse. Je l'ai cherché dans la bibliothèque et je n'ai rien trouvé.
- **Un tribunal qui lit les buts.** Il lirait les balises. Non construit.
- **La forme classique du bloc de test comme forme unique des nouveaux blocs.** Le jugement de l'étude est que le retour « n'est pas une réécriture » mais une décision. La forme classique est la forme unique des nouveaux blocs, et les blocs convertis restent tels qu'ils sont. Le README de l'arbre de tests dit encore de la forme classique qu'elle est la surface de test faisant autorité. Je n'ai trouvé aucune décision qui en fasse la forme unique : cela reste une décision, et le chapitre 5 la nomme.
- **La grammaire d'écriture déclarée en Haro.** La moitié vocabulaire existe : les formes des noms de la bibliothèque sont des données en Haro, et le relevé de la session est de 584 orthographes livrées sur 595 qui concordent. La moitié usage, la scène, la chaîne, l'emplacement du code et la promesse, n'est pas déclarée.
- **La discipline déclarée une fois.** En partie faite sur le site, comme données, ce qui est la source de la page et non un tribunal.

Ce qui est absent :

- Toute machine qui juge, aujourd'hui, le style d'un programme écrit avec la bibliothèque.
- Les règles 12 et 13 comme formes qui s'exécutent. Dans les exécutions de la session de recherche, les exemples quasi naturels du diaporama ne s'exécutaient pas tels qu'écrits, ni une fonction nommée en chinois ou en français.
- Le `@` sur le nom d'un paramètre comme forme qui fonctionne.
- La forme à accolades du langage d'intervalles, `L('{ "♥1" : "♥6" }')`, qui lève une erreur, et les intervalles qui changent de largeur, comme `day8 : day11`, qui lèvent aussi une erreur, avec une erreur de variable non initialisée de l'hôte. Le constructeur de liste à partir d'une chaîne en lève une aussi. Ces trois constats viennent des exécutions de la session de recherche ; aucun bloc de ce chapitre ne les garde.
- La pile d'appels visualisée, et les décorateurs de cache et de journal, qui existent comme noms dans des commentaires.

## 8. Six portes

**Le programmeur.** Quatorze règles contre lesquelles vous pouvez tenir votre propre ligne. Élevez la valeur, demandez dans une scène, mettez la réponse sous `#-->`, nommez le paramètre, chaînez une étape par ligne, lisez la forme du verbe ; et mettez un intervalle, une condition ou une palette dans une chaîne.

**L'analyste.** Les mots de votre problème deviennent les noms des étapes. Une règle écrite dans une chaîne est une règle que vous pouvez stocker et lire, et non du code auquel vous devez faire confiance.

**Le concepteur.** Le préfixe viz dessine la réponse là où l'œil l'attend. Les buts sont les rubriques sous lesquelles une conception est jugée, une fonctionnalité à la fois.

**Le décideur.** Sept buts et trente-trois fonctionnalités sont une grille de lecture. Selon la lecture de l'étude, une fonctionnalité qui n'en sert aucun est refusée, et un but sans fonctionnalité est un écart. Le décompte est imprimé avec ses pertes.

**Le formateur.** La discipline s'enseigne entière et dans l'ordre. La garde convertie pour les listes dans des chaînes garde en commentaire l'espacement erroné de l'ancienne promesse, ce qui est une leçon sur le coût des réponses tapées à la main.

**L'agent.** Les règles vous sont données comme données sur le site. Pour le code que vous écrivez, le tribunal reste une spécification. Écrivez la question, puis la promesse dessous, et mettez votre condition dans l'emplacement, non dans l'évaluation d'une chaîne.

## 9. Exercice

Écrivez, avant d'exécuter quoi que ce soit, la ligne dont chaque tâche a besoin et la promesse dessous :

1. À partir d'une chaîne, la liste `[ "♥7", "♥8", "♥9" ]`.
2. La chaîne `"haro php haro"` avec les deux `haro` numérotés `♥1` et `♥2`, en un seul appel qui emploie le petit langage de la tâche 1.
3. La liste `[ "C", "B", "A" ]` ordonnée en échangeant les premier et troisième éléments, avec les positions nommées.
4. Le nombre de caractères de `"سلام"`, avec le nom qui dit ce qui est compté.
5. Une supposition : qu'imprime `L("day8 : day11")` ?

```haro exercise
# 1.
# 2.
# 3.
# 4.
# 5.
```

Exécutez-le. Pour la cinquième, vous aviez le droit de vous tromper, et vous vous êtes probablement trompé : l'intervalle change de largeur, alors l'hôte lit `day8` comme une variable, et il lève une erreur. C'est la limite du petit langage, apprise en étant surpris une fois. Ne changez pas votre promesse pour qu'elle corresponde à la sortie. Expliquez d'abord la sortie.

Le chapitre 8 prend le nom d'une fonction en entier, comme une expression linguistique, puis la portée : ce nom est une phrase, et ses préfixes, ses suffixes et ses paramètres sont une grammaire que la bibliothèque peut lire.
