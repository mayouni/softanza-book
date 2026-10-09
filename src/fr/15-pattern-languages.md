---
id: pattern-languages
part: 3
number: 15
title: Les langages de motifs
spine: false
narrations: [stznumbrex-pattern-language-for-number.md, stztablex-pattern-langauge-for-tables.md.md, stzlistex-pattern-matching-for-lists.md, stzTimex-A-Pattern-Language-for-Time-in-Softanza.md, stzMatrex-Declarative-Pattern-Matching-for-Matrices.md]
site: [languages]
guards: [00_regex_narrated, 00_numbrex_narrated, tablex_narrated, 00_matrex_narrated, 00_graphex_narrated]
stage:
  built: "des motifs pour le texte, les nombres et les tableaux, chacun avec une garde ; la même petite habitude d'un support à l'autre (un constructeur, un motif dans une chaîne de caractères, Match, Tokens)"
  designed: "un seul moteur de motifs partagé par tous les supports ; le motif comme côté condition de la cascade ; le motif écrit à partir d'exemples"
  absent: "le refus d'un mot que le langage de motifs ne connaît pas, dans les six supports ; des séquences sur une ligne de temps, dans le temps ; une narration et une petite fonction pour les graphes ; les classes sœurs génétique, linguistique et quantique"
status: draft
rulings: ["12.4", "12.18", "12.26"]
research: research/ch15.md
---

## 1. Le concept, tel que le terrain le tient

Pour un programmeur qui travaille, un motif est une expression régulière : une notation compacte de la forme d'une chaîne de caractères, remise à un moteur qui dit si le texte lui correspond, et où. Les moteurs sont anciens et bien connus. Celui qui est sous cette bibliothèque est PCRE2, et le site le mesure contre deux autres.

Pour les données qui ne sont pas du texte, le terrain emploie d'autres outils, un par support et aucun partagé. La mise en correspondance structurelle de motifs dans les langages de la famille ML, en Rust, et depuis Python 3.10 en Python. Les vérifications de schéma pour les listes et les enregistrements. Les bibliothèques de qualité des données pour les tableaux. La reconnaissance de motifs de lignes en SQL, et les moteurs de flux, pour les séquences dans le temps. Et les langages de requête de graphes, dont le cœur est un motif de chemin. (Connaissance générale, bien établie ; le dossier ne contient aucune étude datée d'aucun d'eux, et je n'en invente aucune.)

L'étude de terrain du domaine de projets lui-même, d'août 2026, donne le profil des petits langages qui ont survécu : une grammaire fermée, une question de domaine, du texte brut, une surface minuscule, une spécification avec une suite de conformité, des décennies de stabilité. Un langage de motifs est exactement cela. Une question, ces données correspondent-elles, en quelques caractères. Ce que le terrain n'offre pas, c'est la même notation d'un support à l'autre.

## 2. Le premier principe

**Un motif est une règle sur la forme des données, écrite comme des données. La même habitude sert tous les genres de données.**

La phrase à laquelle reviennent les articles de la bibliothèque, dans chaque support, est celle de l'article sur les nombres : au lieu d'indiquer à la machine comment tester une condition, vous énoncez ce que vous voulez dire. Le dossier de l'étude, qui n'est pas l'étude de terrain ci-dessus, porte aussi une phrase qu'elle dit de l'auteur, « pour la première fois dans l'histoire de l'informatique ». Je ne l'ai trouvée dans aucun texte de la bibliothèque, et l'étude ne laisse pas le site la revendiquer ; le chapitre l'imprime comme l'attribution de l'étude et n'affirme pas plus que l'étude ne permet. L'affirmation que l'étude permet est la mesurée : une seule grammaire en forme de regex pour sept genres de données dans une seule bibliothèque, avec la même habitude de petite fonction. Et je vais vous montrer tout de suite que la grammaire n'est pas tout à fait une.

## 3. La forme Softanza

Un motif appelé par son nom est un catalogue fermé. La bibliothèque a un fichier de données de motifs nommés, et demander un nom qu'elle ne tient pas est refusé :

```haro
? rx(pat(:isoDate)).Match("2023-12-25")
#--> 1
? rx(pat(:isoDate)).Match("25/12/2023")
#--> 0
? rx(pat(:isoDate)).Explain()
#--> Matches ISO 8601 date format (YYYY-MM-DD)
try
	pat(:banana)
catch
	? cCatchError
done
#--> The pattern name you provided does not exist in stzRegexData file.
```

