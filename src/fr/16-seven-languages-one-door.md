---
id: seven-languages-one-door
part: 3
number: 16
title: Sept langages, une porte
spine: false
narrations: [stzexcis-polyglot-programming-in-ring.md, stzexterlib-domain-driven-polyglot-programming.md, stzexcis-performance-battle.md, stz-pycode-bridging-ring-and-python-narration.md]
site: [architecture]
guards: [51_extercode_narrated, governance_narrated, virtual_environment_twin_narrated, pycodegraph_narrated, jscodegraph_narrated]
stage:
  built: "un registre fermé de six runtimes étrangers et un appel par processus qui rapporte sous forme de listes les résultats de Python et de NodeJS ; les postures de confiance ; la répétition d'un lancement par le jumeau ; un lecteur de Python et de JavaScript vers un seul graphe de code"
  designed: "la porte gouvernée, avec une posture demandée à l'appel ; le pont du moteur et ses trois niveaux ; la bibliothèque de domaines au-dessus de la porte ; Haro portant une syntaxe Python et une syntaxe JavaScript"
  absent: "une porte dont le chemin du retour est fermé ; une porte pour R qui s'exécute ; une exécution réussie d'un runtime étranger dans le tribunal de la bibliothèque ; le modèle comme porte"
status: draft
rulings: ["12.19", "12.20", "12.21", "12.22", "12.28", "12.29"]
research: research/ch16.md
---

## 1. Le concept, tel que le terrain le tient

Pour un programmeur qui travaille, atteindre un autre langage depuis celui dans lequel on écrit signifie l'une de deux choses : une interface de fonctions étrangères, un appel dans une bibliothèque partagée, ou un processus enfant, une exécution d'un interpréteur dont on analyse la sortie. Les carnets et les machines virtuelles polyglottes font le même geste avec plus de confort. (Connaissance générale. Le dossier ne tient aucune étude datée de ces outils, et le dit lui-même.)

L'étude de terrain propre du domaine de projets, d'août 2026, a deux phrases sur ce sujet, et elles tirent en sens opposés. À la sortie : le langage hôte est l'issue de secours, et l'issue de secours est toujours prise. Elle donne deux langages internes morts d'ouverture. À l'entrée : le différenciateur est l'évasion ; un langage que l'on fait doit pouvoir être consommé depuis n'importe quelle pile. Elle donne un langage qui a calé à la frontière de son propre monde.

La leçon du terrain est donc double. Une évasion ouverte détruit un langage fermé. Et un langage sans chemin de sortie meurt à sa propre frontière. Une porte est l'endroit où ces deux leçons se rencontrent.

Il y a une seconde habitude, qui ressemble à la première et n'en est pas une. Les outils qui laissent écrire dans la syntaxe que l'on connaît par-dessus un autre moteur, un transpileur, un second front end pour un seul compilateur, je les appellerai du mot de ce livre, des *facettes*. La note de conception du domaine de projets à leur sujet est franche sur leur coût. La promesse honnête d'une seconde face est la lisibilité pour un humain qui connaît l'autre langage, et non le transfert de comportement.

## 2. Le premier principe

**Une facette est une syntaxe d'une grammaire, et jamais un runtime. Une porte est un runtime, et jamais une syntaxe. La porte est une, et elle est la réponse à « et le langage X ? ».**

La phrase propre de la vision, ratifiée en session le 28 août 2026, le dit de la porte : du code étranger dans les langages choisis, gouverné, une porte, sans autres intégrations d'hôtes. L'étude du dossier lit la paire en une ligne que je garde : la facette amène le programmeur, et la porte amène l'écosystème. Les chapitres 1 et 11 ont tous deux promis que ce chapitre dirait la différence. La voici.

## 3. La forme Softanza

La liste de la porte est fermée. Les langages étrangers forment un registre, et l'hôte n'y figure pas. Ce bloc interroge la porte sur six langages, puis sur l'hôte, puis sur un langage qui n'a jamais été sur la liste :

