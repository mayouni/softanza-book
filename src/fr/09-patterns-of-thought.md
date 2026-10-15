---
id: patterns-of-thought
part: 2
number: 9
title: "Les motifs de pensée : le Softanzuter, Reaxis et les moteurs"
spine: false
narrations: [stzregexuter-regex-as-computational-reactive-medium.md, stz-reaxis-reactive-programming-narration.md, stz-managing-deep-lists-narration.md, softanza-reactive-objects-narration.md]
site: [softanzuter, craft]
guards: [00_overflow_narrated, 60_reaxis_on_reactor_narrated, piagent_narrated, 00_grid_narrated, test_timeline_regression, 01_deeplist_narrated]
stage:
  built: "le Regexuter et le Listexuter, qui réagissent avec un état qui se souvient ; Reaxis, la programmation réactive en mots simples, sur la boucle d'événements du moteur ; la ligne de temps, la grille et les opérations profondes ; l'agent d'IA dont les compétences s'enchaînent jusqu'à un point fixe"
  designed: "le Softanzuter proprement dit, plusieurs facultés partageant un seul état et s'enchaînant jusqu'à ce qu'il se stabilise ; le moteur universel derrière lui ; ses quatre frères, analyseur, génétique, linguistique et quantique"
  absent: "une chaîne de dépendance qui relie un déclencheur à un autre ; un verbe de fusion de sections que l'article présente comme son point central"
status: draft
rulings: ["12.4", "12.18", "12.19"]
research: research/ch09.md
---

Dans ce chapitre, je prends tour à tour les trois sujets du titre : le Softanzuter, Reaxis et les moteurs, dont la ligne de temps et la grille tournent ici. Le Regexuter lie un motif à du code qui se déclenche et se souvient de son pourquoi ; Reaxis est de la programmation réactive au vocabulaire repensé. Je gravis l'échelle que dessine l'architecture, quatre échelons, et au troisième je lance le bloc qui échoue à enchaîner plutôt que de revendiquer un échelon qui n'est pas construit. Je dis ce que j'ai refusé : l'expression régulière comme simple façon de lire du texte, les mots du terrain pour la programmation réactive, les quatre frères, et la cascade. Tout sert une seule phrase : un Softanzuter est une représentation computationnelle d'une machine pensante, fondée sur un ou plusieurs Regexuters, qui lui permet de reconnaître des motifs de pensée et d'y réagir.

## 1. Le concept, tel que le terrain le tient

Le terrain a trois outils pour faire réagir un programme. Les expressions régulières reconnaissent une forme dans un texte, et rien de plus : elles disent « cela correspond », et elles s'arrêtent. La programmation réactive, la famille des observables, des abonnés et des ordonnanceurs que Rx a rendue populaire, laisse les données circuler dans un programme au fil du temps. Son vocabulaire vient de la plomberie, de la téléphonie et de l'édition : tuyaux, contre-pression, sources chaudes et froides. Et les moteurs de règles, les systèmes de production du terrain avec leur chaînage avant, déclenchent des règles quand des faits apparaissent, et continuent de déclencher tant que de nouveaux faits apparaissent ; c'est une connaissance générale, et les moteurs de règles du terrain sont plus anciens et plus mûrs que tout ce qui est dans ce chapitre.

Chaque outil est séparé. Une expression régulière ne déclenche pas de calcul, un flux réactif ne reconnaît pas de motif, et un moteur de règles n'a pas de vocabulaire qu'une personne emploierait pour dire une pensée. Je tiens cela pour une vue, non pour un résultat.

La section suivante donne la seule phrase par laquelle je réponds.

## 2. Le premier principe

J'ai donné à ce paradigme une seule phrase, et tout ce qui suit tente de la rendre mécanique : **un Softanzuter est une représentation computationnelle d'une machine pensante, fondée sur un ou plusieurs Regexuters, qui lui permet de reconnaître des motifs de pensée et d'y réagir.**

La section suivante montre jusqu'où la bibliothèque l'a rendue mécanique.

## 3. La forme Softanza

L'architecture la dessine comme une échelle à quatre échelons, chacun ajoutant une chose.

