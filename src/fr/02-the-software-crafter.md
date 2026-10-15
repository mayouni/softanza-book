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
  designed: "une garde qui échoue quand une étape d'une page de parcours casse, chaque étape exécutée dans l'ordre ; la porte par laquelle un agent de code demande à la bibliothèque de juger son travail"
  absent: "les plateformes des trois clients qui tournent sur le moteur Softanza ; le propre médium d'un artisan du logiciel, l'application de messagerie sur son téléphone, comme cible"
status: draft
rulings: ["12.2", "12.12", "12.13", "12.25", "12.29", "12.30"]
research: research/ch02.md
---

Dans ce chapitre, je prends le mot « crafter » au terrain, à son artisanat et à ses deux réponses qui définissent la personne par un outil, le low-code et l'agent de code. Je dis ce que le site entend par lui. Je montre les six portes, chacune avec une ou deux lignes qui s'exécutent, et les trois cas pour lesquels ce livre est écrit : un restaurateur à Lyon, Softibank, une banque à Niamey, une organisation sur le terrain. Je dis ce que j'ai gardé, le programmeur en premier ; ce que j'ai ajouté, l'agent d'IA, avec un pouvoir retenu ; et ce que j'ai refusé, « maker » et « builder ». Le principe est une phrase qui joint celle du site et celle du glossaire : un artisan du logiciel est quiconque déclare ce qu'il sait d'un monde, et possède ce qu'il déclare.

## 1. Le concept, tel que le terrain le tient

Le terrain a déjà un mot pour les programmeurs qui prennent soin de leur travail : l'artisanat (craftsmanship). Un livre de 2001 a donné son nom à l'idée, et un manifeste de 2009 lui a donné son slogan. Depuis, « software craftsman » désigne un professionnel qui tient son code à un niveau plus élevé que celui que le travail exige. Cela relève de la connaissance générale, non d'une lecture du dossier. C'est un bon mouvement. C'est aussi un mouvement de programmeurs, sur les standards des programmeurs.

Les deux autres réponses du terrain à « qui fait le logiciel, si ce ne sont pas les programmeurs » définissent la personne par un outil. La première est le low-code : des gens du métier qui construisent des applications sur la plateforme visuelle d'un éditeur, le « développeur citoyen » des analystes. La seconde est l'agent de code : un modèle d'IA qui lit des fichiers, les modifie et lance des commandes, piloté en mots simples. Le « vibe coding » est le nom de la pratique qui consiste à garder tout ce qu'il écrit. Les deux réponses ont la même forme. La personne est définie par un outil, et le travail vit là où vit l'outil. Quand l'éditeur change ses prix ou son modèle d'IA, le travail de la personne change avec. Cela aussi relève de la connaissance générale, non d'une lecture du dossier.

La section suivante dit ce que le site entend par ce mot.

## 2. Le premier principe

Le site donne la définition en deux phrases. Depuis le 8 octobre 2026, elles disent « crafter » ; avant, elles disaient « maker ». Le glossaire dit qu'un artisan du logiciel est quiconque déclare, au moment où il déclare. Le site dit qu'il possède ce qu'il fait. Je garde les deux, en une phrase : **un artisan du logiciel est quiconque déclare ce qu'il sait d'un monde, et possède ce qu'il déclare : l'artefact est à lui, en texte brut, et il n'expire pas.** La compétence n'entre pas dans la définition. Le mot « artisanat » la suggère, et je garde le mot : la personne est définie par l'acte et par la possession, non par sa compétence de programmation. Je tiens cela pour une vue, non pour un résultat.

## 3. La forme Softanza

J'ai été le premier artisan du logiciel de Softanza, et pas pour une raison que j'aurais choisie. Ma femme dirige un club de musique où l'on apprend à chanter des chansons classiques arabes. Chaque dimanche matin, elle m'envoie la liste des chansons à préparer, et je cherche leurs paroles. Les paroles trouvées en ligne répètent chaque phrase comme le chanteur l'a interprétée, et elle me rappelle, à chaque fois, d'en supprimer les doublons. J'ai écrit `RemoveDuplicates()` pour cesser de le faire à la main. Sa famille est-elle toujours dans la bibliothèque, et que dit-elle d'une liste qui contient trois fois « tea » ?

```haro
o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.ContainsDuplicates()
#--> 1
? o1.NumberOfOccurrence("tea")
#--> 3
```

La famille répond : la liste contient des doublons (`1`), et `tea` apparaît `3` fois.

