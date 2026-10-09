---
id: the-software-crafter
part: 1
number: 2
title: L'artisan du logiciel
spine: true
narrations: [stz-built-on-real-world-need.md, stz-service-virtualization-code-first-subscribe-later.md, stz-agents-that-cannot-hurt-you-narration.md, stz-rules-as-graph-rules-narration.md, stzOrgChartDoc-BankUseCase.md]
site: [offering, customers, forged, coding-agents]
guards: [agentfile_narrated, service_registry_narrated, graphrule_object_narrated, semantic_resolver_narrated, 00_orgchart_narrated]
stage:
  built: "le fichier d'agent et son tribunal ; le registre qui refuse un faux en production ; des règles comme données sur un modèle ; les règles d'un régulateur qui jugent un organigramme ; la couche naturelle en haoussa et en arabe"
  designed: "une page de parcours pour chaque sorte d'artisan du logiciel, chaque étape exécutée ; la porte par laquelle un agent de code demande à la bibliothèque de juger son travail"
  absent: "les plateformes des trois artisans du logiciel qui tournent sur le moteur Softanza ; le propre médium d'un artisan du logiciel, l'application de messagerie sur son téléphone, comme cible"
status: draft
rulings: ["12.2", "12.12", "12.13", "12.25", "12.29", "12.30"]
research: research/ch02.md
---

## 1. Le concept, tel que le terrain le tient

Le terrain a déjà un mot pour les programmeurs qui prennent soin de leur travail : l'artisanat (craftsmanship). Un livre de 2001 a donné son nom à l'idée, un manifeste de 2009 lui a donné son slogan, et depuis, « software craftsman » désigne un professionnel qui tient son code à un niveau plus élevé que celui que le travail exige. (Connaissance générale, non une étude du dossier.) C'est un bon mouvement. C'est aussi un mouvement de programmeurs, sur les standards des programmeurs.

Les deux autres réponses du terrain à « qui fait le logiciel, si ce ne sont pas les programmeurs » définissent la personne par un outil. La première est le low-code : des gens du métier qui construisent des applications sur la plateforme visuelle d'un éditeur, le « développeur citoyen » des analystes. La seconde est l'agent de code : un modèle qui lit des fichiers, les modifie et lance des commandes, piloté en mots simples, avec le « vibe coding » pour nom de la pratique qui consiste à garder tout ce qu'il écrit. Les deux réponses ont la même forme. La personne est définie par un outil, et le travail vit là où vit l'outil. Quand l'éditeur change ses prix ou son modèle, le travail de la personne change avec.

## 2. Le premier principe

Le site donne la définition en deux phrases, avec le mot « maker » dedans, et ce livre les prend avec le mot changé : **un artisan du logiciel transforme ce qu'il sait d'un monde en quelque chose qui tourne, sans attendre l'industrie du logiciel ; il n'est pas défini par sa compétence de programmation mais par la possession : l'artefact est à lui, en texte brut, et il n'expire pas.** [AUTHOR: Ces phrases ont été rédigées pour le site et n'ont pas été tranchées par vous dans le dossier. Et « artisanat » suggère la compétence, là où la phrase dit que l'artisan du logiciel n'est pas défini par elle. Gardez-vous la possession seule, ou formuleriez-vous la définition autour du soin qu'un artisan du logiciel prend ?]

## 3. La forme Softanza

J'ai été le premier artisan du logiciel de Softanza, et pas pour une raison que j'aurais choisie. Ma femme dirige un club de musique où l'on apprend à chanter des chansons classiques arabes. Chaque dimanche matin, elle m'envoie la liste des chansons à préparer, et je cherche leurs paroles. Les paroles trouvées en ligne répètent chaque phrase comme le chanteur l'a interprétée, et elle me rappelle, à chaque fois, d'en supprimer les doublons. J'ai écrit `RemoveDuplicates()` pour cesser de le faire à la main, et sa famille est toujours dans la bibliothèque :

```haro
o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.ContainsDuplicates()
#--> 1
? o1.NumberOfOccurrence("tea")
#--> 3
```

J'en parle dans un article sur ce sur quoi la bibliothèque a été construite : j'ai introduit ses fonctions quand un vrai problème les demandait. L'artisan du logiciel vient d'abord, et la fonction après.

