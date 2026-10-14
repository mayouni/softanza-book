---
id: a-restaurant-in-lyon
part: 6
number: 28
title: Un restaurant à Lyon
spine: false
narrations: [stz-service-virtualization-code-first-subscribe-later.md, stz-perf-judgment-narration.md, stzApp-building-your-first-app-narration.md]
site: [forged, customers]
guards: [06_stzsuperapp_narrated, service_delivery_narrated, payments_port_narrated, judgment_narrated, graphrule_object_narrated]
stage:
  built: "la constellation de mondes avec ses liens et ses normes ; le bac à sable des paiements et la barrière de production qui refuse un faux ; le budget de vitesse déclaré et jugé"
  designed: "le Verrou comme règle de la bibliothèque ; la constellation écrite dans l'idiome proche du naturel que la conception décrit"
  absent: "l'adaptateur de paiement réel du restaurant ; une mesure du budget sur un vrai réseau mobile ; une attente de vitesse dans le percentile propre au propriétaire ; la mesure du temps côté navigateur ; la plateforme sur le moteur Softanza"
status: draft
rulings: ["12.15", "12.19", "12.25", "12.29", "12.30"]
research: research/ch28.md
---

Dans ce chapitre, je raconte une leçon payée dans l'ordre, avec ses dates : un restaurateur de Lyon, deux ans de spécification sans rien d'utilisable, et le renversement du 4 juillet 2026, le client en premier. Je montre ce que la bibliothèque en porte : le Verrou comme règle sur les mondes d'un cycle, un bac à sable de paiements non complaisant, une constellation qui endort un monde, un budget de vitesse déclaré et jugé. Je dis où elle ne porte rien, et les six choses que j'ai refusées, parmi lesquelles le grand système d'un seul bloc, la dérive silencieuse, le faux complaisant, et prêter au propriétaire ce qu'une simulation avait dit. Le principe tient en une phrase sur le site : livrer petit, vite et utile, et laisser les fondations mûrir en parallèle sans jamais bloquer une livraison.

## 1. Le concept, tel que le terrain le tient

Chaque leçon de ce projet a, sur le terrain, un lieu ordinaire, et le terrain la garde en dehors du programme.

Un périmètre fixé pour un cycle vit dans un processus. En Scrum, le but d'un sprint ne change pas pendant qu'il court ; en Shape Up, le temps est fixé et le périmètre varie, et les idées nouvelles attendent hors du cycle. Essayer un service avant de le payer vit dans le mode test d'un fournisseur et dans les outils qui tiennent la place d'un service HTTP. Un budget de performance vit dans un contrôle d'intégration continue du poids et de la vitesse d'une page. La mesure de la vitesse propre au web est un chiffre pris sur de vrais chargements de pages, au soixante-quinzième percentile. L'image de toute une constellation de petites applications vit dans la super-application : un hôte qui embarque un runtime et fait tourner des mini-applications à l'intérieur. Tout cela est une connaissance générale, pas une étude du dossier.

Les quatre sont de bonnes pratiques, et dans les quatre le programme lui-même n'en sait rien.

## 2. Le premier principe

Le projet fut une leçon payée, et la leçon tient en une phrase sur le site : **livrer petit, vite et utile, et laisser les fondations mûrir en parallèle sans jamais bloquer une livraison.**

Sa compagne est la règle de preuve de ce chapitre, prise sur la même page : une leçon n'est listée que lorsqu'un fichier de la bibliothèque la porte.

## 3. La forme Softanza

Un restaurateur de Lyon possède un restaurant de couscous, et il voulait une plateforme pour le commerce de quartier. Il n'est pas programmeur, et les notes du projet le disent. Je vais raconter le projet dans l'ordre, avec ses dates, puis montrer ce que la bibliothèque porte de chaque leçon.

Tout a commencé par une offre, le 2 mai 2024, pour une mission d'analyse métier. Ce qui a suivi, ce sont deux ans, de l'aveu même du propriétaire, de recherche et de réflexion, et de ce que j'appelais la spécification : des analyses fondatrices, un roman de narrations, un premier produit spécifié jusqu'au dernier détail. Cela n'a rien produit qu'il puisse utiliser. Au milieu de 2025, le projet a failli s'arrêter, et un silence de six mois a suivi. C'est là que j'ai appris la doctrine de la section 2 : livrer petit, vite et utile.

