---
id: rehearse-then-commit
part: 5
number: 24
title: Répéter, puis valider
spine: false
narrations: [stz-service-virtualization-code-first-subscribe-later.md, stz-emulating-the-whole-solution-narration.md, stz-deploying-to-target-sites-narration.md, stz-planning-and-provisioning-a-deployment-narration.md, stz-system-dev-to-deploy-narration.md]
site: [forged]
guards: [service_registry_narrated, service_delivery_narrated, virtual_system_twin_narrated, virtual_environment_twin_narrated, emulator_narrated, deployment_narrated, full_scope_model_narrated]
stage:
  built: "un jumeau des fichiers et un jumeau de l'environnement du processus, chacun avec son historique, ses instantanés, un plan narré, ses risques et une vérification contre la réalité ; le plan de placement ; le bundle de l'émulateur, câblé au rattachement de production ; un déploiement comme graphe d'étapes avec un retour arrière ; le registre des services avec ses postures et la barrière qui refuse un faux en production"
  designed: "le moteur vu tournant dans un navigateur ; une vérification de dérive pour les réponses enregistrées ; des branches d'un jumeau ; des jumeaux pour les bases de données, les interfaces et les réseaux ; la phase émulée posée par le déploiement émulé"
  absent: "tout adaptateur réel pour les paiements, un modèle, le courrier, les SMS ou un magasin d'objets ; la vérification réelle d'un hôte distant ; le regard d'une personne sur la surface de l'émulateur ; une solution client émulée et déployée par ce chemin"
status: draft
rulings: ["12.13", "12.19", "12.21", "12.22", "12.25", "12.28", "12.29"]
research: research/ch24.md
---

## 1. Le concept, tel que le terrain le tient

Trois pratiques du terrain se tiennent à côté du programme, chacune avec sa propre configuration.

La première est planifier puis appliquer : l'infrastructure comme code et les chaînes de déploiement. Les références propres du dossier sont le graphe de dépendances des tâches d'une chaîne, le graphe de ressources d'un outil avec appliquer-ou-annuler, et un ordonnanceur de grappe qui place le travail selon les ressources qu'il demande. L'habitude du terrain est que le plan est un fichier pour un outil, et que savoir si le mauvais acteur peut l'appliquer relève d'une politique. Le dossier énonce la perte à laquelle il répond : c'est une convention, appliquée par l'espoir.

La deuxième est la virtualisation de service et le double de test : le mode test d'un fournisseur avec des cartes de test publiées, un serveur bouchon pour HTTP, et les bibliothèques qui enregistrent un appel une fois et le rejouent. L'habitude du terrain est que le double vit dans la suite de tests, et que la production est un autre fichier. La plainte du dossier : aucune passerelle ne refusera une carte parce que vous l'avez demandé poliment.

La troisième est l'émulateur et le simulateur : un émulateur de téléphone, un émulateur de carte, un substitut local d'un nuage. La phrase propre du dossier sur le genre est que les simulateurs mentent. Ils feignent la base de données, bouchonnent l'appareil, approximent le calcul.

Ce que les trois ont en commun, c'est que chacun est un outil séparé, et que le programme lui-même n'en sait rien. (Connaissance générale pour les outils, et non une étude du dossier, sauf là où je cite les documents.)

## 2. Le premier principe

**On atteint la réalité par exactement une porte : répéter sur ce qui ne touche à rien, valider par un acteur gouverné, et laisser la production refuser tout ce qui est faux.**

Le premier principe du dossier pour ce terrain est la première clause, et l'étiquette propre de la bibliothèque l'appelle un premier principe : on atteint la réalité par exactement une porte. Le chemin par défaut d'un changement qui a des conséquences est de répéter dans un jumeau, de générer un plan, et de valider le plan. Le plan est la porte. Le résumé du cadre tient en trois mots : répéter, planifier, valider. La ligne de structure du plan de ce livre dit la dernière clause : la production refuse un faux. La première clause est un document de la bibliothèque sans ligne d'auteur, et la seconde est celle du plan ; le chapitre les joint et attribue chaque partie à sa source.

## 3. La forme Softanza

### Le jumeau

Le seul artefact qui traverse vers la réalité est un plan. Il nomme chaque étape. Il signale celle qui retire quelque chose. Et si on lui demande de vérifier, il relit la réalité et dit que la source qu'il allait déplacer n'y est pas. Le chapitre 20 a dit « je l'ai vu avertir » sans montrer les mots. Les voici. Rien n'est exécuté :

