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
  built: "le premier échelon du modèle de langage de domaine ; la conversation qui demande ; la dérivation avec sa preuve ; l'agent programmatique ; la barrière qui refuse un modèle non gouverné"
  designed: "la cascade de la machine pensante entre les facultés ; l'unité typée de prédiction validée en cinq étapes ; la négociation entre un agent et son relecteur"
  absent: "quatre des cinq agents propres de la bibliothèque, dont l'induction à partir d'exemples"
status: draft
rulings: ["12.18", "12.19", "12.25", "12.26", "12.29"]
research: research/ch17.md
---

## Ce que l'âge de l'IA change ici

Dans les deux mouvements qui précèdent celui-ci, l'âge de l'IA a changé une chose chacun. En programmation, il a changé qui écrit le code. Dans les langages, il a changé qui prononce la phrase. Ici il change tout, parce que ce mouvement porte sur l'intelligence elle-même, et que le terrain emploie désormais le mot pour dire une seule chose : un grand modèle de langage à l'intérieur de votre logiciel.

Alors ce chapitre fait ce que font les deux autres chapitres de loi, et énonce la loi de sa partie avant les preuves. Il dit aussi comment la partie dépend des autres, parce que l'ordre de ce livre va du familier au nouveau, et que l'ordre du dossier va dans l'autre sens. L'intelligence, dans Softanza, est gouvernée par ce qui l'a précédée. Le tribunal qui juge la phrase d'un modèle est le tribunal de la Partie II, qui juge le code quel que soit son auteur. La phrase qu'il juge est une phrase d'un langage fermé, qui est la Partie III. On ne peut mettre un modèle en dernier que parce qu'il y a quelque chose de solide à mettre en premier.

## 1. Le concept, tel que le terrain le tient

Demandez au terrain ce qui rend une application intelligente et la réponse est un modèle. Un agent, au sens du terrain, est un modèle dans une boucle avec des outils, une mémoire et un but. La liste de courses pour en construire un en 2026 est longue : un projet en Python, un fournisseur de modèle, un framework qui câble la boucle comme un graphe, un magasin de vecteurs pour la mémoire, des outils avec des schémas typés, un service de traçage, et un chapitre de conseils de sécurité. La mémoire est souvent de la récupération : une collection de documents, découpés en morceaux, cherchés par similarité et collés dans le prompt.

La sécurité, dans ce tableau, est une propriété de l'agent. C'est l'alignement, les garde-fous, un prompt qui demande confirmation, une case marquée « humain dans la boucle ». Le terrain a aussi appris à tenir la sortie d'un modèle dans une forme, avec des grammaires qui contraignent ce qu'il peut émettre. Tout cela est un travail sérieux, et une partie est très bonne. Tout cela partage une hypothèse : le modèle est l'esprit, et tout le reste est autour de lui.

## 2. Le premier principe

**L'esprit est programmatique par défaut ; un modèle est une faculté parmi d'autres, la dernière appelée, et ce qu'il dit est une proposition que le tribunal admet ou refuse.**

## 3. La forme Softanza

Commençons par ma définition, parce que tout ce qui suit en découle. L'intelligence est la capacité computationnelle de dériver de nouvelles connaissances à partir de connaissances existantes. Rien dans cette phrase n'a besoin d'un modèle.

Voici un modèle de langage de domaine sans aucun neurone. Il est forgé à partir d'un petit graphe de connaissances d'un restaurant, et il répond à partir de ce qui a été enregistré :

```haro
oKB = new stzKnowledgeGraph("restaurant")
oKB.Know("margherita", "dish").
    KnowRelation("margherita", "contains", "tomato-sauce").
    KnowRelation("margherita", "contains", "mozzarella")
oDLM = StzDlmQ(oKB)
? oDLM.Ask("margherita contains what?")
#--> Margherita contains tomato-sauce and mozzarella.
? oDLM.Why()
#--> recorded fact(s): 'margherita' contains tomato-sauce, mozzarella
? oDLM.AskXT("margherita contains what?")[:certainty]
#--> 1
? oDLM.Ask("who won the 1998 world cup?")
#--> That is outside the 'restaurant' domain (I know 1 entities and 1 relations).
```

Il répond, dit pourquoi, et énonce sa certitude. Et quand on lui demande ce qu'il ne sait pas, il ne devine pas : il refuse, et il vous dit combien son monde est petit. Un refus qui nomme sa frontière vaut mieux qu'une réponse fluide qui n'en a pas.