Le premier échelon est le motif. Vous le verrez au chapitre 15 : une forme dans un milieu, une chaîne, une liste, un nombre, qui peut dire « cela correspond, et voici comment », et rien de plus. Le deuxième échelon donne une réaction à un motif : le Regexuter, un arc réflexe. Vous liez un motif à du code, vous traitez un texte, et le code se déclenche à chaque correspondance. Un Regexuter réagit, et il se souvient de ce qu'il a fait. Ici il masque les secrets d'une phrase. Que dit l'état qu'il garde sur chacun : ce qu'il a trouvé, ce qu'il a calculé, où, et quel déclencheur s'est déclenché ?

```haro
rxu() {
	Trigger(:SensitiveData = "(password|secret|key):\s*(\w+)")
	@C(:When = :SensitiveData, :Do = '{ @value = "REDACTED-" + len(@value) }')
	Process("User credentials: password: abc123 secret: def456")
	? @@( Results() )
	#--> [ "REDACTED-16", "REDACTED-14" ]
	? @@( Positions() )
	#--> [ 19, 36 ]
	? State()[1][:matchedvalue]
	#--> password: abc123
	? State()[1][:computedvalue]
	#--> REDACTED-16
	? @@( State()[2][:dependson] )
	#--> [ "sensitivedata" ]
}
```

L'état est une provenance : chaque réaction qui change une valeur garde son pourquoi. La dernière ligne, `[ "sensitivedata" ]`, est aussi une limite honnête, et j'y reviendrai : ce que le Regexuter enregistre comme dépendance n'est aujourd'hui que son propre déclencheur.

Voici maintenant le troisième échelon, celui dont parle la définition. Ce sont plusieurs Regexuters, sur des milieux différents, partageant un seul état, de sorte que ce qu'une faculté écrit est un milieu sur lequel une autre faculté peut chercher des correspondances. Une pensée est une entrée d'état avec sa provenance, et une pensée stabilisée est un état où plus rien ne se déclenche. Cet échelon n'est pas construit, et le bloc montre comment je le sais. Le second déclencheur ci-dessous est écrit pour les nombres de trois chiffres ou plus. Le premier déclencheur transforme le 7 en 700, qui en est un. Si la machine pensait en cascades, le second se déclencherait-il sur le résultat du premier ? Exécutez-le :

```haro
rxu() {
	Trigger(:Number = "\d+")
	Trigger(:Big = "\d{3,}")
	@C(:When = :Number, :Do = '{ @value = @number(@value) * 100 }')
	@C(:When = :Big, :Do = '{ @value = "BIG" }')
	Process("Found 7 items")
	? @@( Matches() )
	#--> [ "7" ]
	? @@( Results() )
	#--> [ 700 ]
	? @@( Triggers() )
	#--> [ "number" ]
}
```

Il ne l'a pas fait : les résultats disent `[ 700 ]`, les déclencheurs qui se sont déclenchés disent `[ "number" ]`. `BIG` n'apparaît nulle part ! Chaque déclencheur est confronté une seule fois au texte d'origine, et ce qu'un déclencheur écrit n'est pas offert aux autres. C'est toute la différence entre le deuxième échelon et le troisième.

La cascade tourne un échelon plus haut, au quatrième, l'agent d'IA : la machine pensante dotée d'un corps dans un monde, et d'un but. Son esprit est fait de compétences, chacune avec une condition et une action, qui s'enchaînent. La deuxième compétence se déclenche sur le fait que la première a écrit. `Pursue()` renvoie combien de déclenchements de compétences ont été vérifiés, et continue jusqu'à ce que le monde cesse de changer, ou vingt tours au plus. Que répond-il quand on le redemande ?

```haro
oAgent = new stzPIAgent("cook")
oAgent.MemoryQ().Learn("order", "state", "placed")
s1 = new stzAgentSkill("cook")
s1.SetWhen(func oM { return oM.Fact("order", "state", "placed") })
s1.SetDoes(func oM { oM.Forget("order","state","placed") oM.Learn("order","state","cooking") return 1 })
s2 = new stzAgentSkill("serve")
s2.SetWhen(func oM { return oM.Fact("order", "state", "cooking") })
s2.SetDoes(func oM { oM.Forget("order","state","cooking") oM.Learn("order","state","served") return 1 })
oAgent.AddSkill(s1)
oAgent.AddSkill(s2)
? oAgent.Pursue()
#--> 2
? oAgent.MemoryQ().Fact("order", "state", "served")
#--> TRUE
? oAgent.Pursue()
#--> 0
```