```haro
oDoor = new stzExterCode(:python)
aNames = [ "c", "nodejs", "julia", "r", "prolog", "python", "ring", "cobol" ]
for cLang in aNames
	? cLang + ": " + oDoor.IsLanguageSupported(cLang)
next
#--> c: 1
#--> nodejs: 1
#--> julia: 1
#--> r: 1
#--> prolog: 1
#--> python: 1
#--> ring: 0
#--> cobol: 0
```

« Et le langage X ? » a une seule réponse, et pour un langage hors de la liste c'est un refus par son nom :

```haro
try
	oNo = new stzExterCode(:cobol)
catch
	? cCatchError
done
#--> Language 'cobol' is not supported
```

Maintenant la porte exécute un vrai runtime. Une note sur la machine d'abord. La porte écrit un script, démarre le runtime avec lui et relit un fichier de résultat. Ce livre a été construit sur une machine où Python vit à son propre chemin, aussi le chemin est-il donné sous forme de chemin court sans espaces, et Node et R se trouvent aux emplacements par défaut de la bibliothèque. Les blocs qui démarrent un runtime sont marqués, dans le lecteur, comme touchant aux fichiers et au système, et ils montrent la sortie qui a été enregistrée à la date de la construction.

Le résultat de Python revient sous la structure propre de l'hôte, une liste, et l'appel laisse une trace :

```haro
cPython = "C:/Users/ASUSV3~1/AppData/Local/Programs/Python/Python313/python.exe"
oPy = new stzExterCode(:python)
oPy.SetRuntimePath(cPython)
oPy.SetCode("
res = { 'numbers': [1, 2, 3, 4, 5], 'mean': sum([1, 2, 3, 4, 5]) / 5 }
")
oPy.Execute()
? @@( oPy.Result() )
#--> [ [ "numbers", [ 1, 2, 3, 4, 5 ] ], [ "mean", 3 ] ]
? oPy.CallTrace()[1][:language]
#--> python
? oPy.CallTrace()[1][:mode]
#--> interpreted
? isNumber(oPy.LastCallDuration())
#--> 1
```

Le flottant Python `3.0` est revenu sous la forme `3`. La trace contient aussi une durée. Le bloc imprime seulement que c'est un nombre, car une durée est une horloge, et une horloge ne se promet pas.

Voilà la raison d'être de tout le volet, en une image : chaque couche d'une solution dans le langage qui y est le meilleur, et l'hôte comme chef d'orchestre qui passe les données en texte et relit les données en retour. L'article de la bibliothèque énumère les couches : la performance système en C, les systèmes événementiels en NodeJS, le calcul scientifique en Julia, les statistiques en R, le raisonnement logique en Prolog, l'apprentissage automatique en Python, le raisonnement d'IA dans un modèle de langage, et l'intégration de la solution dans l'hôte. Voici deux d'entre elles dans un pipeline, Python calculant les moyennes de deux étudiants et NodeJS décidant. Les seuils sont de moi ; les données sont celles de l'article :

```haro
aStudents = [ [ "Alice", [ 85, 90, 78 ] ], [ "Bob", [ 72, 65, 70 ] ] ]
oPy2 = new stzExterCode(:python)
oPy2.SetRuntimePath(cPython)
oPy2.SetCode("
students = " + @@(aStudents) + "
res = [ [ s[0], round(sum(s[1]) / len(s[1]), 2) ] for s in students ]
")
oPy2.Execute()
aAverages = oPy2.Result()
? @@(aAverages)
#--> [ [ "Alice", 84.33 ], [ "Bob", 69 ] ]
oNode = new stzExterCode(:nodejs)
oNode.SetCode("
const avgs = " + @@(aAverages) + ";
const res = avgs.map(a => [ a[0], a[1] >= 80 ? 'Excellent' : 'Needs work' ]);
")
oNode.Execute()
? @@( oNode.Result() )
#--> [ [ "Alice", "Excellent" ], [ "Bob", "Needs work" ] ]
```

Les données entrent en composant la chaîne de code avec l'afficheur de listes propre à l'hôte, puisque les fonctions de conversion de l'article n'existent pas (section 7).