```haro
oBench = new stzVirtualFileSystem()
oBench.CreateFolder("config")
oBench.CreateFile("config/pump.ini", "threshold=40")
oBench.MoveFile("old_settings.txt", "config/legacy.ini")
oPlan = oBench.GenerateUpdatePlan()
? oPlan.Narration()
#--> Update plan (3 of 3 operations to commit):
#-->   * 1. create folder 'config'
#-->   * 2. create file 'config/pump.ini' (12 bytes)
#-->   * 3. move 'old_settings.txt' -> 'config/legacy.ini'
? @@(oPlan.Risks())
#--> [ [ 3, "MOVES (removes source): move 'old_settings.txt' -> 'config/legacy.ini'" ] ]
? @@(oPlan.Validate())
#--> [ [ 3, "source absent in reality: old_settings.txt" ] ]
```

La narration de la bibliothèque imprime une ligne finale, selon laquelle la réalité reste intacte jusqu'à ce que je choisisse de valider ce plan. L'exécution ne l'imprime pas, donc je ne la montre pas.

Le jumeau n'est pas seulement un jumeau de fichiers. Une variable posée, un répertoire changé et un processus enfant mis en file sont enregistrés, narrés et signalés, alors que l'environnement réel n'a pas la variable et qu'aucun processus n'a démarré :

```haro
oEnv = new stzVirtualEnvironment()
oEnv.SetActor("agent-42")
oEnv.SetVar("SHOP_MODE", "rehearsal")
oEnv.Cd("/srv/shop")
oEnv.Spawn("backup-database --all")
? oEnv.Var("SHOP_MODE")
#--> rehearsal
? oEnv.NumberOfPendingSpawns()
#--> 1
? (new stzEnvironment()).Has("SHOP_MODE")
#--> 0
oEnvPlan = oEnv.GenerateUpdatePlan()
? oEnvPlan.Narration()
#--> Update plan (3 of 3 operations to commit):
#-->   * 1. set env var 'SHOP_MODE' = 'rehearsal'
#-->   * 2. change directory to '/srv/shop'
#-->   * 3. spawn process: backup-database --all
? @@(oEnvPlan.Risks())
#--> [ [ 3, "RUNS an external command (side effects): spawn process: backup-database --all" ] ]
```

Le paragraphe de limite du chapitre 20 disait que seuls les fichiers sont construits. C'était faux, et je l'ai corrigé là-bas.

Le jumeau a un second travail. Un développeur sur un portable sans broches écrit du code de broches pour une carte. La portée dit *répété*, comme les chapitres 8 et 31 l'ont montré. Au déploiement, le pont d'abaissement transforme la répétition en source de firmware, et un assistant peut proposer ce déploiement mais pas l'effectuer. `Build()` enregistre la commande de construction et n'exécute pas la chaîne d'outils, et `Deploy` abaisse en mémoire, donc aucun fichier n'est écrit :

```haro
oProduct = new stzPlatformProfile("greenhouse")
oProduct.DevelopedOn(:Windows)
oProduct.WithApp(:sensor, :ESP32)
? oProduct.ReadPinIn(:sensor, 34)
#--> rehearsed
? oProduct.WritePinIn(:sensor, 26, 1)
#--> rehearsed
oPlatform = StzPlatformQ("greenhouse")
oPlatform.SetProfile(oProduct)
oPlatform.Build()
try
	oPlatform.DeployAs(LLMActor("copilot"))
catch
	? cCatchError
done
#--> stzPlatform.Deploy: actor 'copilot' lacks the 'effectful' capability -- it may propose a deploy, not perform it.
? oPlatform.IsDeployed()
#--> 0
oPlatform.DeployAs(HumanActor("me"))
? oPlatform.ArtifactFor(:sensor)
#--> // firmware generated by the Softanza lowering bridge
#--> // target: espidf
#--> void setup() {}
#--> void loop() {
#-->   digitalRead(34);
#-->   digitalWrite(26, 1);
#--> }
```

La limite de ce bloc est à la section 7 : seuls deux verbes sont abaissés.

### Le plan de placement

Avant qu'un octet soit construit, le planificateur de livraison énonce, pour chaque capacité dont une partie a besoin, si la cible la fournit, si le moteur la fournit, si une construction la fournit, ou si le serveur la fournit, et donne la raison en une phrase. Le chiffre entre parenthèses est l'estimation du catalogue et non une mesure, donc ne le citez pas comme une affirmation. « 1 parts » est la grammaire propre de la bibliothèque :