Il répond `2`, puis `0`, et entre les deux le fait `served` dit `TRUE`. C'est un point fixe. La garde qui le prouve étiquette la scène dans ses propres mots : `the cascade to fixpoint (Softanzuter at agent level)`, soit la cascade jusqu'au point fixe, le Softanzuter au niveau de l'agent. Au chapitre 17, vous verrez un agent de cette même classe refusé à une barrière. Voici son autre face : l'agent qui enchaîne, parce que son esprit est programmatique.

Le mot a donc trois sens dans le dossier, et le lecteur mérite qu'on lui dise lequel est lequel. D'abord, dans ce chapitre, « Softanzuter » est le troisième échelon, la machine pensante de la définition : conçu, pas construit. Ensuite, le moteur a un module du même nom, que le macroplan présente comme le socle des agents d'IA. Ses emplacements ont un état et une boîte aux lettres bornée, et un message envoyé dans une file pleine est refusé, compté et jamais jeté en silence ; l'agent du bloc ci-dessus, `stzPIAgent`, ne l'appelle jamais. Enfin, la conception d'un moteur universel derrière tout cela, un milieu où n'importe quel langage de motifs devient un calcul, est planifiée.

**Reaxis** est le deuxième sujet du titre du chapitre, et c'est une idée différente. C'est de la programmation réactive avec un vocabulaire repensé depuis la base. Une chose réactive est un Container, un Stream et une Rfunction : une fonction en attente, qui n'est pas un rappel. Les données circulent dans un flux en mots simples, une transformation, un filtre, ce qu'il faut faire de ce qui passe. Quatre prix entrent, 80, 90, 100 et 120 : lesquels ressortent, et à quelle valeur ?

```haro
aSeen = []
Rs = new stzReactiveSystem()
Rs {
	oStream = CreateStream("prices")
	oStream {
		Transform(func price { return price * 1.20 })
		Filter(func price { return price >= 100 })
		OnPassed(func item { aSeen + item })
		FeedMany([ 80, 90, 100, 120 ])
	}
	RunLoop()
}
? @@( aSeen )
#--> [ 108, 120, 144 ]
```

`aSeen` dit `[ 108, 120, 144 ]` : le 80 est devenu 96 et a été écarté par le filtre ; le 90 est devenu 108 et est passé. Trois fonctions sont en attente, et rien de tout cela ne s'appelle un abonné ; l'ancien mot `Subscribe` survit comme alias de `OnPassed`.

Reaxis a remplacé la contre-pression par le débordement, un mot qu'on n'a pas besoin d'un schéma pour comprendre. Et il a été audité. Une lecture des quatre stratégies que l'article documentait a trouvé que trois d'entre elles perdaient des données sans en signaler aucune. La stratégie par défaut écartait tout ce qui dépassait la capacité pendant que le compteur affichait zéro. C'est corrigé, et prouvé pour les quatre stratégies. Ici, quatre éléments entrent dans un tampon de deux. Que dit le flux de ce qui s'est passé ?

```haro
oRs = new stzReactiveSystem()
oS = oRs.CreateStream("probe")
oS {
	SetOverflowStrategy(BUFFER_REJECT_NEWEST, 2)
	for i = 1 to 4
		Receive(i)
	next
	? OverflowStats()[:currentBuffer]
	#--> 2
	? OverflowStats()[:droppedCount]
	#--> 2
}
```

Il dit que `currentBuffer` vaut `2` et que `droppedCount` vaut `2`. Le compteur qui affichait zéro compte désormais !

Et pour ce que le terrain appelle debounce, Reaxis dit ce que cela veut dire : attendre que l'attribut se stabilise. Trois changements en succession rapide : combien de réactions, une fois que la valeur a cessé de changer pendant cinquante millisecondes ?

```haro
nSettled = 0
oRs4 = new stzReactive()
oX = oRs4.ReactiveObject()
oX.WaitForAttributeToSettle("query", 50, func(attr, oldV, newV) { nSettled++ })
oX.SetAttribute("query", "s")
oX.SetAttribute("query", "so")
oX.SetAttribute("query", "sof")
oX { ProcessPendingReactions() }
oRs4.RunLoop()
? nSettled
#--> 1
oRs4.Stop()
```