**Lesquels, ces sept ?** Le titre s'engage sur un nombre, et le dossier le compte de quatre façons. L'article sur le plan et l'article sur la performance comptent six runtimes et l'hôte. L'article sur la bibliothèque de domaines et l'étude comptent sept domaines : les six et un modèle de langage, l'hôte étant un huitième qui orchestre. Le registre de la bibliothèque en a six et pas d'hôte. La vision dit « les 7 langages choisis » et ne les énumère jamais. La conception du moteur a encore une autre énumération, de cinq, avec COBOL et sans C, NodeJS ni Prolog. Je ne choisis pas entre elles dans une phrase que le dossier ne tient pas. Le registre ci-dessus est celui qui s'exécute. [AUTHOR: Quels sept le chapitre nomme-t-il, et le modèle de langage est-il l'un d'eux ? Les chapitres 17 et 20 font du modèle un proposeur qui ne peut pas valider, alors que les narrations l'exécutent comme un runtime de première classe par une fonction qui n'existe pas.]

**Une facette n'est pas une porte.** Lire un langage étranger n'est pas non plus l'exécuter. Les deux langages que l'auteur nomme comme facettes prévues de Haro sont aussi les deux que la bibliothèque sait déjà lire, sans les exécuter ni les écrire, dans un seul graphe de code. Un seul jeu de questions répond sur les deux :

```haro
cPy = "class Animal:" + nl +
      "    def speak(self):" + nl +
      "        return '...'" + nl +
      "" + nl +
      "class Dog(Animal):" + nl +
      "    def speak(self):" + nl +
      "        return 'woof'"
cJs = "class Animal { speak() { return '...' } }" + nl +
      "class Dog extends Animal { speak() { return 'woof' } }"
oPG = StzPyCodeGraphFromSourceTS(cPy)
oJG = StzJsCodeGraphFromSourceTS(cJs)
? oPG.Language()
#--> python
? @@( oPG.ParentsOf("Dog") )
#--> [ "Animal" ]
? @@( oPG.OwnersOf("speak") )
#--> [ "Animal", "Dog" ]
? oJG.Language()
#--> javascript
? @@( oJG.ParentsOf("Dog") )
#--> [ "Animal" ]
? @@( oJG.OwnersOf("speak") )
#--> [ "Animal", "Dog" ]
```

C'est un analyseur qui produit un index de classes, de méthodes et d'héritage, et non un graphe de programme capable d'imprimer un programme. C'est une coïncidence de l'ordre du travail, et pas encore une facette. Ce que le dossier tient des facettes, c'est ma déclaration, en session le 8 octobre 2026 : un lien doit être fait avec la future vision de Haro et de ses langages à facettes, où Ring est déjà là et où Python et JavaScript sont prévus. La charte de Haro sur cette machine parle d'une grammaire et d'un texte, et sa note de conception pour une seconde face, qui ne propose ni ne tranche rien, les appelle des faces et recommande des afficheurs lus par des humains avant tout analyseur. Sa propre table énumère les collisions : un lecteur de Python attend une indexation à partir de zéro, et celle de Haro part de un. [AUTHOR: Le chapitre peut-il nommer Python et JavaScript comme les facettes prévues de Haro sur votre seule parole ? Le livre dit facette et la note dit face.]

**Une porte est gouvernée.** La gouvernance a le mot pour le code étranger. Un exécuteur sans posture de confiance déclarée ne procède jamais, et le refus dit pourquoi. `external` est la posture que la bibliothèque définit comme hors processus :

```haro
oGov = new stzGovernance("shop")
? oGov.MayExecute("python")
#--> 0
? oGov.Why()
#--> refused: 'python' has NO declared trust posture
oGov.DeclarePosture("python", :External)
? oGov.MayExecute("python")
#--> 1
? oGov.Why()
#--> allowed: posture 'external' declared
```

Et le jumeau peut répéter un lancement avant qu'il s'exécute, signalé comme un risque. Le chapitre 24 traite du jumeau, et un bloc ici suffit pour dire ce que la porte n'utilise pas :

