---
id: a-world-a-constellation-a-platform
part: 5
number: 23
title: Un monde, une constellation, une plateforme, et l'architecte
spine: false
narrations: [stzApp-building-your-first-app-narration.md, stz-system-dev-to-deploy-narration.md, stz-built-on-real-world-need.md]
site: [platforms, offering, forged]
guards: [06_stzsuperapp_narrated, 01_platform_narrated, full_scope_model_narrated, 04_stzapp_pursue_narrated, 05_stzapp_live_narrated]
stage:
  built: "un monde comme déclaration avec un être, un devenir et une manière d'être rencontré ; un but dont l'écart est mesuré ; une constellation de mondes avec des liens et trois barrières sur chaque traversée ; le socle commun comme plateforme ; la jointure des capacités ; le profil d'une solution comme fichier texte, et les trois portées du système"
  designed: "l'idiome quasi naturel de la constellation ; un appel acheminé dans une constellation emboîtée ; des coques qui embarquent le moteur ; la certification de l'architecte, qui est une proposition ; la fiche de garanties de cinq lignes, comme exigence"
  absent: "un monde qui juge ses propres vérités ; une narration pour la constellation ou pour l'enveloppe de la plateforme ; une fiche de garanties de cinq lignes écrite pour une solution"
status: draft
rulings: ["12.2", "12.12", "12.13", "12.15", "12.19", "12.25", "12.29"]
research: research/ch23.md
---

Dans ce chapitre, je déclare une solution à trois niveaux, un monde, une constellation et une plateforme, et je nomme la seule personne qui déclare les trois, l'architecte. Je prends d'abord les trois habitudes du terrain : la super-appli, la carte de contextes et l'équipe de plateforme. Puis je fais tourner un monde qui s'explique lui-même, une constellation dont les traversées sont refusées une barrière à la fois, et un profil qu'une plateforme refuse de construire quand il n'est pas sain. Je dis où le code s'arrête : les vérités d'un monde sont narrées et non jugées, les coques sont minuscules, et la certification de l'architecte est une proposition. Le principe est celui-ci : la solution est déclarée en mondes, en liens et en une enveloppe avant que rien en soit construit, et chaque traversée entre eux est gouvernée.

## 1. Le concept, tel que le terrain le tient

Trois habitudes du terrain ont chacune un foyer, et je les prends de la connaissance générale, non d'une étude du dossier. Le dossier ne tient aucune étude de terrain sur les super-applis, sur l'ingénierie de plateforme ou sur les cartes de contextes. Son seul terrain nommé est une ligne d'un document de conception : une célèbre super-appli de messagerie, et ses semblables.

La première est la super-appli et le mini-programme. Une grande application embarque un runtime et fait tourner de petites applications en elle, partageant ses services et son magasin. L'hôte est privilégié, la mini-appli de seconde classe, et l'isolation un bac à sable.

La deuxième est le contexte borné et la carte de contextes de la conception pilotée par le domaine, de 2003. Un grand système est découpé en modèles, chacun avec ses mots, et une carte montre comment ils se relient. C'est l'idée du terrain la plus proche d'un monde et d'un lien. Elle vit dans des diagrammes et en revue, et non dans un registre vivant qui refuse un appel.

La troisième est l'équipe de plateforme et le déploiement déclaré comme code. Une équipe construit la base interne sur laquelle les autres déploient, et des outils déclarent des machines avant qu'elles existent. La personne qui travaille à travers les étages est, sur le terrain, un architecte logiciel, un architecte de solutions ou un ingénieur de plateforme. C'est un titre tenu par une personne, dont les artefacts sont des diagrammes et des manifestes.

Pour les portées, le foyer du terrain est le compilateur : la cible d'une construction, et la vérification qui signale un appel que le niveau minimal de plateforme n'a pas. Chacun décide pour quel système le code est fait. Aucun ne laisse le programme nommer ce système au site d'appel et refuser l'acte.

La forme partagée : le terrain dessine l'image, un hôte, une carte, un diagramme, et garde le juge à l'extérieur. Dans les trois, le programme ne sait rien de sa propre composition. C'est ma lecture des trois, non une enquête sur le terrain.

À cette forme, j'oppose un principe.

## 2. Le premier principe

**La solution est déclarée en mondes, en liens et en une enveloppe avant que rien en soit construit, et chaque traversée entre eux est gouvernée.**

Les phrases du dossier sont trois. Une application est un monde vivant de sens. Des mondes, non des mini-applis : un graphe gouverné et non un conteneur hôte. Un architecte Softanza modélise d'abord l'architecture de déploiement, comme artefact déclaratif, avant une ligne de code de fonctionnalité système. La phrase ci-dessus est faite des trois et de la méthode du livre, qui est de déclarer puis de gouverner. Les trois sont celles du dossier, dites avec mes mots ; la phrase ci-dessus est le principe propre du chapitre, dans la voix du livre.

