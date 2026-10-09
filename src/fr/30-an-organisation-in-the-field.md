---
id: an-organisation-in-the-field
part: 6
number: 30
title: Une organisation sur le terrain
spine: false
narrations: [stz-rules-as-graph-rules-narration.md, stz-governance-lineage-narration.md]
site: [forged, customers]
guards: [graphruleset_narrated, gg_rule_governance, wisecoding_narrated, governance_narrated, governance_lineage_narrated, 01_platform_narrated]
stage:
  built: "une règle écrite comme une donnée sur un modèle, changée et jugée de nouveau ; le gouverneur qui nomme une règle qui ne gouverne rien ; un refus qui atteint une personne avec son contexte ; l'autorité mise face au risque ; une décision gardée avec son autorité du moment ; le hors ligne comme une capacité qu'un monde doit demander"
  designed: "le hub et son étude ; un langage de règles qu'un développeur local peut apprendre ; les promesses de l'étude : qu'une règle est vérifiée avant de s'appliquer et peut être défaite"
  absent: "le hub, construit ; un mécanisme pour le travail fait hors ligne, gardé et envoyé plus tard ; un historique des versions d'une règle ; une plateforme client sur le moteur"
status: draft
rulings: ["12.13", "12.29"]
research: research/ch30.md
---

## 1. Le concept, tel que le terrain le tient

Le terrain a deux pratiques dont ce projet avait besoin, et il les garde en des lieux séparés.

La première est la règle métier qu'une personne du métier peut changer. Les moteurs de règles et les tables de décision existent depuis des décennies ; le Decision Model and Notation, une norme de 2015, donne aux analystes métier une table où un plafond d'approbation est un nombre dans une cellule. La seconde est l'application qui continue de marcher sans réseau. La conception hors ligne d'abord est une pratique à part entière, avec des bases de données qui se synchronisent et, depuis un essai de 2019, un nom pour sa philosophie, le logiciel local d'abord (local-first software) : les données sont sur votre appareil, et le réseau est une commodité.

Une troisième pratique est venue avec les agents : un modèle propose, et une personne approuve. Sur le terrain, c'est un bouton.

## 2. Le premier principe

L'étude de l'organisation sur son propre projet le dit en une phrase, et je la prends comme le principe de ce chapitre : **l'agent propose, et une personne décide.**

## 3. La forme Softanza

Une organisation travaille au Niger, avec un siège à Niamey et des bases sur le terrain. Sa propre spécification préférait une plateforme low-code construite sur la suite bureautique d'un grand éditeur. Mon offre du 5 août 2026 a été celle retenue, pour une raison que le chapitre 2 a donnée : la propriété. Elle possède son vocabulaire et ses règles ; elle les change sans programmer ; elle ne paie aucune licence par poste ; et elle peut tout confier à un développeur de son propre pays. Nous avons construit l'étude de conception ensemble, avec ses équipes, du 22 septembre au 8 octobre 2026. Je dis « étude de conception » et non « livraison » chaque fois, parce que le hub n'est pas construit. La version 1.2 de l'étude est soumise au directeur exécutif pour validation, et le dossier ne dit pas qu'elle l'ait été.

Quatre choses de cette étude, la bibliothèque les porte. Je les montrerai dans l'ordre où l'organisation les rencontrerait, puis celle qu'elle a demandée et que la bibliothèque ne porte pas.

**Une règle est une donnée.** Un plafond d'approbation est une phrase avec un nombre dedans, attachée au modèle des avances qu'elle gouverne. Le modèle se juge lui-même, et dit combien de sujets la règle regarde. Les données ci-dessous sont inventées pour ce chapitre, quatre avances avec un montant et un compte d'approbations ; ce ne sont pas les chiffres de l'organisation, et les nombres cinq cents et deux cents sont les miens, pas ses seuils.

```haro
oG = new stzGraph("advances")
oG.AddNodeXTT("a0", "A0", [ :amount = 120, :approvals = 1 ])
oG.AddNodeXTT("a1", "A1", [ :amount = 250, :approvals = 1 ])
oG.AddNodeXTT("a2", "A2", [ :amount = 600, :approvals = 1 ])
oG.AddNodeXTT("a3", "A3", [ :amount = 900, :approvals = 2 ])
oRule = new stzGraphRule("second-approval")
oRule.SetDomainQ("advances")
oRule.SetMessageQ("above the ceiling an advance needs two approvals")
oRule.WhenQ("amount", "greaterthan", 500)
oRule.ThenQ("approvals", "greaterthan", 1)
oRule.ThenViolationQ("two approvals needed")
oG.AddRule(oRule)
oG.RulesReport()
#--> Rule report 'advances': 1 finding(s), 1 error(s), 0 warning(s) -> UNSOUND (errors present)
#      [advances] 1 finding(s)
#        ERROR second-approval @ a2 -- two approvals needed
? len(oRule.SubjectsIn(oG))
#--> 2
```