```haro
oTwin = new stzVirtualEnvironment()
oTwin.Spawn("python analyse.py")
? oTwin.NumberOfPendingSpawns()
#--> 1
oPlan = oTwin.GenerateUpdatePlan()
? oPlan.Narration()
#--> Update plan (1 of 1 operations to commit):
#-->   * 1. spawn process: python analyse.py
? @@( oPlan.Risks() )
#--> [ [ 1, "RUNS an external command (side effects): spawn process: python analyse.py" ] ]
```

Rien n'y est exécuté. Le script nommé n'existe pas.

## 4. La décision, et ce que j'ai refusé

**J'ai décidé d'une seule porte.** Son nom de vision est la porte des langages étrangers, et la lettre en est x : la famille des lettres de la plateforme en a une qui désigne l'externe. Les noms retirés sont deux plus anciens. La lettre X a été refusée pour l'algorithmique, parce qu'elle se serait tenue à côté de la porte, la collision que le chapitre de l'alphabet a nommée comme la plus aiguë. La porte a pris une lettre et l'a gardée.

**J'ai refusé d'autres intégrations d'hôtes.** La porte est la réponse à « et le langage X ? ». Le chapitre 1 a promis ce chapitre sur ces mots : sept langages ont été choisis pour sept couches d'une solution.

**J'ai refusé d'abandonner les domaines au code généré.** L'article sur la bibliothèque de domaines le pose comme une position : plutôt que de forcer les développeurs à maîtriser chaque domaine, ou à s'abandonner au code généré par l'IA, fournir des abstractions soigneusement conçues. C'est une position de 2025, et son code est absent.

**J'ai refusé une facette comme runtime.** Le plan de l'étude le dit en une ligne : une facette est une syntaxe d'une grammaire et jamais un runtime, de sorte que la porte reste le seul chemin vers le code étranger. C'est un plan, proposé. Ce n'est pas tranché.

**J'ai refusé un afficheur qui approche.** La règle de la note de conception pour les faces : un afficheur refuse avant d'approcher, et une face épelle le graphe et ne lui donne jamais le sens de Python ou de JavaScript.

## 5. Le tribunal

`51_extercode_narrated` prouve que le registre connaît Python, R, Julia, Prolog, C et NodeJS, sans égard à la casse, et rejette un nom inconnu ; que le code posé est le code relu ; et que la fabrique construit et transmet. Son en-tête dit qu'il n'a pas d'`Execute` : pas de véritable entrée ou sortie dans les tests. `governance_narrated`, scène six, prouve qu'une exécution sans posture refuse, qu'une posture déclarée procède et se nomme, et que les postures voyagent par la sauvegarde et le chargement. `virtual_environment_twin_narrated` prouve qu'un lancement mis en file ne s'exécute pas avant la validation, par un fichier témoin ; qu'une portée refuse ; et que le plan narre et signale le lancement. `pycodegraph_narrated` et `jscodegraph_narrated` prouvent les classes, les méthodes, les chaînes d'héritage, les propriétaires, l'impact et la cascade sur des sources Python et sur des sources JavaScript, hors ligne et sans le runtime ; le second est sauté quand le tree-sitter du moteur est absent.

Je veux être exact sur le tribunal de la porte. Aucune garde de l'instantané n'exécute un runtime étranger et ne passe. Le tribunal de la porte est un registre et un test de construction. Le propre relevé d'exécution du répertoire, sous une version plus ancienne du runtime, énumère trente-sept échecs ; plusieurs promesses ne peuvent pas correspondre par construction, parce que les noms de fichiers portent un suffixe aléatoire et les appels une durée.

## 6. Le terrain, et où il mène

L'hôte perd la course pour laquelle la porte existe. L'article sur la performance mesure sept runtimes sur trois tâches, et l'hôte arrive dernier dans deux d'entre elles ; je reprends ses réserves du chapitre 22 : il n'a ni versions ni dates dans son texte, et dit que ses temps sont relatifs à un environnement informatique précis. Trier un million d'éléments prend à l'hôte environ trente secondes et à Python environ quatre, dans la table de l'article. Je n'en imprime pas davantage.