Un motif peut aussi répondre à la valeur à moitié écrite, ce que veut un formulaire pendant que la personne tape :

```haro
o1 = new stzRegex("^\d{3}-\d{2}-\d{4}$")
? o1.MatchAsYouType("123-45")
#--> 1
? o1.MatchAsYouType("abc")
#--> 0
? o1.IsPartialMatch("123-45")
#--> 1
? o1.IsPartialMatch("123-45-6789")
#--> 0
```

Voici maintenant le geste qui donne son titre au chapitre. Prenons une liste. Son motif s'écrit entre crochets, et les comptes, l'imbrication et la négation sont écrits, non bouclés. `@N` représente un nombre, `@S` une chaîne de caractères, `+` un ou plus, `@N1-3` un à trois, et `@!` le non :

```haro
? Lx("[@N+, @S]").Match([1, 2, 3, "end"])
#--> 1
? Lx("[@N1-3, @S]").Match([1, 2, 3, 4, "end"])
#--> 0
? Lx("[@S, [@N+]]").Match(["tea", [1, 2, 3]])
#--> 1
? Lx("[@S, [@N+]]").Match(["tea", ["x"]])
#--> 0
? Lx("[@!N, @N]").Match(["a", 1])
#--> 1
? Lx("[@!N, @N]").Match([1, 1])
#--> 0
```

Chaque appel ici utilise un objet neuf, pour une raison que donne la section 7. Le chapitre 11 a montré quatre appels du même langage, et je ne les répète pas.

Les nombres ont des propriétés, et une propriété est du sens, non de la procédure. La dernière ligne fait passer un motif d'un test à une recherche :

```haro
? Nx("{@Property(Even) & @Property(Prime)}").Match(2)
#--> 1
? Nx("{@Property(Even) & @Property(Prime)}").Match(4)
#--> 0
? Nx("{@Digit(:unique)+}").Match(1234)
#--> 1
? Nx("{@Digit(:unique)+}").Match(1223)
#--> 0
? Nx("{@Relation(Mod:5=0)}").Match(10)
#--> 1
? @@( Nx("{@Property(Perfect)}").MatchingNumbersBetween(1, 500) )
#--> [ 6, 28, 496 ]
```

Les tableaux : une règle de qualité des données est une phrase du langage. La personne qui possède les données peut la lire. Niamey apparaît deux fois, donc les villes ne sont pas uniques, et la négation de cela est vraie :

```haro
oT = new stzTable([
	[ :ID, :NAME, :AGE, :CITY ],
	[ 1, "Ali", 28, "Niamey" ],
	[ 2, "Sara", 32, "Paris" ],
	[ 3, "Omar", 41, "Niamey" ],
	[ 4, "Awa", 25, "Dakar" ]
])
? Tbx("{cols(4) & unique(id) & avgcol(age:>30)}").Match(oT)
#--> 1
? Tbx("{cols(4) & unique(city)}").Match(oT)
#--> 0
? Tbx("{@!unique(city)}").Match(oT)
#--> 1
? Tbx("{sorted(id) & numeric(age) & alphabetic(name)}").Match(oT)
#--> 1
```

Un motif est une donnée, donc les motifs se composent : on en construit un à partir de motifs.

```haro
oA = new stzTablex("{cols(4)}")
oB = new stzTablex("{rows(4)}")
oAnd = oA.And_(oB)
? oAnd.Pattern()
#--> {cols(4) & rows(4)}
? oAnd.Match(oT)
#--> 1
? oA.Not_().Pattern()
#--> {@!cols(4)}
? oA.Not_().Match(oT)
#--> 0
```

Une matrice : un concept, carrée et symétrique, tient en une ligne.

```haro
? Mx("{shape(square) & property(symmetric)}").Match([ [1,2,3], [2,4,5], [3,5,6] ])
#--> 1
? Mx("{shape(square) & property(symmetric)}").Match([ [1,2,3], [4,5,6], [7,8,9] ])
#--> 0
? Mx("{size(2x3)}").Match([ [1,2,3], [4,5,6] ])
#--> 1
? Mx("{property(identity)}").Match([ [1,0], [0,1] ])
#--> 1
```

Le temps, dans la part qui s'exécute. Une durée doit satisfaire une règle : quatre-vingt-dix minutes sont dans l'intervalle d'une à deux heures et sur un pas d'un quart d'heure ; quatre-vingts y sont et hors du pas ; trois heures sont dehors.