Une seule réaction. `nSettled` dit `1`.

Le troisième sujet du chapitre, ce sont les moteurs, les petits paradigmes que la bibliothèque a repensés un par un. Le chapitre 3 vous a donné la vérité et le vide. En voici deux de plus, exécutés ici. Le temps est un espace de travail, pas un nombre. Une ligne de temps tient des plages et calcule les vides et les chevauchements. Que dit-elle du vide entre deux phases, et que fait-elle d'un point qui tomberait dans une région bloquée ?

```haro
oTl = new stzTimeLine("2024-01-01 00:00:00", "2024-12-31 23:59:59")
oTl {
	AddSpan("PHASE1", "2024-01-01 00:00:00", "2024-02-15 23:59:59")
	AddSpan("PHASE2", "2024-03-01 00:00:00", "2024-04-15 23:59:59")
	? len(Gaps())
	#--> 1
	? Gaps()[1][:after]
	#--> PHASE1
	? Gaps()[1][:before]
	#--> PHASE2
	? HasOverlaps()
	#--> FALSE
	AddSpan("PHASE2B", "2024-04-01 00:00:00", "2024-05-15 23:59:59")
	? HasOverlaps()
	#--> TRUE
}
oB = new stzTimeLine("2024-01-01", "2024-12-31")
oB {
	AddBlockedSpan("MAINTENANCE", "2024-06-15 09:00:00", "2024-06-15 17:00:00")
	AddPoint("EVENT1", "2024-06-15 08:00:00")
	try
		AddPoint("EVENT2", "2024-06-15 12:00:00")
	catch
		? cCatchError
	done
	#--> Point 'EVENT2' falls within a blocked span or blocked point
}
```

Le vide est nommé par ce qu'il sépare, `PHASE1` et `PHASE2`. La plage bloquée a refusé `EVENT2` ! Le refus porte sa raison : `Point 'EVENT2' falls within a blocked span or blocked point`.

Et une grille a un curseur qui sait où il est : la position est une colonne et une ligne, et se déplacer au-delà d'un bord reste au bord. Deux pas vers le bas et trois vers la droite, puis trois de plus vers la droite : où est le curseur ?

```haro
StzGridQ([ 5, 5 ]) {
	MoveDown()
	MoveDown()
	MoveRight()
	MoveRight()
	MoveRight()
	? @@( CurrentPosition() )
	#--> [ 4, 3 ]
	MoveRight()
	MoveRight()
	MoveRight()
	? @@( CurrentPosition() )
	#--> [ 5, 3 ]
}
```

En `[ 4, 3 ]`, puis en `[ 5, 3 ]`. Trois pas de plus vers la droite ont gagné une colonne, et le curseur est resté au bord !

## 4. La décision, et ce que j'ai refusé

**J'ai refusé de laisser l'expression régulière n'être qu'une façon de lire du texte.** J'en ai fait un milieu computationnel. Un déclencheur lance un calcul, le calcul écrit un état quand il change la valeur, et l'état enregistre son pourquoi. Le Regexuter est une faculté et pas un esprit, et il ne tient aucun but. J'ai ajouté le but deux échelons plus haut, au quatrième, dans l'agent, exprès.

**J'ai refusé le vocabulaire du terrain pour la programmation réactive.** Observables, abonnés, contre-pression, sources chaudes et froides, ordonnanceurs : empruntés à la plomberie, à la téléphonie et à l'édition, et pas au problème. Une fonction en attente est une Rfunction. Les données circulent, et rien ne s'appelle producteur ou consommateur. Le débordement remplace la contre-pression. Attendre qu'un attribut se stabilise remplace le debounce. Les anciennes orthographes marchent encore comme alias : feed, emit, send et receive appellent tous une même méthode, mon changement était donc un changement de nom et pas un retrait.

**J'ai refusé de construire les frères.** L'article qui raconte le Regexuter en décrit quatre autres : un analyseur, un génétique, un linguistique et un quantique. Dans le génétique les motifs évoluent contre un critère d'adaptation, dans le linguistique les déclencheurs sont des règles de grammaire, et dans le quantique un motif peut être dans plusieurs états à la fois. L'article donne à chacun un exemple d'appel, et aucune classe ne se tient derrière. La conception a trouvé plus tard un but pour deux d'entre eux. Répondre par l'exemple exige l'induction de motifs, le terrain du génétique ; plusieurs réponses acceptables exigent des candidats superposés, réduits par des règles ou par un choix, celui du quantique. Le chapitre 18 dit où cela en est. Ils restent une vision ; deux ont leur but écrit.