Depuis 2022, je présente Softanza non par son anatomie, ses modules et ses classes, mais par qui vous êtes et ce que vous essayez de faire. La présentation de 2022 avait cinq publics, chacun avec une recette de trois à cinq étapes. Le site d'aujourd'hui a six portes, une par sorte d'artisan du logiciel, et chaque porte dit ce que vous déclarez, ce que vous obtenez, et par où commencer. Voici ce que chacune déclare, en une ou deux lignes qui s'exécutent.

**Le programmeur** déclare l'intention dans une bibliothèque qui se lit comme une phrase. Vous venez de la voir.

**L'analyste** déclare les données d'un monde, et le moteur calcule la vue. Ici, trois régions du Niger avec la population que le recensement de 2012 a comptée :

```haro
o = new stzTable([ [ :region, :population ],
    [ "Agadez", 487620 ], [ "Maradi", 3402094 ], [ "Zinder", 3539764 ] ])
o.Show()
#--> ╭────────┬────────────╮
#    │ Region │ Population │
#    ├────────┼────────────┤
#    │ Agadez │     487620 │
#    │ Maradi │    3402094 │
#    │ Zinder │    3539764 │
#    ╰────────┴────────────╯
```

**Le concepteur** déclare une image comme un programme, et obtient la même image à chaque fois :

```haro
? Q("Softanza").BoxedXT([ :AllCorners = :Round ])
#--> ╭──────────╮
#    │ Softanza │
#    ╰──────────╯
```

**Le décideur** déclare ce que chaque acteur du monde peut faire, une personne ou un agent, et le tribunal l'impose. Un agent est un petit fichier texte ; celui qui ne dit pas ce qu'il couvre est refusé quand il est chargé, non quand il agit pour la première fois :

```haro
cPia = "pia: 1
name: stock-watcher
kind: pi
reversibility: compensable
schedule:
  timer: 20
skills:
  - name: restock
    does: learn stock level ordered
"
oD = StzAgentDeclarationQ(cPia)
? oD.IsValid()
#--> 0
? oD.CiteFindings()
#--> [pia-coverage @ coverage] an agent must say WHAT IT COVERS. The engine loop refuses to schedule an agent with no coverage statement (law 18), so a file without one could never run and is refused here instead of at the first tick.
```

**Le formateur** déclare un cours, et l'apprenant parle à la machine dans sa propre langue. Une phrase en haoussa s'exécute ; le moteur compte les lettres d'un mot arabe, non ses octets, et connaît son écriture :

```haro
? NaturallyIn("ha", "Yi rubutu dauke 'hello' Maida shi").Result()
#--> HELLO
? Q("سلام").NumberOfChars()
#--> 4
? Q("مرحبا بالعالم").Script()
#--> arabic
```

**L'agent** est le sixième artisan du logiciel, celui que 2020 ne pouvait pas dessiner. Il se déclare dans le même genre de fichier, et il est le bienvenu, avec une seule chose retenue. Un agent dont l'esprit est un modèle de langage peut proposer ; il ne peut pas détenir d'effet, et un fichier qui lui en donne un est refusé à la construction :

```haro
cLlm = "pia: 1
name: rogue
kind: llm
coverage: proposes a summary
reversibility: reversible
schedule:
  timer: 20
proposes:
  prompt: Summarize {input}
  structure:
    - field: topic
      type: string
skills:
  - name: send
    when: always
    does: propose
    effect: send-email
"
oBad = StzAgentDeclarationQ(cLlm)
? oBad.IsValid()
#--> 0
? oBad.CiteFindings()
#--> [no-llm-effectful @ skills.send.effect] REFUSED: granting 'effectful' to llm actor 'rogue' -- an LLM proposes, only a pi-gate commits (no-llm-effectful, enforced at CONSTRUCTION, not merely audited).
```

Voici maintenant les trois artisans du logiciel pour qui ce livre est écrit. Ce ne sont pas des personas. Ce sont des gens avec des documents, et la partie VI raconte chacun en entier. Ici, une page chacun.

