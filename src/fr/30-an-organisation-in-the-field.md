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
  built: "une règle construite comme un objet sur un modèle, son nombre changé et le modèle jugé de nouveau ; le gouverneur de règles qui nomme une règle qui ne gouverne rien ; un refus gardé comme un point de contrôle qu'une personne peut lire, avec son contexte ; l'autorité mise face au risque ; une décision gardée avec son autorité du moment ; le hors ligne comme une capacité qu'un monde doit demander"
  designed: "le hub et son étude ; un langage de règles qu'un développeur local peut apprendre ; les promesses de l'étude : qu'une règle est vérifiée avant de s'appliquer et peut être défaite"
  absent: "le hub, construit ; un mécanisme pour le travail fait hors ligne, gardé et envoyé plus tard ; un historique des versions d'une règle ; une plateforme client sur le moteur"
status: draft
rulings: ["12.13", "12.29"]
research: research/ch30.md
---

Dans ce chapitre, je prends l'étude de conception d'une organisation et je montre les quatre choses qu'elle contient et que la bibliothèque porte. Ce sont une règle comme un objet dont les nombres peuvent être changés, un refus qu'une personne peut lire, l'autorité mise face au risque, et une décision gardée avec son autorité du moment. Puis je montre la chose que l'organisation a demandée et que la bibliothèque ne porte pas, le hors ligne, et je lis ce bloc comme une limite et non comme une victoire. Je dis « étude de conception » et non « livraison » chaque fois, parce que le hub n'est pas construit. Le principe est celui de l'organisation : l'agent propose, et une personne décide.

## 1. Le concept, tel que le terrain le tient

Le terrain a deux pratiques dont ce projet avait besoin, et il les garde en des lieux séparés.

La première est la règle métier qu'une personne du métier peut changer. Les moteurs de règles et les tables de décision existent depuis des décennies ; le Decision Model and Notation, une norme de 2015, donne aux analystes métier une table où un plafond d'approbation est un nombre dans une cellule. La seconde est l'application qui continue de marcher sans réseau. La conception hors ligne d'abord est une pratique à part entière, avec des bases de données qui se synchronisent. Depuis un essai de 2019, elle a un nom pour sa philosophie, le logiciel local d'abord (local-first software) : les données sont sur votre appareil, et le réseau est une commodité.

Une troisième pratique est venue avec les agents : un modèle propose, et une personne approuve. Sur le terrain, c'est un bouton.

L'étude de l'organisation fait de cette troisième pratique un principe.

## 2. Le premier principe

L'étude de l'organisation sur son propre projet en fait un titre de section, « L'agent IA propose, une personne décide », et je le prends comme le principe de ce chapitre : **l'agent propose, et une personne décide.**

## 3. La forme Softanza

Une organisation travaille au Niger, avec un siège à Niamey et des bases sur le terrain. Sa propre spécification préférait une plateforme low-code construite sur la suite bureautique d'un grand éditeur. Mon offre du 5 août 2026 a été celle retenue. L'étude liste quatre gains, et la propriété est le premier qu'elle liste. L'organisation possède son vocabulaire et ses règles ; elle les change sans programmer ; elle ne paie aucune licence par poste pour la plateforme ; et elle peut tout confier à un programmeur de son propre pays. Nous avons construit l'étude de conception ensemble, avec ses équipes, du 22 septembre au 8 octobre 2026. Je dis « étude de conception » et non « livraison » chaque fois, parce que le hub n'est pas construit. La version 1.2 de l'étude est soumise au directeur exécutif pour validation, et le dossier ne dit pas qu'elle l'ait été.

Quatre choses de cette étude, la bibliothèque les porte. Je les montrerai dans l'ordre où l'organisation les rencontrerait, puis celle qu'elle a demandée et que la bibliothèque ne porte pas.

**Une règle est un objet dont les nombres peuvent être changés.** Un plafond d'approbation est une phrase avec un nombre dedans, attachée au modèle des avances qu'elle gouverne. Le modèle se juge lui-même, et dit combien de sujets la règle regarde. Les données ci-dessous sont inventées pour ce chapitre, quatre avances avec un montant et un compte d'approbations. Ce ne sont pas les chiffres de l'organisation, et les nombres cinq cents et deux cents sont les miens, pas ses seuils. Un plafond de cinq cents repère-t-il une avance, et combien d'avances la règle regarde-t-elle ?

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