**J'ai refusé de revendiquer la cascade.** L'architecture de la bibliothèque le dit elle-même : l'échafaudage anticipe la cascade mais ne redéclenche pas encore les déclencheurs dépendants jusqu'à un point fixe. Je préfère vous montrer le bloc qui échoue à enchaîner plutôt qu'un bloc qui y arrive.

## 5. Le tribunal

Le Regexuter et le Listexuter ont des tests classiques, et aucune garde narrée. Les huit tests classiques du Regexuter ont tourné sans erreur : le journal du dossier dit `PASS 8 ERR 0`. Rien n'y vérifie ce qu'ils impriment. Cinq des sept tests du Listexuter échouent à leur propre sortie attendue, et deux ne promettent rien. La cascade de l'agent est prouvée par `piagent_narrated`, scène cinq. Reaxis a beaucoup de gardes. `00_overflow_narrated` prouve les quatre stratégies de débordement et le cas qui ne perd rien ; `60_reaxis_on_reactor_narrated` prouve un minuteur à coup unique, le minuteur répété, le HTTP non bloquant et l'attribut qui se stabilise sur la boucle du moteur. La ligne de temps a `test_timeline_regression`, qui couvre la construction, la durée, l'ajout de points et le déplacement des bornes, mais ni les vides, ni les chevauchements, ni les plages bloquées. La grille a `00_grid_narrated`, et les opérations profondes `01_deeplist_narrated`.

La section suivante place ce dossier à côté de celui du terrain.

## 6. Le terrain, et où il mène

Les moteurs de règles du terrain mènent. Ils sont plus anciens et plus mûrs que le Regexuter, ils s'enchaînent jusqu'à un point fixe, et les algorithmes qui les portent ont des décennies. Ce que je revendique n'est pas un moteur de règles. C'est le côté condition : des règles qui sont des phrases des langages de motifs, sur les deux milieux qui ont une machine réagissante construite, le texte pour le Regexuter et les listes pour le Listexuter. L'état garde, pour chaque déclenchement qui change une valeur, son pourquoi. L'architecture même de la bibliothèque appelle le Regexuter un moteur de règles à chaînage avant naissant, et je n'en dirai pas plus.

Les bibliothèques réactives du terrain mènent en portée. Rx existe dans la plupart des langages courants, avec un grand nombre d'opérateurs ; c'est une connaissance générale. Reaxis est une bibliothèque sur une boucle d'événements. Le module propre du moteur pour cela est une petite table de règles sur des sous-chaînes : le modèle Container, Stream et Rfunction vit dans la bibliothèque, sur la boucle d'événements du moteur.

Je n'imprimerai pas la comparaison par étoiles avec les outils du terrain que porte l'article de la bibliothèque sur les objets réactifs. Elle n'est ni datée ni sourcée.

La section suivante dit où tout cela s'arrête.

## 7. La limite

Ce qui est construit : le Regexuter et le Listexuter ; Reaxis sur la boucle d'événements du moteur ; la ligne de temps, la grille et les opérations profondes ; l'agent d'IA dont les compétences s'enchaînent.

Ce qui est conçu : le troisième échelon, plusieurs facultés sur un état partagé, s'enchaînant jusqu'à ce qu'il se stabilise. Le moteur universel pour cela est planifié. Les quatre frères sont une vision. Le macroplan marque le module du moteur comme fait, et le tableau d'architecture le marque comme planifié : le même nom pour deux choses. Ce tableau marque comme planifié tout module de sa cinquième couche, y compris ceux qui ont du code source, et il est donc périmé sur ce point. Le milieu universel est planifié dans le document de conception du moteur.

Ce qui est absent ou cassé à ce commit :