Le 3 juillet 2026, nous avons répété le projet à deux : un cadrage de ses réponses que j'ai écrit avec une session, et une campagne de vingt-deux tests simulés, menés par des sessions jouant le propriétaire. Je dis « simulés » chaque fois, parce que les réponses de ce fichier ne sont pas les siennes. Le lendemain, 4 juillet, il a répondu avec ses propres mots à un vrai rapport de cadrage. Il a renversé l'ordre du travail. Nous avions imaginé une ligne qui allait du fournisseur au restaurateur et finissait par le client. Il l'a retournée : le client d'abord, le restaurateur ensuite, le fournisseur en dernier. Et il a écrit que la vitesse de commande était sa première priorité, non négociable. Sa grande crainte était la friction au premier chargement, et la seconde crainte, dans le même rapport, était le calendrier : aucune des échéances jusque-là n'avait été tenue.

La réponse du projet à sa crainte est un document et un carnet. Nous l'avons appelée le Verrou. En juillet, un second cadrage la lui a proposée, clause par clause. Les trois premières : un seul avenant ; toute idée nouvelle va dans un carnet, relu à la fin du cycle ; une entrée exige une sortie écrite. Les deux dernières : une démonstration toutes les deux semaines et aucune date au-delà du prochain cycle ; et une définition de « terminé ». Il a accepté quatre clauses telles qu'écrites et ajusté la cinquième en y ajoutant un critère de lui : que d'autres commerçants et partenaires puissent installer le produit seuls. Dans le dossier, c'est moi qui ai demandé le Verrou en premier, comme une règle sur moi-même : que le changement de cap soit le seul changement de cap permis. Le 4 août 2026, le premier avenant a été clos. Douze décisions ont été scellées ; trois ont été reposées en termes simples, parce que lui-même avait signalé qu'il ne les avait pas comprises. La leçon notée porte sur la manière de demander : dès qu'une question parle de jalons, de phasage et de cycles, le propriétaire cesse de suivre. Alors les questions sont passées dans la langue de son métier.

Le 15 août, la première démonstration a été conçue pour lui seul. La liste de contrôle porte son nom et « seul » dans son titre. Il ouvre la livraison sur son propre ordinateur, scanne un code avec son téléphone et un autre avec sa tablette, passe sa propre commande depuis le téléphone, et la regarde arriver sur la tablette. S'il reste bloqué, un bouton prépare un message à coller dans une messagerie. Le critère de réussite se lit : il commande depuis son téléphone, et cela arrive sur sa tablette, sans nous. Le carnet montre que cela s'est produit : ses remarques de ce jour y ont été saisies le 17. Et le 19 août, il a passé une journée de terrain avec deux téléphones et des photographies envoyées par une messagerie, à mesurer sur un vrai téléphone. Un point d'accès fonctionne sans carte dedans ; l'adresse de la passerelle était stable d'un redémarrage à l'autre. Un téléphone est client Wi-Fi ou point d'accès, jamais les deux ; le système d'un iPhone ne revient pas de lui-même sur un réseau sans internet. Les notes du projet l'appellent alors son co-architecte. Le dossier s'arrête le 25 août 2026.

Voilà l'histoire. Qu'en porte la bibliothèque ?

**Le Verrou.** Je dois être exact ici. La page Forged du site contient une règle que j'ai faite : une leçon n'est listée que lorsqu'un fichier de la bibliothèque la porte. Aucun fichier ne porte le Verrou. C'était un pacte et un carnet, tenus dans des documents. Ce que la bibliothèque peut faire, c'est vous donner la déclaration qui s'en approche le plus : une règle sur les mondes d'un cycle, selon laquelle un monde sans admission écrite est un constat. Que dit le tribunal quand une idée entre dans le cycle sans admission écrite ? Ce bloc est une construction, pas le code du restaurant :