## 3. La forme Softanza

Trois niveaux, donc. Un monde est une application. Une constellation est un graphe de mondes. Une plateforme est l'enveloppe autour d'une solution et le sol sur lequel se tient une constellation. Et une seule personne déclare les trois.

### Un monde

Un monde a un être, un devenir, et une manière d'être rencontré. Le chapitre 4 a montré son être. Que répond un monde quand on lui demande d'expliquer les trois ? Demandez-le à un monde, pour une agence qui rend visite à des clients :

```haro
oApp = new stzApp("FieldVisits")
oApp {
    AddThingQ(:Account) { Has([ :number, :chapter, :balance ])  IsTrue(:balance, "@ >= 0") }
    AddThingQ(:Client)  { Has([ :code, :name, :city ])  Owns(:Account) }
    AddThingQ(:Visit)   { Of(:Client)  Has([ :agent, :date, :subject ]) }
    AddRelation(:Account, :belongsTo, :Client)
    AddFlowQ(:agent, :records, :Visit) { Require(:subject) }
    AddReactionQ(:Client).Unseen(90, :Days) { Propose(:Visit) }
    AddGoalQ(:EveryClientSeenThisQuarter) {
        Means      = "every :Client Has(:visit) Since(:quarterStart)"
        ReachedBy  = :planning
    }
    SetBody([ :GraphDB, :Files ]) { Graph = ".stzapp/world.stzgraf"  Files = "./" }
}
oApp.AddScreenQ(:ClientFile) { ToUnderstand(:Client)  Shows([ :identity, :accounts, :visits ]) }
oApp.AddRefinementQ(:balance).Bounds(0, 1000000)
oApp.AddReaches([ :mobile, :desktop, :web ])
oApp.Explain()
#--> WORLD FieldVisits   lives in: graphdb + files
#      BEING
#        account (number, chapter, balance)
#            true when balance @ >= 0
#        client (code, name, city)
#        visit (agent, date, subject)
#      RELATIONS
#        client owns account
#        visit of client
#        account belongsto client
#      BECOMING
#        when agent records visit require subject
#        whenever client unseen 90 days -> propose visit
#        wants everyclientseenthisquarter -> reached by planning
#      MET FROM WITHOUT
#        screen clientfile: understand client shows identity, accounts, visits
#        refine balance bounds [0..1000000]
#        reaches mobile, desktop, web
```

Il a répondu sous trois titres, `BEING`, `BECOMING` et `MET FROM WITHOUT`. `SetBody` ne fait que déclarer. Aucun fichier n'a été écrit par ce bloc.

Un monde tend vers quelque chose. Un but est un état voulu du graphe, et l'écart est mesuré. Un but sans motif à évaluer est refusé, et jamais simulé :

```haro
oApp = StzAppQ("visits")
oApp.AddThingQ(:Client) { Has([ :code, :name ]) }
oApp.AddThingQ(:Visit)  { Of(:Client) }
oApp.AddGoalQ(:EveryClientVisited) { Means = "every :Client Has(:visited)"  ReachedBy = :planning }
oApp.AddInstance("anna", :Client)
oApp.AddInstance("bilal", :Client)
oApp.Relate("anna", :visited, "visit1")
? @@( oApp.Pursue(:EveryClientVisited) )
#--> pursuing everyclientvisited via planning -- 1 proposal(s)
#    [ [ "attend", "client", "for", "bilal" ] ]
? oApp.GoalSatisfied(:EveryClientVisited)
#--> 0
oApp.Relate("bilal", :visited, "visit2")
? @@( oApp.Pursue(:EveryClientVisited) )
#--> pursuing everyclientvisited via planning -- 0 proposal(s)
#    [ ]
? oApp.GoalSatisfied(:EveryClientVisited)
#--> 1
oApp.AddGoalQ(:Vague) { Means = "make things nice" }
try
    oApp.Pursue(:Vague)
catch
    ? cCatchError
done
#--> stzGraphGoal.FromMeans: no 'every :Type' clause in 'make things nice'.
```

`Pursue` imprime sa propre première ligne, puis le `?` imprime la liste qu'il renvoie. Une relation plus tard, l'écart est comblé : `0 proposal(s)`, et `GoalSatisfied` répond `1`. Le but vague est refusé avec sa raison : `no 'every :Type' clause in 'make things nice'`. Avec une réaction déclarée, le même écart propose une *visit* pour Bilal, et sans elle, comme dans l'exécution ci-dessus, l'acte par défaut est *attend* : `[ "attend", "client", "for", "bilal" ]`.

### Une constellation