```haro
oShip = new stzDelivery("shop")
oShip.AddSuperApp(:phone, :Android)
oShip.NeedsIn(:phone, [ :Unicode, :PivotTable, :Collection, :Neural ])
oShip.Plan().Show()
#--> Solution 'shop' -- placement & scope plan (rehearsal; nothing built yet)
#--> ==============================================================================
#-->
#-->   Part 'phone' [superapp] -> android (mobile / edge)
#-->      Unicode            [target]    Unicode: the target-platform is strong at it -> use its own
#-->      PivotTable         [stz.wasm]  PivotTable: Softanza-differential, mobile weak -> the on-device engine
#-->      Collection         [stz.js]    Collection: ergonomic -> a Softanza construct in the target language
#-->      Neural             [server]    Neural: heavy -> runs on the backend, not the edge
#-->      -> stz.wasm carries: [ "PivotTable" ]  (~12 KB, 1 of 4)
#-->
#-->   Summary: 4 capabilities across 1 parts -> target 1, engine 1, construct 1, server 1.
#-->   Build() will compile exactly this scope; Deploy() will commit it.
```

La règle derrière le plan, dans la conception de l'émulation : la périphérie ne porte une capacité que si elle est critique, et soit propre à Softanza, soit faible ou absente sur la plateforme cible. Une expression régulière est une construction posée sur celle de la plateforme, et jamais le module de correspondance du moteur compilé pour le navigateur.

### L'émulation

L'émulateur transforme le plan en un bundle, et le bundle est ce qui est livré. Dans le bloc suivant, le bundle généré pour la répétition est câblé directement au rattachement de production, et c'est l'acteur qui décide. Un assistant qui appelle `Deploy(:Production)` laisse le site `absent`. Une personne qui l'appelle rend le site `launched`. Le manifeste qui arrive nomme le groupe du moteur que la partie porte. La cible ici est un répertoire local, le seul genre de site qui stocke pour de vrai sans réseau :

```haro
cHere = StzReplace(WorkingDirectory(), "\", "/")
oFront = new stzDelivery("shopfront")
oFront.AddSuperApp(:web, :Browser)
oFront.NeedsIn(:web, [ :Unicode, :PivotTable, :Collection ])
oBundle = new stzEmulator(oFront)
oBundle.CompileEngineQ(FALSE)
oBundle.SetOutDirQ(cHere + "/_bundle")
oBundle.Build()
oSite = new stzDeploymentSite("cdn")
oSite.SetKindQ(:LocalRepo).SetStoreAtQ(cHere + "/_live")
oFront.DeployTo(oSite, :web)
oFront.ShipSlice(:web, oBundle)
oFront.SetActor(LLMActor("assistant"))
oFront.Deploy(:Production)
? oSite.Status()
#--> absent
oFront.SetActor(HumanActor("ops"))
oFront.Deploy(:Production)
? oSite.Status()
#--> launched
? @@(StzEngineDirListFiles(cHere + "/_live"))
#--> [ ".stzsite", "deploy.json", "index.html", "stz.js" ]
? read(cHere + "/_live/deploy.json")
#--> {
#-->   "solution": "shopfront",
#-->   "part": "web",
#-->   "engine": "aggregation",
#-->   "artifacts": "index.html,stz.js"
#--> }
StzDirDeleteAll(cHere + "/_bundle")
StzDirDeleteAll(cHere + "/_live")
```

La moitié honnête : aucun fichier du moteur pour la partie web n'est dans le manifeste, parce que la compilation du moteur était désactivée. Le bloc dit ce que l'exécution a livré, et non ce qu'une exécution complète livrerait. Un `Deploy(:Production)` nu, sans acteur du tout, renvoie une répétition et écrit un avertissement, "no effectful actor -- returning a rehearsal (nothing committed)". Je l'ai exécuté aussi : le site est resté absent et rien n'a été écrit.

Je n'ai pas exécuté `Deploy(:Emulated)`, parce qu'il construit le sous-ensemble de chaque partie par la chaîne d'outils du moteur, et que la construction de cette chaîne d'outils est une chose que cette machine ne doit pas exécuter. Ce que j'ai exécuté, c'est le bundle sans la compilation, et sa carte nomme un fichier du moteur qui n'y est pas. La section 7 dit ce que cela signifie pour l'affirmation que le moteur tourne dans un navigateur.

### Le déploiement

Un déploiement qui échoue défait ce qu'il avait fait. La partie web se déploie et passe sa barrière. Le stockage de la partie api échoue. Les étapes restantes sont sautées, le déploiement ne valide pas, et le site web, déjà en ligne, est ramené en arrière. Le site qui échoue est un serveur sans emplacement de stockage, ce qui échoue sans lancer quoi que ce soit :