Le plafond est changé, et le même modèle est jugé de nouveau. Un changement de la règle est un changement de ses valeurs, et le verdict et sa portée suivent :

```haro
oG.ClearAttachedRules()
oRule = new stzGraphRule("second-approval")
oRule.SetDomainQ("advances")
oRule.SetMessageQ("above the ceiling an advance needs two approvals")
oRule.WhenQ("amount", "greaterthan", 200)
oRule.ThenQ("approvals", "greaterthan", 1)
oRule.ThenViolationQ("two approvals needed")
oG.AddRule(oRule)
oG.RulesReport()
#--> Rule report 'advances': 2 finding(s), 2 error(s), 0 warning(s) -> UNSOUND (errors present)
#      [advances] 2 finding(s)
#        ERROR second-approval @ a1 -- two approvals needed
#        ERROR second-approval @ a2 -- two approvals needed
? len(oRule.SubjectsIn(oG))
#--> 3
```

Je dois être honnête sur ce que ce bloc montre. Le « changement » est une règle reconstruite dans le code avec un autre nombre. Que la personne même de l'organisation la change comme on remplit un formulaire est la promesse de l'étude, et je n'ai pas trouvé de fichier de la bibliothèque qui la réalise ; la section 7 dit ce qui existe et ce qui n'existe pas.

Ce que la bibliothèque porte, c'est la réponse à la pire chose qui puisse arriver quand une personne qui ne programme pas édite une règle : une règle qui ne gouverne rien, en silence. Faites une faute de frappe sur une propriété, et la règle ne trouve rien, et le modèle déclare qu'il est sain. Un gouverneur, qui demande aux règles ce qu'elles gouvernent et non ce qu'elles disent, nomme la règle morte :

```haro
oTypo = new stzGraphRule("second-approval-typo")
oTypo.SetMessageQ("above the ceiling an advance needs two approvals")
oTypo.WhenQ("amont", "greaterthan", 200)
oTypo.ThenQ("approvals", "greaterthan", 1)
oTypo.ThenViolationQ("two approvals needed")
? len(oTypo.Check(oG))
#--> 0
oWatch = StzRuleGovernance("hub")
oWatch.AddRule(oTypo)
oWatch.AddCase("advances", oG)
aF = oWatch.CheckRules()
? aF[1][:rule]
#--> scope_empty
? aF[1][:message]
#--> governs nothing in 1 pictures -- a dead rule and a misspelt scope predicate both report as passing
oWatch2 = StzRuleGovernance("hub")
oWatch2.AddRule(oRule)
oWatch2.AddCase("advances", oG)
? len(oWatch2.CheckRules())
#--> 0
```

Une règle morte et un feu vert produisent la même sortie : le silence. Le tribunal doit distinguer « rien n'était faux » de « rien n'a été regardé ». Le mot « pictures » dans le message est l'origine du gouverneur : il a d'abord été construit pour les dessins du plan des graphes, et je dirais « cas ».

**Une personne voit le refus.** Quand une réponse rompt une loi que l'organisation a déclarée, elle est refusée avec sa raison, et le refus est gardé comme un point de contrôle pour qu'une personne le voie, avec son contexte. Le chapitre 17 a montré la moitié qui demande de cette machine. Voici la moitié qui refuse : une demande a besoin d'une approbation, la loi dit qu'une demande a un approbateur, et un second approbateur est refusé :

```haro
oKB = new stzKnowledgeGraph("requests")
oKB.AddConversationQ("review").SetGoal(StzGoalQ().RequireOne("request-7", "approved-by"))
? oKB.AskIn("review")
#--> What does 'request-7' have for 'approved-by'?  (why: 'request-7' needs 'approved-by')
oKB.ConstrainRelation("approved-by", :Unique)
oKB.KnowRelation("request-7", "approved-by", "approver-1")
aR = oKB.ReplyIn("review", "approver-2")
? aR[:refused][1][2]
#--> 'request-7' already bears 'approved-by' (to 'approver-1'); the relation is :Unique
aCp = oKB.ConversationQ("review").Checkpoints()
? len(aCp)
#--> 1
? aCp[1][:attempted]
#--> approver-2
? aCp[1][:why]
#--> 'request-7' already bears 'approved-by' (to 'approver-1'); the relation is :Unique
```

**L'autorité n'est pas la permission.** L'assistant de cette organisation peut préparer un dossier. Il peut détenir la permission de débloquer une avance et être quand même refusé, parce que son autorité ne couvre pas le risque de l'acte. Une personne qui a l'autorité est autorisée. Le verdict dit pourquoi, dans les deux cas :