Rien ne passe entre les mondes à moins d'être déclaré et gouverné. Un lien doit exister, puis trois barrières se tiennent sur la traversée : l'acte doit avoir un niveau de risque déclaré, l'appelant doit détenir la permission, et l'autorité de l'appelant doit couvrir le risque. Chaque refus nomme sa barrière. Quelle barrière refuse la première ? Le lien existe dans les quatre appels ci-dessous, donc les trois refus sont ceux de la gouvernance :

```haro
oResto = StzAppQ("resto")
oResto.AddThingQ(:dish) { Has([ :name, :price ]) }
oSupplier = StzAppQ("supplier")
oSupplier.AddThingQ(:crate) { Has([ :produce, :qty ]) }
oCon = new stzSuperApp("acme-group")
oCon.AddWorld("resto", oResto)
oCon.AddWorld("supplier", oSupplier)
oCon.Bond("resto", "supplier", "order-produce")
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 0
? oCon.Why()
#--> governance refused: refused: 'order-produce' has NO declared risk tier (undeclared actions never proceed)
oCon.GovDeclareRisk("order-produce", 2)
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 0
? oCon.Why()
#--> governance refused: refused: 'resto' lacks PERMISSION (can) for 'order-produce'
oCon.GovGrant("resto", "order-produce")
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 0
? oCon.Why()
#--> governance refused: refused: 'resto' holds '' authority (level 0) but 'order-produce' is risk tier 2 (SHOULD does not cover it)
oCon.GovSetAuthority("resto", :Delegated)
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 1
? oCon.Why()
#--> allowed: active + bonded + governed
? oCon.GovernanceQ().NumberOfDecisions()
#--> 1
? @@( oCon.GovernanceQ().DecisionsOf("resto")[1][2] )
#--> [ "rationale", "cross-world call cleared" ]
```

Le niveau de risque refuse le premier : `'order-produce' has NO declared risk tier`. Le mot doublé « refused: refused: » est le texte propre de la bibliothèque. La traversée autorisée a écrit une décision d'elle-même ! Son enregistrement tient l'autorité et le risque de cet instant, et une lecture d'horloge, de sorte que le bloc n'imprime que la justification : `cross-world call cleared`. C'est la filiation qu'utilise le chapitre 30.

Le sol partagé est un monde aussi. Dans une constellation, le socle commun est lui-même une plateforme, et il tient une identité, une session et un magasin. Le socle commun n'est pas un genre particulier de nœud ; les mots propres de la conception sont qu'il est uniforme et récursif. De quelle classe est le socle commun ? Demandez-le-lui :

```haro
oCon = new stzSuperApp("acme-group")
oDb = new stzDatabase(":memory:")
oCon.OpenCommonsOn(oDb)
? classname( oCon.CommonsQ() )
#--> stzplatform
? oCon.RegisterIdentity("owner", "s3cret")
#--> 1
? oCon.RegisterIdentity("owner", "other")
#--> 0
? len( oCon.OpenSession("owner", "s3cret") ) > 0
#--> 1
? oCon.OpenSession("owner", "wrong") = ""
#--> 1
oCon.StorePut("currency", "EUR")
? oCon.StoreGet("currency")
#--> EUR
oDb.Close()
```

Ce bloc utilise une base de données en mémoire, donc ni fichier ni réseau. Le jeton de session est aléatoire, et seule sa présence est imprimée. Les secrets sont stockés salés et hachés, avec la fonction de dérivation de clé du moteur. La première ligne répond `stzplatform`, et c'est là le point : une plateforme n'est pas seulement l'enveloppe autour d'une solution. C'est ce sur quoi se tient une constellation. Dans le code, le socle commun n'est pas un nœud du graphe de la constellation : quand je l'ai sondé, le graphe tenait deux nœuds pour deux mondes enregistrés. Le monde zéro est un rôle que joue la plateforme.

Un monde échangé à chaud garde-t-il ses liens ? Une constellation s'emboîte aussi dans une autre, et un nom ne se prend qu'une fois :

```haro
oResto = StzAppQ("resto")
oResto.AddThingQ(:dish) { Has([ :name, :price ]) }
oCon = new stzSuperApp("acme-group")
oCon.AddWorld("resto", oResto)
oCon.AddWorld("supplier", StzAppQ("supplier"))
oCon.Bond("resto", "supplier", "order-produce")
oCon.GovDeclareRisk("order-produce", 2)
oCon.GovGrant("resto", "order-produce")
oCon.GovSetAuthority("resto", :Delegated)
oNew = StzAppQ("supplier-v2")
oCon.Swap("supplier", oNew)
? oCon.NumberOfWorlds()
#--> 2
? oCon.WorldQ("supplier").Name()
#--> supplier-v2
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 1
oHolding = new stzSuperApp("holding")
oHolding.AddConstellation("acme", oCon)
? oHolding.KindOf("acme")
#--> super
? oHolding.WorldQ("acme").NumberOfWorlds()
#--> 2
? oCon.KindOf("resto")
#--> app
try
    oCon.AddWorld("resto", oResto)
catch
    ? cCatchError
done
#--> stzSuperApp: world 'resto' already in the constellation.
```