```haro
cHere = StzReplace(WorkingDirectory(), "\", "/")
oShop10 = new stzDelivery("shop")
oShop10.AddBackend(:api, :LinuxServer)
oShop10.AddSuperApp(:web, :Browser)
oGood = new stzDeploymentSite("cdn")
oGood.SetKindQ(:LocalRepo).SetStoreAtQ(cHere + "/_site_cdn")
oBad = new stzDeploymentSite("prod-api")
oBad.SetKindQ(:Server)
oRun = new stzDeployment(oShop10)
oRun.SetActor(HumanActor("ops"))
oRun.SetTarget(:web, oGood)
oRun.SetTarget(:api, oBad)
oRun.RunAfter(:api, :web)
aRun = oRun.Run()
? aRun[1]
#--> 0
for aLine in aRun[2]
	? aLine[1] + " -> " + aLine[2]
next
#--> store:web -> done
#--> launch:web -> done
#--> verify:web -> done
#--> store:api -> FAILED
#--> launch:api -> skipped
#--> verify:api -> skipped
? oGood.Status()
#--> rolledback
StzDirDeleteAll(cHere + "/_site_cdn")
```

Avec un assistant comme acteur, la même exécution renvoie chaque étape comme *répétée*, le site reste absent, et aucun répertoire n'est créé. Je l'ai exécuté et je ne l'imprime pas.

### Le code d'abord, l'abonnement ensuite

Le code demande un service par son nom et n'apprend jamais quelle implémentation il a reçue. Le bac à sable voit le premier appel et aucun après la bascule, le second appel va vers l'adaptateur réel, et la surface est saine dès que chaque liaison réelle nomme un secret que le magasin de secrets détient. La passerelle réelle de ce bloc est une classe de remplacement écrite ici, puisque la bibliothèque ne livre aucun adaptateur de paiements. Une classe de remplacement nommée `LiveGateway` qui renvoie "authorized" est un faux en tout sauf son nom ; le registre la prend pour réelle parce qu'elle ne déclare rien, et la section 7 dit pourquoi cela compte :

```haro
oPay = new stzPaymentsSandbox()
oReg = new stzServiceRegistry("shop")
oReg.DeclareMany([ :payments, :mail ])
oReg.Bind(:payments, oPay)
oReg.Bind(:mail, new stzMailSandbox())
? Checkout(oReg, 4200)
#--> authorized
? oPay.NumberOfAuthorizations()
#--> 1
oStoreCf = new stzSecretStore("shop")
oStoreCf.Register( (new stzApiKey("stripe-key")).FromLiteralQ("sk-test-123") )
oStoreCf.Register( (new stzApiKey("mail-key")).FromLiteralQ("mk-test-123") )
oReg.BindLive(:payments, new LiveGateway, "stripe-key")
oReg.BindLive(:mail, new LiveMailer, "mail-key")
? Checkout(oReg, 4200)
#--> authorized
? oPay.NumberOfAuthorizations()
#--> 1
? oReg.PostureOf(:payments)
#--> live
oReg.SetPhase(:production)
? oReg.IsSoundVia(oStoreCf)
#--> 1

func Checkout poReg, nCents
	aRes = poReg.Service(:payments).Authorize(nCents, "tok_visa")
	poReg.Service(:mail).Send("dana@example.com", "Receipt", "Thank you.")
	return aRes[:status]

class LiveGateway
	def init
		return
	def Authorize nAmount, cToken
		return [ :status = "authorized" ]

class LiveMailer
	def init
		return
	def Send cTo, cSubject, cBody
		return 1
```

Le jour où vous vous abonnez, vous changez une liaison et pas une ligne. La clé est la clé de test d'un fournisseur et non une vraie.

### La production refuse

Un seul rapport nomme toutes les façons dont une surface n'est pas apte à la production : un service déclaré jamais lié, un faux, une vraie base de données qui disparaît au redémarrage, un adaptateur réel dont la clé n'est pas dans le magasin de secrets, et, en avertissement, un adaptateur réel qui ne nomme aucun secret. Le chapitre 31 a montré le service non lié et la levée d'erreur. Voici le reste de la liste. En phase de développement, la surface n'est déjà pas saine, puisqu'un service non lié et une clé manquante sont des erreurs dans toute phase. Les deux autres erreurs n'apparaissent qu'en phase de production. Le code liste huit invariants, et le plan et la narration en listent cinq :

