---
id: law-programmatic-by-default
part: 4
number: 17
title: "Loi : programmatique par défaut, le modèle en dernier, l'admission plutôt que la génération"
law: "programmatic by default, the model last, admission over generation"
spine: true
narrations: [stz-agents-that-cannot-hurt-you-narration.md, stz-service-virtualization-code-first-subscribe-later.md, stz-knowledge-programming-narration.md]
site: [agentic, wise]
guards: [dlm_narrated, wisecoding_narrated, knowledge_integration_narrated, agentgraph_narrated, piagent_narrated, ownagentstack_narrated]
stage:
  built: "le premier échelon du modèle de langage de domaine et son second, un petit bigramme ; la conversation qui demande ; la dérivation avec sa preuve ; l'agent programmatique ; la barrière qui refuse un modèle d'IA non gouverné"
  designed: "la cascade de la machine pensante entre les facultés ; la pile de décision, ses pièces à côté de l'agent et pas encore dedans ; l'unité typée de prédiction, une conception du domaine de projets avec cinq étapes de validation et aucune chaîne de celles-ci dans la bibliothèque ; la négociation entre un agent et son relecteur"
  absent: "quatre des cinq agents propres de la bibliothèque, dont l'induction à partir d'exemples"
status: draft
rulings: ["12.18", "12.19", "12.25", "12.26", "12.29"]
research: research/ch17.md
---

Dans ce chapitre, j'énonce la loi de la partie IV et je la fais tourner. Je commence par ma définition de l'intelligence et par un modèle de langage de domaine sans aucun neurone, qui répond, dit pourquoi, et refuse ce qu'on ne lui a jamais dit. Puis je montre une conversation qui vous interroge, un fait que personne n'a enregistré prouvé à partir d'une seule loi déclarée, un modèle d'IA tenu à proposer, et un agent dont l'esprit est du code, refusé à la barrière. Je dis ce que j'ai refusé, quelles gardes prouvent chaque bloc, et où le terrain mène. Vient ensuite la limite, imprimée comme l'étape qu'elle est : une question posée avec d'autres mots, et une réponse là où un refus est l'étape suivante. La loi elle-même tient en une phrase : l'esprit est programmatique par défaut, un modèle est une faculté parmi d'autres, la dernière appelée, et ce qu'il dit est une proposition que le tribunal admet ou refuse.

## Ce que l'âge de l'IA change ici

Dans les deux mouvements qui précèdent celui-ci, l'âge de l'IA a changé une chose chacun. En programmation, il a changé qui écrit le code. Dans les langages, il a changé qui prononce la phrase. Ici il change tout, parce que ce mouvement porte sur l'intelligence elle-même, et que le terrain emploie désormais le mot surtout pour dire une seule chose : un grand modèle de langage à l'intérieur de votre logiciel.

Alors ce chapitre fait ce que font les deux autres chapitres de loi, et énonce la loi de sa partie avant les preuves. Il dit aussi comment la partie dépend des autres, parce que l'ordre de ce livre va du familier au nouveau. L'intelligence, dans Softanza, est gouvernée par ce qui l'a précédée. Le tribunal qui juge la phrase d'un modèle est le tribunal de la Partie II, qui juge le code quel que soit son auteur. La phrase qu'il juge est une phrase d'un langage fermé, qui est la Partie III. On ne peut mettre un modèle en dernier que parce qu'il y a quelque chose de solide à mettre en premier.

## 1. Le concept, tel que le terrain le tient

Demandez au terrain ce qui rend une application intelligente et la réponse est un modèle d'IA. Un agent d'IA, au sens du terrain, est un modèle dans une boucle avec des outils, une mémoire et un but. La liste de courses pour en construire un en 2026 est longue. Il faut un projet en Python, un fournisseur de modèle, un framework qui câble la boucle comme un graphe, un magasin de vecteurs pour la mémoire, des outils avec des schémas typés, un service de traçage, et un chapitre de conseils de sécurité. La mémoire est souvent de la récupération : une collection de documents, découpés en morceaux, cherchés par similarité et collés dans le prompt.