Voici maintenant la deuxième pièce, celle qui retourne le dialogue habituel. Sur le terrain, vous soumettez un prompt à la machine et gardez ce qui en sort. Ici le système vous interroge :

```haro
oMenu = new stzKnowledgeGraph("menu")
oMenu.Know("margherita", "dish").Know("tiramisu", "dish")
oMenu.AddConversationQ("setup").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
? oMenu.AskIn("setup")
#--> What does 'margherita' have for 'contains'?  (why: every dish needs 'contains')
try
	oMenu.ConcludeIn("setup", "menu")
catch
	? cCatchError
done
#--> Can't conclude: 2 gap(s) remain -- the wise-coding loop is not done. Ask the next question.
```

Un but a été déclaré : chaque plat doit dire ce qu'il contient. L'écart entre le but et ce qui est connu a engendré la question, et la question porte sa raison. Le monde ne peut pas être clos tant qu'il est incomplet. Le chapitre 18 montre les cinq façons de répondre : une option d'une liste, une structure de données, une formule, une phrase, ou des exemples. Le modèle, s'il y en a un, est le dernier de ces moyens, pas le premier.

La troisième pièce est la dérivation, ma définition à l'œuvre. Une loi est déclarée, et un fait que personne n'a enregistré est prouvé :

```haro
oKG = new stzKnowledgeGraph("kitchen")
oKG.ConstrainRelation("contains", :Transitive)
oKG.KnowRelation("margherita", "contains", "tomato-sauce").
    KnowRelation("tomato-sauce", "contains", "tomato")
? oKG.Prove([ "margherita", "contains", "tomato" ])[:narration]
#--> proved: margherita contains tomato-sauce contains tomato
? oKG.Prove([ "margherita", "contains", "luigi" ])[:narration]
#--> not derivable: no recorded fact or lawful chain gives 'margherita' contains 'luigi'
```

De la connaissance nouvelle à partir de la connaissance existante, avec sa chaîne écrite en toutes lettres. Et un « non » aussi certain que le « oui », parce qu'il est le résultat d'une recherche, pas d'une humeur. Pas de récupération, pas d'entraînement. Ajouter un fait fait que le système sait davantage ; ajouter une loi lui fait raisonner plus loin.

Puis le modèle. Il est le bienvenu, et il est tenu. Branchez la sortie d'un modèle directement sur un effet, ici l'envoi d'un message, et la composition est refusée avant que rien ne s'exécute :

```haro
oG = new stzAgentGraph("mailer")
oG.AddLLMActor("writer")
oG.AddEffect("send")
oG.Proposes("writer", "send")
? oG.IsSound()
#--> 0
? len(oG.Violations())
#--> 3
```

Trois lois se déclenchent : tout effet doit passer une barrière, tout texte libre doit avoir un endroit sûr où atterrir, et tout effet doit laisser un témoin. Un acteur modèle ne détient aucune capacité à effet ; il propose, et c'est tout son pouvoir :

```haro
oF = new stzLLMFunction("sum")
oF.SetPrompt("summarize: {input}")
oF.Budget(2)
oF.SeedAnswer("hello world", "a greeting")
oLLM = new stzLLMAgent("summarizer")
oLLM.SetSkillFrom(oF)
? oLLM.Propose("hello world")
#--> a greeting
? oLLM.HoldsEffectful()
#--> 0
```

Aucun modèle n'est chargé dans ce bloc : la réponse est fixée d'avance, comme un test fixe une réponse golden, afin que la page s'exécute de la même façon chaque nuit. Ce que le bloc prouve ne dépend pas du modèle : quoi qu'il dise, il ne détient rien qui puisse agir.

Et l'agent lui-même a un esprit fait de code. Une compétence est une condition et une action ; elle se déclenche sur ce que l'agent perçoit ; et la gouvernance soumet l'acte à la barrière avant qu'il ait lieu :

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

Le stock est bas, la compétence veut commander, et l'agent n'a jamais reçu la permission. Il ne se passe rien, et le journal dit pourquoi, par son nom. Le monde est comme il était.

Mettez les pièces sur une ligne et vous avez la pile que nomme la vision de la plateforme : percevoir, décider, réagir, apprendre, sans aucun modèle de langage. La perception classe le monde dans le graphe de connaissances. Un planificateur décide. Des règles réagissent. L'agent note ses plans et garde le meilleur. Un modèle peut se tenir à côté de chaque étape comme une faculté de plus, et aucune ne dépend de lui.