```haro
oRule = new stzGraphRule("the-lock")
oRule.SetDomainQ("scope")
oRule.WhenQ("kind", "equals", "world")
oRule.WhenQ("admitted-by", "missing", "")
oRule.ThenViolationQ("a world entered the cycle with no written admission")
g = new stzGraph("cycle-1")
g.AddNode("customer-phone")
g.SetNodeProperty("customer-phone", "kind", "world")
g.SetNodeProperty("customer-phone", "admitted-by", "the opening scope")
g.AddRule(oRule)
? g.RulesAreSound()
#--> 1
g.AddNode("loyalty-club")
g.SetNodeProperty("loyalty-club", "kind", "world")
g.RulesReport()
#--> Rule report 'cycle-1': 1 finding(s), 1 error(s), 0 warning(s) -> UNSOUND (errors present)
#      [scope] 1 finding(s)
#        ERROR the-lock @ loyalty-club -- a world entered the cycle with no written admission
g.SetNodeProperty("loyalty-club", "admitted-by", "a notebook entry, and one exit written")
? g.RulesAreSound()
#--> 1
```

L'idée d'un club de fidélité arrive, et le cycle n'est plus sain ! Le tribunal répond `UNSOUND (errors present)`, et nomme la règle et le nœud : `ERROR the-lock @ loyalty-club`. Le cycle redevient sain quand l'idée porte son admission écrite.

**Essayer des paiements sans abonnement.** La règle du projet était de tester sans s'engager. Cela voulait dire le bac à sable gratuit d'un établissement de paiement et les services simulés de la bibliothèque, et aucun abonnement avant une barrière que les notes appellent la barrière de mise en service. Le côté de la bibliothèque est un bac à sable de paiements qui n'est pas complaisant. Il se comporte comme une passerelle : un rejet est une réponse, une panne n'en est pas une, et une capture ne peut pas être faite deux fois. Les montants sont des entiers en unités mineures, donc 4 200 font quarante-deux euros. Que répond-il à un jeton qu'on lui a dit de rejeter, à une panne, et à une seconde capture ? Lancez-le :

```haro
oPay = new stzPaymentsSandbox()
oPay.DeclineTokenQ("tok_chargeback")
? oPay.Authorize(4200, "tok_chargeback")[:status]
#--> declined
oPay.FailNextQ()
? oPay.Authorize(4200, "tok_visa")[:status]
#--> refused
aAuth = oPay.Authorize(4200, "tok_visa")
? aAuth[:status]
#--> authorized
oPay.Capture(aAuth[:id])
? oPay.Capture(aAuth[:id])[:why]
#--> this authorization was already captured
```

Trois lignes imprimées, un rejet, un refus et une raison, et aucune n'est une chaîne vide : `declined`, `refused`, et `this authorization was already captured`.

Et la barrière de production refuse de s'ouvrir tant qu'un faux est encore lié, même pour une personne habilitée. Ici le lien réel est un bac à sable HTTP qui tient la place d'un adaptateur, comme le fait la garde : le registre ne tient que le nom du secret. Que répond la barrière de production quand le propriétaire, habilité, demande la production tant que le faux est encore lié ? Lancez-le :

```haro
oReg = new stzServiceRegistry("shop")
oReg.BindSandbox(:payments, new stzPaymentsSandbox())
oDel = new stzDelivery("shop")
oDel.AddBackend("api", "linux")
oDel.UseServicesQ(oReg)
oDel.NeedsServiceInQ("api", [ :payments ])
oDel.DeployTo(StzDeploymentSiteQ("host1"), "api")
oDel.SetActor( HumanActor("owner") )
? oDel.Deploy(:Production).WasCommitted()
#--> 0
? oDel.Log().EntriesOfLevel(:error)[1][:message]
#--> REFUSED -- the external surface is not production-ready
? oDel.WhyServicesNotReady()
#--> sandbox-in-production: still bound to a SANDBOX in a production phase -- a fake must never ship
oDel.ServicesQ().BindLiveQ(:payments, new stzHttpSandbox(), "payments_key")
? oDel.ServicesAreProductionReady()
#--> 1
```

Le propriétaire est habilité, et il est refusé ! Rien n'est validé, et le journal dit pourquoi : `REFUSED -- the external surface is not production-ready` ; la raison dessous est la règle : `a fake must never ship`. Elle s'ouvre quand le lien est déclaré réel : la barrière lit la nature du lien, bac à sable ou réel, et non la classe derrière lui, et c'est pourquoi un bac à sable HTTP lié comme réel l'ouvre ici.