J'en parle dans un article sur ce sur quoi la bibliothèque a été construite : j'ai introduit ses fonctions quand un vrai problème les demandait, ou quand j'anticipais qu'elles répondraient aux besoins des programmeurs. Celle-ci est née d'un problème : l'artisan du logiciel vient d'abord, et la fonction après.

Depuis 2022, je présente Softanza non par son anatomie, ses modules et ses classes, mais par qui vous êtes et ce que vous essayez de faire. La présentation de 2022 avait cinq publics, chacun avec une recette de trois à cinq étapes. Le 9 octobre 2026, le site avait sept portes, une par sorte d'artisan du logiciel. La septième, pour une équipe qui livre une application, y a été ajoutée ce jour-là, et ce chapitre garde les six avec lesquelles il a été rédigé. Chaque porte dit ce que vous déclarez, ce que vous obtenez, et par où commencer. Voici ce que chacune des six déclare, en une ou deux lignes qui s'exécutent.

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

Le moteur a dessiné la vue à partir des seules données : `Maradi │ 3402094` en est une ligne.

**Le concepteur** déclare une image comme un programme, et obtient la même image à chaque fois :

```haro
? Q("Softanza").BoxedXT([ :AllCorners = :Round ])
#--> ╭──────────╮
#    │ Softanza │
#    ╰──────────╯
```

L'image est la sortie du programme : un `Softanza` encadré, aux coins arrondis.

**Le décideur** déclare ce que chaque acteur du monde peut faire, une personne ou un agent d'IA, et le tribunal l'impose. Un agent est un petit fichier texte. Que dit le tribunal à celui qui ne dit pas ce qu'il couvre ? Chargez-le :

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

Le tribunal l'a refusé ! Sa raison est imprimée : `[pia-coverage @ coverage] an agent must say WHAT IT COVERS`. Ici « law 18 » est la règle du moteur selon laquelle un agent sans énoncé de couverture n'est jamais planifié, et `pia` nomme le format du fichier, comme le montre sa première ligne.

**Le formateur** déclare dans la propre langue de l'apprenant. Une phrase en haoussa s'exécute : elle demande un texte contenant `'hello'`, passé en capitales. Le moteur compte-t-il les lettres d'un mot arabe plutôt que ses octets, et connaît-il son écriture ?

```haro
? NaturallyIn("ha", "Yi rubutu dauke 'hello' Maida shi").Result()
#--> HELLO
? Q("سلام").NumberOfChars()
#--> 4
? Q("مرحبا بالعالم").Script()
#--> arabic
```

La phrase en haoussa est revenue en `HELLO`. Le mot arabe compte `4`, ses lettres et non ses octets, et son écriture est `arabic`.

**L'agent** est le sixième artisan du logiciel, celui que la présentation de 2020 de la plateforme ne pouvait pas dessiner, selon les mots de la vision que j'ai ratifiée. Un agent d'IA se déclare dans le même genre de fichier, et il est le bienvenu, avec une seule chose retenue. Un agent dont l'esprit est un modèle de langage peut proposer ; il ne peut pas détenir d'effet. Qu'arrive-t-il à un fichier qui lui en donne un ?

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

L'acteur llm `rogue` n'obtient pas son effet ! Le tribunal répond `REFUSED`, et dit quand : `enforced at CONSTRUCTION, not merely audited`. Un « pi-gate » est la barrière où un acteur gouverné valide.

Voici maintenant les trois cas pour lesquels ce livre est écrit. Ce ne sont pas des personas. Ce sont des gens et des organisations avec des documents, et la partie VI raconte chacun en entier. Ici, une page chacun.

**Un restaurateur à Lyon.** Il possède un restaurant de couscous, et le projet est une plateforme pour le commerce de quartier. Les notes du projet le disent sans détour : il n'est pas programmeur. Le projet a commencé par une offre en mai 2024 puis deux années de spécification riche qui n'ont rien produit qu'il puisse utiliser. Ce qui est sorti de cet échec est la règle selon laquelle je travaille depuis. Livrer petit, vite et utile, et laisser les fondations mûrir en parallèle sans jamais bloquer une livraison.

Le 4 juillet 2026, il a répondu à un rapport de cadrage dans ses propres mots et a renversé l'ordre du travail : client d'abord, restaurateur ensuite, fournisseur en dernier. L'architecture du projet a été redessinée en constellation de mondes, à partir de la conception de la bibliothèque, et le premier avenant a été clos le 4 août 2026.

Une constellation est un graphe de mondes. Un monde est une application ; un lien est une relation déclarée entre deux mondes, pour un acte nommé, et rien ne passe sans lui. Le chapitre 23 montre les trois à l'exécution ; ici, ce n'est que la forme que le projet a prise.