Le chapitre 18 raconte les cinq registres d'une réponse et la conversation qui demande. Le chapitre 19 raconte le modèle de langage de domaine, de son premier échelon, sans neurones, à son second, entraîné sur les faits propres du premier et rien d'autre. Le chapitre 20 raconte l'agent qui ne peut pas vous nuire : il propose, un atelier répète, le tribunal juge, et seul un acteur gouverné valide. Le chapitre 21 raconte le tribunal lui-même. Le chapitre 22 compare tout cela au terrain, et imprime où le terrain mène.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé le modèle comme esprit.** Quand les modèles sont arrivés, le geste évident était d'en mettre un au centre et de l'enclore. J'ai écrit le contraire dans l'architecture : l'esprit est programmatique par défaut, et un modèle est une faculté enfichable, l'une parmi plusieurs, jamais la définition de l'esprit. La boucle de l'industrie est un cas particulier de cette conception, avec une seule faculté et aucune gouvernance. [AUTHOR: Y a-t-il un moment ou une phrase de vous, antérieur à l'architecture de juillet 2026, sur lequel ce chapitre devrait s'ouvrir ?]

**J'ai refusé tout ce qui est payant ou distant comme exigence.** Chaque capacité a un plancher qui n'exige ni installation, ni abonnement, ni réseau. Un modèle peut être ajouté par-dessus. Il n'est jamais le prix d'entrée. [AUTHOR: Quand un modèle est appelé en dernier, peut-il s'agir d'un modèle de pointe distant, sous un budget et sous le tribunal, ou « en dernier » désigne-t-il toujours un modèle local ? Le dossier soutient les deux lectures.]

**J'ai refusé de deviner.** Toute ambiguïté refuse plutôt que de deviner. L'habitude du terrain de soumettre un prompt et de garder ce qui sort a désormais un nom ; ici, deviner est remplacé par demander, et les impressions sont remplacées par la gouvernance.

**J'ai refusé la récupération comme mémoire.** La mémoire est un graphe gouverné, non un tas de fragments semblables. La dérivation remplace la récupération : le système sait ce qu'on lui a dit et ce qui en découle par la loi, et il peut prouver les deux.

**J'ai refusé un enseignant que je ne peux pas voir.** Le second échelon du modèle de langage de domaine est entraîné sur les faits de la base de connaissances du premier échelon et sur rien d'autre, et aucun modèle distant ne l'enseigne. La conception va plus loin et dit que le texte d'entraînement du second échelon est validé par la grammaire du premier avant d'être admis, de sorte qu'il est correct par construction. Dans la bibliothèque, les faits sont rendus directement en texte, sans encore une telle vérification ; le chapitre 19 dit où cela en est. J'ai donné le concept d'un modèle de langage de domaine, conçu d'abord pour l'un des produits du domaine, à la fondation ouverte, afin que tout projet qui fournit une base de connaissances puisse livrer gratuitement son propre modèle.

**J'ai refusé un bouchon.** La bibliothèque déclare cinq agents propres et en a câblé un. En demander un qui n'est pas câblé lève une erreur ; elle ne renvoie pas quelque chose qui ressemble à un agent. Faire semblant serait plus facile, et cela ferait valoir moins tous les autres refus de ce chapitre.

## 5. Le tribunal

Chaque bloc ci-dessus repose sur une garde. `dlm_narrated` prouve le modèle de langage de domaine : des réponses avec leur pourquoi, le refus hors du domaine, la complétion tenue aux entités et aux relations du domaine, un lot autonome, et un second échelon entraîné sur son propre corpus. `wisecoding_narrated` prouve la conversation qui demande et le refus de conclure. `knowledge_integration_narrated` prouve la dérivation et le « non » certain. `agentgraph_narrated` prouve qu'un modèle branché directement sur un effet n'est pas sain, que la forme gouvernée l'est, et qu'un acteur modèle propose et ne valide jamais. `piagent_narrated` prouve l'agent programmatique et son refus à la barrière. `ownagentstack_narrated` prouve la liste honnête des agents propres de la bibliothèque.

## 6. Le terrain, et où il mène

Le terrain mène en portée. Ses frameworks se connectent à des services hébergés de toutes sortes, ses magasins cherchent dans des collections ouvertes de documents, et ses boucles appellent les plus grands modèles disponibles à chaque étape. L'inversion de Softanza, constituer un domaine et en dériver, gagne sur un domaine constitué et perd sur le web ouvert. Quand la tâche est un travail de langage ouvert sur une matière que personne ne peut constituer, résumer des documents arbitraires ou faire de la recherche sur le web, la pile du terrain est le bon outil, et le dossier le dit en ces mots.

