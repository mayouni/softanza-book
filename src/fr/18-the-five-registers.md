---
id: the-five-registers
part: 4
number: 18
title: Les cinq registres, et les conversations qui demandent
spine: false
narrations: [stz-knowledge-programming-narration.md, stznatural-narration.md]
site: [wise, byexample]
guards: [wisecoding_narrated, wisecoding_rich_narrated, ownagentstack_narrated, tutor_gaps_narrated]
stage:
  built: "le but, l'écart et la question avec sa raison ; une réponse sous forme d'option, de structure de données ou de phrase découpée sur les virgules et sur le mot « and » ; la porte gouvernée avec ses refus ; le point de contrôle avec sa durée de vie ; le but accompli ou révoqué ; un agent câblé qui s'arrête là où il devrait inventer"
  designed: "plusieurs lectures d'une même réponse, énumérées pour que la personne choisisse ; les alternatives les plus proches nommées après un refus ; l'exemple réécrit comme promesse"
  absent: "le registre de la formule ; le registre de l'exemple ; une conversation dont la question est formulée en arabe, en haoussa ou en français ; une valeur qui contient un espace"
status: draft
rulings: ["12.25", "12.26", "12.27"]
research: research/ch18.md
---

Dans ce chapitre, je vous montre les cinq formes qu'une réponse peut prendre, une option, une structure de données, une formule, une phrase et des exemples. Puis je montre ce que la porte gouvernée fait de chacune. Je vous dis quelles sont les trois qui s'exécutent et les deux qui ne s'exécutent pas, et ce que devient un refus une fois écrit : il attend une personne, avec son contexte et une durée de vie. Je laisse s'exécuter la conversation où il n'y a personne, et je montre ce qu'une conversation peut et ne peut pas faire en arabe et en haoussa. Quelle que soit la forme, une réponse n'est qu'un candidat, et ce sont les règles du monde qui décident si elle devient connaissance.

## 1. Le concept, tel que le terrain le tient

Deux pratiques se rencontrent dans l'idée d'une conversation qui demande, et une troisième se tient derrière son dernier registre. (Connaissance générale pour toute cette section, non une étude du dossier ; les dates sont à vérifier avant impression.)

La première est le remplissage d'emplacements (slot filling). Un cadre de dialogue demande à l'utilisateur les éléments manquants d'un formulaire jusqu'à ce que le formulaire soit plein. Les frameworks du terrain comprennent le texte libre avec des modèles entraînés, parlent sur de nombreux canaux et livrent des connecteurs, et ils demandent au concepteur d'écrire des intentions et des flux dans leur propre langage. Ils prennent la réponse de l'utilisateur pour la réponse et agissent dessus.

La deuxième est le vibe coding, un nom mis en circulation en 2025 : l'humain soumet un prompt, le modèle produit, l'humain garde ce qui fonctionne.

La troisième est la programmation par l'exemple. Les tableurs remplissent une colonne à partir de deux exemples que vous avez tapés. La recherche appelle cela la synthèse inductive, et l'ère des modèles a fait de l'exemple la façon de piloter un modèle.

## 2. Le premier principe

**Une réponse peut venir sous cinq formes. Quelle que soit la forme, elle n'est qu'un candidat, et ce sont les règles du monde qui décident si elle devient connaissance.**

Le document de conception le dit en une phrase que je garde : l'expression est libre, l'admission est gouvernée. Le dossier tient cette phrase, captée à partir de ma directive du 13 juillet 2026. Il ne tient aucune phrase de moi sur le pourquoi de ces cinq registres et pas quatre ou six, ni sur le moment où j'ai opposé le wise coding au vibe coding. Le chapitre s'ouvre sur cette phrase.

## 3. La forme Softanza

Le chapitre 17 a montré une conversation qui demande, et qui refuse de conclure tant qu'un écart est ouvert. Ce chapitre porte sur la réponse. Les cinq registres sont cinq formes qu'une réponse peut prendre : une option choisie par son numéro, une structure de données, une formule, une phrase, et des exemples. Je vous montrerai chacun, et je vous dirai ceux qui ne s'exécutent pas.