```haro
oStoreSf = new stzSecretStore("shop")
oSurf = new stzServiceRegistry("shop")
oSurf.Bind(:payments, new stzPaymentsSandbox())
oSurf.Bind(:scratch, StzMemoryDataSourceQ())
oSurf.BindLive(:cache, new stzString("cache-adapter"), "redis-url")
oSurf.BindLive(:sms, new stzString("sms-adapter"), "")
oSurf.Declare(:reporting)
? oSurf.IsSoundVia(oStoreSf)
#--> 0
oSurf.SetPhase(:production)
oSurf.ReportVia(oStoreSf)
#--> Service registry 'shop' [production] -- 4 bound: 1 sandboxed, 1 local, 2 live
#-->   [ERROR] unbound-service @ shop/reporting -- declared but never bound -- asking for it will raise
#-->   [ERROR] sandbox-in-production @ shop/payments -- still bound to a SANDBOX in a production phase -- a fake must never ship
#-->   [ERROR] ephemeral-in-production @ shop/scratch -- a LOCAL source that vanishes on restart (in-memory) is bound in a production phase
#-->   [ERROR] live-without-secret @ shop/cache -- credential 'redis-url' is not in the secret store
#-->   [WARN] inline-credential @ shop/sms -- live adapter bound without naming a store secret
```

Deux questions différentes sont posées à la porte. Qui est refusé, et ce qui est refusé. Un assistant est refusé pour ce qu'il est. Une personne est refusée pour ce qu'est la surface. Et poser la question laisse la phase où elle était ; la question est posée dans le cadre de la production même en phase de développement :

```haro
oStoreWw = new stzSecretStore("shop")
oOne = new stzServiceRegistry("shop")
oOne.Bind(:payments, new stzPaymentsSandbox())
? oOne.Phase()
#--> development
? oOne.MayGoLive(LLMActor("assistant"), oStoreWw)
#--> 0
? oOne.WhyNotLive(LLMActor("assistant"), oStoreWw)
#--> actor 'assistant' is not effectful -- it may propose, not commit
? oOne.MayGoLive(HumanActor("dana"), oStoreWw)
#--> 0
? oOne.WhyNotLive(HumanActor("dana"), oStoreWw)
#--> sandbox-in-production: still bound to a SANDBOX in a production phase -- a fake must never ship
? oOne.Phase()
#--> development
```

Et le registre connaît des services alors que la livraison connaît des parties. Réunis, ils répondent à la question qu'aucun des deux ne peut traiter : quelle partie est sur le point de partir sur un double. Le registre lui-même ne signale rien, puisque la phase est le développement et qu'il n'y a pas de constats. La vérification au niveau des parties répond quand même, par destination, et nomme la partie :

```haro
oS3 = new stzServiceRegistry("shop")
oS3.DeclareMany([ :payments, :cache ])
oS3.BindSandbox(:payments, new stzPaymentsSandbox())
oS3.BindLocal(:cache, StzMemoryBlobStoreQ())
oD3 = new stzDelivery("shop")
oD3.AddBackend("api", "linux")
oD3.AddApp("web", "browser")
oD3.UseServicesQ(oS3)
oD3.NeedsServiceInQ("api", [ :payments, :cache ])
oD3.NeedsServiceInQ("web", [ :reporting ])
oD3.DeployTo(StzDeploymentSiteQ("host1"), "api")
? oS3.Phase()
#--> development
? len(oS3.Findings())
#--> 0
for aF in StzCheckServiceDelivery(oD3)
	? aF[:rule] + " @ " + aF[:where] + " [" + aF[:severity] + "]"
next
#--> production-part-uses-sandbox @ api [error]
#--> production-part-uses-ephemeral @ api [error]
#--> part-uses-undeclared-service @ web [warning]
```

## 4. La décision, et ce que j'ai refusé

Tout ce qui suit vient des documents de conception et des narrations de la bibliothèque, écrits en sessions sans ligne d'auteur. Le dossier ne contient aucune décision de ma part pour ce chapitre. Ses décisions sont celles des documents.

**J'ai refusé le simulateur qui ment.** L'émulateur ne feint rien. Chaque partie exécute le même artefact de moteur compilé qui sera livré à sa cible. Cette affirmation a une mise en garde, à la section 7 : la preuve que le moteur tourne dans un navigateur n'est pas dans l'arbre épinglé.

**J'ai refusé de relivrer ce que la cible fait bien.** La périphérie ne porte une capacité que si elle est critique et soit unique, soit faible sur la cible.

**J'ai refusé la prolifération d'outils, et la convention appliquée par l'espoir.** La cible doit être à une configuration près, et la déployer doit être un seul acte gouverné.

**J'ai refusé un secret écrit en dur.** Un site porte une référence d'authentification, pas une clé.