**La constellation.** Quand il a renversé l'ordre du travail, l'architecture du projet a été redessinée en une constellation de cinq mondes sur un socle commun. Les mondes sont le téléphone du client, l'écran de la cuisine, l'atelier du commerçant, la gestion, qui est la première application gardée et mise en sommeil, et la console de l'éditeur. Le socle commun est l'identité, le catalogue, les commandes, les paiements et la flotte. Dans la bibliothèque, le dernier monde dans l'ordre du travail peut être mis en sommeil, et il est réveillé quand son tour vient. Que répond un appel à travers un lien tant que le monde visé dort, et une fois qu'il est réveillé ? Lancez-le :

```haro
oCon = new stzSuperApp("neighbourhood")
oCon.AddWorld("customer", StzAppQ("customer"))
oCon.AddWorld("kitchen", StzAppQ("kitchen"))
oCon.AddWorld("supplier", StzAppQ("supplier"))
oCon.Bond("customer", "kitchen", "send-order")
oCon.Bond("kitchen", "supplier", "order-produce")
oCon.GovDeclareRisk("send-order", 1)
oCon.GovDeclareRisk("order-produce", 2)
oCon.GovGrant("customer", "send-order")
oCon.GovGrant("kitchen", "order-produce")
oCon.GovSetAuthority("customer", :Delegated)
oCon.GovSetAuthority("kitchen", :Delegated)
oCon.Retire("supplier")
? oCon.CallAcross("customer", "kitchen", "send-order")
#--> 1
? oCon.CallAcross("kitchen", "supplier", "order-produce")
#--> 0
? oCon.Why()
#--> target world 'supplier' is not active.
oCon.Revive("supplier")
? oCon.CallAcross("kitchen", "supplier", "order-produce")
#--> 1
```

L'appel à travers le lien passe. L'appel vers le monde en sommeil est refusé ! La raison tient en une ligne : `target world 'supplier' is not active.` Réveillé, il passe.

**Le budget de vitesse.** La première priorité du propriétaire était la vitesse, donc la vitesse devait être une promesse jugée par quelque chose, pas une aspiration. Je tiens cela pour une vue, non pour un résultat. Le budget a trois nombres : le temps du premier affichage, le temps de réaction à un appui, et le temps pour qu'une commande arrive en cuisine. La bibliothèque les déclare à côté du code comme des attentes et les juge contre ce qui a été mesuré. Un dépassement fait échouer la même barrière qu'un constat de sécurité. Il a resserré les seuils lui-même, dans son second cadrage, et je n'en imprime aucun. Le nom du moniteur, les bornes et les échantillons de ce bloc sont les miens, pour montrer la forme ; ce ne sont pas le budget du projet. À quoi ressemble un dépassement ? Lancez-le :

```haro
oMon = StzPerfMonitor("remote-control")
oMon.NewTimer("first.display.ms").Record(900)
oMon.NewTimer("tap.ms").Record(40)
oMon.NewTimer("order.to.kitchen.ms").Record(1800)
oSla = StzSla("speed-budget")
oSla.ExpectP95("first.display.ms").Under(1200)
oSla.ExpectP95("tap.ms").Under(80)
oSla.ExpectP95("order.to.kitchen.ms").Under(2500)
oSla.CheckAgainst(oMon)
oSla.Show()
#--> SLA speed-budget -- 3 expectation(s), last check: MET.
#      [MET] p95-first.display.ms-under-1200: measured 900 (must be <= 1200)
#      [MET] p95-tap.ms-under-80: measured 40 (must be <= 80)
#      [MET] p95-order.to.kitchen.ms-under-2500: measured 1800 (must be <= 2500)
oMon.MetricQ("order.to.kitchen.ms").Record(3100)
oSla.CheckAgainst(oMon)
oRep = new stzRuleReport("cycle-gate")
oRep.Ingest(oSla.Findings())
? oRep.IsSound()
#--> 0
? oSla.Findings()[1][:message]
#--> p95-order.to.kitchen.ms-under-2500: measured 3100 (must be <= 2500)
```