Le terrain mène dans les runtimes qu'il peut réellement exécuter. Sur six portes, trois ont tourné sur cette machine : Node, Python, et R, qui a levé une erreur. Les trois autres n'avaient aucun runtime à démarrer. L'étude dit que sa description des outils polyglottes du terrain a été écrite d'après le genre et non relue, et je ne revendique aucune comparaison mesurée.

Le terrain mène dans l'écosystème et dans l'usage. La page de comparaison ne parle de Python que comme d'un rival ; pour couvrir ses trente lignes en Python, on assemble numpy, pandas et d'autres. La porte est la façon dont une solution Softanza les prend sans partir.

L'autre perte du terrain est que le processus étranger est hors du tribunal. Le modèle de menace du chapitre 21 met hors de portée le code déjà exécuté dans le processus.

Et le coût honnête d'une facette, dans la table de la note : un lecteur de Python attend une indexation à partir de zéro, et celle de Haro part de un ; la chaîne avec un saut de ligne est une barre oblique inverse et un `n` ; deux lettres de casse différente sont une seule variable. « Tout modèle écrit Haro sous la forme qu'il connaît » n'est vrai que des graphies qui sont la minorité.

## 7. La limite

Le mot *gouverné* est une conception. Voici le bloc qui le montre. La gouvernance dit non, et la porte s'exécute quand même :

```haro
oGov2 = new stzGovernance("shop")
? oGov2.MayExecute("python")
#--> 0
oPy3 = new stzExterCode(:python)
oPy3.SetRuntimePath(cPython)
oPy3.SetCode("res = 6 * 7")
oPy3.Execute()
? oPy3.Result()
#--> 42
```

Rien dans le répertoire de la porte ne mentionne la gouvernance ni la posture. La porte appelle directement le système, et non le jumeau.

Le chemin du retour n'est pas fermé. Le fichier de résultat est lu par le propre `eval` de l'hôte, et une chaîne qui sort du runtime étranger est enveloppée entre apostrophes simples sans échappement. Une chaîne étrangère qui porte une apostrophe et un appel atteint le code de l'hôte. La fonction utilisée ici est `upper`, inoffensive exprès :

```haro
oPy4 = new stzExterCode(:python)
oPy4.SetRuntimePath(cPython)
oPy4.SetCode(`
res = "x' + upper('y') + 'z"
`)
oPy4.Execute()
? oPy4.Result()
#--> xYz
```

Le fichier de résultat contenait `'x' + upper('y') + 'z'`, et `Result()` l'a évalué. Une simple apostrophe dans des données, `it's fine`, écrit une chaîne que l'hôte ne peut pas lire, et la méthode imprime l'erreur et renvoie le texte brut. C'est la même classe de défaut que la liste du chapitre 11 dans une phrase naturelle. Je n'ai pas testé la conversion des cinq autres langages.

La porte R lève une erreur à chaque appel, parce que son script généré n'est pas du R valide : il contient un identifiant qui commence par un tiret bas, que R rejette. Je l'ai confirmé avec R sur un fichier d'une ligne. Et la trace enregistre un code de sortie de 0 pour un appel qui a échoué, parce que le code passe un 0 littéral à l'enregistreur, et que l'échec n'est détecté que par l'absence du fichier de résultat :

```haro
oStat = new stzExterCode(:R)
oStat.SetCode("res <- c(1, 2, 3)")
bRaised = 0
try
	oStat.Execute()
catch
	bRaised = 1