**J'ai refusé de toucher à la réalité par défaut.** La production ne valide que si l'acteur peut valider. Un `Deploy(:Production)` nu, sans acteur, ne touche à rien.

**J'ai refusé le faux complaisant.** Un faux complaisant est plus dangereux que pas de faux du tout. Le silence est la pire réponse : le mode indulgent répond 501, parce qu'un échec de correspondance ne doit jamais pouvoir passer pour un succès.

**J'ai refusé « faux contre réel » comme vérité entière.** C'était trop grossier. Il y a maintenant quatre postures : bac à sable, local, réel et conformité. La troisième a été ajoutée quand l'exemple de la base de données a montré qu'un fichier SQLite est une vraie base de données dans un fichier qu'on possède.

**J'ai refusé une barrière qui échoue en laissant passer.** Le registre gardait autrefois son état dans des attributs, si bien que l'attacher à une livraison en prenait un instantané, et la barrière aurait laissé passer une surface non saine. Une barrière qui échoue en laissant passer est pire que pas de barrière. L'état se trouve désormais dans une table indexée par identité, de sorte que chaque copie est le registre. Tout ce qui gouverne les autres doit survivre à la copie.

**J'ai refusé de virtualiser la qualité d'un modèle.** La qualité d'un modèle de pointe ne peut pas être virtualisée. Ce que le bac à sable vend à la place, c'est le déterminisme, un coût sur lequel on peut faire une assertion, et le travail hors ligne.

**J'ai refusé de livrer les adaptateurs réels.** Les adaptateurs réels de paiement ne sont délibérément pas livrés, puisqu'un compte, une clé et un réseau dépendent de l'infrastructure. Le contrat est défini, et le registre refuse de laisser le faux partir à sa place.

**J'ai refusé de poser une question dans le mauvais cadre.** `MayGoLive` interrogeait autrefois sur la santé dans la phase courante, si bien qu'avec un faux lié il répondait oui. Maintenant il est interrogé dans le cadre de la production quelle que soit la phase.

**J'ai refusé de dire que le besoin du restaurant était l'origine de la conception.** Le site dit que les conceptions de l'émulation et du déploiement prennent une solution comme exemple, et que c'est un exemple, pas l'origine de la conception. La solution d'exemple des documents porte le nom de produit d'un client, et je l'ai renommée dans chaque bloc. Le chapitre 28 a raconté l'histoire, et je ne la répète pas.

Le plan des services est intitulé « écrit le 23 juillet 2026 en réponse à la question de l'utilisateur ». La question demande si l'émulation couvre les bases de données, les API métier, les modèles de pointe et les fournisseurs de nuage, afin qu'un programmeur puisse coder un programme entier sans abonnements ni frais et obtenir quand même une solution fonctionnelle prête à déployer. Le chapitre rapporte le titre du plan et sa date. Le dossier ne dit pas qui a posé la question, et le chapitre ne prétend pas que c'était celle de l'auteur.

## 5. Le tribunal

`service_registry_narrated` prouve la surface déclarée ; qu'un service non lié lève une erreur ; que l'application demande par nom ; qu'un bac à sable en production est une violation, avec un constat par faux ; que le justificatif doit être dans le magasin de secrets ; que passer en réel est un franchissement gouverné, avec un assistant refusé et une personne refusée à cause d'un faux ; que poser la question laisse la phase ; les aides d'intégration continue ; la quatrième posture ; et un adaptateur réel qui a besoin d'un certificat. `service_delivery_narrated` prouve la surface externe répétée dans le plan ; le contrôle préalable ; la barrière, qui lors d'un déploiement en production refuse un faux et consigne chaque raison, et s'ouvre quand la surface est réelle ; que le registre est un seul registre quel que soit le nombre de copies faites ; et la question de savoir quelle partie dépend d'un faux. J'ai exécuté les deux le 8 octobre 2026 : 93 sur 93 et 60 sur 60. Le second a laissé à côté de lui un fichier de zéro octet, et je l'ai supprimé.

`virtual_system_twin_narrated` prouve, en douze scènes, que le jumeau ne touche à rien de réel, que le plan narre et signale, que la validation est l'unique porte, qu'une portée refuse, qu'un relecteur rejette une étape, que cent opérations restent en mémoire jusqu'à une seule validation. `virtual_environment_twin_narrated` prouve la même forme pour les variables, un répertoire et des lancements de processus en file. `emulator_narrated` prouve que le bundle se génère, que la carte rend chaque partie par rôle, et que chaque partie ne porte que son sous-ensemble. `deployment_narrated` prouve le site comme configuration, la validation gouvernée, le plan d'étapes, le retour arrière, la faisabilité, et le backend git ; il lance `git`, donc le livre ne l'exécute pas. `full_scope_model_narrated`, scènes 13 à 16, prouve que construire précède déployer, qu'une solution non saine ne peut pas être construite, le pont d'abaissement, et le déploiement gouverné.