Le premier contrôle imprime `3 expectation(s), last check: MET.` Puis une commande prend 3 100 millisecondes, et la barrière n'est plus saine ! Le constat le dit dans les mots du budget : `p95-order.to.kitchen.ms-under-2500: measured 3100 (must be <= 2500)`.

La bibliothèque porte-t-elle ce que le projet a appris des interfaces ? Non. Le fichier de règles d'interface du projet est de l'expérience en quelques lignes, quinze règles sous une seule directive que le projet appelle le test des trois secondes, qu'un restaurateur n'a pas le temps de regarder plusieurs secondes un écran encombré : une action claire par écran ; annuler plutôt que confirmer ; un bouton refusé est désactivé à la vue, jamais caché. Et un test : une première journée simulée sur une base vide a trouvé le trou le plus grave, qu'aucun fournisseur ne pouvait être créé en production. Ces règles ont été forgées, au compte du projet lui-même, par onze itérations et une campagne de vingt-deux tests simulés avec dix-sept corrections. La bibliothèque n'en porte aucune comme contrôle. Donc, selon la règle de ce chapitre, elles sont la leçon du projet et non celle de la bibliothèque, et je les raconte ici sans bloc.

Six refus suivent, chacun avec sa raison.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé le grand système d'un seul bloc.** Après deux ans de spécification riche, le projet a failli s'arrêter. L'estimation de 2025 reste la référence pour le périmètre du projet ; elle ne doit jamais être présentée comme le calendrier d'aujourd'hui. Ce qui l'a remplacée est la doctrine de ce chapitre : livrer petit, vite et utile.

**J'ai refusé de jeter la première application.** Quand le propriétaire a renversé l'ordre, l'application déjà construite a été gardée, en sommeil, jusqu'à ce que la première version du nouvel ordre soit en production. Les mots du projet lui-même : rien n'est jeté.

**J'ai refusé la dérive silencieuse.** Le Verrou existe parce qu'un projet qui a échoué une fois dérive sans que personne ne l'ait décidé. Un second changement de cap avant que la première version tourne en production est refusé, et une idée qui entre dans le cycle sans sortie écrite l'est aussi.

**J'ai refusé le faux complaisant.** Un double qui répond en silence par une chaîne vide produit un test qui passe pour la mauvaise raison. Le bac à sable décline quand une passerelle décline, refuse quand une passerelle est en panne, et refuse une seconde capture. Et j'ai refusé un tarif fixe avant la barrière de mise en service : aucun abonnement à un établissement de paiement avant l'accord écrit du propriétaire.

**J'ai refusé de prêter au propriétaire ce qu'une simulation avait dit.** Le projet porte une règle depuis juillet 2026, selon laquelle aucune action de ses écrans ne prend plus de deux gestes. Le site l'imprime comme une part du premier avenant, et les documents du projet la portent comme une contrainte du propriétaire. Sa plus ancienne source est une ligne du fichier de réponses simulées du 3 juillet, écrite par moi et une session. Le projet se l'est donnée à lui-même, à partir de sa propre simulation de ses réponses, et l'a gardée. Je la raconte ainsi. Ce qu'il a dit, lui, et que je tiens pour sien, c'est la priorité de la vitesse.

**J'ai refusé de dire que la bibliothèque était née de son besoin.** Voici les dates. La conception de la constellation, le plan de virtualisation, le registre, le port des paiements et le jugement de performance ont tous été commités pour la première fois après le renversement du 4 juillet. Le plan est daté du 23 juillet, et l'étude de performance du 29 juillet. Le site dit avec soin que le projet avait besoin de ces choses et que la bibliothèque les porte. Je n'en dirai pas plus. Le dossier ne dit pas ce qui est venu en premier, son besoin ou les parties : il montre le projet les trouvant dans la bibliothèque, et je laisse l'ordre ouvert.

Cinq gardes se tiennent derrière les cinq blocs ci-dessus.

## 5. Le tribunal