```haro
oGov = new stzGovernance("hub")
oGov.DeclareRisk("prepare-file", 1)
oGov.DeclareRisk("release-advance", 3)
oGov.GrantPermission("assistant", "prepare-file")
oGov.GrantPermission("assistant", "release-advance")
oGov.SetAuthority("assistant", :Advisory)
oGov.GrantPermission("approver-1", "release-advance")
oGov.SetAuthority("approver-1", :Autonomous)
? oGov.MayProceed("assistant", "prepare-file")
#--> 1
? oGov.MayProceed("assistant", "release-advance")
#--> 0
? oGov.Why()
#--> refused: 'assistant' holds 'advisory' authority (level 1) but 'release-advance' is risk tier 3 (SHOULD does not cover it)
? oGov.MayProceed("approver-1", "release-advance")
#--> 1
? oGov.Why()
#--> allowed: permission held AND 'autonomous' authority (level 3) covers risk tier 3
```

La bibliothèque ne connaît un acteur que par un nom et un niveau d'autorité. Qu'un acteur soit une personne ou un assistant, c'est ce que son niveau est déclaré être, et lier un niveau à une personne connectée est le travail du plan d'authentification, que je n'ai pas lu pour ce chapitre.

**Une décision garde son autorité du moment.** Chaque décision enregistre sa raison, son acteur, l'acte, l'autorité et le risque de cet instant. Une nouvelle décision remplace l'ancienne sans l'effacer :

```haro
nAt = 1785700000000
oGov.RecordDecisionAt("c-1", "ceiling raised for the harvest season", "approver-1", "release-advance", nAt)
oGov.RecordDecisionAt("c-1", "ceiling restored, the season is over", "approver-1", "release-advance", nAt + 3600000)
? oGov.LineageOf("c-1")[:rationale]
#--> ceiling restored, the season is over
? len(oGov.LineageHistoryOf("c-1"))
#--> 2
? oGov.LineageHistoryOf("c-1")[1][:rationale]
#--> ceiling raised for the harvest season
? oGov.LineageOf("c-1")[:authorityAtTime]
#--> autonomous
```

L'instant est un nombre fixe, donc l'horloge n'est pas lue. Cela garde la décision capable de répondre. Ce n'est pas un magasin de versions de la règle elle-même, et je ne ferai pas semblant que ce l'est.

Et celle que l'organisation a demandée en premier. Son option par défaut est de travailler hors ligne : des bases sur le terrain sans réseau, qui saisissent ce qu'elles font et l'envoient plus tard. La bibliothèque connaît le hors ligne comme une capacité déclarée et gouvernée d'un monde, demandée puis accordée ou refusée comme la caméra ou les paiements. C'est tout ce qu'elle en connaît :

```haro
oApp = StzAppQ("field-visits")
oPlat = StzPlatformQ("field")
oPlat.SetWorld(oApp)
oRegime = new stzGovernance("field-regime")
oRegime.GrantPermission("field-visits", "use-offline")
oRegime.SetAuthority("field-visits", :Advisory)
oPlat.SetGovernedBy(oRegime)
? oPlat.Granted(:offline)
#--> 0
? oPlat.Why()
#--> capability 'offline' was never requested via AddCapabilityQ().
oPlat.AddCapabilityQ(:offline).SetPurposes([ :enter_without_network ])
? oPlat.Granted(:offline)
#--> 1
? oPlat.Why()
#--> allowed: permission held AND 'advisory' authority (level 1) covers risk tier 1
```

Lisez ce bloc comme une limite et non comme une victoire. Rien n'y met quoi que ce soit en file. La bibliothèque ne garde pas d'entrées sur un appareil, ne les envoie pas quand le réseau revient, et ne règle pas les modifications de deux personnes.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé une plateforme à licence par poste comme socle de l'organisation.** La spécification préférait le low-code sur la suite d'un éditeur. L'offre retenue propose Softanza pour une raison au-dessus des autres : l'organisation possède son vocabulaire et ses règles, qu'elle peut changer sans programmer, et l'ensemble du travail, programmes, configuration et données, est le sien, avec une passation à un développeur local. La suite de l'éditeur reste là où elle était bonne, pour les comptes d'utilisateurs, les documents et les notifications. Le dossier a le résultat et les gains, et non la délibération : qui a choisi, et ce qu'on a pesé contre le low-code, il ne le dit pas, et le chapitre ne comble pas le vide.

**J'ai refusé de laisser l'assistant décider.** Il propose. Son autorité est consultative ; celle d'une personne couvre le risque. Le refus nomme le niveau, le niveau de risque, et la phrase qui dit que l'autorité ne couvre pas l'acte.

**J'ai refusé une règle silencieuse.** Une règle qui ne gouverne rien est signalée. Une règle sans message l'est aussi. C'est le prix de laisser une personne qui ne programme pas toucher à une règle, et je n'ai pas attendu le premier incident pour le payer.