```haro
oTm = new stzTimex("{@Duration(1h..2h:15min)}")
? oTm.Match(new stzDuration("1 hour 30 minutes"))
#--> 1
? oTm.Match(new stzDuration("1 hour 20 minutes"))
#--> 0
? oTm.Match(new stzDuration("3 hours"))
#--> 0
```

Un graphe : un motif se lit comme le chemin qu'il cherche. Les étiquettes correspondent sans égard à la casse, et le sens compte, comme le montre la deuxième ligne :

```haro
g = new stzGraph("Order")
g.AddNodeXT(:a, "Placed")
g.AddNodeXT(:b, "Cooking")
g.AddNodeXT(:c, "Served")
g.AddEdgeXT(:a, :b, "starts")
g.AddEdgeXT(:b, :c, "finishes")
? (new stzGraphex("{@Node(placed) -> @Edge(starts) -> @Node(cooking)}", g)).Match(g)
#--> 1
? (new stzGraphex("{@Node(served) -> @Node(placed)}", g)).Match(g)
#--> 0
? (new stzGraphex("{@Node(placed) -> @!Node(refunded)}", g)).Match(g)
#--> 1
```

Enfin, l'habitude. Le motif est une donnée dans chaque langage, et un langage qui expose ses jetons peut être relu par une personne et par un agent. Cinq des six langages le font :

```haro
? len( Lx("[@N, @S]").Tokens() )
#--> 2
? Lx("[@N, @S]").Tokens()[2][:type]
#--> string
? Nx("{@Property(Even) & @Property(Prime)}").Tokens()[1][:type]
#--> conjunction
? len( Mx("{shape(square) & property(symmetric)}").Tokens()[1][:conditions] )
#--> 2
```

Les graphes n'ont ni `Tokens`, ni `Pattern`, ni `Explain` qui fonctionne à ce commit, et pas de petite fonction non plus. Il n'y a pas de `Gx`, et il n'y a pas de `Tx` pour le temps, bien que le tableau de l'étude nomme les deux. Les petites fonctions sont `rx`, `Lx`, `Nx`, `Tbx`, `Mx` et `Tmx`.

## 4. La décision, et ce que j'ai refusé

**J'ai décidé qu'un motif énonce un sens et non une procédure.** Cette décision est dans les articles, et les articles sont les miens. Les mêmes ont décidé de porter l'idée de la regex aux données qui ne sont pas du texte avec une seule habitude : des accolades, un `@` pour un jeton, `&`, `|`, `@!` pour le non, `@cs:` pour la casse. Les listes gardent les crochets. Les cinq autres utilisent des accolades. C'est la première correction honnête de l'expression « une seule grammaire ».

**J'ai refusé de réinventer la notation pour le texte.** Les correspondances simples sont gardées : une chaîne de motif classique, les groupes nommés et les captures fonctionnent comme écrits. Des noms plus clairs sont posés autour. Le travail plus ancien sur le nommage est gardé comme histoire, pour sa valeur éducative, ce qui est la bonne façon de mettre à la retraite un mécanisme.

**J'ai refusé, pour l'instant, de construire les classes sœurs.** Les articles prévoyaient des classes dans lesquelles les motifs sont génétiques, linguistiques ou quantiques. L'article dit qu'elles sont dans un prototype précoce et non dans la bibliothèque, et une recherche dans le dossier de la regex des mots « induce », « from example » et « infer » ne trouve rien. L'étude date la découverte de leur but de deux ans plus tard, dans le protocole de réponse (la façon dont une personne peut répondre par des exemples) : l'induction à partir d'exemples, et les candidats superposés. C'est le terrain du chapitre 18, et le refus du chapitre 9.

**J'ai refusé le constructeur déclaratif comme titre phare.** Les constructeurs sont les classes qui écrivent une regex à partir d'étapes nommées dans le code, et non d'une chaîne de caractères. Dix-huit des cinquante et un fichiers du dossier de tests du constructeur sont marqués retirés : l'analyseur d'un motif déclaratif est en attente. L'exemple d'ouverture de l'article, `CanContainAChar(:Between = ...)`, lève une erreur. Ce qui tourne, c'est le constructeur conditionnel, et l'objet de look-around. Je ne bâtis pas le chapitre sur la forme phare du constructeur.

**Je n'ai pas encore refusé un mot que le langage ne connaît pas.** C'est la tension de ce chapitre, et je la garde pour la section 7.