Le rapport nomme une avance, `a2`, à 600 avec une seule approbation, et la règle en regarde `2` sur les quatre, `a2` et `a3`.

Que se passe-t-il quand le plafond est changé et que le même modèle est jugé de nouveau ? Un changement de la règle est un changement de ses valeurs, et le verdict et sa portée suivent :

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

Le rapport dit maintenant `2 finding(s), 2 error(s)` là où il en disait un, et la portée est `3` là où elle était `2` ! Je dois être honnête sur ce que ce bloc montre. Le « changement » est une règle reconstruite dans le code avec un autre nombre. Que la personne même de l'organisation la change comme on remplit un formulaire est la promesse de l'étude. Je n'ai pas trouvé de fichier de la bibliothèque qui la réalise. La section 7 dit ce qui existe et ce qui n'existe pas.

Ce que la bibliothèque porte, c'est la réponse à la pire chose qui puisse arriver quand une personne qui ne programme pas édite une règle : une règle qui ne gouverne rien, en silence. Je tiens cela pour une vue, non pour un résultat. Faites une faute de frappe sur une propriété, et la règle ne trouve rien, et le modèle déclare qu'il est sain. Que dit un gouverneur de règles de la même règle ? La classe est `StzRuleGovernance` ; elle demande aux règles ce qu'elles gouvernent et non ce qu'elles disent, et elle nomme la règle morte :

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

La règle mal orthographiée ne trouve rien, `0`, et pour le modèle, rien trouvé veut dire sain ! Le gouverneur répond `scope_empty`, et dit pourquoi : `governs nothing in 1 pictures -- a dead rule and a misspelt scope predicate both report as passing`. Une règle morte et un feu vert produisent la même sortie : le silence. Le tribunal doit distinguer « rien n'était faux » de « rien n'a été regardé ». Le mot « pictures » dans le message est l'origine du gouverneur de règles : il a d'abord été construit pour les dessins du volet des graphes, et je dirais « cas ».

**Une personne peut lire le refus.** Quand une réponse rompt une loi que l'organisation a déclarée, elle est refusée avec sa raison. Le refus est gardé comme un point de contrôle qu'une personne peut lire, avec son contexte. Le chapitre 17 a montré la moitié qui demande de cette machine. Voici la moitié qui refuse. Une demande a besoin d'une approbation, et la loi dit qu'une demande a un approbateur. Que fait la machine d'un second approbateur ?

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

La machine demande d'abord : `What does 'request-7' have for 'approved-by'?  (why: 'request-7' needs 'approved-by')`. Puis le second approbateur est refusé ! Le point de contrôle garde ce qui a été tenté, `approver-2`, et la raison, dans les mots mêmes du refus : `'request-7' already bears 'approved-by' (to 'approver-1'); the relation is :Unique`.

**L'autorité n'est pas la permission.** L'assistant de cette organisation peut préparer un dossier. Il peut détenir la permission de débloquer une avance et être quand même refusé, parce que son autorité ne couvre pas le risque de l'acte. Une personne qui a l'autorité est autorisée. L'assistant peut-il débloquer l'avance, et l'approbateur le peut-il ? Le verdict dit pourquoi, dans les deux cas :

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

L'assistant détient la permission de `release-advance`, et la réponse est `0` ! Le verdict dit `refused: 'assistant' holds 'advisory' authority (level 1) but 'release-advance' is risk tier 3 (SHOULD does not cover it)`. Pour l'approbateur, il dit `allowed: permission held AND 'autonomous' authority (level 3) covers risk tier 3`.

La classe d'ici, `stzGovernance`, juge l'autorité ; ce n'est pas le gouverneur de règles de la règle morte plus haut. La bibliothèque ne connaît un acteur que par un nom et un niveau d'autorité. Qu'un acteur soit une personne ou un assistant, c'est ce que son niveau est déclaré être. Lier un niveau à une personne connectée est le travail du volet d'authentification, que je n'ai pas lu pour ce chapitre.

**Une décision garde son autorité du moment.** Chaque décision enregistre sa raison, son acteur, l'acte, l'autorité et le risque de cet instant. Une nouvelle décision remplace l'ancienne sans l'effacer, jusqu'à une capacité (512 décisions par défaut), et la gouvernance compte ce qu'elle a abandonné. Si l'on enregistre deux décisions sur le même cas, à une heure d'écart, laquelle la filiation donne-t-elle, et la première survit-elle ?

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