Le projet compte onze itérations et une campagne de vingt-deux tests simulés derrière ses règles d'interface. Dans son propre rapport, la vitesse de commande est sa première priorité, non négociable. Et le 19 août, après une journée de tests sur le terrain avec deux téléphones et une application de messagerie, les notes l'appellent le co-architecte du projet.

La première démonstration, le 15 août 2026, a été la sienne seule : la liste de vérification du dossier la prévoit pour le propriétaire seul, avec son propre téléphone et une application de messagerie comme ligne d'assistance. Les mesures qu'il a envoyées par une application de messagerie sont celles du 19 août.

L'un de ses besoins est porté par une loi de la bibliothèque : essayer les paiements avant de payer quiconque pour un compte. Que dit le registre d'un faux service de paiement pendant que vous répétez, et que dit-il quand vous passez au réel ? Exécutez-le. Le registre est nommé une fois, et chaque ligne entre les accolades lui parle : le chapitre 5 appelle cette forme la scène.

```haro
oReg = new stzServiceRegistry("restaurant")
oReg {
	Bind(:payments, new stzPaymentsSandbox())
	SetPhase(:emulated)
	? IsSound()
	#--> 1
	SetPhase(:production)
	? IsSound()
	#--> 0
	? Findings()[1][:message]
	#--> still bound to a SANDBOX in a production phase -- a fake must never ship
}
```

Il répond `1` en phase émulée et `0` en production, et dit pourquoi : `still bound to a SANDBOX in a production phase -- a fake must never ship`. Un faux en production est refusé !

**Une banque à Niamey.** Une banque commerciale soumise aux règles de la banque centrale de l'union monétaire ouest-africaine est titulaire d'une licence pour un produit d'évaluation d'organisation que j'ai construit à côté de la bibliothèque. Il est installé sur son propre réseau interne, sous cette licence. Le guide d'installation livré à la banque est le document qui l'atteste. La leçon qu'il a laissée dans la bibliothèque est qu'une organisation peut être jugée par son propre organigramme, selon les règles d'un régulateur. Déclarez un organigramme avec un directeur général et un audit interne qui lui rend compte. Que disent les règles du régulateur à son sujet ?

```haro
oOrg = new stzOrgChart("bank")
oOrg {
	AddPositionXTT("ceo", "Chief Executive", [ :department = "executive" ])
	AddPositionXTT("audit", "Internal Audit", [ :department = "audit", :reportsTo = "ceo" ])
	? @@( ValidateBCEAOGovernance() )
	#--> [ [ "status", "fail" ], [ "domain", "BCEAO_governance" ], [ "issuecount", 3 ], [ "issues", [ "BCEAO-001: No Board of Directors found", "BCEAO-002: Audit reports to non-board position", "BCEAO-003: No dedicated Risk Management function" ] ] ]
}
```

L'organigramme échoue, avec `"issuecount", 3` : trois constats pour un organigramme de deux postes ! Chacun est une règle avec un numéro qu'un auditeur peut lire : `BCEAO-001: No Board of Directors found` est le premier. Le dossier montre la banque comme titulaire d'une licence d'un produit que j'ai construit ; il ne dit pas qui, à la banque, a déclaré quoi que ce soit.

**Une organisation sur le terrain.** Une organisation qui travaille au Niger, avec un siège à Niamey et des bases sur le terrain, a demandé un hub. Son propre cahier des charges préférait une plateforme low-code construite sur la suite bureautique d'un grand éditeur. Mon offre du 5 août 2026 a été choisie à la place. L'étude de conception liste quatre gains, la possession en tête. L'organisation possède son vocabulaire et ses règles, les change sans programmer, ne paie pas de licence par poste, et peut tout remettre à un programmeur de son propre pays. L'étude de conception a été construite avec ses équipes entre le 22 septembre et le 8 octobre 2026. Deux de ses principes sont ceux du livre en petit : par défaut on travaille hors ligne, et l'agent d'IA propose tandis qu'une personne décide. Cette règle est une donnée que l'organisation attache à son propre modèle de domaine. Ce modèle se juge-t-il lui-même, avec en lui un acteur LLM qui détient un effet ?

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

`RulesAreSound()` répond `0` : le modèle de domaine trouve son propre `writer`, un acteur LLM qui détient `effectful`, en violation de la règle.

Les trois cas sont un restaurateur qui n'est pas programmeur, une banque sous un régulateur et une organisation qui a choisi la possession plutôt qu'un éditeur. Le restaurateur et l'organisation sont des artisans du logiciel selon le dossier ; la banque est titulaire d'une licence d'un produit, et le dossier ne dit pas qui, là-bas, a déclaré quoi que ce soit. Le restaurateur et l'organisation n'ont pas attendu l'industrie du logiciel, et chacun se voit offrir la possession de ce qui est construit pour lui.