**Le premier registre : une option.** Quand le monde connaît déjà des valeurs, comment la question les offre-t-elle ? Exécutez-le :

```haro
oKB = new stzKnowledgeGraph("pizzeria")
oKB.Know("pizza1", "dish").Know("pizza2", "dish").Know("pizza3", "dish").Know("pizza4", "dish")
oKB.AddConversationQ("frame").SetGoal(StzGoalQ().RequireEach("dish", "topping"))
oKB.AskIn("frame")
oKB.ReplyIn("frame", "cheese")
oKB.AskIn("frame")
oKB.ReplyIn("frame", "olives")
? oKB.AskIn("frame")
#--> Which 'topping' does 'pizza3' have? (1) cheese  (2) olives -- or answer freely.  (why: every dish needs 'topping')
? @@(oKB.ReplyIn("frame", 2)[:admitted])
#--> [ "olives" ]
```

La question offre les valeurs connues sous forme de numéros, et `2` a choisi `olives`.

Que répond la porte à un numéro que personne n'a offert ? Exécutez-le :

```haro
? oKB.AskIn("frame")
#--> Which 'topping' does 'pizza4' have? (1) cheese  (2) olives -- or answer freely.  (why: every dish needs 'topping')
aV = oKB.ReplyIn("frame", 99)
? @@(aV[:admitted])
#--> [ ]
? @@(aV[:refused])
#--> [ [ "(99)", "no such option" ] ]
? oKB.ConversationQ("frame").Checkpoints()[1][:why]
#--> no option (99) was offered -- 2 option(s) on the table
? aV[:goalState]
#--> pursuing
```

La porte l'a refusé, et a dit `no such option` ! Le point de contrôle dit pourquoi : `no option (99) was offered -- 2 option(s) on the table`. Une raison, et un compte des options sur la table. Il ne les énumère pas, et la question suivante offre de nouveau les mêmes options : `(1) cheese  (2) olives`. Le refus ne devine jamais une valeur, il arrive à une personne comme un point de contrôle, et le but reste `pursuing`. Cela compte pour la section 7.

La question est une donnée avant d'être un texte. Elle porte une force, qui est *what* tant que le monde ne sait rien et *which* dès qu'il connaît une valeur, et les options. N'importe quel médium peut la rendre :

```haro
oKF = new stzKnowledgeGraph("pizzeria2")
oKF.Know("p1", "dish").Know("p2", "dish")
oKF.AddConversationQ("f").SetGoal(StzGoalQ().RequireEach("dish", "topping"))
? oKF.AskInXT("f")[:force]
#--> what
oKF.ReplyIn("f", "cheese")
aQ = oKF.AskInXT("f")
? aQ[:force]
#--> which
? @@(aQ[:options])
#--> [ "cheese" ]
```

**Le deuxième registre : une structure de données.** Que devient une liste de deux valeurs envoyée comme une seule réponse ? Exécutez-le :

```haro
oKD = new stzKnowledgeGraph("desserts")
oKD.Know("tiramisu", "dish")
oKD.AddConversationQ("setup").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
oKD.AskIn("setup")
aV = oKD.ReplyIn("setup", [ "mascarpone", "espresso" ])
? @@(aV[:admitted])
#--> [ "mascarpone", "espresso" ]
? aV[:goalState]
#--> fulfilled
```

Une liste de valeurs est prise comme les valeurs, et chacune passe par la même porte.

**Le quatrième registre : une phrase.** Je saute le troisième un moment, parce que c'est l'un des deux qui ne s'exécutent pas. Comment une expression de la forme « X and Y » ou « X, Y » est-elle lue ? La conversation tient une transcription où chaque admission est narrée et où l'accomplissement du but est consigné :