## 5. Le tribunal

`00_regex_narrated` prouve les ancres et la recherche, les classes, les quantificateurs exacts, les groupes, les quatre types de correspondance, la correspondance partielle pendant la frappe, et les positions comme données. `00_numbrex_narrated` prouve premier, parfait, Fibonacci, pair et impair, carré et composé, chacun avec un nombre qui correspond et un qui ne correspond pas ; son en-tête consigne une régression où `Match()` renvoyait autrefois TRUE pour toute entrée. `tablex_narrated` prouve l'analyseur, le comptage, l'unicité, le tri, les types, les sommes et les moyennes, les trois connecteurs, les séquences, et la construction de motifs à partir de motifs. Son en-tête nomme la faute qu'il a tuée : l'analyseur découpait avec une position de fin à travers une fonction qui compte, et environ quatre-vingt-dix motifs étaient analysés en un jeton du bon type sans valeur. `00_matrex_narrated` prouve la taille exacte, toute taille et la forme carrée ; son en-tête consigne que `Match()` renvoyait autrefois FALSE pour toute entrée. `00_graphex_narrated` prouve qu'un motif se compile en un graphe, les étiquettes présentes et absentes, une séquence comme sous-suite, les règles de casse, la négation, l'alternance, les propriétés numériques, et le cache par signature de graphe.

Notez l'emplacement : la garde des tableaux vit dans le dossier de la regex, et son nom n'a pas de préfixe `00_`.

Il n'y a pas de garde narrée pour les listes, le temps ou les constructeurs de regex. Les tribunaux de ceux-ci sont des fichiers classiques sans promesses utilisables. Les tests des listes sont placés après une définition de fonction, de sorte que le langage hôte les lit comme le corps de la fonction et n'en exécute aucun. J'ai lancé une copie avec la fonction déplacée à la fin, et je le consigne dans mes notes de recherche, non dans un bloc : soixante vérifications se sont exécutées, et deux d'entre elles contredisent l'attente du fichier lui-même. Le fichier classique du temps dit qu'une promesse est TRUE et l'exécution imprime 0, et le dossier central l'a consigné le 1er octobre 2026 comme encore ouvert.

## 6. Le terrain, et où il mène

**Chaînes de caractères.** Le terrain mène en sûreté et en vitesse, et Softanza mène en nommage. La page du site pour ce domaine le dit elle-même : elle est derrière les moteurs modernes en sûreté et en débit, sans JIT et sans moteur de correspondance en temps linéaire, et le contrôle contre le retour arrière catastrophique n'est pas atteignable depuis Haro, bien que le code pour les deux soit déjà compilé dans le binaire. L'en-tête du moteur confirme que le durcissement existe en dessous : une limite de correspondances, une limite de récursion, des plafonds de longueur.

**Listes, nombres, temps, graphes.** Le terrain a des outils uniques plus anciens et plus forts. L'étude le dit sans les classer : un outil a des motifs de listes, l'unicité et des intervalles à pas ; trois langages ont la mise en correspondance structurelle ; les langages de requête de graphes existent ; le traitement d'événements existe pour le temps. Ce que le terrain n'a pas, et ce que le dossier revendique, c'est l'habitude unique d'un support à l'autre.

**Tableaux.** Les bibliothèques de qualité des données mènent en portée et en écosystème. Ici une règle est une phrase que la personne qui possède les données peut lire. La perte est qu'elle ne s'exécute que sur `stzTable`.

**Là où la famille est faible en elle-même.** Les en-têtes de classe impriment leurs défauts comme des avertissements : pour les matrices et les graphes. C'est rare, et je le dis. Graphes : les quantificateurs sont analysés mais pas encore utilisés par la correspondance. Matrices : des manques connus aujourd'hui, chacun porté comme un avertissement sur sa méthode.

**Une date pour le bogue récurrent de la famille.** La même cause racine a frappé la famille langage par langage : les analyseurs découpaient avec une position de fin à travers une fonction qui compte. Les nombres et les matrices ont été réparés le 14 juin 2026, les tableaux le 5 octobre, et les graphes dans une correction dont le fichier ne donne pas la date. Le temps le porte encore. C'est la preuve que la famille partage une seule conception et les habitudes d'un seul analyseur ; c'est aussi une raison probable pour laquelle le temps échoue.

## 7. La limite

Ce qui est construit : les chaînes de caractères, les nombres et les tableaux, chacun avec une garde et une petite fonction. L'habitude partagée.