Le lien a survécu à l'échange : `CallAcross` répond encore `1` ! Le chapitre 28 a utilisé `Retire` et `Revive`, et ce bloc est `Swap` et `AddConstellation`. L'emboîtement est un fait du registre. Rien dans le code n'achemine un appel dans une constellation emboîtée, donc la récursion de la conception est celle d'un registre et pas encore celle d'un appel. Une traversée est un verdict : `CallAcross` autorise ou refuse par 1 ou 0, et rien n'est encore remis à la cible.

Un piège. Un monde enregistré est une copie. L'ancien langage hôte copie un objet par valeur quand il est stocké, de sorte que le monde que vous enregistrez n'est pas le monde que vous tenez. L'en-tête de la classe le dit : les objets monde s'atteignent par l'index du registre, le chemin vivant. Configurez le monde entièrement, enregistrez-le, et atteignez-le par la constellation à partir de là. L'enveloppe a la même doctrine : poser un monde sur la plateforme récolte ses déclarations au moment de l'appel, et poser la gouvernance prend un instantané du régime.

### L'enveloppe, et la jointure

Une plateforme n'accorde une capacité d'un appareil que si la gouvernance en autorise le risque. Une permission détenue suffit-elle ? Les niveaux de risque, deux pour la caméra et quatre pour les paiements, sont ceux que la bibliothèque a déclarés :

```haro
oGov = new stzGovernance("resto-regime")
oGov.GrantPermission("resto", "use-camera")
oGov.GrantPermission("resto", "use-payments")
oGov.SetAuthority("resto", :Delegated)
oResto = StzAppQ("resto")
oResto.AddThingQ(:dish) { Has([ :name, :price ]) }
oPlat = StzPlatformQ("resto-envelope")
oPlat.SetWorld(oResto)
oPlat.SetGovernedBy(oGov)
oPlat.AddCapabilityQ(:camera).SetPurposes([ :scan_dish_photo ])
? oPlat.Granted(:camera)
#--> 1
oPlat.AddCapabilityQ(:payments).SetPurposes([ :charge_guests ])
? oPlat.Granted(:payments)
#--> 0
? oPlat.Why()
#--> refused: 'resto' holds 'delegated' authority (level 2) but 'use-payments' is risk tier 4 (SHOULD does not cover it)
```

La permission était détenue pour les deux, et les paiements ont été refusés quand même ! La raison : `'resto' holds 'delegated' authority (level 2) but 'use-payments' is risk tier 4`.

L'en-tête de la classe dit ce qui manque au monde : le monde modélise le monde, et manque délibérément de l'enveloppe opérationnelle. Les devoirs de l'enveloppe sont la génération, la jointure des capacités, le runtime du socle commun, un corps en réseau et un registre avec application. La génération est réelle, et refuse de générer pour un monde qui ne déclare aucune atteinte. Le chemin du succès écrit de vrais fichiers, donc je ne l'exécute pas ici. Je l'ai exécuté une fois, pour un monde d'un écran et d'une chose, et j'ai retiré ce qu'il avait écrit. La coque web est une page de 318 octets avec les écrans et les choses du monde comme éléments de liste, et la coque de bureau un lanceur de 251 octets. D'autres mondes donnent d'autres tailles. Telle est la limite des « coques par plateforme » : la génération est réelle, et minuscule.

### L'architecte, et les trois portées

Par *portée* j'entends celle de la System Foundation : développement, déploiement et exécution courante. Chaque acte système est écrit dans une portée nommée. Un architecte Softanza modélise d'abord l'architecture de déploiement. Le même verbe, dans deux portées, reçoit deux verdicts, et les mots propres de la cible disent pourquoi :

```haro
oSol = new stzPlatformProfile("greenhouse")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oSol.WithSuperApp(:phone, :Android)
oSol.WithApp(:sensor, :ESP32)
? oSol.DevelopmentSystem().OSName()
#--> windows
? oSol.App(:phone).System().OSName()
#--> android
? oSol.App(:sensor).System().OSName()
#--> espidf
? @@( oSol.App(:sensor).System().System().Capabilities() )
#--> [ "gpio", "network", "clock", "threads" ]
? oSol.CurrentSystem().IsRuntime()
#--> 1
? oSol.App(:backend).System().Spawn("cron")
#--> native
try
    oSol.App(:phone).System().Spawn("cron")
catch
    ? cCatchError
done
#--> scope 'android' (android) forbids 'process' -- spawn 'cron'. This target has no such capability.
```