## 4. La décision, et ce que j'ai refusé

**J'ai gardé le programmeur en premier.** La vision de la plateforme, que j'ai ratifiée, le dit en une ligne : le premier public reste le programmeur d'une petite équipe ; l'ère agentique ne l'a pas remplacé, elle l'a multiplié. J'ai tenu que les agents d'IA ne rendent pas les programmeurs obsolètes.

**J'ai ajouté l'agent d'IA comme artisan du logiciel, et retenu un pouvoir.** L'agent est le sixième lecteur de chaque langage Softanza : à la fois un constructeur et un utilisateur. Il reçoit un atelier et un tribunal. Il ne reçoit pas la capacité de valider.

**J'ai refusé « maker », et j'ai refusé « builder ».** « Maker » nomme le mouvement des ateliers, le fer à souder et l'imprimante 3D, comme la connaissance générale le tient. L'accroche du site l'a employé jusqu'au 8 octobre 2026. « Builder » nomme quelqu'un qui assemble ce qu'un plan dit. Aucun des deux ne dit ce que je crois qu'est la programmation. C'est un travail de la main, fait avec soin, sur quelque chose qui est à vous : c'est de l'artisanat. J'appelle la personne qui le fait un artisan du logiciel.

**J'ai refusé de compter un client sans document.** Le site ne liste un projet comme référence que lorsqu'un document le prouve, et ne cite aucun nombre de pays ni aucun nombre de programmeurs. Le nom d'un client va sur le site sur ma parole ; son rang de référence demande le document. Une leçon n'est listée que lorsqu'un fichier de la bibliothèque la porte.

**J'ai refusé de présenter la bibliothèque par son anatomie.** Depuis 2022, la porte d'entrée est qui vous êtes et ce que vous voulez faire, et l'anatomie est placée sous chaque étape. Le 9 octobre 2026, le site gardait sept portes, et les parcours derrière elles existaient comme pages, neuf ce jour-là, chaque étape portant son mot d'étape. Que chaque étape s'exécute dans l'ordre sous une garde est conçu ; le construire est l'étape suivante.

Les gardes qui prouvent ces affirmations, et celle qui est en développement, sont dans la section suivante.

## 5. Le tribunal

`agentfile_narrated` prouve qu'un agent est un fichier jugé quand il est chargé : un refus par barrière, la couverture manquante parmi eux, et l'agent dont l'esprit est un modèle de langage, qui détient un effet refusé par la même règle que celle qu'emploie le graphe. `service_registry_narrated` prouve qu'un bac à sable en production est une violation. `graphrule_object_narrated` prouve la règle comme un objet attaché à un modèle. `semantic_resolver_narrated` tient le chemin haoussa comme dernier scénario. À ce commit, elle est en développement : son exécution s'arrête après 29 assertions, avant les assertions haoussa, sur une erreur levée par une fonction de découpage de chaînes, et terminer cette exécution est l'étape suivante. La page compte donc ses assertions et ne revendique pas son verdict ; le bloc haoussa a été exécuté seul. `00_orgchart_narrated` prouve les postes, les liens hiérarchiques et le suivi des vacances de l'organigramme ; le constat BCEAO imprimé plus haut vient d'un fichier voisin, `14_bceao_governance.ring`.

## 6. Le terrain, et où il mène

Les agents de code mènent en mains. Ils lisent, cherchent, modifient et exécutent déjà. Ce qui leur manque, selon le site lui-même, c'est un moyen de connaître une interface inconnue sans deviner, de juger leur travail selon des règles et des promesses, et de présenter un changement comme une intention qu'une personne peut relire. Les juges de Softanza sont construits ; la porte entre eux et un agent de code est conçue, et la construire est l'étape suivante.

Le low-code mène en base installée et en tout ce qui l'entoure, comme la connaissance générale le tient. L'organisation sur le terrain garde la suite de son éditeur pour ses comptes, ses documents et ses notifications. La plateforme de l'artisan du logiciel se place à côté des outils du terrain, non à leur place.

Les applications de messagerie mènent là où les artisans du logiciel sont déjà, et le dossier du restaurant n'en fait pas encore son médium. L'outil du restaurateur avant le projet était un tableur ; son propre rapport du 4 juillet 2026 le dit. La ligne qui nomme les applications de messagerie est l'intitulé d'une option du formulaire de cadrage, et non sa réponse. Aucune page du site ne nomme ces applications, et aucun médium conversationnel n'est encore une cible de la plateforme. Le chapitre 25 parle de cette direction.