La sécurité, dans ce tableau, est une propriété de l'agent. C'est l'alignement, les garde-fous, un prompt qui demande confirmation, une case marquée « humain dans la boucle ». Le terrain a aussi appris à tenir la sortie d'un modèle dans une forme, avec des grammaires qui contraignent ce qu'il peut émettre. Tout cela est un travail sérieux, et une partie est bonne. Tout cela partage une hypothèse : le modèle est l'esprit, et tout le reste est autour de lui.

## 2. Le premier principe

**L'esprit est programmatique par défaut ; un modèle est une faculté parmi d'autres, la dernière appelée, et ce qu'il dit est une proposition que le tribunal admet ou refuse.**

## 3. La forme Softanza

Commençons par ma définition, parce que tout ce qui suit en découle. L'intelligence est la capacité computationnelle de dériver de nouvelles connaissances à partir de connaissances existantes. Rien dans cette phrase n'a besoin d'un modèle.

Voici un modèle de langage de domaine sans aucun neurone, forgé à partir d'un petit graphe de connaissances d'un restaurant. Que répond-il à partir de ce qui a été enregistré, et que dit-il de la coupe du monde de 1998 ? Exécutez-le :

```haro
oKB = new stzKnowledgeGraph("restaurant")
oKB {
	Know("margherita", "dish")
	KnowRelation("margherita", "contains", "tomato-sauce")
	KnowRelation("margherita", "contains", "mozzarella")
}
oDLM = StzDlmQ(oKB)
oDLM {
	? Ask("margherita contains what?")
	#--> Margherita contains tomato-sauce and mozzarella.
	? Why()
	#--> recorded fact(s): 'margherita' contains tomato-sauce, mozzarella
	? AskXT("margherita contains what?")[:certainty]
	#--> 1
	? Ask("who won the 1998 world cup?")
	#--> That is outside the 'restaurant' domain (I know 1 entities and 1 relations).
}
```

Il répond, dit pourquoi (`recorded fact(s): 'margherita' contains tomato-sauce, mozzarella`), et énonce sa certitude (`1`). Et quand on lui demande ce qu'il ne sait pas, il ne devine pas. Il refuse, et il vous dit combien son monde est petit : `I know 1 entities and 1 relations`. Une entité, parce que seule `margherita` a été déclarée par `Know`, et une relation, `contains` : les objets des deux faits ne sont pas comptés comme des entités. Un refus qui nomme sa frontière vaut mieux qu'une réponse fluide qui n'en a pas. C'est mon point de vue.

Voici maintenant la deuxième pièce, celle qui retourne le dialogue habituel. Sur le terrain, vous soumettez un prompt à la machine et gardez ce qui en sort. Ici le système vous interroge. Que demande-t-il, et que se passe-t-il si vous essayez de conclure avant d'avoir répondu ?

```haro
StzKnowledgeGraphQ("menu") {
	Know("margherita", "dish")
	Know("tiramisu", "dish")
	AddConversationQ("setup").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
	? AskIn("setup")
	#--> What does 'margherita' have for 'contains'?  (why: every dish needs 'contains')
	try
		ConcludeIn("setup", "menu")
	catch
		? cCatchError
	done
	#--> Can't conclude: 2 gap(s) remain -- the wise-coding loop is not done. Ask the next question.
}
```