Le nom du système de développement est celui qui a été déclaré, donc il ne dépend pas de la machine. La ligne `native` dépend de l'hôte : elle ne tient que sur un hôte qui peut lancer un processus, comme le chapitre 31 le dit de son propre mot. Le refus d'Android, `scope 'android' (android) forbids 'process'`, et la liste de capacités de la carte sont ceux de la cible, quel que soit l'hôte. Les trois portées sont `new stzDevSystem()` ou `DevelopmentSystem()` pour le développement, qui est de l'outillage seulement ; `App(:x).System()` pour le déploiement, où le code des fonctionnalités est écrit et vérifié ; et `new stzCurrentSystem()` ou `CurrentSystem()` pour l'exécution courante, qui est ce qui tourne maintenant. L'objet portée n'a pas de `Capabilities()` propre : l'appel passe par `.System().System()`. Une demande.

L'artefact de l'architecte est un fichier texte. Peut-il être relu, et que dit la plateforme d'une solution qui n'est pas saine ? Exécutez-le :

```haro
oSol = new stzPlatformProfile("greenhouse")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oSol.WithSuperApp(:phone, :Android)
oSol.WithApp(:sensor, :ESP32)
? oSol.ToStzPlatform()
#--> # .stzplatform -- a Softanza solution profile
#    platform: greenhouse
#    developed_on: windows
#    server: backend -> linux
#    superapp: phone -> android
#    app: sensor -> espidf
oBack = StzPlatformProfileQ()
oBack.FromString( oSol.ToStzPlatform() )
? oBack.App(:sensor).DeploymentOSName()
#--> espidf
oBad = new stzPlatformProfile("empty")
? @@( oBad.Validate() )
#--> [ "no development system declared (use DevelopedOn)", "the solution deploys no apps" ]
oPlat = StzPlatformQ("empty")
oPlat.SetProfile(oBad)
try
    oPlat.Build()
catch
    ? cCatchError
done
#--> stzPlatform.Build: the solution is not sound -- no development system declared (use DevelopedOn); the solution deploys no apps
```

La forme fichier est un texte simple que l'architecte possède, et elle fait l'aller-retour depuis une chaîne. La solution malsaine est refusée avant la construction, ses deux défauts nommés : `the solution is not sound -- no development system declared (use DevelopedOn); the solution deploys no apps`. L'ordre de construction et de déploiement est celui du chapitre 33, et la barrière sur qui déploie est celle du chapitre 24.

Qui est l'architecte ? Le dossier nomme la personne deux fois par son nom : dans la System Foundation, et dans la note de Central pour une école qui certifierait des architectes de Softanza, avec trois niveaux. Cette note est marquée retirée, comme prompt de lancement, le jour même où elle a été écrite. Un troisième endroit, un livre privé du domaine de projets sur la modélisation de plateforme, modélise des plateformes et ne nomme pas l'architecte. Cette certification est une proposition du 30 septembre 2026, non une livraison, et le site ne doit pas l'annoncer. Le protocole du domaine de projets définit un rôle comme un profil tenu dans une portée. Appliqué ici, ce qui est mon application et non celle du dossier, l'architecte n'est pas un rang. C'est ce que l'on tient dans la portée d'une solution : le profil, les mondes, la gouvernance. Je tiens cela pour une vue, non pour un résultat. Le site a une page de parcours pour l'architecte de plateforme et une page de certification qui dit que la proposition n'est pas annoncée (lu sur le site, le 9 octobre 2026). Je raconte l'architecte comme ce que l'on déclare, et la certification n'est que cette proposition ; aucune école n'est nommée ici.

Sept refus se tiennent derrière cette forme.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé l'hôte et la mini-appli.** Des mondes, non des mini-applis ; un graphe gouverné, non un conteneur hôte. Le chapitre 4 l'a raconté, et je renvoie à lui.

**J'ai refusé de faire du socle commun un genre particulier de nœud.** C'est un monde, et un monde est uniforme et récursif.

**J'ai refusé le bac à sable comme définition de l'isolation.** L'isolation est un sens déclaré et inspectable, et non une machine virtuelle en boîte noire. Un corps souverain de monde plus des liens barrés par une norme. Un bac à sable d'exécution n'est qu'une implémentation pour des mondes non dignes de confiance.

**J'ai refusé de faire de la gouvernance une facette de plus, à côté de la constellation, des liens, du socle commun, de l'atteinte et de la présence de la conception.** Elle est l'ambiant. Dans le code, une gouvernance par constellation, configurée par elle, de sorte qu'il y ait une gouvernance vivante et jamais une copie périmée tenue par un appelant.

**J'ai refusé de donner l'enveloppe au monde.** `stzApp` modélise le monde, et manque délibérément de l'enveloppe opérationnelle.