**J'ai refusé d'appeler le hors ligne une leçon.** La page Forged le dit en quatre mots : un manque, pas une leçon. Un restaurant a demandé la même chose. L'étude est claire sur le fait que le hors ligne est l'option par défaut de l'organisation, et la bibliothèque n'en a qu'une permission. Un paquet frère du domaine de projets, côté navigateur, contient une boîte d'envoi durable sur l'appareil et une relecture ordonnée et idempotente ; il est extérieur à la bibliothèque, et je ne l'ai pas exécuté.

## 5. Le tribunal

`graphruleset_narrated` prouve une règle avec une comparaison et une exigence transformée en implication. `gg_rule_governance` prouve qu'une règle qui ne gouverne rien est signalée. `wisecoding_narrated`, sa troisième scène, prouve un refus gouverné et mis en point de contrôle. `governance_narrated` prouve que pouvoir n'est pas devoir : une permission détenue sans l'autorité est un refus. `governance_lineage_narrated` prouve la décision gardée avec son autorité du moment. `01_platform_narrated` prouve la jointure des capacités : la caméra accordée, les paiements refusés, une capacité jamais demandée refusée avec une raison honnête. La garde n'utilise pas elle-même la capacité pour le hors ligne ; le bloc ci-dessus le fait, avec le niveau que la plateforme déclare pour elle.

## 6. Le terrain, et où il mène

Le terrain mène en règles métier pour des gens du métier. Les tables de décision sont une norme ; une personne édite une cellule, pas un programme. Ici le changement est une règle reconstruite dans le code, et la forme de fichier qui porterait une règle comme un texte charge des règles et ne juge rien : elle lit le nom d'une règle, son genre, sa gravité, sa fonction et son message, et ne lit pas les lignes `when` et `then` de son propre exemple.

Le terrain mène en hors ligne. Le logiciel local d'abord est une pratique avec des bases de données qui se synchronisent et une décennie d'expérience. La bibliothèque a une permission.

Le terrain mène en gens. Une table de décision est une chose qu'un analyste formé sait déjà lire. Et la spécification propre de l'organisation, qui préférait la suite de l'éditeur, avait de bonnes raisons : ses utilisateurs y ont déjà des comptes.

## 7. La limite

Ce qui est construit : une règle comme donnée, changée et jugée de nouveau ; le gouverneur qui nomme une règle morte ; le point de contrôle ; l'autorité face au risque ; la filiation ; le hors ligne comme capacité.

Ce qui est conçu : le hub et son étude, dont le calendrier est dans le futur ; un langage de règles qu'un développeur local peut apprendre, dont l'exemple dans l'étude est écrit dans une notation qui n'est pas celle de la bibliothèque ; et les promesses de l'étude sur les règles : qu'elles sont vérifiées avant de s'appliquer, que leur effet est montré avant d'être appliqué, qu'elles peuvent être défaites et que leur historique est gardé. La bibliothèque a les pièces, le gouverneur, le refus d'un type de règle inconnu ou d'un fichier manquant, et le refus d'un nom en double.

Ce qui est absent : un historique des versions d'une règle avec un retour en arrière : la filiation enregistre la décision, et la règle est reliée de nouveau ; je n'ai trouvé aucun magasin de versions de règles, et ma recherche n'était pas exhaustive. Le hub, construit. Le hors ligne comme mécanisme : aucune classe de la bibliothèque ne met en file, ne synchronise ni ne règle un conflit. Et une plateforme client sur le moteur Softanza.

## 8. Six portes

**Le programmeur.** Une règle est un objet avec une comparaison et une exigence, attaché à un modèle, et un gouverneur vous dit quand elle ne gouverne rien.

**L'analyste.** Vous changez les valeurs d'une règle, pas son programme, et le modèle est jugé de nouveau avec la nouvelle portée.

**Le concepteur.** Un refus garde son contexte pour la personne qui le lira.

**Le décideur.** L'autorité n'est pas la permission : demandez quel niveau couvre quel risque, et lisez la filiation d'une décision.

**Le formateur.** La règle d'une organisation peut s'enseigner comme une phrase avec un nombre dedans.

**L'agent.** Vous préparez. Une personne décide. Et vous serez refusé, avec le niveau et le niveau de risque nommés.

## 9. Exercice

Choisissez une règle d'une organisation que vous connaissez qui contient un nombre, un plafond, un délai, un nombre d'approbations. Écrivez-la comme une règle avec une condition et une exigence, sur quatre cas inventés, deux qui la satisfont et deux qui ne la satisfont pas. Avant de lancer quoi que ce soit, écrivez le rapport que vous attendez. Puis faites exprès une faute de frappe sur une propriété de la condition, et dites ce que le modèle rapporte, et ce que le gouverneur rapporte.

Lancez-la. La différence entre ces deux réponses est le chapitre.