Le refus que fait la production est prouvé par les deux premières gardes, qui ont tourné. Que le moteur répété tourne dans un navigateur n'est prouvé par aucune garde qui tourne.

## 6. Le terrain, et où il mène

Les services réels sont en tête. Le plan le dit : un double n'est pas le service réel, et il faut encore au moins une exécution réelle avant la production. Une passerelle scriptée n'est pas l'ensemble des cas limites d'un fournisseur. Les réponses enregistrées dérivent, et une suite de rejeu demande de ré-enregistrer et de tester les contrats contre l'API réelle. La bibliothèque a l'appel d'enregistrement et pas de vérification de dérive.

Les modèles de pointe sont en tête, et ne peuvent pas être émulés. Le modèle est jugé contre le vrai modèle, délibérément, comme sa propre activité.

L'infrastructure réelle est en tête. Le déploiement dépend de l'infrastructure : vérification réelle contre un hôte ou un compte réel. Les commandes sont générées, et à un hôte joignable près d'être littérales.

Les outils de déploiement matures sont en tête. La narration le dit simplement : cela ne remplace pas tous les outils de déploiement matures, cela unifie les coutures que ces outils laissent exposées.

La fidélité est limitée, et le dit. L'émulation est fidèle mais pas omnisciente, donc elle dit ce qui est quoi. Ce qu'un double prouve est plus étroit encore : un puits de capture prouve ce que vous auriez envoyé, et un répertoire n'est pas un CDN.

Là où je pense que le dossier se distingue, c'est dans le couplage. Le double, le plan, les noms de justificatifs, la barrière et l'acteur sont déclarés dans le même programme que celui qui est livré, et une seule barrière les juge.

## 7. La limite

**Un faux écrit à la main qui ne dit rien de lui-même passe la barrière.** Le registre lit ce que l'objet dit qu'il est. Un double qui ne déclare ni qu'il est un bac à sable ni qu'il est local et réel est pris pour réel : pas d'avis veut dire réel. Donc « la production refuse un faux » est exact pour les doubles propres de la bibliothèque, et pour tout double qui se déclare. Un faux non déclaré passe :

```haro
oUndeclared = new stzServiceRegistry("shop")
oUndeclared.Bind(:payments, new AlwaysYes)
oUndeclared.SetPhase(:production)
? oUndeclared.PostureOf(:payments)
#--> live
? oUndeclared.IsSound()
#--> 1

class AlwaysYes
	def init
		return
	def Authorize nAmount, cToken
		return [ :status = "authorized" ]
```

La classe de remplacement du bloc précédent, `LiveGateway`, est un tel objet.

**L'abaissement connaît deux verbes.** Seuls `read_pin` et `write_pin` deviennent du code. Toute autre opération répétée devient une ligne de commentaire. J'ai répété `UseIn(:sensor, :gpio, "blink the status led")` et le firmware a reçu un commentaire. Pour un serveur ou un téléphone, l'artefact est un en-tête sans ligne quand rien n'a été répété. Le « la carte est le dernier pouce » de la narration vaut pour les lectures et écritures de broches seulement.

**Le contrat de fidélité est par classe de cible.** La conception dit que chaque partie déclare ce qui est fidèle et ce qui est approximé. Le code renvoie un texte fixe pour un microcontrôleur, qui liste deux choses approximées, et un pour tout le reste, "faithful".

**Les tailles sont des estimations.** Le plan imprime un chiffre tiré d'un catalogue, et la narration imprime deux chiffres différents pour la même partie. N'imprimez pas une taille comme une affirmation.

**`Deploy(:Emulated)` ne déplace jamais le registre.** Le plan dit qu'il résout les services vers des bacs à sable. Le code construit l'émulateur et retourne ; seul le déploiement de production touche à la phase du registre, et la valeur de phase `:emulated` que possède le registre n'est posée par rien.

**Un `Deploy(:Production)` refusé laisse le registre en phase de production.** Après mon déploiement refusé, `Phase()` a imprimé `production`. Le contrôle préalable restaure la phase, et le déploiement non.

**Un plan signale, il ne classe pas.** Le chapitre 20 l'a dit, et le document du cadre dit "ranked risk assessment".