La filiation répond `ceiling restored, the season is over`. Elle garde `2` décisions, et la première dit encore `ceiling raised for the harvest season`. L'autorité du moment est `autonomous`. L'instant est un nombre fixe, donc l'horloge n'est pas lue. Cela rend le bloc répétable. Ce n'est pas un magasin de versions de la règle elle-même, et je ne ferai pas semblant que ce l'est.

Et celle qu'elle a demandée et que la bibliothèque ne porte pas. Son option par défaut est de travailler hors ligne : des bases sur le terrain sans réseau, qui saisissent ce qu'elles font et l'envoient plus tard. La bibliothèque connaît le hors ligne comme une capacité déclarée et gouvernée d'un monde, demandée puis accordée ou refusée comme la caméra ou les paiements. Le hors ligne est-il accordé avant que le monde le demande, et après ? C'est tout ce que la bibliothèque en connaît :

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

Avant la demande, `Granted(:offline)` vaut `0`, et la raison imprimée est `capability 'offline' was never requested via AddCapabilityQ().`. Après la demande, il vaut `1`, et la raison imprimée est `allowed: permission held AND 'advisory' authority (level 1) covers risk tier 1`.

Lisez ce bloc comme une limite et non comme une victoire. Rien n'y met quoi que ce soit en file. La bibliothèque ne garde pas d'entrées sur un appareil, ne les envoie pas quand le réseau revient, et ne règle pas les modifications de deux personnes.

La section suivante pose la décision, et ce que j'ai refusé.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé une plateforme à licence par poste comme socle de l'organisation.** La spécification préférait le low-code sur la suite d'un éditeur. L'offre retenue propose Softanza, et parmi ses gains l'étude met la propriété en premier. L'organisation possède son vocabulaire et ses règles, qu'elle peut changer sans programmer, et l'ensemble du travail, programmes, configuration et données, est le sien, avec une passation à un programmeur local. La suite de l'éditeur reste là où elle était bonne, pour les comptes d'utilisateurs, les documents et les notifications. Le dossier a le résultat et les gains, et non la délibération. Qui a choisi, et ce qu'on a pesé contre le low-code, il ne le dit pas. Le chapitre ne comble pas le vide.

**J'ai refusé de laisser l'assistant décider.** Il propose. Son autorité est consultative ; celle d'une personne couvre le risque. Le refus nomme le niveau, le niveau de risque, et la phrase qui dit que l'autorité ne couvre pas l'acte : `SHOULD does not cover it`.

**J'ai refusé une règle silencieuse.** Une règle qui ne gouverne rien est signalée. Une règle sans message l'est aussi. C'est le prix de laisser une personne qui ne programme pas toucher à une règle. Le gouverneur de règles existe parce que la règle silencieuse s'est déjà produite dans la bibliothèque.

**J'ai refusé d'appeler le hors ligne une leçon.** La page Forged, lue le 9 octobre 2026, dit : « C'est un manque, pas une leçon apprise. » Un restaurant a demandé la même chose. L'étude est claire sur le fait que le hors ligne est l'option par défaut de l'organisation, et la bibliothèque n'en a qu'une permission. Un paquet frère du domaine de projets, côté navigateur, contient une boîte d'envoi durable sur l'appareil et une relecture ordonnée et idempotente ; il est extérieur à la bibliothèque. Je ne l'ai pas exécuté.

## 5. Le tribunal

`graphruleset_narrated` prouve une règle avec une comparaison et une exigence transformée en implication. `gg_rule_governance` prouve qu'une règle qui ne gouverne rien est signalée. `wisecoding_narrated`, sa troisième scène, prouve un refus gouverné et mis en point de contrôle. `governance_narrated` prouve que pouvoir n'est pas devoir : une permission détenue sans l'autorité est un refus. `governance_lineage_narrated` prouve la décision gardée avec son autorité du moment. `01_platform_narrated` prouve la jointure des capacités : la caméra accordée, les paiements refusés, une capacité jamais demandée refusée avec une raison honnête. La garde n'utilise pas elle-même la capacité pour le hors ligne ; le bloc ci-dessus le fait, avec le niveau que la plateforme déclare pour elle. Le refus d'un type de règle inconnu, d'un fichier manquant et d'un nom en double repose sur les scènes 4 et 5 de `rulz_roundtrip_narrated`. C'est un test narré de la bibliothèque, et ce livre ne l'exécute pas comme l'une de ses gardes.