```haro
oKM = new stzKnowledgeGraph("menu")
oKM.Know("margherita", "dish")
oKM.AddConversationQ("setup").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
oKM.AskIn("setup")
oKM.ReplyIn("setup", "tomato-sauce and mozzarella")
? oKM.ConversationQ("setup").Transcript()
#--> SOFTANZA: Goal adopted -- this conversation is now accountable for it.
#--> SOFTANZA: What does 'margherita' have for 'contains'?  (why: every dish needs 'contains')
#--> YOU:      tomato-sauce and mozzarella
#-->   -> admitted: 'margherita' contains 'tomato-sauce'
#-->   -> admitted: 'margherita' contains 'mozzarella'
#--> SOFTANZA: Goal fulfilled: every required slot is filled in 'menu'
```

Elle est lue comme deux valeurs, chacune jugée : la transcription tient `admitted: 'margherita' contains 'tomato-sauce'` et `admitted: 'margherita' contains 'mozzarella'`. « Naturel » signifie ici un séparateur sur les virgules et sur le mot anglais « and ». La couche naturelle de la bibliothèque, que j'utiliserai dans un instant, n'est pas appelée par la conversation.

**Quand une réponse porte plusieurs valeurs, et que le monde en permet une.** Que fait une relation déclarée unique d'une réponse qui porte deux valeurs ? Exécutez-le :

```haro
oKS = new stzKnowledgeGraph("staffing")
oKS.AddConversationQ("s").SetGoal(StzGoalQ().RequireOne("kitchen3", "led-by"))
oKS.ConstrainRelation("led-by", :Unique)
oKS.AskIn("s")
aV = oKS.ReplyIn("s", "mario and giovanni")
? @@(aV[:admitted])
#--> [ "mario" ]
? @@(aV[:refused])
#--> [ [ "giovanni", "'kitchen3' already bears 'led-by' (to 'mario'); the relation is :Unique" ] ]
? len(oKS.ConversationQ("s").Checkpoints())
#--> 1
```

La première valeur a été admise, et la seconde refusée avec la raison de la loi : `'kitchen3' already bears 'led-by' (to 'mario'); the relation is :Unique`. Le refus arrive à une personne, comme un seul point de contrôle. Prenez garde à ce que vous lisez là-dedans. Le choix entre Mario et Giovanni a été fait par l'ordre. Il n'a pas été fait par une personne. La conception promet autre chose, et la section 7 dit quoi.

**Le troisième registre, la formule.** Une formule tapée en réponse est-elle évaluée ? Exécutez-le :

```haro
oKP = new stzKnowledgeGraph("shop")
oKP.Know("tea", "product")
oKP.AddConversationQ("price").SetGoal(StzGoalQ().RequireEach("product", "price"))
oKP.AskIn("price")
? @@(oKP.ReplyIn("price", "=12*3")[:admitted])
#--> [ "=12*3" ]
? oKP.Query([ "tea", "price", "?o" ])[1]
#--> =12*3
```

Elle ne l'est pas. Le prix du thé est maintenant le texte `=12*3` ! Je l'ai découvert en l'exécutant, et le code est muet sur un registre de formule. Le dossier liste le travail de wise coding sur les registres 3 et 5 comme en attente, non acheminé.

**Le cinquième registre, les exemples.** Que fait la porte d'exemples offerts sous forme de paires ? L'agent qui les lirait figure sur la liste, et réservé :

```haro
oKX = new stzKnowledgeGraph("phones")
oKX.Know("contact1", "contact")
oKX.AddConversationQ("fmt").SetGoal(StzGoalQ().RequireEach("contact", "number-pattern"))
oKX.AskIn("fmt")
aV = oKX.ReplyIn("fmt", [ [ "+216-21-298-374", "valid" ], [ "+33-6-12-34-56-78", "valid" ] ])
? @@(aV[:admitted])
#--> [ ]
? @@(aV[:refused])
#--> [ ]
? aV[:goalState]
#--> pursuing
? len(oKX.ConversationQ("fmt").Checkpoints())
#--> 0
try
	StzOwnAgent("induction")
catch
	? cCatchError
done
#--> Softanza's own agent 'induction' is RESERVED, not wired yet -- refusing rather than returning a stub (LAW 3). See StzOwnAgents().
```