**Un restaurateur à Lyon.** Il possède un restaurant de couscous, et avec quelques voisins il voulait une plateforme pour le commerce de quartier. Les notes du projet le disent sans détour : il n'est pas programmeur. Le projet a commencé par une offre en mai 2024 puis deux années de spécification riche qui n'ont rien produit qu'il puisse utiliser. Ce qui est sorti de cet échec est la règle selon laquelle je travaille depuis : livrer petit, vite et utile, et laisser les fondations mûrir en parallèle sans jamais bloquer une livraison. Le 4 juillet 2026, il a répondu à un rapport de cadrage dans ses propres mots et a renversé l'ordre du travail : client d'abord, restaurateur ensuite, fournisseur en dernier. L'architecture du projet a été redessinée en constellation de mondes, à partir de la conception de la bibliothèque, et le premier avenant a été clos le 4 août 2026. Le projet compte onze itérations et une campagne de vingt-deux tests simulés derrière ses règles d'interface, et dans son propre rapport la vitesse de commande est sa première priorité, non négociable. Et le 19 août, après une journée de tests sur le terrain avec deux téléphones et une application de messagerie, les notes l'appellent le co-architecte du projet. [AUTHOR: Le chapitre 1 dit que la première démonstration a été faite par le propriétaire lui-même, sur son propre téléphone, par une application de messagerie. La liste de vérification du dossier pour la démonstration du 15 août la prévoit pour le propriétaire seul, avec son propre téléphone et une application de messagerie comme ligne d'assistance, et les mesures qu'il a prises par une application de messagerie sont celles du 19 août. La phrase du chapitre 1 peut-elle rester telle qu'elle est écrite ?]

L'un de ses besoins est porté par une loi de la bibliothèque : essayer les paiements avant de payer quiconque pour un compte. Un faux service de paiement est bienvenu pendant que vous répétez, et refusé quand vous passez au réel :

```haro
oReg = new stzServiceRegistry("restaurant")
oReg.Bind(:payments, new stzPaymentsSandbox())
oReg.SetPhase(:emulated)
? oReg.IsSound()
#--> 1
oReg.SetPhase(:production)
? oReg.IsSound()
#--> 0
? oReg.Findings()[1][:message]
#--> still bound to a SANDBOX in a production phase -- a fake must never ship
```

**Une banque à Niamey.** Une banque commerciale soumise aux règles de la banque centrale de l'union monétaire ouest-africaine fait tourner un produit d'évaluation d'organisation que j'ai construit, sous licence, sur son propre réseau interne ; le guide d'installation livré à la banque est le document qui l'atteste. La leçon qu'il a laissée dans la bibliothèque est qu'une organisation peut être jugée par son propre organigramme, selon les règles d'un régulateur. Déclarez un organigramme avec un directeur général et un audit interne qui lui rend compte, et les règles du régulateur répondent :

```haro
oOrg = new stzOrgChart("bank")
oOrg.AddPositionXTT("ceo", "Chief Executive", [ :department = "executive" ])
oOrg.AddPositionXTT("audit", "Internal Audit", [ :department = "audit", :reportsTo = "ceo" ])
? @@( oOrg.ValidateBCEAOGovernance() )
#--> [ [ "status", "fail" ], [ "domain", "BCEAO_governance" ], [ "issuecount", 3 ], [ "issues", [ "BCEAO-001: No Board of Directors found", "BCEAO-002: Audit reports to non-board position", "BCEAO-003: No dedicated Risk Management function" ] ] ]
```

Trois constats, chacun une règle avec un numéro qu'un auditeur peut lire. [AUTHOR: Qui, à la banque, est l'artisan du logiciel au sens de ce chapitre, et qu'a-t-il déclaré ? Le dossier montre la banque comme titulaire d'une licence d'un produit que vous avez construit ; il est muet sur ce que les gens de la banque ont eux-mêmes déclaré.]

**Une organisation sur le terrain.** Une organisation qui travaille au Niger, avec un siège à Niamey et des bases sur le terrain, a demandé un hub. Son propre cahier des charges préférait une plateforme low-code construite sur la suite bureautique d'un grand éditeur. Mon offre du 5 août 2026 a été choisie à la place, pour une raison au-dessus des autres : la possession. L'organisation possède son vocabulaire et ses règles, les change sans programmer, ne paie pas de licence par poste, et peut tout remettre à un développeur de son propre pays. L'étude de conception a été construite avec ses équipes entre le 22 septembre et le 8 octobre 2026. Deux de ses principes sont ceux du livre en petit : par défaut on travaille hors ligne, et l'agent propose tandis qu'une personne décide. Cette règle est une donnée que l'organisation attache à son propre modèle, et le modèle se juge lui-même :

```haro
oRule = new stzGraphRule("no-llm-effectful")
oRule.SetDomainQ("agentic")
oRule.WhenQ("kind", "equals", "llm_actor")
oRule.WhenQ("capabilities", "contains", "effectful")
oRule.ThenViolationQ("an LLM proposes, only a pi-gate commits")
g = new stzGraph("agents")
g.AddNode("writer")
g.SetNodeProperty("writer", "kind", "llm_actor")
g.SetNodeProperty("writer", "capabilities", [ "inference", "effectful" ])
g.AddRule(oRule)
? g.RulesAreSound()
#--> 0
```

Trois artisans du logiciel : un restaurateur qui n'est pas programmeur, une banque sous un régulateur, une organisation qui a choisi la possession plutôt qu'un éditeur. Aucun d'eux n'a attendu l'industrie du logiciel. Chacun possède, ou possédera, ce qui a été construit.

## 4. La décision, et ce que j'ai refusé

**J'ai gardé le programmeur en premier.** La vision de la plateforme, que j'ai ratifiée, le dit en une ligne : le premier public reste le programmeur d'une petite équipe ; l'ère agentique ne l'a pas remplacé, elle l'a multiplié. J'ai refusé la lecture selon laquelle les agents rendent les programmeurs obsolètes.

**J'ai ajouté l'agent comme artisan du logiciel, et retenu un pouvoir.** L'agent est le sixième lecteur de chaque langage Softanza : à la fois un constructeur et un utilisateur. Il reçoit un atelier et un tribunal. Il ne reçoit pas la capacité de valider.

**J'ai refusé « maker », et j'ai refusé « builder ».** « Maker » nomme le mouvement des ateliers, le fer à souder et l'imprimante 3D, et l'accroche du site l'a employé pendant un an. « Builder » nomme quelqu'un qui assemble ce qu'un plan dit. Aucun des deux ne dit ce que je crois qu'est la programmation. C'est un travail de la main, fait avec soin, sur quelque chose qui est à vous : c'est de l'artisanat. J'appelle la personne qui le fait un artisan du logiciel, et le mot porte la culture de l'image de couverture de ce livre autant que ma propre vision du travail. [AUTHOR: Dites avec vos propres mots ce que porte l'image de couverture, et je mettrai votre phrase ici.]