Un but a été déclaré : chaque plat doit dire ce qu'il contient. L'écart entre le but et ce qui est connu a engendré la question, et la question porte sa raison. Le monde ne peut pas être clos tant qu'il est incomplet : `Can't conclude: 2 gap(s) remain`. Le chapitre 18 montre les cinq façons de répondre : une option d'une liste, une structure de données, une formule, une phrase, ou des exemples. Trois sont câblées ; la formule et les exemples sont absents. Un modèle d'IA, s'il y en a un, vient après toutes, pas en premier.

La troisième pièce est la dérivation, ma définition à l'œuvre. Une loi est déclarée, et un fait que personne n'a enregistré est prouvé :

```haro
StzKnowledgeGraphQ("kitchen") {
	ConstrainRelation("contains", :Transitive)
	KnowRelation("margherita", "contains", "tomato-sauce").
	    KnowRelation("tomato-sauce", "contains", "tomato")
	? Prove([ "margherita", "contains", "tomato" ])[:narration]
	#--> proved: margherita contains tomato-sauce contains tomato
	? Prove([ "margherita", "contains", "luigi" ])[:narration]
	#--> not derivable: no recorded fact or lawful chain gives 'margherita' contains 'luigi'
}
```

De la connaissance nouvelle à partir de la connaissance existante, avec sa chaîne écrite en toutes lettres ! Et un « non » aussi certain que le « oui », parce qu'il est le résultat d'une recherche, pas d'une humeur. La page l'a imprimé ainsi : `not derivable: no recorded fact or lawful chain gives 'margherita' contains 'luigi'`. Il est certain de ce qui est enregistré et déclaré, pas du monde : il dit `not derivable`, pas « faux ». Pas de récupération, pas d'entraînement. Ajouter un fait fait que le système sait davantage ; ajouter une loi lui fait raisonner plus loin.

Puis le modèle d'IA. Il est le bienvenu, et il est tenu. Branchez la sortie d'un modèle directement sur un effet, ici l'envoi d'un message. La composition est-elle saine ?

```haro
oG = new stzAgentGraph("mailer")
oG {
	AddLLMActor("writer")
	AddEffect("send")
	Proposes("writer", "send")
	? IsSound()
	#--> 0
	? len(Violations())
	#--> 3
}
```

Elle ne l'est pas : `IsSound()` a imprimé `0`, et elle est refusée avant que rien ne s'exécute ! Trois lois se déclenchent, et `len(Violations())` a imprimé `3` : tout effet doit passer une barrière, tout texte libre doit avoir un endroit sûr où atterrir, et tout effet doit laisser un témoin. Que détient un acteur modèle qui puisse agir ? Aucun modèle d'IA n'est chargé dans le bloc qui le demande : la réponse est fixée d'avance, comme un test fixe une réponse golden, afin que la page s'exécute de la même façon chaque nuit. Interrogez-en un :

```haro
oF = new stzLLMFunction("sum")
oF {
	SetPrompt("summarize: {input}")
	Budget(2)
	SeedAnswer("hello world", "a greeting")
}
oLLM = new stzLLMAgent("summarizer")
oLLM {
	SetSkillFrom(oF)
	? Propose("hello world")
	#--> a greeting
	? HoldsEffectful()
	#--> 0
}
```

Rien. Un acteur modèle ne détient aucune capacité à effet ; il propose, et c'est tout son pouvoir. `HoldsEffectful()` a imprimé `0`. Ce que le bloc prouve ne dépend pas du modèle : quoi qu'il dise, il ne détient rien qui puisse agir.

Et l'agent programmatique lui-même a un esprit fait de code. Une compétence est une condition et une action, et elle se déclenche sur ce que l'agent perçoit. La gouvernance soumet l'acte à la barrière avant qu'il ait lieu. Quand le stock est bas et que la compétence veut commander, l'acte passe-t-il ?

```haro
oRog = new stzPIAgent("rogue-bot")
oRog.MemoryQ().Learn("stock", "level", "low")
oRog.GovernanceQ().DeclareRisk("order-stock", 2)
oSk = new stzAgentSkill("restock")
oSk.SetWhen(func oM { return oM.Fact("stock", "level", "low") })
oSk.SetDoes(func oM { oM.Learn("stock", "level", "ordered")  return 1 })
oRog.AddGovernedSkill(oSk, "order-stock")
? oRog.Pursue()
#--> 0
? oRog.DecisionLog()[1][:why]
#--> refused: 'rogue-bot' lacks PERMISSION (can) for 'order-stock'
```

Le stock est bas, la compétence veut commander, et l'agent n'a jamais reçu la permission. `Pursue()` a imprimé `0` : la gouvernance l'a refusé ! Il ne se passe rien, et le journal dit pourquoi, par son nom : `refused: 'rogue-bot' lacks PERMISSION (can) for 'order-stock'`. Le monde est comme il était.

Mettez les pièces sur une ligne et vous avez la pile que la vision de la plateforme nomme son Étoile polaire, ratifiée le 27 septembre 2026 : percevoir, décider, réagir, apprendre. Rien de tout cela n'a besoin d'un modèle de langage. C'est une conception, pas un agent assemblé. Dans cette conception, la perception classe le monde dans le graphe de connaissances. Un planificateur décide. Des règles réagissent. L'agent note ses plans et garde le meilleur. Les pièces existent dans la bibliothèque à côté de l'agent, pas encore dedans : l'agent ci-dessus n'en appelle aucune. Un modèle peut se tenir à côté de chaque étape comme une faculté de plus, et aucune ne dépend de lui.

Le chapitre 18 raconte les cinq registres d'une réponse et la conversation qui demande. Le chapitre 19 raconte le modèle de langage de domaine, de son premier échelon, sans neurones, à son second, entraîné sur les faits propres du premier et rien d'autre. Le chapitre 20 raconte l'agent qui ne peut pas vous nuire : il propose, un atelier répète, le tribunal juge, et seul un acteur gouverné valide. Le chapitre 21 raconte le tribunal lui-même. Le chapitre 22 compare tout cela au terrain, et imprime où le terrain mène.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé le modèle d'IA comme esprit.** Quand les modèles sont arrivés, le geste était d'en mettre un au centre et de l'enclore. J'ai écrit le contraire dans l'architecture : l'esprit est programmatique par défaut, et un modèle est une faculté enfichable, l'une parmi plusieurs, jamais la définition de l'esprit. La boucle de l'industrie est un cas particulier de cette conception, avec une seule faculté et aucune gouvernance. La plus ancienne phrase de moi que le dossier tienne là-dessus est l'architecture de juillet 2026.

**J'ai refusé tout ce qui est payant ou distant comme exigence.** Chaque capacité a un plancher qui n'exige ni installation, ni abonnement, ni réseau. Un modèle peut être ajouté par-dessus. Il n'est jamais le prix d'entrée. « En dernier » veut dire après le chemin programmatique, et sous le tribunal et un budget. Que le dernier proposant puisse être un modèle distant sous ce budget, ou doive toujours être un modèle local, le dossier admet les deux lectures, et je ne tranche pas ici entre elles.

**J'ai refusé de deviner.** Toute ambiguïté refuse plutôt que de deviner. L'habitude du terrain de soumettre un prompt et de garder ce qui sort a désormais un nom ; ici, deviner est remplacé par demander, et les impressions sont remplacées par la gouvernance.

**J'ai refusé la récupération comme mémoire.** La mémoire est un graphe gouverné, non un tas de fragments semblables. La dérivation remplace la récupération : le système sait ce qu'on lui a dit et ce qui en découle par la loi, et il peut prouver les deux.

**J'ai refusé un enseignant que je ne peux pas voir.** Le second échelon du modèle de langage de domaine est entraîné sur les faits de la base de connaissances du premier échelon et sur rien d'autre. Aucun modèle d'IA distant ne l'enseigne. La conception va plus loin et dit que le texte d'entraînement du second échelon est validé par la grammaire du premier avant d'être admis, de sorte qu'il est correct par construction. Dans la bibliothèque, les faits sont rendus directement en texte, sans encore une telle vérification ; le chapitre 19 dit où cela en est. J'ai donné le concept d'un modèle de langage de domaine, conçu d'abord pour l'un des produits du domaine de projets, à la fondation ouverte. Tout projet qui fournit une base de connaissances peut livrer gratuitement son propre modèle.

**J'ai refusé un bouchon.** La bibliothèque déclare cinq agents propres et en a câblé un. En demander un qui n'est pas câblé lève une erreur ; elle ne renvoie pas quelque chose qui ressemble à un agent. Faire semblant serait plus facile, et cela ferait valoir moins tous les autres refus de ce chapitre.

Derrière les blocs se tiennent six gardes, et la section suivante les nomme.

## 5. Le tribunal

Chaque bloc ci-dessus repose sur une garde. `dlm_narrated` prouve le modèle de langage de domaine : des réponses avec leur pourquoi, le refus hors du domaine, la complétion tenue aux entités et aux relations du domaine, un lot autonome, et un second échelon entraîné sur son propre corpus. `wisecoding_narrated` prouve la conversation qui demande et le refus de conclure. `knowledge_integration_narrated` prouve la dérivation et le « non » certain. `agentgraph_narrated` prouve qu'un modèle branché directement sur un effet n'est pas sain, que la forme gouvernée l'est, et qu'un acteur modèle propose et ne valide jamais. `piagent_narrated` prouve l'agent programmatique et son refus à la barrière. `ownagentstack_narrated` prouve la liste honnête des agents propres de la bibliothèque.

Ces six gardes prouvent ce qui a tourné ; la section suivante dit où le terrain mène.

## 6. Le terrain, et où il mène

Le terrain mène en portée. Ses frameworks se connectent à des services hébergés de toutes sortes, ses magasins cherchent dans des collections ouvertes de documents, et ses boucles appellent les plus grands modèles disponibles à chaque étape. L'inversion de Softanza, constituer un domaine et en dériver, mène sur un domaine constitué, et sur le web ouvert le terrain mène aujourd'hui. Quand la tâche est un travail de langage ouvert sur une matière que personne ne peut constituer, résumer des documents arbitraires ou faire de la recherche sur le web, la pile du terrain est le bon outil. Le dossier le dit en ces mots.

Le terrain mène sur le marché. Il existe aujourd'hui un marché du travail pour sa pile ; celui de cette pile est à venir.

Le terrain mène sur les modèles d'IA. Le second échelon du modèle de langage de domaine, tel que construit, est un petit modèle neuronal de paires de mots, et la fonderie au-delà du bigramme est conçue (chapitre 19). Softanza ne construit pas les grands générateurs et ne rivalise pas avec eux.

Là où je pense que la loi se distingue, c'est en trois endroits. Une décision ici ne coûte rien, s'exécute hors ligne et donne la même réponse chaque jour, de sorte qu'on peut la tester avec des promesses ordinaires. Un modèle d'IA ici ne peut pas agir, par construction, pas par vigilance. Et la phrase d'un modèle, là où l'on en emploie un, peut être tenue à la grammaire d'un langage déclaré avant d'être émise, au lieu d'être vérifiée puis relancée après.

La section suivante dit où la loi s'arrête.

## 7. La limite

Ce qui est construit : le premier échelon du modèle de langage de domaine et son second, un petit bigramme, la conversation qui demande, la dérivation avec sa preuve, l'agent programmatique, et la barrière qui refuse une composition non gouvernée.

Ce qui est conçu : la machine pensante du chapitre 9, où de nombreuses facultés partagent un état et se déclenchent en cascade jusqu'à ce qu'il se stabilise. La pile de décision qui perçoit, décide, réagit et apprend, dont les pièces existent à côté de l'agent et pas encore dedans. L'unité typée de prédiction, que le chapitre 19 raconte comme une conception du domaine de projets, validée en cinq étapes dans cette conception et enchaînée nulle part dans la bibliothèque. La conversation entre un agent et celui qui relit son plan : le plan atteint désormais l'agent, et la conversation à son sujet pas encore.

Ce qui est absent : quatre des cinq agents propres de la bibliothèque. Combien la bibliothèque en déclare-t-elle, et combien sont câblés ? La liste le dit clairement :

```haro
? len(StzOwnAgents())
#--> 5
? StzOwnAgentIsWired("wise-coder")
#--> 1
? StzOwnAgentIsWired("induction")
#--> 0
```

Le validateur, le classeur, le planificateur et l'agent qui induirait un motif à partir de vos exemples sont déclarés et réservés. Ainsi le cinquième registre d'une réponse, les exemples, attend un agent qui n'existe pas encore.

Et une limite du premier échelon que vous rencontrerez dès que vous reformulerez une question. Il ne reconnaît une relation que par le mot avec lequel elle a été déclarée. Que fait-il quand vous demandez avec d'autres mots ?

```haro
? oDLM.Ask("what does margherita contain?")
#--> Margherita is a dish.
```

Il n'a pas refusé ! Il a imprimé `Margherita is a dish.` Cette réponse est vraie, et ce n'est pas ce qui était demandé. Par la loi de ce chapitre, la réponse ici est un refus, et ce refus est l'étape suivante. Je l'imprime ici parce qu'une loi se montre par une page qui imprime son étape telle qu'elle est, limite comprise. La demande à la bibliothèque est de refuser une question dont le verbe n'est pas une relation déclarée.

## 8. Six portes

**Le programmeur.** L'esprit de votre agent est du code que vous pouvez tester avec des promesses ordinaires. Un modèle d'IA peut être une faculté ; il ne peut jamais détenir un effet.

**L'analyste.** Un fait ou une règle que vous ajoutez fait que le système en sait plus, sans changement de code et sans entraînement, et chaque réponse porte son pourquoi.

**Le concepteur.** Le système pose à l'utilisateur une question responsable à la fois, et la question est remise à n'importe quelle porte sous forme de cadre, pour qu'un terminal, une page ou un agent puisse la rendre. Seul le terminal a tourné ici.

**Le décideur.** Une décision ne coûte rien par appel, s'exécute hors ligne et est la même demain. Les quatre agents encore réservés sont l'étape suivante.

**Le formateur.** La conversation demande et ne répond jamais la première, et elle n'emploie la fluidité d'un modèle que lorsqu'un modèle est là, de sorte qu'un apprenant voit toujours le plancher.

**L'agent.** Vous pouvez proposer. Vous ne pouvez pas valider. Un refus nomme sa loi, et vous pouvez apprendre la plateforme depuis la plateforme et être corrigé par elle.

Voici maintenant l'exercice : un domaine à vous, et les promesses que vous attendez.

## 9. Exercice

Construisez un domaine à vous avec trois faits : une boutique, une clinique, une classe. Avant d'exécuter quoi que ce soit, écrivez sous chaque ligne la promesse que vous attendez : une question dans le domaine, une hors du domaine. Ajoutez un but selon lequel chaque élément doit avoir une relation, et écrivez la première question que le système vous posera. Puis exécutez-le.

Si une promesse est brisée, ne changez pas la promesse pour qu'elle corresponde à la sortie. Expliquez d'abord la sortie.

Je vous laisse celui-ci, volontairement. La section 7 montre une question à laquelle le premier échelon a répondu alors que la loi veut un refus, et je ne l'ai pas corrigé. Reprenez votre propre domaine et posez de nouveau l'une de vos questions promises avec d'autres mots, et un verbe que vous n'avez pas déclaré comme relation. Regardez ce qui revient et comparez-le à ce que vous avez demandé. Puis dites en une phrase pourquoi il a répondu, et quelles lignes de la section 7 vous le disent.

Quand vous l'aurez résolu, vous saurez pourquoi un premier échelon qui ne reconnaît une relation que par le mot avec lequel elle a été déclarée peut répondre à une question que vous n'avez pas posée.

Le chapitre 18 est *Les cinq registres, et les conversations qui demandent*. Son principe : une réponse peut venir sous cinq formes, et quelle que soit la forme, elle n'est qu'un candidat, et ce sont les règles du monde qui décident si elle devient connaissance.