`06_stzsuperapp_narrated` prouve la constellation : des mondes qui se joignent, un appel entre mondes qui exige que les deux soient actifs, un lien et une gouvernance déclarés, et un monde retiré qui rompt ses liens puis se réveille. `service_delivery_narrated` prouve qu'un déploiement en production par un acteur habilité est refusé tant qu'un faux est lié, chaque raison étant consignée, et qu'il s'ouvre une fois le lien réel. `payments_port_narrated` prouve la machine à états du bac à sable : capturer une fois, capturer seulement un débit autorisé, ne pas rembourser plus que ce qui a été capturé. Un rejet est une réponse et une panne n'en est pas une. `judgment_narrated` prouve une attente déclarée dans le vocabulaire opérationnel et jugée contre des nombres mesurés, un dépassement comme un constat qui fait échouer la barrière. Une attente sur un nombre que personne ne mesure y est une erreur, et jamais un passage silencieux. `graphrule_object_narrated` prouve la règle comme un objet attaché à un modèle, avec les opérateurs qu'utilise la construction du Verrou.

Le tribunal prouve ce que la bibliothèque fait ; il ne dit pas où le terrain fait mieux.

## 6. Le terrain, et où il mène

Le terrain mène en stockage, en requêtes et en écosystème. L'étude propre de la bibliothèque sur le terrain de la performance, écrite contre les outils du début de 2026, le dit sans l'adoucir. Pas de base de données de séries temporelles, pas de langage de requête pour elle, pas de tableaux de bord, par conception ; l'export à la place. Parmi les cinq propriétés qu'elle revendique contre eux, celle que ce chapitre utilise est la première : rien sur le terrain ne couple un budget au propre système de règles du code.

Le terrain mène dans le navigateur. Les mondes du restaurant tournent dans les navigateurs des clients et de la cuisine, et je n'ai rien trouvé dans la bibliothèque qui y mesure un premier affichage ou un appui. Le moniteur de la bibliothèque observe un serveur, et le SLA juge les nombres qu'on enregistre dans un chronomètre. Le protocole de mesure du propriétaire est au soixante-quinzième percentile sur un téléphone de milieu de gamme. Les termes de la bibliothèque ne peuvent pas le déclarer exactement : ils offrent le cinquantième, le quatre-vingt-quinzième et le quatre-vingt-dix-neuvième.

Le terrain mène sur les services réels. Un double n'est pas le service, et le plan le dit : il faut encore au moins une exécution réelle avant la production, et les réponses enregistrées dérivent. Les vrais fournisseurs mènent dans les cas limites que le bac à sable ne modélise pas.

Et les hôtes de super-applications mènent en base installée. La conception nomme ce que la super-application de l'industrie possède, une boutique, une revue, un pont natif, et le remplace ; elle ne revendique pas d'utilisateurs.

Je dis maintenant où le chapitre s'arrête.

## 7. La limite

Ce qui est construit : la constellation de mondes avec ses liens et ses passages gouvernés par des normes, le retrait, le réveil, l'échange à chaud et l'imbrication ; le bac à sable des paiements et la barrière de production. Le budget de vitesse déclaré et jugé ; les règles de graphe qu'utilise la construction du Verrou.

Ce qui est conçu : le Verrou comme règle de la bibliothèque, dont le dossier n'a aucun code ; l'idiome proche du naturel de la constellation, avec les verbes que la conception nomme et que la classe n'a pas.

Ce qui est absent : l'adaptateur de paiement réel du restaurant, que la charte de la bibliothèque appelle une tâche ultérieure et la décision du propriétaire. Une mesure du budget sur un vrai réseau mobile, que le tableau de bord du projet du 23 août a reportée au cycle suivant. Les règles d'interface, dont la règle des deux gestes, comme contrôles, une attente au soixante-quinzième percentile et la mesure du temps côté navigateur, dont aucun document de la bibliothèque ne porte la conception. Et l'état de la plateforme après le 25 août 2026, où le dossier s'arrête. Rien n'y dit que la première version soit arrivée en production au restaurant, ait passé la barrière de mise en service, ou ait pris une vraie commande d'un vrai client. Le dossier est muet sur ce qui s'est passé après le 25 août 2026, et je le dis. Des seuils de vitesse resserrés du propriétaire, je n'en imprime aucun, et dis seulement qu'un tel budget existe.