**J'ai refusé de figer *courant* sous un meilleur nom.** Le remède n'est pas un meilleur nom : chaque acte système est écrit dans une portée nommée. Les tentatives qu'elle refuse sont une paire de mots, ce système et le système cible, et un triplet, hôte, runtime et cible.

**J'ai refusé de déployer un profil.** Nous ne déployons pas un profil ; nous déployons une plateforme et ses parties. Le profil ne fait que décrire. La plateforme le possède et conduit la construction puis le déploiement.

Le tribunal dit maintenant ce qui, de tout cela, tourne.

## 5. Le tribunal

`06_stzsuperapp_narrated` prouve que les mondes s'enregistrent comme nœuds ; que le socle commun tient une identité et un magasin ; qu'une traversée est refusée pour un risque non déclaré, acceptée quand elle est gouvernée, et refusée quand elle n'est pas liée, avec le lien nommé ; qu'un monde retiré rompt ses liens et revit ; qu'un échange garde le nœud et le lien ; et qu'une constellation s'emboîte dans une autre. `01_platform_narrated` prouve que des coques sont générées selon l'atteinte déclarée et qu'un monde sans atteinte est refusé ; qu'une capacité n'est accordée que lorsque la gouvernance couvre son niveau de risque, et qu'une capacité jamais demandée est refusée avec une raison. Elle prouve que le socle commun enregistre des identités, ouvre des sessions, poste et lit des messages, et stocke. Elle prouve que le monde est servi sur un vrai port, et que le registre refuse un appel vers un monde non lié ou retiré. Elle écrit des coques à côté d'elle et ouvre un port de boucle locale. `full_scope_model_narrated`, que la garde appelle le socle commun de l'architecte, prouve que la solution est modélisée d'abord, qu'une solution malsaine est signalée, que les trois portées sont distinctes, que la portée refuse ce que la cible interdit et répète ce qui manque à l'hôte, que le fichier texte fait l'aller-retour, que la construction précède le déploiement, et qu'un déploiement par un acteur modèle de langage est refusé. `04_stzapp_pursue_narrated` et `05_stzapp_live_narrated` portent le but et les réactions.

La garde que le chapitre n'a pas : aucune ne juge les vérités d'un monde, un flux, ou le moment d'une réaction.

Je place maintenant le dossier à côté du terrain.

## 6. Le terrain, et où il mène

La super-appli mène en utilisateurs. La conception nomme son modèle et le remplace ; le chapitre 4 dit que le dossier ne mesure rien contre eux. La page Plateformes imprime l'autre moitié : les plateformes de clients tournent aujourd'hui sur des piles web ordinaires. Aucune plateforme ne tourne sur la constellation en production.

Le terrain mène en coques. La conception promet une application web progressive, une coque de bureau, une coque mobile. Le code génère une page et un lanceur de quelques centaines d'octets. Les coques sont conçues. La génération est construite, et minuscule.

Le terrain mène en ce que porte un contexte borné : une équipe et un langage. Un monde porte un graphe et une narration. Le persona pour lequel est fait un monde n'est pas un champ de la classe : un monde a la liste des surfaces qu'il atteint et rien d'autre sur qui il sert. Les cinq choses du site, un sol partagé, un monde pour chaque personne et appareil, des liens, des règles, des rôles, sont vraies du socle commun, des liens et de la gouvernance. Les rôles sont les acteurs, les permissions et l'autorité de la gouvernance. Il n'y a pas de classe rôle, et un monde par personne et appareil est une convention de nommage.

L'Atlas ne note pas ce volet. `stzApp` y est nommé une fois, dans le couloir du domaine des interfaces intitulé coque d'application et fenêtrage. C'est ce couloir, non le monde, qui est noté solide, avec la note qu'il n'y a ni orchestration multi-fenêtres, ni dialogues, ni menus, ni zone de notification. La plateforme dans un couloir du domaine du système. La constellation dans aucun.

Le compilateur mène sur les portées. Il vérifie contre une cible en usage quotidien à grande échelle ; la portée de Softanza est un objet d'exécution qu'un programme interroge. Ce qu'elle ajoute est un verdict au site d'appel dans les mots propres de la cible, et un jumeau qui répète ce qui manque à l'hôte, ce qui est le chapitre 24.

Là où le terrain et le dossier se rencontrent : une super-appli est un graphe de graphes. La carte de contextes du terrain est un diagramme. Celle de Softanza est un registre qui refuse.

## 7. La limite

Les vérités d'un monde sont narrées et non jugées. Le nombre dans une réaction en est le premier cas. Quatre-vingt-dix jours et un jour donnent-ils des propositions différentes ? Une réaction se déclenche pour chaque instance qui n'a pas de relation nommée d'après la chose qu'elle propose, et le commentaire au-dessus de `Pulse()` le dit. Faites tourner deux cliniques :