**J'ai refusé de compter un client sans document.** Le site ne compte un projet comme référence que lorsqu'un document le prouve, ne cite aucun nombre de pays ni aucun nombre de développeurs, et ne nomme un client que sur ma parole. Une leçon n'est listée que lorsqu'un fichier de la bibliothèque la porte.

**J'ai refusé de présenter la bibliothèque par son anatomie.** Depuis 2022, la porte d'entrée est qui vous êtes et ce que vous voulez faire, et l'anatomie est placée sous chaque étape. Le site garde six portes ; les parcours derrière elles, une page par artisan du logiciel avec chaque étape exécutée, sont conçus et non construits.

## 5. Le tribunal

`agentfile_narrated` prouve qu'un agent est un fichier jugé quand il est chargé : un refus par barrière, la couverture manquante parmi eux, et l'agent modèle qui détient un effet refusé par la même règle que celle qu'emploie le graphe. `service_registry_narrated` prouve qu'un bac à sable en production est une violation. `graphrule_object_narrated` prouve la règle comme un objet attaché à un modèle. `semantic_resolver_narrated` prouve le chemin haoussa. Elle ne passe pas à ce commit : je l'ai exécutée le 9 octobre 2026 et elle s'arrête sur une erreur levée par une fonction de découpage de chaînes, avant la fin, de sorte que la page compte ses assertions et ne revendique pas son verdict. `00_orgchart_narrated` prouve l'organigramme et ses validateurs.