Et la porte du formateur en est à une étape plus précoce que les autres. Les éditions du cours en français, en arabe et en haoussa sont des brouillons qu'un relecteur n'a pas encore lus, et la première institution à l'adopter reste à venir.

La section suivante dit ce qui est construit, ce qui est conçu et ce qui est absent.

## 7. La limite

Ce qui est construit : le fichier d'agent et son tribunal ; le registre qui refuse un faux en production ; des règles comme données sur un modèle ; les règles d'un régulateur qui jugent un organigramme ; la couche naturelle en haoussa et en arabe.

Ce qui est conçu : une garde qui échoue quand une étape d'une page de parcours casse, chaque étape exécutée dans l'ordre ; la porte par laquelle un agent de code demande à la bibliothèque de juger son travail.

Ce qui est absent : les plateformes des trois clients qui tournent sur le moteur Softanza. Aujourd'hui la plateforme du restaurant est un ensemble de mondes web, chacun un fichier unique ; celle de la banque est une application Python ; le hub de l'organisation est une conception. Leurs déclarations sont en cours d'écriture comme celles de Softanza. Et le propre médium de l'artisan du logiciel, l'application de messagerie sur son téléphone, n'est pas encore quelque chose auquel un monde puisse être déclaré.

## 8. Six portes

**Le programmeur.** Vous déclarez l'intention dans une bibliothèque qui se lit comme une phrase, et un moteur calcule sous chaque appel. Vous restez le premier public.

**L'analyste.** Vous déclarez en texte brut les entités, les règles et les flux de votre organisation, et les règles jugent le modèle.

**Le concepteur.** Vous déclarez une image, une carte ou un écran comme un programme, et la première règle d'une interface peut venir d'un vrai métier : pour un restaurateur, la vitesse de commande.

**Le décideur.** Vous déclarez votre monde, votre gouvernance, et ce que chaque acteur peut valider, et vous possédez tout, en texte brut.

**Le formateur.** Vous déclarez un cours dans la langue de vos apprenants, et chaque exercice est vérifié en l'exécutant, selon les mots du site. Les éditions en français, en arabe et en haoussa sont des brouillons qu'un relecteur n'a pas encore lus.

**L'agent.** Vous vous déclarez dans un fichier : ce que vous couvrez, à quel point vos actes sont réversibles. Vous recevez un atelier et un tribunal. Vous ne recevez pas la capacité de valider.

## 9. Exercice

Déclarez un agent d'IA pour un monde que vous connaissez : une boutique, une classe, un bureau. Écrivez son fichier : ce qu'il couvre, à quel point ses actes sont réversibles, quand il s'exécute, une compétence. Avant de l'exécuter, écrivez la promesse que vous attendez sous la question ci-dessous. Puis exécutez-le.

```haro exercise
? StzAgentDeclarationQ(cYourAgent).IsValid()
#--> 1
```

Si le tribunal refuse, lisez la règle qu'il cite et changez votre fichier, non le tribunal. Puis faites de votre agent un modèle de langage et donnez-lui un effet, et lisez pourquoi il est refusé. Vous ne trouverez pas le fichier corrigé dans ce livre.

Je vous laisse celui-ci. Prenez le bloc de la règle de graphe de la section 3, celui de l'organisation sur le terrain, et changez une ligne : les capacités de `writer` deviennent `[ "inference" ]`, sans `"effectful"`. Exécutez-le et lisez la dernière réponse.

```haro exercise
oRule = new stzGraphRule("no-llm-effectful")
oRule.SetDomainQ("agentic")
oRule.WhenQ("kind", "equals", "llm_actor")
oRule.WhenQ("capabilities", "contains", "effectful")
oRule.ThenViolationQ("an LLM proposes, only a pi-gate commits")
g = new stzGraph("agents")
g.AddNode("writer")
g.SetNodeProperty("writer", "kind", "llm_actor")
g.SetNodeProperty("writer", "capabilities", [ "inference" ])
g.AddRule(oRule)
? g.RulesAreSound()
```

Comparez-la ensuite à la réponse imprimée dans la section 3, et dites ce que la règle a lu pour donner chacune. La section 3 montre ses deux conditions. Quand vous saurez le dire, vous saurez quelle ligne du modèle de domaine la règle lit.

Le chapitre 3 est la méthode, depuis les premiers principes, et la phrase à laquelle sa méthode revient est celle-ci : vous déclarez un monde dans un langage fait pour lui, et vous gouvernez la façon dont ce monde change.