```haro
oA = StzAppQ("clinic-a")
oA.AddThingQ(:Patient) { Has([ :name ]) }
oA.AddThing(:Checkup)
oA.AddReactionQ(:Patient).Unseen(90, :Days) { Propose(:Checkup) }
oA.AddInstance("alice", :Patient)
oA.AddInstance("bob", :Patient)
oA.Relate("alice", :checkup, "checkup-1")
oB = StzAppQ("clinic-b")
oB.AddThingQ(:Patient) { Has([ :name ]) }
oB.AddThing(:Checkup)
oB.AddReactionQ(:Patient).Unseen(1, :Days) { Propose(:Checkup) }
oB.AddInstance("alice", :Patient)
oB.AddInstance("bob", :Patient)
oB.Relate("alice", :checkup, "checkup-1")
oA.Live()
#--> [clinic-a] is live -- 2 thing(s), 0 flow(s), 1 reaction(s), 0 goal(s); 1 proposal(s)
oB.Live()
#--> [clinic-b] is live -- 2 thing(s), 0 flow(s), 1 reaction(s), 0 goal(s); 1 proposal(s)
? @@( oA.Proposals() )
#--> [ [ "propose", "checkup", "for", "bob" ] ]
? @@( oB.Proposals() )
#--> [ [ "propose", "checkup", "for", "bob" ] ]
```

Les deux cliniques répondent `[ "propose", "checkup", "for", "bob" ]`. Quatre-vingt-dix jours et un jour donnent les mêmes propositions !

La même lecture vaut pour `IsTrue`, qui est stocké et narré alors que les instances ne portent pas de champs contre lesquels le juger. Elle vaut pour le `Require` et le `Then` d'un flux, stockés et narrés, où je n'ai trouvé aucun exécutant ; et pour les bornes d'un raffinement. Un monde déclare aujourd'hui qu'un solde ne doit pas être négatif. Il ne juge pas un solde. Ce qu'il juge, c'est l'écart d'un but, une traversée et une capacité. Donc je dis « un monde qui veut » pour le but, et « narré » pour la vérité. Le `true when balance @ >= 0` du chapitre 4 est une déclaration seulement. Le chapitre le dit donc en une ligne : déclaré et narré ; jugé seulement pour les buts, les traversées et les capacités.

La conception écrit plus que la classe ne parle. La classe parle-t-elle l'idiome quasi naturel de la conception pour la constellation ? Demandez-lui `Hosts`, `Admits` et `Explain` :

```haro
oSuper = new stzSuperApp("acme-group")
try
    oSuper.Hosts(:VisitApp)
catch
    ? cCatchError
done
#--> Error (R14) : Calling Method without definition: hosts
try
    oSuper.Admits(:VisitApp)
catch
    ? cCatchError
done
#--> Error (R14) : Calling Method without definition: admits
try
    oSuper.Explain()
catch
    ? cCatchError
done
#--> Error (R14) : Calling Method without definition: explain
```

Trois fois la réponse est `Calling Method without definition`. `Shares`, `Provides`, `Norm`, `Reaches` et `Generate` ne sont pas non plus définis sur une constellation. La classe a `AddWorld`, `AddConstellation`, `Bond`, `Retire`, `Revive`, `Swap`, la famille `Gov*`, `CallAcross`, `Crossings`, les appels du socle commun, et des appels qui regardent : `Why`, `GraphQ`, `WorldQ`, `KindOf`, `IsActive`, `HasWorld`, `NumberOfWorlds`, `AreBonded`, `CrossingCount` et `LastCallMs`. Les verbes de composition sont ceux-là. Les trois aspects de la conception s'atteignent aujourd'hui par `AddWorld`, `Bond` et `OpenCommonsOn`, et la gouvernance par `Gov*` ; l'atteinte et la présence sont la partie qui n'est pas là. L'en-tête de la conception appelle elle-même le document une conception à venir.

Ce qui est construit : le monde ; la constellation avec ses barrières, son registre de traversées avec les durées, une décision écrite sur une traversée autorisée, et une traversée refusée notée comme preuve ; la jointure des capacités de la plateforme, son socle commun, son registre, ses coques, son profil avec construction puis déploiement ; les trois portées.

Ce qui est conçu : l'idiome quasi naturel ; un appel acheminé dans une constellation emboîtée (aujourd'hui une traversée est un verdict, et rien n'est remis à la cible) ; charger un monde sans reconstruire un hôte ; des coques qui embarquent le moteur ; la fiche de garanties de cinq lignes, que la vision demande et que la page de parcours du site marque conçue : une ligne pour chacun de cinq systèmes auxquels la solution répond, technique, social, écologique, économique et culturel.