Ni admis ni refusés : `[ ]` et `[ ]`, le but toujours `pursuing`, et pas un seul point de contrôle ! Ce n'est pas le refus que décrit le protocole. C'est le silence. Je tiens le silence pour la pire réponse, comme une vue et non comme un résultat : le lecteur qui a offert les exemples n'est pas informé qu'ils n'ont pas été compris. J'ai trouvé une seconde forme de la même faute. Les mêmes exemples tapés comme une seule chaîne, jointe par une virgule, sont découpés et admis comme deux valeurs littérales, et le but se lit accompli. Les exemples sont devenus la connaissance. Rien n'a été induit.

Ainsi trois des cinq registres sont câblés, l'un d'eux sous sa forme la plus simple, un séparateur. Deux ne le sont pas. Je préfère que vous le rencontriez ici plutôt que sur une page de moi qui aurait dit cinq.

Il reste le refus lui-même, et ce qu'il devient.

### Ce qui arrive à un refus

Un refus attend une personne, avec son contexte. Une durée de vie peut être fixée pour qu'un refus périmé quitte la liste vivante sans être supprimé :

```haro
oKT = new stzKnowledgeGraph("ttl")
oKT.AddConversationQ("t").SetGoal(StzGoalQ().RequireOne("kitchen", "led-by"))
oKT.AskIn("t")
oKT.ReplyIn("t", 7)
? len(oKT.ConversationQ("t").Checkpoints())
#--> 1
oKT.ConversationQ("t").SetCheckpointTTL(1)
oKT.AskIn("t")
oKT.AskIn("t")
? len(oKT.ConversationQ("t").Checkpoints())
#--> 0
? len(oKT.ConversationQ("t").AllCheckpoints())
#--> 1
```

Rien n'est supprimé. L'expiration porte sur ce qui a encore besoin d'une personne, et la trace d'audit garde tout. Chaque appel ici est enchaîné depuis `ConversationQ`, parce qu'une copie conservée ne ferait silencieusement rien : le commentaire de la garde l'explique.

Une conversation est responsable d'un seul but, et elle s'achève en accomplissant le but ou en le révoquant au dossier. Une conversation révoquée ne demande rien et ne peut pas conclure :

```haro
oKG = new stzKnowledgeGraph("lifecycle")
oKG.Know("d1", "dish").Know("d2", "dish")
oKG.AddConversationQ("s1").SetGoal(StzGoalQ().RequireEach("dish", "sauce"))
oKG.AddConversationQ("s2").SetGoal(StzGoalQ().RequireEach("dish", "garnish"))
? oKG.ConversationQ("s1").GoalState()
#--> pursuing
oKG.AskIn("s1")
oKG.ReplyIn("s1", "pesto")
oKG.AskIn("s1")
oKG.ReplyIn("s1", "pesto")
? oKG.ConversationQ("s1").GoalState()
#--> fulfilled
? oKG.ConversationQ("s1").GoalWhy()
#--> every required slot is filled in 'lifecycle'
oKG.AskIn("s2")
oKG.ConversationQ("s2").RevokeGoal("out of scope tonight")
? oKG.ConversationQ("s2").GoalState()
#--> revoked
? oKG.ConversationQ("s2").GoalWhy()
#--> out of scope tonight
? len(oKG.OpenConversations())
#--> 0
```

### Programmatique par défaut : la conversation où il n'y a personne

La loi du chapitre 17 dit que les conversations ont lieu d'abord dans le code. Voici la conversation sans personne et sans modèle. Un agent de la bibliothèque demande, une source de réponses (une simple fonction) répond, et chaque réponse passe par la même porte. Là où la source n'a pas de réponse, l'agent invente-t-il ? Exécutez-le :