- La chaîne de dépendance n'en est pas une. Chaque entrée d'état ne dépend que de son propre déclencheur, de sorte que la chaîne enregistre quel déclencheur était actif et jamais un lien entre deux. Demander la chaîne fait déborder la pile : l'exécution se termine par `Error (R4) : Stack Overflow`. Aucun test ne l'appelle.
- Cinq des sept tests classiques du Listexuter échouent à leur propre sortie attendue, et deux ne promettent rien. Le journal d'erreurs de ce dossier note, dans le sixième fichier, `Error (C8) : Parentheses ')' is missing`.
- Une liste imbriquée qui correspond en entier est signalée deux fois.
- Le minuteur répété de l'article prend trois arguments et la bibliothèque en prend deux ; la forme avec unités est `RunEveryXT`.
- Deux des verbes de chemin de l'article sur les listes profondes, `ItemAtPath` et `ItemsAtPaths`, vivent sur une sous-classe, `stzDeepList`, et pas sur une liste ordinaire ; `Paths()` est sur une liste ordinaire.
- L'article sur la fusion de sections présente comme son point central un verbe général qui n'existe pas. Les deux qui existent, fusionner ce qui se chevauche et fusionner ce qui est inclus, tournent. La fusion de sections n'a pas de fichier de test à elle.
- Il n'y a pas de module natif du moteur pour le modèle Container, Stream et Rfunction : il tourne dans la bibliothèque, et le module réactif propre du moteur est une petite table de règles sur des sous-chaînes. La garde de la ligne de temps ne vérifie ni vide, ni chevauchement, ni plage bloquée ; dans les fichiers classiques de la ligne de temps, sept échouent à leur sortie attendue et dix-huit ne promettent rien. Le navigateur de grille adossé au moteur, `stzGridNav`, n'a aucun test.

## 8. Six portes

**Le programmeur.** Liez un motif à du code, et traitez ; ou déclarez un flux et dites en mots ce qui arrive aux données qui y circulent.

**L'analyste.** Le temps est un espace de travail : les vides, les chevauchements et les régions bloquées sont calculés, et un point qui tomberait dans une région bloquée est refusé avec la raison.

**Le concepteur.** L'état d'une réaction qui change une valeur garde son pourquoi : la correspondance, la valeur calculée, la position, le déclencheur.

**Le décideur.** Le débordement est un nombre que vous pouvez lire : gardé, écarté. Une stratégie qui perdait des données sans le dire a été trouvée par un audit, et corrigée.

**Le formateur.** L'échelle est un cursus : un motif, une réaction, un état, un but.

**L'agent.** Votre esprit peut être des compétences qui s'enchaînent sur ce qu'elles perçoivent, jusqu'à ce que le monde cesse de changer.

## 9. Exercice

Écrivez un Regexuter avec deux déclencheurs, un pour les nombres et un pour les nombres de trois chiffres ou plus, avec du code qui transforme un nombre en son triple. Avant de l'exécuter, écrivez sous chaque question ce que vous attendez : quelles sont les correspondances, quels sont les résultats, et si le second déclencheur se déclenche sur le résultat du premier. Exécutez-le. Si le second déclencheur se déclenche, vous avez trouvé quelque chose que je n'ai pas trouvé.

Puis dites en une phrase ce qu'il faudrait changer dans la machine pour qu'il se déclenche, et à quel échelon de l'échelle ce changement appartient.

Je vous laisse celui-ci. Reprenez le deuxième bloc de la section 3 et écrivez ses deux lignes `Trigger` dans l'autre ordre, celui des trois chiffres d'abord :

```haro exercise
rxu() {
	Trigger(:Big = "\d{3,}")
	Trigger(:Number = "\d+")
	@C(:When = :Number, :Do = '{ @value = @number(@value) * 100 }')
	@C(:When = :Big, :Do = '{ @value = "BIG" }')
	Process("Found 7 items")
	? @@( Matches() )
	? @@( Results() )
	? @@( Triggers() )
}
```

Avant de l'exécuter, écrivez si l'ordre change ce que contiennent `Results()` et `Triggers()`. Je n'imprime pas la sortie de cette version et je ne vous donne pas la réponse : la section 3 dit contre quoi chaque déclencheur est comparé, et la section 4 dit ce que j'ai refusé d'affirmer. Quand vous saurez dire pourquoi, vous saurez ce qui sépare le deuxième échelon du troisième.

Le chapitre 10 passe de la machine qui pense au code qui change. Son titre est *La programmation devient raffinement*, et il tient à un seul principe : cessez de vouloir gouverner l'intelligence, et gouvernez le changement.