Ce qui est construit en partie :

- **Listes** : les types, les comptes, l'imbrication, la négation, l'alternance et les ensembles s'exécutent. Les intervalles à pas lèvent une erreur. Dans mon exécution (notes de recherche, sans bloc), le drapeau d'unicité a été ignoré, de sorte que `[@N2-3{1; 2; 3}U]` a accepté `[1, 1]`, bien que la classe ait du code pour une vérification d'unicité. Le joker de l'article, `@A`, n'est pas un jeton ; le vrai joker est `@$`. Et un objet réutilisé répond depuis un cache dont la clé est la longueur de la liste et la somme des codes de ses caractères, ce qui ne dépend pas de l'ordre. Un objet neuf répond 0 pour `["hello", 1]`, et le même objet après `[1, "hello"]` répond 1.
- **Matrices** : la taille, la forme, l'élément et trois propriétés s'exécutent. L'en-tête de la classe liste les termes qui acceptent toute matrice : `row`, `col`, `pattern`, `determinant` et `sum`. Une matrice de deux par deux est acceptée par `{row(99)}`.
- **Temps** : les instants et les durées avec un pas s'exécutent. Dans mon exécution (sans bloc), un intervalle sans pas a levé une erreur. Et les séquences sur une ligne de temps ne s'exécutent pas du tout : voici une ligne de temps avec une réunion, une pause et un déjeuner, et le motif que l'article promet, qui devrait correspondre :

```haro
oTl = new stzTimeLine("2025-10-22", "2025-10-22")
oTl.AddInstant("Meeting", "2025-10-22 09:00:00")
oTl.AddSpan("Break", "2025-10-22 10:00:00", "2025-10-22 10:15:00")
oTl.AddInstant("Lunch", "2025-10-22 12:00:00")
o1 = new stzTimex("{@Event(Meeting) -> @Duration* -> @Event(Break)}")
? o1.MatchPartial(oTl)
#--> 0
o2 = new stzTimex("{@Event(Lunch)}")
? o2.MatchPartial(oTl)
#--> 0
? @@( o2.Tokens()[1][:label] )
#--> "Lunch)"
```

L'article promet que le premier est TRUE. Le deuxième montre que même un événement unique que la ligne de temps contient ne correspond pas, et le troisième montre pourquoi : l'étiquette a été lue avec sa parenthèse fermante. C'est le bogue partagé, toujours présent dans le temps.

- **Graphes** : les étiquettes dans l'ordre le long d'un chemin, la négation, l'alternance et les propriétés numériques s'exécutent. La flèche signifie *plus tard sur un chemin*, et non *suivant*. Les quantificateurs (`+`, `*`, `?` ou un nombre après un jeton) sont lus et ignorés. Le graphe de la section 3 a trois nœuds ; ici `@Node10`, un nœud avec le quantificateur dix, est demandé entre eux, et le motif correspond :

```haro
? (new stzGraphex("{@Node(placed) -> @Node(served)}", g)).Match(g)
#--> 1
? (new stzGraphex("{@Node(placed) -> @Node10 -> @Node(served)}", g)).Match(g)
#--> 1
```

Cooking se trouve entre le premier et le dernier, donc la première réponse est le sens de la flèche. La seconde est le quantificateur ignoré. Le cache de cette classe est indexé par les comptes de nœuds et d'arêtes et les identifiants de nœuds, de sorte qu'un second graphe avec les mêmes identifiants et d'autres étiquettes est servi depuis le cache, jusqu'à `ClearCache()`.

**Le refus que la famille n'a pas encore fait.** La loi du chapitre 11 est qu'un langage est déclaré et fermé, avec des refus. Voici la famille, à qui l'on demande un mot qu'elle ne connaît pas :

```haro
? Nx("{@Banana(3)}").Match(7)
#--> 1
? Nx("{@Banana(3)}").Match(1000003)
#--> 1
? @@( Nx("{@Banana(3)}").Tokens() )
#--> [ ]
? Nx("{@Property(Banana)}").Match(7)
#--> 0
```