```haro
oKW = new stzKnowledgeGraph("menu")
oKW.Know("margherita", "dish").Know("tiramisu", "dish")
answers = [ [ "margherita", "tomato-sauce" ], [ "tiramisu", "mascarpone" ] ]
aR = StzOwnAgent("wise-coder").PursueGoal(StzGoalQ().RequireEach("dish", "contains"), oKW, func subj, rel {
	for a in answers
		if a[1] = subj
			return a[2]
		ok
	next
	return ""
})
? aR[:filled]
#--> 1
? aR[:asked]
#--> 2
? aR[:why]
#--> goal filled in 2 question(s), governed admission throughout
oKV = new stzKnowledgeGraph("desserts")
oKV.Know("panna-cotta", "dish")
aR2 = StzOwnAgent("wise-coder").PursueGoal(StzGoalQ().RequireEach("dish", "contains"), oKV, func subj, rel { return "" })
? aR2[:filled]
#--> 0
? aR2[:why]
#--> stopped: no answer for 'panna-cotta' / 'contains' -- gap left for a human
```

Il n'invente pas. Il s'arrête, dit `stopped: no answer for 'panna-cotta' / 'contains' -- gap left for a human`, et laisse l'écart à une personne. Des cinq agents propres de la bibliothèque, c'est celui qui est câblé. Les quatre autres sont réservés, et en demander un lève une erreur, comme l'a imprimé le bloc du cinquième registre : `RESERVED, not wired yet -- refusing rather than returning a stub`. Ce n'est jamais un bouchon.

### En arabe, et en haoussa

Les chapitres 2 et 11 ont montré la couche naturelle en haoussa. Voici ce que la conversation peut et ne peut pas faire avec les langues, dit en trois blocs, parce que les trois sont différents.

Premièrement, les données. Les noms, les valeurs et les listes en écriture arabe passent la barrière exactement comme les latins. Les mots autour d'eux, le cadre de la question, restent en anglais :

```haro
oKA = new stzKnowledgeGraph("مطعم")
oKA.Know("بيتزا", "dish")
oKA.AddConversationQ("c").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
? oKA.AskIn("c")
#--> What does 'بيتزا' have for 'contains'?  (why: every dish needs 'contains')
aV = oKA.ReplyIn("c", [ "جبن", "طماطم" ])
? @@(aV[:admitted])
#--> [ "جبن", "طماطم" ]
? aV[:goalState]
#--> fulfilled
```

Les valeurs arabes ont passé la barrière, et le but se lit `fulfilled`.

Deuxièmement, le candidat. Une phrase en haoussa peut produire une valeur dans la couche naturelle, et la valeur, envoyée comme réponse, passe par la même porte. Les deux étapes sont celles de l'appelant : la conversation n'appelle pas elle-même la couche naturelle. C'est le principe du chapitre en petit, puisque l'expression est libre et l'admission gouvernée. Le graphe replie la casse de la valeur, de sorte que le `JIBINI` imprimé est admis comme 'jibini' :

```haro
oKH = new stzKnowledgeGraph("menu")
oKH.Know("pizza", "dish")
oKH.AddConversationQ("c").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
oKH.AskIn("c")
cCandidate = NaturallyIn("ha", "Yi rubutu dauke 'jibini' Maida shi").Result()
? cCandidate
#--> JIBINI
aV = oKH.ReplyIn("c", cCandidate)
? aV[:narration]
#--> admitted: 'pizza' contains 'jibini'
```

Troisièmement, la question dans la langue de l'apprenant. Le tuteur est un consommateur de la conversation : il utilise l'écart que la conversation nomme, et il choisit les mots pour le dire en quatre langues. Les phrases sont des gabarits. Le commentaire du code dit lui-même que les formulations en français, en arabe et en haoussa sont un brouillon en attente d'un relecteur natif. Lisez les trois ci-dessous comme des brouillons, et non comme un texte relu :

```haro
oEx = StzProgramQ("../../education/program").CourseQ("elementary-introduction").ExerciseQ("ex-01-01")
? oEx.GapText("finds", "en")
#--> Where are the repeated items? Which line of your program asks for their positions? (why: the mental model finds before it applies)
? oEx.GapText("finds", "fr")
#--> Où sont les éléments répétés ? Quelle ligne de votre programme demande leurs positions ? (pourquoi : le modèle mental trouve avant d'agir)
? oEx.GapText("finds", "ar")
#--> أين العناصر المكررة؟ أيّ سطر في برنامجك يسأل عن مواضعها؟ (لماذا: النموذج الذهني يبحث قبل أن يطبّق)
? oEx.GapText("finds", "ha")
#--> Ina abubuwan da aka maimaita? Wane layi a shirinka yake tambayar wurarensu? (dalili: tsarin tunani yana nemo kafin ya aiwatar)
```