Le terrain mène sur le marché. Il existe un marché du travail pour sa pile, et pas encore pour celle-ci.

Le terrain mène sur les modèles. Le second échelon du modèle de langage de domaine, tel que construit, est un petit modèle neuronal de paires de mots, et l'étape qui ferait de lui davantage n'est pas commencée. Softanza ne construit pas les grands générateurs et ne rivalise pas avec eux.

Là où je pense que la loi se distingue, c'est en trois endroits. Une décision ici ne coûte rien, s'exécute hors ligne et donne la même réponse chaque jour, de sorte qu'on peut la tester avec des promesses ordinaires. Un modèle ici ne peut pas agir, par construction, pas par vigilance. Et la phrase d'un modèle, là où l'on en emploie un, peut être tenue à la grammaire d'un langage déclaré avant d'être émise, au lieu d'être vérifiée puis relancée après.

## 7. La limite

Ce qui est construit : le premier échelon du modèle de langage de domaine, la conversation qui demande, la dérivation avec sa preuve, l'agent programmatique, et la barrière qui refuse une composition non gouvernée.

Ce qui est conçu : la machine pensante du chapitre 9, où de nombreuses facultés partagent un état et se déclenchent en cascade jusqu'à ce qu'il se stabilise ; l'unité typée de prédiction, validée en cinq étapes avant de pouvoir entrer dans le graphe ; la conversation entre un agent et celui qui relit son plan, qui atteint le plan et pas encore la discussion à son sujet.

Ce qui est absent : quatre des cinq agents propres de la bibliothèque. La liste le dit simplement :

```haro
? len(StzOwnAgents())
#--> 5
? StzOwnAgentIsWired("wise-coder")
#--> 1
? StzOwnAgentIsWired("induction")
#--> 0
```

Le validateur, le classeur, le planificateur et l'agent qui induirait un motif à partir de vos exemples sont déclarés et réservés. Ainsi le cinquième registre d'une réponse, les exemples, attend un agent qui n'existe pas encore.

Et une limite du premier échelon que vous rencontrerez dès que vous reformulerez une question. Il ne reconnaît une relation que par le mot avec lequel elle a été déclarée. Demandez avec d'autres mots, et il ne refuse pas ; il répond à une autre question :

```haro
? oDLM.Ask("what does margherita contain?")
#--> Margherita is a dish.
```

Cette réponse est vraie, et ce n'est pas ce qui était demandé. Par la loi de ce chapitre, cela aurait dû être un refus. Je la montre ici plutôt que de la cacher, parce qu'une loi ne vaut que ce que vaut la page qui imprime où elle est brisée. La demande à la bibliothèque est de refuser une question dont le verbe n'est pas une relation déclarée.

## 8. Six portes

**Le programmeur.** L'esprit de votre agent est du code que vous pouvez tester avec des promesses ordinaires. Un modèle peut être une faculté ; il ne peut jamais détenir un effet.

**L'analyste.** Un fait ou une règle que vous ajoutez fait que le système en sait plus, sans changement de code et sans entraînement, et chaque réponse porte son pourquoi.

**Le concepteur.** Le système pose à l'utilisateur une question responsable à la fois, et la question peut être rendue dans n'importe quel médium : un terminal, une page, un agent.

**Le décideur.** Une décision ne coûte rien par appel, s'exécute hors ligne et est la même demain. Les quatre agents encore réservés sont l'écart honnête.

**Le formateur.** La conversation demande et ne répond jamais la première, et elle n'emploie la fluidité d'un modèle que lorsqu'un modèle est réellement là, de sorte qu'un apprenant voit toujours le plancher.

**L'agent.** Vous pouvez proposer. Vous ne pouvez pas valider. Un refus nomme sa loi, et vous pouvez apprendre la plateforme depuis la plateforme et être corrigé par elle.

## 9. Exercice

Construisez un domaine à vous avec trois faits : une boutique, une clinique, une classe. Avant d'exécuter quoi que ce soit, écrivez sous chaque ligne la promesse que vous attendez : une question dans le domaine, une hors du domaine et, avec un but selon lequel chaque élément doit avoir une relation, la première question que le système vous posera. Puis exécutez-le.

Si une promesse est brisée, ne changez pas la promesse pour qu'elle corresponde à la sortie. Expliquez d'abord la sortie. Vous découvrirez peut-être, comme moi, que la machine a répondu à une question que vous n'aviez pas posée.