Et ce qui tourne aujourd'hui est ordinaire. Les mondes sont des fichiers HTML uniques, un par monde, avec un cadriciel embarqué, sans étape de construction et sans réseau de contenu. Le serveur est un programme Node de quelques centaines de lignes. Il utilise cinq modules propres à Node, sert les mondes sur le réseau local, et ne garde qu'une chose : un journal, chaîné par des empreintes, rejoué au redémarrage. La première application de gestion a une enveloppe de téléphone autour d'une vue web. Rien de tout cela ne tourne sur le moteur Softanza. La bibliothèque est la référence de conception du projet. La constellation est, selon les mots du site, une conception que la bibliothèque sait exécuter. Le restaurant, non.

Six portes suivent, une pour chaque lecteur.

## 8. Six portes

**Le programmeur.** Vous déclarez des mondes et des liens et vous exécutez une constellation où un appel vers un monde qui n'est pas encore actif est refusé avec sa raison. Le code du restaurant, lui, est une application web.

**L'analyste.** La rigueur dans les nombres était le contrat de la première application : une échéance calculée à partir de la date de facture, une date obligatoire, une dette sans échéance rendue visible.

**Le concepteur.** Quinze règles d'interface à partir d'une seule directive, le test des trois secondes ; et un bouton refusé est désactivé et visible, jamais caché. Sur qui tenait le téléphone dans les onze itérations, les fichiers du projet disent les deux, l'utilisateur réel et moi, et le chapitre ne tranche pas.

**Le décideur.** Le propriétaire a accepté le Verrou par écrit, a resserré lui-même le budget de vitesse, et a gardé la barrière sur les tarifs fixes. Le miroir de la bibliothèque est un déploiement qu'une personne habilitée peut valider et qui est quand même refusé tant qu'il porte un faux.

**Le formateur.** Le dossier ne soutient qu'une petite chose : la première application enseignait son utilisateur en faisant, avec des guides dont les mots ne laissent aucun doute. Il n'y a pas de formateur dans cette histoire, et je le dis.

**L'agent.** Un agent d'IA peut conduire un déploiement en production sans rien changer : la barrière laisse passer les services, rien n'est validé, et la raison donnée est l'acteur et non les services. Dans le projet, l'agent d'IA est la session qui travaille à mes côtés sous le Verrou, avec une personne qui décide.

## 9. Exercice

Déclarez votre propre Verrou pour un cycle. Puis écrivez les mondes du cycle où vous êtes, trois d'entre eux, comme le ferait un restaurant : le téléphone du client, l'écran de la cuisine, et un de plus, chacun avec la raison écrite de sa présence. Ajoutez-en un quatrième, l'idée que vous avez eue ce matin. Lancez le tribunal. Changez la déclaration, pas le tribunal, jusqu'à ce qu'il dise que le cycle est sain.

```haro exercise
? YourGraph.RulesAreSound()
#--> 1
```

Le tribunal vous dira la circonstance et la règle. Il n'écrira pas la déclaration. Si vous voulez une épreuve plus dure, ajoutez une règle sur les actions de votre cycle, et trouvez l'action qui coûte un troisième geste.

Je vous laisse celui-ci, volontairement. Le protocole de vitesse du propriétaire est au soixante-quinzième percentile, et le budget de la section 3 est jugé au quatre-vingt-quinzième. Prenez ce bloc, changez le percentile d'une attente pour un autre que la bibliothèque offre, gardez toutes les autres lignes, et lancez-le. Lisez ce que le tribunal juge contre ce qu'il a demandé. La section 6 dit ce que les termes de la bibliothèque offrent, et la section 7 range son attente parmi les choses absentes. Je ne vous donne ni le verdict ni la réponse.

Quand vous l'aurez résolu, vous saurez pourquoi une promesse que le tribunal sait juger n'est pas encore la promesse que le propriétaire a demandée.

Le chapitre 29 est une banque à Niamey, où une organisation est jugée par son propre organigramme, selon les règles d'un régulateur, par un programme qui lit l'organigramme comme une donnée. L'organigramme dit ce qui est, la règle dit ce qui doit être, et le verdict nomme la règle et le lieu.