## 6. Le terrain, et où il mène

Les agents de code mènent en mains. Ils lisent, cherchent, modifient et exécutent déjà, sur n'importe quel projet, dans n'importe quel langage. Ce qui leur manque, selon le site lui-même, c'est un moyen de connaître une interface inconnue sans deviner, de juger leur travail selon des règles et des promesses, et de présenter un changement comme une intention qu'une personne peut relire. Les juges de Softanza sont construits ; la porte entre eux et un agent de code est décidée et non construite.

Le low-code mène en base installée et en tout ce qui l'entoure. L'organisation sur le terrain garde la suite de son éditeur pour ses comptes, ses documents et ses notifications ; la plateforme de l'artisan du logiciel se place à côté des outils du terrain, non à leur place.

Les applications de messagerie mènent là où les artisans du logiciel sont déjà. Les outils du restaurateur avant le projet étaient sa tête, un carnet papier et un tableur ; son propre rapport du 4 juillet 2026 donne le tableur, et la ligne qui nomme les applications de messagerie est l'intitulé d'une option du formulaire de cadrage, et non sa réponse. Aucune page du site ne nomme ces applications, et aucun médium conversationnel n'est encore une cible de la plateforme. Le chapitre 25 parle de cet écart.

Et la porte du formateur est la moins prouvée des six. Les éditions du cours en français, en arabe et en haoussa sont des brouillons qu'aucun relecteur n'a lus, et aucune institution ne l'a adopté.

## 7. La limite

Ce qui est construit : le fichier d'agent et son tribunal ; le registre qui refuse un faux en production ; des règles comme données sur un modèle ; les règles d'un régulateur qui jugent un organigramme ; la couche naturelle en haoussa et en arabe.

Ce qui est conçu : une page de parcours pour chaque sorte d'artisan du logiciel, chaque étape exécutée dans l'ordre et une garde qui échoue quand une étape casse ; la porte par laquelle un agent de code demande à la bibliothèque de juger son travail.

Ce qui est absent : les plateformes des trois artisans du logiciel qui tournent sur le moteur Softanza. Aujourd'hui la plateforme du restaurant est un ensemble de mondes web, chacun un fichier unique ; celle de la banque est une application Python ; le hub de l'organisation est une conception. Leurs déclarations sont en cours d'écriture comme celles de Softanza. Et le propre médium de l'artisan du logiciel, l'application de messagerie sur son téléphone, n'est pas encore quelque chose auquel un monde puisse être déclaré.

## 8. Six portes

**Le programmeur.** Vous déclarez l'intention dans une bibliothèque qui se lit comme une phrase, et un moteur calcule sous chaque appel. Vous restez le premier public.

**L'analyste.** Vous déclarez en texte brut les entités, les règles et les flux de votre organisation, et les règles jugent le modèle.

**Le concepteur.** Vous déclarez une image, une carte ou un écran comme un programme, et la première règle d'une interface peut venir d'un vrai métier : pour un restaurateur, la vitesse de commande.

**Le décideur.** Vous déclarez votre monde, votre gouvernance, et ce que chaque acteur peut valider, et vous possédez tout, en texte brut.

**Le formateur.** Vous déclarez un cours dans la langue de vos apprenants, et chaque exercice est vérifié en l'exécutant.

**L'agent.** Vous vous déclarez dans un fichier : ce que vous couvrez, à quel point vos actes sont réversibles. Vous recevez un atelier et un tribunal. Vous ne recevez pas la capacité de valider.

## 9. Exercice

Déclarez un agent pour un monde que vous connaissez : une boutique, une classe, un bureau. Écrivez son fichier : ce qu'il couvre, à quel point ses actes sont réversibles, quand il s'exécute, une compétence. Avant de l'exécuter, écrivez la promesse que vous attendez sous la question ci-dessous. Puis exécutez-le.

```haro exercise
? StzAgentDeclarationQ(cYourAgent).IsValid()
#--> 1
```

Si le tribunal refuse, lisez la règle qu'il cite et changez votre fichier, non le tribunal. Puis faites de votre agent un modèle de langage et donnez-lui un effet, et lisez pourquoi il est refusé. Vous ne trouverez pas le fichier corrigé dans ce livre.