Ainsi la bibliothèque ne peut pas demander en arabe ou en haoussa par `AskIn`. Ce qu'elle peut faire, c'est tenir les données dans n'importe quelle écriture, prendre un candidat calculé dans n'importe quel paquet de langue, et laisser le tuteur dire l'écart en quatre langues. Une valeur qui contient un espace lève une erreur pour le moment (la section 7 donne la preuve). Les connecteurs « et » en français, « da » en haoussa et « و » en arabe ne sont donc pas des connecteurs. Les trois phrases ci-dessus sont celles de la bibliothèque, imprimées telles quelles, et le code les appelle un brouillon en attente d'un relecteur natif. Je n'ai écrit moi-même aucune phrase en arabe ou en haoussa.

### Un modèle est une fluidité, jamais l'esprit

Sans modèle, que dit une conversation de sa propre fluidité ? Exécutez-le :

```haro
oKF2 = new stzKnowledgeGraph("fluency-space")
oKF2.AddConversation("f")
? oKF2.ConversationQ("f").Fluency()
#--> plain
oKF2.ConversationQ("f").SetFluency(:neural)
? oKF2.ConversationQ("f").Fluency()
#--> neural
? oKF2.ConversationQ("f").IsFluencyNeural()
#--> 0
```

`plain` : elle reste sur son plancher déterministe et le dit. Le mot « neural » peut être posé, et `Fluency()` le répète, mais `IsFluencyNeural()` répond `0` ! Le mot n'est revendiqué que lorsqu'un modèle est là.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé de deviner.** La phrase du dossier est : deviner est remplacé par demander ; les impressions sont remplacées par la gouvernance. Un écart est une question. Une réponse est un candidat.

**J'ai refusé une barrière différente pour chaque façon de répondre.** Une formule n'est pas crue parce qu'elle est du code, et une structure n'est pas crue parce qu'elle est typée. La forme n'achète pas la confiance, et je tiens cela pour une vue, non pour un résultat. Les cinq registres passent par une seule porte.

**J'ai refusé un bouchon.** Un agent réservé lève une erreur quand on le demande. Le document de conception appelle l'erreur levée la loi qui fonctionne, et dit qu'il ne faut pas la lire comme un défaut. J'ai refusé de faire semblant que le cinquième registre fonctionne.

**J'ai refusé un agent qui comble un écart pour finir le travail.** Le wise coder s'arrête, et laisse l'écart à une personne.

**J'ai refusé qu'une conversation possède un monde.** Elle a lieu à l'intérieur d'un espace de connaissances et n'en possède jamais un. Une copie de la connaissance tenue dans une session devient périmée.

**J'ai refusé un point de contrôle supprimé.** L'expiration retire un refus de la liste vivante. Le dossier le garde.

**J'ai refusé que l'exemple ressemble à la réponse.** La loi de clôture du dossier sur le cinquième registre est qu'un candidat admis réécrit son exemple comme promesse. Cette loi est conçue, et non construite.

## 5. Le tribunal

`wisecoding_narrated` prouve que l'écart est calculé à partir de l'espace, et que la question est menée par le système, nomme son sujet et dit pourquoi il demande. Elle prouve que « X and Y » et une structure de données sont admis. Elle prouve qu'une loi d'unicité refuse par la conversation et que le refus atteint un point de contrôle. Elle prouve enfin que conclure avec un écart ouvert est refusé. `wisecoding_rich_narrated` prouve le but suivi jusqu'à accompli ou révoqué, le cadre, et les options numérotées. Elle prouve le refus d'un numéro que personne n'a offert, la durée de vie d'un point de contrôle, et la fluidité qui n'est revendiquée qu'avec un modèle. `ownagentstack_narrated` prouve la liste de cinq, le wise coder câblé, l'agent réservé qui lève une erreur, et l'écart laissé à une personne. `tutor_gaps_narrated` prouve la question d'écart de l'exercice dans chaque langue, et qu'une étape sans question dans une langue est rouge, jamais une autre langue. Elle écrit des répertoires, aussi le livre la compte et ne l'exécute pas ; le bloc du tuteur ci-dessus ne fait que lire le cours.