La section suivante met ce que fait le terrain face à ce que la bibliothèque a.

## 6. Le terrain, et où il mène

Le terrain mène en règles métier pour des gens du métier. Les tables de décision sont une norme ; une personne édite une cellule, pas un programme. Ici le changement est une règle reconstruite dans le code. La forme de fichier qui porterait une règle comme un texte, le fichier `.stzrulz`, lit le nom d'une règle, son type, sa gravité, sa fonction, ses paramètres et son message. Elle ne lit pas les lignes `when` et `then` de son propre exemple.

Le terrain mène en hors ligne. Le logiciel local d'abord est une pratique avec des bases de données qui se synchronisent et une décennie d'expérience. La bibliothèque a une permission.

Le terrain mène en gens. Une table de décision est une chose qu'un analyste formé sait déjà lire. Et la spécification propre de l'organisation, qui préférait la suite de l'éditeur, avait de bonnes raisons : ses utilisateurs y ont déjà des comptes.

La section suivante liste ce qui est construit, ce qui est conçu et ce qui est absent.

## 7. La limite

Ce qui est construit : une règle comme objet, son nombre changé et le modèle jugé de nouveau ; le gouverneur de règles qui nomme une règle morte ; le point de contrôle ; l'autorité face au risque ; la filiation ; le hors ligne comme capacité.

Ce qui est conçu : le hub et son étude, dont le calendrier est dans le futur ; un langage de règles qu'un programmeur local peut apprendre ; et les promesses de l'étude sur les règles. L'exemple du langage dans l'étude est écrit dans une notation qui n'est pas celle de la bibliothèque. L'étude promet qu'une règle est vérifiée avant de s'appliquer, que son effet est montré avant d'être appliqué, qu'elle peut être défaite et que son historique est gardé. La bibliothèque n'a que les pièces. Ce sont le gouverneur de règles, le refus d'un type de règle inconnu ou d'un fichier manquant, et le refus d'un nom en double.

Ce qui est absent : un historique des versions d'une règle avec un retour en arrière. La filiation enregistre la décision, et la règle est reliée de nouveau. Je n'ai trouvé aucun magasin de versions de règles, et ma recherche n'était pas exhaustive. Le hub, construit. Le hors ligne comme mécanisme : aucune classe de la bibliothèque ne garde des entrées sur un appareil et ne les envoie quand le réseau revient. Et une plateforme client sur le moteur Softanza.

## 8. Six portes

**Le programmeur.** Une règle est un objet avec une comparaison et une exigence, attaché à un modèle, et un gouverneur de règles vous dit quand elle ne gouverne rien.

**L'analyste.** L'étude promet que vous changez les valeurs d'une règle, pas son programme. Dans la bibliothèque, quand les valeurs changent, le modèle est jugé de nouveau avec la nouvelle portée.

**Le concepteur.** Un refus garde son contexte pour la personne qui le lira.

**Le décideur.** L'autorité n'est pas la permission : demandez quel niveau couvre quel risque, et lisez la filiation d'une décision.

**Le formateur.** La règle d'une organisation peut s'enseigner comme une phrase avec un nombre dedans.

**L'agent.** Vous préparez. Une personne décide. Et vous serez refusé, avec le niveau et le niveau de risque nommés.

## 9. Exercice

Choisissez une règle d'une organisation que vous connaissez qui contient un nombre, un plafond, un délai, un nombre d'approbations. Écrivez-la comme une règle avec une condition et une exigence, sur quatre cas inventés, deux qui la satisfont et deux qui ne la satisfont pas. Avant de lancer quoi que ce soit, écrivez le rapport que vous attendez. Puis faites exprès une faute de frappe sur une propriété de la condition, et dites ce que le modèle rapporte, et ce que le gouverneur rapporte.

Lancez-la. La différence entre ces deux réponses est le chapitre.

Le chapitre suivant demande ce que les projets n'ont pas prouvé. Sa mesure est celle-ci : un projet prouve exactement ce qu'un document, un fichier, une exécution et une personne nommée atteignent, et la page dit où ils s'arrêtent.