Un motif avec un mot que le langage ne connaît pas correspond à tous les nombres. Les jetons sont vides, et rien n'est levé. Les langages des matrices et des tableaux renvoient un jeton ERROR que rien ne lève, et les langages des nombres et du temps renvoient une liste vide. La session de la charte de Haro l'a consigné comme constat, que le dossier central a relayé le 28 septembre 2026 : les six classes de motifs acceptent en silence les jetons inconnus. Je l'ai reproduit à ce commit, et la demande n'est pas close. Un langage fermé qui ne peut pas refuser n'est pas encore la loi du chapitre 11. Le chapitre l'imprime comme un constat du tribunal, et non comme une dette de moi.

Ce qui est conçu : un seul moteur de motifs partagé par tous les supports. La conception du moteur dit que le moteur à retour arrière, le solveur de contraintes et le compilateur de motifs sont les mêmes dans tous les domaines, et que seul le vocabulaire change. Son étape est planifiée. À ce commit le vocabulaire change et le code aussi. Le fichier propre du moteur nommé *pattern* est autre chose : les palindromes, les répétitions et les suites arithmétiques et géométriques. Le motif comme côté condition de la cascade, plusieurs facultés qui se déclenchent l'une après l'autre sur un état partagé, est le troisième échelon du chapitre 9, et conçu.

Ce qui est absent : l'induction à partir d'exemples, qui est réservée. Les classes sœurs génétique, linguistique et quantique, qui sont de la vision seulement. L'explication d'un motif sans nom, puisque `rx("[a-z]+").Explain()` lève une erreur parce que la classe d'analyse n'a jamais été construite. Et tout usage des classes de motifs par le reste de la bibliothèque : en dehors du dossier de la regex, des tests et de la documentation, aucune classe ne prend un motif. `stzList`, `stzNumber`, `stzTable`, `stzMatrix` et `stzGraph` n'ont pas de `Matches(pattern)`. Dans la documentation, le cours d'éducation les utilise, dans un chapitre et un exercice dont la réponse est vérifiée en exécutant le programme de l'apprenant, et la galerie a quelques scripts qui les utilisent.

## 8. Six portes

**Le programmeur.** Une habitude pour six genres de données, les graphes mis à part : un petit constructeur, un motif dans une chaîne de caractères, `Match`. Le motif est une donnée que vous pouvez lire et composer. Servez-vous de ceux qui ont une garde : le texte, les nombres, les tableaux, les matrices et les graphes, et ne bâtissez rien sur le cache d'un motif de liste réutilisé.

**L'analyste.** Une règle de qualité des données est une phrase du langage des tableaux. La personne qui possède les données peut la lire.

**Le concepteur.** Un motif énonce une forme que l'interface peut montrer avant que les données n'arrivent, et une valeur à moitié tapée reçoit une réponse en chemin.

**Le décideur.** Une règle est une ligne et non une procédure. Elle peut être relue, et son verdict est 1 ou 0. Dites à côté qu'un motif avec un mot inconnu n'est pas refusé, et qu'une flèche de graphe signifie *plus tard*.

**Le formateur.** Le cours enseigne les motifs en deux chapitres, en anglais, en français, en arabe et en haoussa. L'échelle est un programme : texte, liste, nombre.

**L'agent.** Un motif est une petite notation fermée à laquelle un agent peut être tenu et qu'il peut relire. On vous dit qu'aucun des six supports ne peut encore refuser un mot qu'il ne connaît pas, et que l'écriture d'un motif à partir d'exemples est réservée.

## 9. Exercice

Trois petits tableaux sont donnés. Écrivez un seul motif qui n'accepte que le premier. Avant de rien exécuter, écrivez sous chacune des trois lignes imprimées ce que vous attendez et pourquoi.

```haro exercise
t1 = new stzTable([ [ :ID, :EMAIL ], [ 1, "ali@x.org" ], [ 2, "sara@x.org" ] ])
t2 = new stzTable([ [ :ID, :EMAIL ], [ 1, "ali@x.org" ], [ 1, "sara@x.org" ] ])
t3 = new stzTable([ [ :ID, :EMAIL ], [ 1, "ali@x.org" ], [ 2, "" ] ])
# write ONE pattern, then print whether it matches t1, t2, t3, on three lines
cPattern = "{ ... }"
? Tbx(cPattern).Match(t1)
? Tbx(cPattern).Match(t2)
? Tbx(cPattern).Match(t3)
#--> 1
#--> 0
#--> 0
```

Exécutez-le. Une clause rejette le deuxième tableau et une autre rejette le troisième ; laquelle est laquelle ? Et que dirait le motif si l'email était une simple espace ? Je ne réponds pas en premier. Si une promesse se rompt, ne la changez pas : expliquez la sortie.