done
? bRaised
#--> 1
? oStat.CallTrace()[1][:exitcode]
#--> 0
```

Le message de R était en français sur cette machine, je ne le promets donc pas. [AUTHOR: À ce commit, la porte n'est ni gouvernée ni fermée sur le chemin du retour, et la porte R lève une erreur. Le chapitre peut-il imprimer ces trois points comme sa limite, avec les exécutions, dans la voix de la liste ouverte du chapitre 11 ? Je conseille oui, et le mot « gouvernée » de la vision reste alors une conception.]

Ce qui est conçu en plus : le pont polyglotte propre du moteur, que la conception du moteur marque comme prévu (le macroplan porte une correction qui dit que le module a été marqué fait alors qu'il n'avait aucune source) ; les trois niveaux pour Python, dont seul le sous-processus externe existe ; la bibliothèque de domaines au-dessus de la porte, dont je n'ai trouvé aucune classe dans le code ; et les facettes, une note qui propose et ne tranche rien.

Ce qui est absent : les fonctions de l'article qui font entrer les données, `@@R`, `@@C`, `XC()` et `XAI()`, qui ne sont définies dans aucun fichier. Des fabriques existent pour Python, R, Julia et Prolog. Les portes C et NodeJS ne sont atteintes que par la classe. Le modèle n'est pas du tout une porte de ce plan ; la fonction de l'article qui l'exécute dans l'hôte est le contraire de la loi du chapitre 17, et le livre ne l'enseigne pas.

Et une forme de porte que je n'ai pas exécutée : Julia, C et Prolog, pour lesquels aucun runtime n'est installé ici. Et une troisième relation, nommée dans l'étude à côté de la porte, l'adaptateur qui colle une solution trouvée sur internet dans un autre langage et la change un peu : `range0`, le range de Python comme fonction de l'hôte, s'exécute ; la forme de tranche de Python imprime une liste vide, et le relevé propre de la garde la liste comme un échec.

## 8. Six portes

**Le programmeur.** Vous écrivez du Haro et, pour la couche qu'un autre langage fait le mieux, vous lui remettez une chaîne de code et une liste de données et vous reprenez une liste. Dans le plan, un programmeur Python ou JavaScript écrira aussi du Haro dans une syntaxe qu'il connaît. Deux choses différentes : une syntaxe vous amène, et un runtime amène vos bibliothèques.

**L'analyste.** La couche statistique est celle de R, la couche d'apprentissage automatique celle de Python, la couche logique celle de Prolog. Vous restez dans un fichier et une liste de résultats. Aujourd'hui la porte R lève une erreur, et le dossier le dit.

**Le concepteur.** Il n'y a rien à concevoir à la porte elle-même. La leçon du dossier est son refus : un langage hors de la liste est refusé par son nom, et « et mon langage ? » a une seule réponse.

**Le décideur.** La porte est l'unique endroit où la fermeture prend fin, par décision. À ce commit elle n'est pas encore gouvernée et son chemin du retour atteint le code de l'hôte. Le mot « gouvernée » de la vision est une conception. La durée de chaque appel est enregistrée aujourd'hui dans la trace.

**Le formateur.** Un apprenant voit quelle couche appartient à quel langage et exécute un pipeline à deux portes. La leçon est la différence entre lire un langage, l'exécuter, et écrire dans sa syntaxe.

**L'agent.** Vous n'atteignez jamais la porte par vous-même. Une fonction dans le fichier d'un agent doit porter une posture, et `external` convient à un runtime étranger ; et un modèle n'a aucune capacité de produire des effets (chapitre 20).

## 9. Exercice

Vous construisez une petite solution avec trois tâches : trier un million de nombres, décider lequel de deux étudiants réussit, et vérifier dans un arbre généalogique qui est l'ancêtre de qui. Pour chaque tâche, choisissez dans la table de la section 3 le langage qui possède sa couche, et écrivez votre raison en une ligne. Puis, sans rien exécuter, écrivez la promesse pour chaque ligne de ce bloc, et exécutez-le :

```haro exercise
oDoor = new stzExterCode(:python)
# promise: the door answers "julia" with ...
# promise: the door answers "ring" with ...
# promise: asking for "cobol" raises with the sentence ...
oGov = new stzGovernance("mine")
# promise: oGov.MayExecute("prolog") before any posture is declared gives ...
# promise: after oGov.DeclarePosture("prolog", :External), it gives ...
```

La dernière promesse est celle qui compte. Si vous appelez maintenant la porte pour Prolog, la gouvernance aura-t-elle été interrogée ? Écrivez oui ou non, et pourquoi. Puis lisez la section 7. Si une promesse se brise, ne la changez pas : expliquez d'abord la sortie.