Ce qui est conçu : le moteur tournant dans un navigateur. Les documents disent que le `solve 2 -8` du téléphone renvoie `x = 4` dans une page. La garde qui le vérifie, `wasm_narrated`, dit dans son propre en-tête qu'elle vérifie le câblage et la construction, puisque l'ancien langage hôte ne peut pas exécuter wasm, et elle cite une page dans le navigateur avec "8/8 checks". Cette page n'est pas dans l'arbre épinglé : je l'ai cherchée et n'en ai trouvé aucune. Et je n'ai pas vu la surface de l'émulateur dans un navigateur, et le dossier ne nomme personne qui l'ait vue. Par la loi du chapitre 33, cette surface est non perçue. Le chapitre dit donc : câblé, construit par la chaîne d'outils, non vu dans un navigateur par quiconque le dossier nomme.

Est aussi conçu : des branches d'un jumeau et les alternatives et le retour du plan, pour lesquels aucune méthode n'existe ; des jumeaux pour les bases de données, les interfaces et les réseaux ; et une vérification de dérive pour les réponses enregistrées.

Ce qui est absent : un adaptateur réel pour les paiements, un modèle de pointe, un magasin d'objets, les SMS ou le courrier. Les contrats et les doubles sont livrés, et les clients réels ne le sont pas, délibérément. La vérification réelle d'un hôte ou d'un compte distant : les commandes sont générées, et rien n'a tourné contre un hôte. Une solution client émulée et déployée par ce chemin : rien dans le dossier, ce que le chapitre 33 porte comme la ligne encore due.

## 8. Six portes

**Le programmeur.** Vous codez toute l'intégration contre des noms, avec des doubles qui lèvent une erreur quand vous avez oublié quelque chose et un compteur qui vous permet de faire une assertion sur un frais. Le jour où vous vous abonnez, vous changez une liaison et pas une ligne. La perte : le double toujours-oui que vous avez écrit vous-même passe la barrière.

**L'analyste.** Avant que quoi que ce soit bouge, vous pouvez lire le plan de placement, les dépendances externes avec les justificatifs que la production demandera par leur nom, le graphe d'étapes, et quelle partie dépend d'un faux. Les tailles sont des estimations, et les constats sont par partie.

**Le concepteur.** L'émulateur génère une surface à partir du plan, avec une grille de parties par rôle et une fenêtre par partie. J'ai vérifié le texte généré seulement, et jamais l'apparence. Dites « généré », et non « vu ».

**Le décideur.** « Qui peut déployer ? » est une propriété. Un assistant peut planifier la livraison et le site reste absent. Une personne peut valider. Aucun des deux ne peut livrer un faux. La perte à imprimer : les hôtes réels et les fournisseurs réels dépendent de l'infrastructure, et le dossier ne nomme aucune exécution réelle.

**Le formateur.** Une personne qui apprend peut construire l'intégration d'une boutique entière sans compte, sans clé et sans frais, et regarder le double refuser ce qu'elle a oublié. Son déploiement échoue sans danger et revient en arrière.

**L'agent.** Vous pouvez répéter toute l'intégration et planifier toute la livraison, dans un monde où rien de réel ne peut bouger : un paiement en bac à sable ne déplace aucun argent et un puits de courrier n'envoie aucun courrier. Vous pouvez demander si vous pouvez passer en réel et qu'on vous dise pourquoi non. Vous ne pouvez pas valider. La perte : cette garantie couvre les doubles propres de la bibliothèque, et une surface liée à quelque chose de réel est hors de sa portée.

## 9. Exercice

Écrivez, sous chaque ligne, ce que vous attendez avant de l'exécuter :

```haro exercise
oMine = new stzServiceRegistry("my-project")
oMine.Bind(:payments, new stzPaymentsSandbox())
oMine.Bind(:notes, StzMemoryDataSourceQ())
oMine.BindLive(:maps, new stzString("maps-adapter"), "maps_key")
oStoreMine = new stzSecretStore("my-project")
# under each line, write the line you expect before you run it
? oMine.IsSound()
? oMine.IsSoundVia(oStoreMine)
? len(oMine.FindingsForProductionVia(oStoreMine))
? oMine.MayGoLive(HumanActor("me"), oStoreMine)
? oMine.Phase()
```

Ensuite, enregistrez une clé nommée `maps_key` dans le magasin de secrets, et écrivez de nouveau le nombre de constats de production. Puis liez une classe écrite à la main avec une méthode `Authorize` qui dit toujours oui, et demandez quelle posture le registre lui donne. Si une promesse casse, ne la changez pas : expliquez d'abord la sortie. Je ne vous dis pas où vous serez surpris.