Ce qui est absent : une narration pour la constellation ou pour l'enveloppe, puisqu'aucune n'existe. La narration pour construire une première appli utilise des verbes que la classe n'a pas. Sept de ses appels échouent à ce commit, et je la cite pour l'idée et non pour la syntaxe. Une plateforme de client sur le moteur comme constellation. La fiche de garanties de cinq lignes écrite : aucune solution n'en a une. Un couloir de l'Atlas pour le monde, la constellation ou l'enveloppe.

Les six portes viennent ensuite.

## 8. Six portes

**Le programmeur.** Vous déclarez un monde avec des accolades, vous lui demandez de s'expliquer, et vous traversez entre les mondes avec un appel qui renvoie 0 et un `Why()` qui nomme la barrière. Surveillez la copie : configurez, puis enregistrez.

**L'analyste.** Vous déclarez des choses, des relations et un but comme un état voulu du graphe, et l'écart est mesuré. Vos vérités et vos durées sont narrées et pas encore jugées.

**Le concepteur.** Un monde déclare des écrans comme des intentions, un raffinement comme un bouton borné, et où il apparaît. Les coques générées aujourd'hui sont des bouchons, et le persona qu'un monde sert n'est pas un champ.

**Le décideur.** Vous déclarez qui peut traverser où et à quel risque, en trois barrières, et chaque traversée autorisée laisse une décision avec l'acteur, l'autorité et le risque de son instant. Le fichier de votre architecte est un texte que vous possédez.

**Le formateur.** Le dossier est mince. Le plan d'éducation liste une échelle du praticien à l'architecte puis au contributeur parmi cinq schémas de niveaux concurrents, et je le dis. L'exercice ci-dessous se juge en l'exécutant.

**L'agent.** Un monde peut être enveloppé comme un agent d'IA que l'hôte fait avancer d'un tick à la fois. Un déploiement par un acteur modèle de langage est refusé, et rien n'est déployé. La traversée entre les mondes est gouvernée par le nom et l'autorité du monde appelant.

## 9. Exercice

Déclarez deux mondes pour un lieu que vous connaissez : une boutique et son fournisseur, une classe et sa bibliothèque, une clinique et sa pharmacie. Donnez à chacun une chose. Reliez-les par un lien pour un acte. Avant d'exécuter quoi que ce soit, écrivez ce que vous attendez que `CallAcross` renvoie, et quelle raison vous vous attendez à lire d'abord.

```haro exercise
? YourConstellation.CallAcross("a", "b", "act")
#--> 1
```

Puis demandez l'appel, lisez la raison, et réparez la déclaration, non le tribunal, une barrière à la fois, jusqu'à ce qu'il renvoie 1. Comptez les refus. Quelle barrière auriez-vous oubliée sans le tribunal ? Le tribunal vous dit quelle barrière refuse : un niveau de risque manquant, une permission manquante, une autorité qui ne couvre pas le risque. Il n'écrit pas la déclaration. Un exercice plus dur : retirez le second monde et prédisez la nouvelle raison avant de la demander ; puis enregistrez une copie du premier, changez votre original, et prédisez ce que voit la constellation.

Je vous laisse celui-ci. Prenez le bloc des barrières de la section 3 et supprimez une ligne : `oCon.GovSetAuthority("resto", :Delegated)`. Arrêtez le bloc à son dernier `Why()`, comme ici, et je n'imprime rien dessous :

```haro exercise
oResto = StzAppQ("resto")
oResto.AddThingQ(:dish) { Has([ :name, :price ]) }
oSupplier = StzAppQ("supplier")
oSupplier.AddThingQ(:crate) { Has([ :produce, :qty ]) }
oCon = new stzSuperApp("acme-group")
oCon.AddWorld("resto", oResto)
oCon.AddWorld("supplier", oSupplier)
oCon.Bond("resto", "supplier", "order-produce")
? oCon.CallAcross("resto", "supplier", "order-produce")
? oCon.Why()
oCon.GovDeclareRisk("order-produce", 2)
? oCon.CallAcross("resto", "supplier", "order-produce")
? oCon.Why()
oCon.GovGrant("resto", "order-produce")
? oCon.CallAcross("resto", "supplier", "order-produce")
? oCon.Why()
? oCon.CallAcross("resto", "supplier", "order-produce")
? oCon.Why()
```

Exécutez-le et lisez le dernier `Why()`. Nommez la barrière qui refuse, et dites ce que le bloc devrait dire pour que la traversée soit autorisée. La section 3 dit ce que demande chacune des trois barrières, et que chaque refus nomme sa barrière. Quand vous l'aurez résolu, vous saurez que le tribunal nomme la barrière qui refuse et n'écrit pas la déclaration.

Le chapitre suivant dit comment une solution déclarée atteint la réalité, par exactement une porte : répéter sur ce qui ne touche à rien, valider par un acteur gouverné, et laisser la production refuser tout ce qui est faux. Répéter, puis valider.