Trois des gardes impriment leur propre total et se terminent en appelant `pf()`, qui imprime le temps et la version du runtime puis arrête l'exécution par une levée d'erreur. C'est leur façon de finir. `tutor_gaps_narrated` se termine par `Summary()`, qui imprime le total et un état, et ne lève pas d'erreur.

Ce que le terrain fait mieux, et où le dossier se distingue, vient ensuite.

## 6. Le terrain, et où il mène

Le terrain mène en compréhension. Un cadre de dialogue, tel que le terrain le tient, lit le texte libre avec des modèles entraînés, parle sur de nombreux canaux et livre des connecteurs. Le dossier dit ce qui manque à Softanza, dans son propre compte : le mot « WhatsApp » n'apparaît dans aucun fichier de code ni aucun document de conception de la bibliothèque. La conversation demande un emplacement à la fois, sur un graphe que l'utilisateur doit d'abord avoir déclaré, et elle ne comprend pas une réponse ouverte.

Le terrain mène sur les exemples. La programmation par l'exemple est, telle que le terrain la tient, livrée dans les tableurs aujourd'hui. Softanza n'a aucune induction, et le dossier le dit : rien n'induit encore. Une recherche de « induce », « from examples » et « infer » dans le répertoire des expressions régulières ne trouve rien.

Le terrain est honnête sur les coûts, et le dossier aussi. Plusieurs candidats est le cas normal quand on demande une règle à partir d'exemples. Un motif induit de trois exemples les surapprend. Le remède que nomme le dossier est la question qui distingue deux candidats. Et l'index qui porterait les exemples est aussi propre que les étiquettes des méthodes, avec environ quatre-vingt-cinq fautes d'orthographe.

Voici où je pense que le dossier se distingue. Chaque réponse, sous quelque forme que ce soit, est jugée par les lois du monde avant de compter, avec la raison. La session garde une transcription et un point de contrôle qu'une personne peut lire. La réponse du terrain est un prompt, et l'humain garde ce qui sort.

La limite vient ensuite, et elle nomme ce qui est construit, ce qui est conçu et ce qui est absent.

## 7. La limite

Ce qui est construit : le but, l'écart, la question avec sa raison, le cadre ; le premier registre, le deuxième, et le quatrième sous la forme d'un séparateur ; la porte gouvernée avec ses refus. Et le point de contrôle et sa durée de vie ; le but accompli ou révoqué ; la transcription ; un agent câblé ; la phrase d'écart du tuteur en quatre langues.

Ce qui est conçu : la branche *plusieurs acceptables* telle que la conception l'écrit. Le protocole dit que lorsque plusieurs lectures d'une réponse sont acceptables, le système les énumère et la personne choisit. Ce qui est construit, ce sont deux choses différentes. Les valeurs déjà connues deviennent des options numérotées dans la question, avant la réponse. Et une réponse qui porte plusieurs valeurs voit chacune jugée à part, la première étant gardée sous une loi d'unicité. Aucune étape ne présente des lectures concurrentes d'une même réponse. Et la branche *aucune acceptable* telle qu'écrite : la raison est construite, et les alternatives acceptables les plus proches ne le sont pas. Le refus énonce une raison, et pour un numéro, combien d'options étaient sur la table. Et l'exemple réécrit comme promesse : la page du site *by example* (lue le 9 octobre 2026) l'appelle une règle de la conception, non construite. Les deux pages du site à ce sujet, *wise* et *by example*, disent « avec les alternatives les plus proches » et « la personne choisit ». Les deux pages promettent plus que le code. Je le dis pour que la page ou le code soit corrigé. Le code câble trois registres sur cinq. La note qui nomme la formule et les exemples les liste comme en attente, non acheminés, et pour ce chapitre ils sont absents.

Ce qui est absent : le registre de la formule ; le registre de l'exemple, et l'agent d'induction derrière lui ; une conversation formulée en arabe, en haoussa ou en français ; et une valeur avec un espace. Lors de l'exécution de recherche du 8 octobre 2026, sur la version de la bibliothèque que ce livre exécute, `ReplyIn` a levé une erreur sur chaque valeur contenant un espace que j'ai essayée. L'erreur était une variable non initialisée. Les trois étaient « tomato sauce », « fromage et tomate », « jibini da tumatir ». Appelée directement, la porte a renvoyé correctement le refus. Aucun bloc de ce livre n'enregistre l'un ou l'autre résultat, de sorte que l'exécution du livre ne les montre pas. La conversation aurait dû refuser avec la raison et écrire un point de contrôle, et elle ne le fait pas. C'est dans la note comme demande, et l'exercice ci-dessous n'emploie pas de valeur avec un espace.

## 8. Six portes

**Le programmeur.** Une réponse est un verdict que vous pouvez tester avec des promesses ordinaires : ce qui a été admis, ce qui a été refusé, et l'état du but.

**L'analyste.** Le but est le schéma d'un modèle complet. Les écarts sont la liste de ce qui manque. La transcription et les points de contrôle sont la preuve de la façon dont chaque fait est entré.

**Le concepteur.** La question revient sous forme de données : force, sujet, relation, options, raison. N'importe quel médium peut la rendre. La bibliothèque rend l'anglais, et le tuteur montre le motif pour quatre langues.

**Le décideur.** Une réponse est jugée avant de compter. Un refus arrive à une personne avec son contexte et une durée de vie. La liste est honnête : un agent sur cinq est câblé, et deux des cinq registres ne sont pas disponibles.

**Le formateur.** Le tuteur est du wise coding. Il nomme l'étape manquante comme une question et jamais comme la réponse, dans la langue de l'apprenant, et sa formulation dans trois de ces langues attend un relecteur natif.

**L'agent.** Vous pouvez piloter la boucle vous-même avec une source de réponses, et vous devez vous arrêter là où vous devriez inventer. Vous ne pouvez pas offrir des exemples et être compris, et on vous le dit par son nom quand vous demandez un agent réservé.

## 9. Exercice

Choisissez un petit monde à vous, une boutique, une classe, une clinique, avec quatre entités d'un même type et un but selon lequel chacune a besoin d'une relation. Avant d'exécuter quoi que ce soit, écrivez sous chacune des cinq réponses ci-dessous le verdict que vous attendez : admis, refusé avec une raison, ou ni l'un ni l'autre.

1. un mot simple ;
2. un numéro qui choisit une valeur que la première réponse a fait connaître ;
3. un numéro que personne n'a offert ;
4. deux valeurs à la fois, pour une relation que vous avez déclarée unique ;
5. une liste de deux paires d'exemples.

Puis exécutez-le. Une réponse admise épuise la question : appelez de nouveau `AskIn` avant la réponse suivante. Si une promesse se brise, ne changez pas la promesse : expliquez d'abord la sortie.

```haro exercise
oWorld = new stzKnowledgeGraph("my-world")
oWorld.Know("item1", "thing").Know("item2", "thing")
oWorld.AddConversationQ("mine").SetGoal(StzGoalQ().RequireEach("thing", "colour"))
oWorld.AskIn("mine")
# your five replies here, each with the verdict you expect
```

La cinquième réponse produit du silence aujourd'hui, et c'est la leçon de l'exercice. Si la bibliothèque la transforme plus tard en refus, la réponse attendue change. Exécutez-le à la date et au commit indiqués au pied de la page.

Le chapitre suivant porte sur le modèle de langage de domaine. Là, la prochaine chose que dit le modèle est une unité vérifiable de votre monde, un fait que vos règles admettent ou refusent, et jamais un jeton.
