---
id: what-the-projects-did-not-prove
part: 6
number: 31
title: Ce que les projets n'ont pas prouvé
spine: false
narrations: [stz-built-on-real-world-need.md, stz-service-virtualization-code-first-subscribe-later.md, stz-getting-paid-and-paying-narration.md, stz-system-dev-to-deploy-narration.md]
site: [customers, forged, platforms, estate]
guards: [service_registry_narrated, full_scope_model_narrated, payments_live_adapter_narrated, sound_mu5_narrated, deployment_narrated, orgrule_narrated, 14_bceao_governance, governance_narrated]
stage:
  built: "les trois leçons que la bibliothèque porte, chacune avec une garde (un faux ne part jamais ; un organigramme jugé selon les règles d'un régulateur ; l'autorité face au risque, avec sa filiation) ; des refus qui montrent une absence au lieu de la cacher"
  designed: "la fiche de garanties en cinq lignes ; un runtime qui est celui du langage lui-même et fait tourner la bibliothèque ; la machine déclarée sur une carte"
  absent: "toute plateforme client sur le moteur ; les déclarations des clients écrites comme celles de Softanza elle-même, en fichiers ; un mot de la banque ; l'usage du restaurant après le 25 août 2026 ; le hub de l'organisation ; un mécanisme hors ligne dans la bibliothèque ; une exécution réelle des paiements contre le bac à sable de la banque centrale ; le verdict d'une personne nommée sur tout cela"
status: draft
rulings: ["12.5", "12.10", "12.13", "12.21", "12.22", "12.29", "12.30"]
research: research/ch31.md
---

Dans ce chapitre, je dis, projet par projet, ce que les trois projets des chapitres 28 à 30 n'ont pas prouvé. Je commence par les trois habitudes du terrain pour dire ce qu'un travail a prouvé. Puis je lance cinq petits blocs où la bibliothèque montre une absence en refusant, et je dresse les tableaux : pour chaque projet, l'affirmation, le document ou le fichier qui la prouve, et ce qui est absent. Je dis ce que j'ai refusé, la mémoire de l'auteur comme preuve d'abord, et je donne le tribunal, le terrain et la limite dans les mots d'étape. Le principe est la phrase propre du chapitre : un projet prouve exactement ce qu'un document, un fichier, une exécution et une personne nommée atteignent, et la page dit où ils s'arrêtent.

## 1. Le concept, tel que le terrain le tient

Le terrain a trois habitudes pour dire ce qu'un travail a prouvé.

La première est la référence : un logo sur une page d'accueil, une histoire de client de deux pages, la phrase « ils nous font confiance ». Elle prouve que quelqu'un a payé ou signé. Elle ne dit pas ce qu'il a fait tourner, pendant combien de temps, ni ce qu'il en a dit.

La deuxième est l'échelle de maturité. Les niveaux de maturité technologique de la NASA, devenus ensuite une norme internationale, nomment la distance qu'une technologie a parcourue du laboratoire jusqu'au lieu pour lequel elle a été construite. Le plus haut niveau est un système éprouvé en exploitation. C'est un vocabulaire d'étape, et ce livre en utilise un qui lui est propre (construit, conçu, absent).

La troisième est la section des limites. Une étude empirique doit énoncer les menaces à sa validité. Un modèle d'apprentissage automatique est livré avec une fiche dont la dernière partie est ses réserves. Un artefact soumis à une conférence de recherche reçoit un badge selon ce que quelqu'un d'autre en a fait. C'est la forme la plus proche de ce chapitre, et celle qu'on saute le plus souvent quand le lecteur est un acheteur.

Ce que les trois ont en commun, c'est que l'affirmation et sa preuve voyagent séparément. Une page dit « utilisé par », et la preuve est une confiance accordée à la page. (Connaissance générale, pas une étude du dossier.)

## 2. Le premier principe

Le dossier donne deux phrases, et elles n'en font qu'une. Le site dit : « Rien n'est une référence tant qu'un document ne le prouve pas. » Et, de ce dont l'auteur se souvient : ce qu'« aucun fichier ne prouve n'est pas listé ».

**Un projet prouve exactement ce qu'un document, un fichier, une exécution et une personne nommée atteignent, et la page dit où ils s'arrêtent.** C'est la phrase propre du chapitre, tirée des deux phrases du site ; les mots du site sont les deux cités plus haut, de sa page des clients et de sa page forgée.

## 3. La forme Softanza

Ce chapitre est l'autre moitié des chapitres 28 à 30. Ceux-là disaient ce que trois projets ont appris à la bibliothèque. Celui-ci dit, projet par projet, ce qu'ils n'ont pas prouvé. Je ne l'ai pas écrit après coup, par modestie. La page forgée du site porte une section avec le même titre.

La forme de la réponse est un tableau de trois colonnes pour chaque projet : l'affirmation, le document ou le fichier qui la prouve, et ce qui est absent. Je laisse une cellule vide quand je ne peux pas nommer ce qui la remplit. Et je ne remplirai pas la troisième colonne de mémoire.

Avant les tableaux, cinq petits blocs. Chacun est un lieu où la bibliothèque montre une absence en refusant, au lieu de passer en silence. Ils sont la phrase du chapitre, écrite comme du code.

**Une dépendance déclarée et jamais liée est une erreur.** La surface d'une solution est déclarée avant que rien ne soit lié. Un service déclaré que rien ne soutient est compté comme un constat, pas comme un passage, et le demander lève une erreur là où est la faute. C'est la première chose non prouvée que la leçon du restaurant ne peut pas cacher : aucun vrai service de paiement n'est lié nulle part dans le dossier. Que répond le registre quand on lui demande le service de paiement et que rien ne le soutient ? Lancez-le :

```haro
oReg = new stzServiceRegistry("shop")
oReg.DeclareMany([ :mail, :payments ])
? @@( oReg.UnboundServices() )
#--> [ "mail", "payments" ]
? oReg.Findings()[1][:invariant]
#--> unbound-service
? oReg.IsSound()
#--> 0
try
	oReg.Service(:payments)
catch
	? cCatchError
done
#--> stzServiceRegistry(shop): nothing is bound for service 'payments'. Bind it (or BindLive it) before use.
```

Deux services déclarés, aucun lié, et le registre le dit lui-même : `nothing is bound for service 'payments'` !

**Ce qu'une répétition peut affirmer, et ce que seule la cible peut affirmer.** Le modèle de plateforme donne trois verdicts pour la même opération. *Refusé* : la cible l'interdit. *Natif* : l'hôte lui-même peut le faire. *Répété* : la cible le permet et l'hôte ne l'a pas, de sorte que l'exécution ne prouve que le plan. Lire une broche sur une machine de développement est répété, pas natif. Le mot dépend de la machine sur laquelle ce livre a été exécuté : un PC Windows n'a pas une telle broche, et une carte qui en a une imprimerait `native` pour la même ligne.

```haro
oSol = new stzPlatformProfile("kiosk")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oSol.WithApp(:firmware, :ESP32)
oFw = oSol.App(:firmware).System()
? oFw.ReadPin(4)
#--> rehearsed
try
	oFw.Spawn("worker")
catch
	? cCatchError
done
#--> scope 'esp32' (espidf) forbids 'process' -- spawn 'worker'. This target has no such capability.
oFw.Show()
#--> Scope: esp32 (espidf)
#      [rehearsed] read pin 4
```

Le commentaire de la bibliothèque, dans la classe qui abaisse une répétition en artefact réel, dit que la dernière étape, flasher une carte, « remains a PLANNED external action ».

**L'adaptateur de paiement réel existe, et refuse de deviner.** Le code du système de paiement réel existe. Il n'a jamais été exécuté contre le bac à sable de la banque centrale. Sans identifiants, il refuse avant tout appel réseau et dit ce qui manque. Que dit-il quand on lui demande des comptes et qu'il n'a aucun identifiant ? L'hôte de ce bloc n'existe pas, et rien ne l'atteint :

```haro
oAd = new stzPispiHttpAdapter()
oAd.WithParticipant("shop")
oAd.WithBaseUrl("https://pispi.example")
oAd.AsLive()
? oAd.IsSandbox()
#--> 0
try
	oAd.Request("GET", "/comptes", [], [])
catch
	? cCatchError
done
#--> stzPispiHttpAdapter: no credentials. Give it the store and an actor: WithSecretsFrom(oStore, oActor).
? oAd.TokensFetched()
#--> 0
```

L'adaptateur répond `no credentials`, nomme ce qui comblerait le manque, `WithSecretsFrom(oStore, oActor)`, et `TokensFetched()` reste à `0`.

La bibliothèque a un script qui tente l'exécution réelle. Je l'ai lancé une fois, sans aucune de ses variables définie, pour ce chapitre. Il a imprimé le mot UNPERCEIVED, nommé les quatre variables qui manquent, et dit que rien de l'adaptateur réel n'est perçu tant qu'une personne nommée n'a pas vu un paiement arriver. Il s'est terminé sans échec. L'exécution a été reportée, par moi, pour une raison qui n'est pas celle de la bibliothèque : elle exige l'implication de l'organisation. Une exécution qui n'a pas pu avoir lieu est rapportée comme non perçue. Elle n'est rapportée ni comme un passage ni comme un échec.

**Une fonction qui attend une personne nommée.** Dans le volet du son, la bibliothèque tient comme donnée le verdict d'une personne sur une chose que seule une personne peut juger. Tant que le verdict est UNPERCEIVED, le verbe qui revendiquerait le résultat refuse et dit pourquoi. Là où une personne a dit oui, le verdict porte la date et ses mots :

```haro
oVoice = StzSoundFormantVoiceQ()
oVoice.Sing("la la la", "c4 e4 g4")
? oVoice.Refusals()
#--> 1
? oVoice.LastError()
#--> Sing is not available YET: the formant voice has not been heard by the author (sound_mu5_demo.ring plays it). SAPI was measured and does not hold a pitch (measured 2026-09-26: +-6 st asked, +-2.5 st given, up to 407 cents off, 286-575 cents of wander within a syllable -- it speaks, it cannot hold a note). Until the author calls the formant voice singing, Vowel and VowelsQ are what this voice honestly does
aVerdicts = StzSoundSingingVerdict()
? aVerdicts[:formant][:verdict]
#--> UNPERCEIVED
? aVerdicts[:retuned][:verdict]
#--> SINGING
? aVerdicts[:retuned][:date]
#--> 2026-09-27
? aVerdicts[:retuned][:said]
#--> the retuned voice is somehow singing, open Sing()
```

Le verdict de la voix réaccordée se lit `SINGING`, avec la date `2026-09-27` et les mots `the retuned voice is somehow singing, open Sing()`. C'est la forme de la ligne dont le chapitre 33 dit que les exécutions des clients ne l'ont pas encore : une date, une personne, et une phrase. Le dossier porte aussi le nom de la personne à côté, et je ne l'imprime pas ici. (SAPI est l'interface vocale du système d'exploitation.)

**Un contrôle préalable qui dit « faisable » sans toucher un hôte.** Le contrôle préalable du déploiement refuse un hôte trop petit. Pour un hôte dont le fournisseur est un cloud, il dit faisable et « provision on aws », sans aucun compte. Une faisabilité est un plan, pas une vérification. Le fichier de conception le dit clairement : ce qui reste est la vérification contre un vrai hôte ou compte, barrée par l'infrastructure. Les chiffres ci-dessous sont illustratifs. Que répond le contrôle préalable à un hôte trop petit, et à un fournisseur cloud sans aucun compte ? Lancez le bloc :

```haro
oBrain = new stzDelivery("shop")
oBrain.AddBackend(:api, :LinuxServer)
oBrain.RequiresIn(:api, StzResourcesQ().SetMemoryQ(2048).SetComputeQ(2).SetStorageQ(20))
oSmall = new stzDeploymentSite("tiny")
oSmall.SetKindQ(:Server).SetCapacityQ(StzResourcesQ().SetMemoryQ(512).SetComputeQ(1).SetStorageQ(5))
oTiny = new stzDeployment(oBrain)
oTiny.SetTarget(:api, oSmall)
? oTiny.Feasible()
#--> 0
? oTiny.Feasibility()[1][5]
#--> SHORTFALL -- host too small
oCloud = new stzDeploymentSite("pool")
oCloud.SetKindQ(:Server).SetProviderQ(:aws)
oPool = new stzDeployment(oBrain)
oPool.SetTarget(:api, oCloud)
? oPool.Feasible()
#--> 1
? oPool.Feasibility()[1][5]
#--> provision on aws
```

Voici maintenant les tableaux. Chaque cellule vient du dossier, lu le 8 octobre 2026. Un compte de lignes ou une date de fichier que j'ai lus moi-même sont étiquetés comme miens.

### Le restaurant à Lyon

| Affirmation | Preuve | Ce qui est absent |
|---|---|---|
| La plateforme existe, et sa première livraison a été faite | le site : un avenant clos le 4 août 2026 ; le commit « iteration 1 » du projet du 15 août ; un serveur de 565 lignes que j'ai lu ; le dernier commit, 25 août 2026, 13 h 07 | tout ce qui suit le 25 août : la production, une vraie commande, la barrière de mise en service prévue. Le dossier est muet |
| Le restaurant la fait tourner | une journée de mesures de terrain avec deux téléphones, le 19 août | une phrase qui dise qu'elle tourne. Le chapitre 1 écrit « tourne » |
| Aucune croissance du périmètre pendant un cycle (le Verrou, chapitre 28) | le pacte et le carnet du Verrou : des documents privés | le Verrou comme code. Le chapitre 28 montre ce que la bibliothèque donne de plus proche |
| On peut essayer des paiements sans abonnement, et un faux ne part jamais | le registre et la barrière de production, avec leurs gardes | l'adaptateur de paiement réel pour le restaurant : « a later desk » dans le propre fichier de conception de la bibliothèque. Aucun vrai service n'est lié en réel |
| La constellation de mondes | la carte des mondes du restaurant ; la classe de super-application de la bibliothèque, avec une garde | le restaurant sur la constellation : ses mondes sont des pages web en fichier unique, et la carte dit qu'elle est une carte, pas une réalisation |
| Un budget de vitesse est une promesse | l'objet de niveau de service de la bibliothèque, avec une garde | une mesure sur un vrai réseau 4G : la liste de suivi du projet la reporte au cycle suivant |
| Les règles d'interface ont été forgées avec le propriétaire, le téléphone en main | le fichier du projet dit onze itérations avec l'utilisateur réel | qui tenait le téléphone. L'étude (12.29) confond deux faits |

### La banque à Niamey

| Affirmation | Preuve | Ce qui est absent |
|---|---|---|
| La banque fait tourner le produit d'évaluation de l'auteur | le guide d'installation remis à la banque ; un fichier de licence | un mot de la banque : qui déclare l'organigramme, depuis combien de temps, combien de personnes l'utilisent. Et aucune date de livraison : les fichiers portent des horodatages du système de fichiers, qui ne sont pas des dates |
| Le produit est « construit avec Softanza » | l'auteur a construit les deux | le produit n'appelle pas la bibliothèque. C'est une application Python avec un petit serveur web ; j'ai cherché dans son code, et je n'y ai trouvé aucun contrôle régional ou de Bâle et aucun appel à la bibliothèque |
| Les règles du régulateur jugent l'organigramme | le validateur de trois règles de la bibliothèque et celui de la séparation des tâches, avec leurs gardes | les validateurs à l'intérieur du produit ; un article du texte de la banque centrale pour les trois codes de règle ; un constat lu par un auditeur |
| Un fichier de règles pour la banque | un fichier de deux règles régionales qui se charge | il ne juge rien : sur un organigramme sans conseil, il rapporte sain |
| Les règles d'interface du produit viennent de la banque | les règles 117 à 121 de la constitution de l'interface | la ligne de preuve de la règle 117 dans la constitution dit « A banking supervision product (April 2026) » et ne nomme aucune banque. L'étude les attache à cette banque |

### L'organisation sur le terrain

| Affirmation | Preuve | Ce qui est absent |
|---|---|---|
| L'organisation a choisi mon offre | l'offre du 5 août 2026 a été retenue ; l'étude de conception du 8 octobre 2026 | le hub de l'organisation : rien de lui n'est en production, et la version 1.2 de l'étude est soumise à validation. Et qui a choisi : le dossier est muet |
| Les règles sont des données qu'une personne change sans programmeur | les clauses de règles de la bibliothèque et le gouverneur qui nomme une règle morte | une forme texte pour les règles à clauses ; un historique des versions avec retour en arrière, que l'étude promet ; la notation de règles de l'étude n'est pas celle de la bibliothèque |
| Un agent prépare, une personne décide, avec l'autorité du moment | l'objet de gouvernance et sa filiation, avec leurs gardes | une personne liée à un compte connecté ; un hub où le faire |
| Hors ligne par défaut | le mot de l'étude selon lequel la boîte d'envoi côté navigateur est déjà en service | dans la bibliothèque : ni file, ni boîte d'envoi, ni synchronisation. Le site l'appelle « un manque, pas une leçon apprise ». Le dernier bloc du chapitre 30 en est le tout |

### Sur les trois

| Affirmation | Preuve | Ce qui est absent |
|---|---|---|
| Les plateformes tournent aujourd'hui sur des piles ordinaires | la page propre du site : des mondes web en fichier unique et un petit serveur Node ; une application Python ; le hub de l'organisation non construit | aucune plateforme ne tourne sur le moteur. Le site le dit, et chaque dépôt que j'ai ouvert est d'accord |
| Leurs déclarations « sont en cours d'écriture comme celles de Softanza » | la page des plateformes et la page forgée, comme intention | j'ai cherché, le 8 octobre 2026, et je ne les ai pas trouvées comme fichier : dans le dépôt du restaurant, aucun fichier de code ne déclare une application, une constellation ou une plateforme ; dans la livraison de la banque, aucun ; dans le dossier d'étude de l'organisation, aucun (son annexe utilise une notation qui n'est pas celle de la bibliothèque). Le dossier montre l'intention et les cartes, pas encore les déclarations |
| Un changement de moteur, pas de plan | le principe : la réécriture a été refusée | le déplacement lui-même ; qui se déplace en premier ; qui le perçoit |
| Une solution écrit sa fiche de garanties en cinq lignes | la vision la demande | aucune solution n'en a une ; aucune classe, fixture ou garde de la bibliothèque n'a la fiche |
| Le runtime en dessous est celui du langage lui-même | la charte ratifiée le 1er octobre 2026 ; ses étapes passent sur ses propres fixtures | Haro ne fait pas tourner la bibliothèque. Une note de session du 5 octobre 2026 rapporte que le runtime de pont passe chaque assertion que l'ancien runtime passe sur la bibliothèque, mais que tous les programmes ne s'accordent pas sur chaque ligne stable ; le passage sous Linux est l'étape suivante. Je n'imprime aucun pourcentage. Les blocs de ce livre s'exécutent sur l'ancien runtime, 1.27 |
| Un hôte réel vérifie un déploiement | la conception du déploiement | la vérification est barrée par l'infrastructure. Les sites locaux tournent pour de vrai ; le transfert distant est « a later slice » |
| Le volet des paiements fonctionne contre le bac à sable de la banque centrale | le jumeau, servi par HTTP, avec une garde | l'exécution du bac à sable : non perçue, reportée. La production ne vient jamais de ce volet |
| Une personne nommée a dit ce qu'elle a vu | un tambour, et la voix réaccordée, dans un autre volet | aucune des trois plateformes |

### Ce que l'étude du dossier n'a pas mesuré

L'étude comparative qui a lu le dossier dit, dans ses propres paragraphes intitulés « Non mesuré », ce qu'elle ne pouvait pas soutenir. Elle n'a pas exécuté ce qu'elle a lu : son évaluation de clôture du dossier dit « Rien n'en a été exécuté ». Elle n'a pas mesuré si le runtime de Haro fait tourner la bibliothèque. Elle n'a pas vérifié si deux mesures de vitesse publiées tiennent encore aujourd'hui, et les deux ont été faites sur l'ancien runtime. Certaines gardes du dossier système ont pris leurs totaux dans des documents de conception, et l'un de ces documents dit encore quarante-cinq là où sa garde en tient maintenant davantage. Les quarante et une images de la première partie de la galerie ont été jugées par un modèle, et aucune personne ne les a regardées. Le budget de vitesse du restaurant n'a aucune vraie mesure 4G. L'étude s'applique à elle-même sa propre loi de la perception, et c'est pourquoi je fais confiance au paragraphe.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé la mémoire de l'auteur comme preuve.** Le site ne liste rien dont je me souvienne et qu'aucun fichier ne prouve. La même règle liait la banque : je connais le produit, parce que je l'ai construit, et ce que les gens de la banque en ont fait n'est dans aucun fichier.

**J'ai refusé d'appeler la bibliothèque l'origine de ce qu'elle n'utilise que comme exemple.** La page forgée dit « exemple » là où la bibliothèque tient un projet comme son exemple et non comme son origine. Et je ne répéterai pas une phrase de l'étude du 12.29 qui dit qu'une leçon est « née du besoin du client ». Le registre et le SLA ont été commités pour la première fois après le renversement du 4 juillet, selon le journal de la bibliothèque tel que le lit le chapitre 28. L'ordre des commits rend « née de » non prouvé. Ce que je peux dire, c'est « avait besoin » et « porte ».

**J'ai refusé deux formulations de moi.** Aux chapitres 1, 2 et 33, j'ai écrit que la banque « fait tourner » un produit « construit avec » Softanza, et que le restaurant « fait tourner » une plateforme. Le dossier montre une application Python qui n'appelle pas la bibliothèque, construite à côté d'elle par la même personne, et pour le restaurant une première livraison et une journée de terrain, puis le silence après le 25 août. La formulation honnête est *construit par moi, sous la discipline que la bibliothèque porte désormais*, et *livré et éprouvé sur le terrain*. Les chapitres 2 et 33 portent désormais ces formulations. Le chapitre 1 garde la sienne, et ce paragraphe est l'endroit où se tient la formulation plus exacte du dossier.

**J'ai refusé un mot d'étape que le dépôt ne porte pas.** La page du domaine de projets du site le dit : ne jamais appeler disponible avant que ce ne soit. Un travail qui atteint une personne par un sens est perçu par une personne, et jusque-là il est non perçu, ce qui est un état et non un échec.

**J'ai refusé d'imprimer un pourcentage.** J'ai dit à voix haute jusqu'où le runtime de pont est arrivé. L'étude a jugé que le chiffre ne devait pas être imprimé sans la garde qui le produit. Je suis d'accord.

## 5. Le tribunal

`service_registry_narrated` prouve qu'un service déclaré que personne ne soutient est un constat d'erreur, qu'un service non lié lève une erreur, et qu'un bac à sable en production est une violation. `full_scope_model_narrated`, scènes 5 à 8, prouve les trois verdicts : refusé, répété, natif. `payments_live_adapter_narrated` prouve l'adaptateur contre un jumeau servi par HTTP, un adaptateur sans identifiants qui refuse de deviner, et le scénario qui dit que l'étape (b) est non perçue. Elle démarre de vrais processus serveur, et le livre ne l'exécute pas ; il ne fait que compter ses assertions. `sound_mu5_narrated` prouve, dans sa cinquième scène, que tant que le verdict est non perçu `Sing` ne retourne rien et dit pourquoi. `deployment_narrated` prouve qu'un hôte sous-dimensionné n'est pas faisable, et qu'un assistant répète et ne valide rien ; elle écrit un dossier temporaire à côté d'elle, donc le livre ne l'exécute pas non plus. `orgrule_narrated` prouve les règles universelles de l'organigramme et la séparation des tâches. `14_bceao_governance`, une assertion, exécute les règles régionales sur un organigramme sans conseil et sans fonction de gestion des risques. `governance_narrated` prouve l'autorité face au risque, avec sa filiation.

Le tribunal du sujet de ce chapitre n'est pas une garde. C'est une ligne du dossier, de la forme que prescrit la loi du domaine de projets : une date, une personne, et ce qu'elle a dit. La bibliothèque tient une telle ligne dans ses données, dans le volet du son. Le domaine de projets en tient une dans son dossier, et le chapitre 33 la raconte.

## 6. Le terrain, et où il mène

Le terrain mène en production. Des piles ordinaires font tourner de vraies charges pour de vrais utilisateurs, y compris, selon la page propre du site, les trois plateformes de cette partie.

Le terrain mène en références à grande échelle. Le site imprime deux références et une étude de conception, et ne cite aucun nombre de pays et aucun nombre de programmeurs. Un acheteur qui lit un mur de logos en voit davantage.

Le terrain mène en infrastructure réelle. Les outils de provisionnement pilotent de vrais fournisseurs chaque jour. Le déploiement de la bibliothèque s'arrête avant un vrai hôte, et le cinquième bloc montre où.

Le terrain mène en matériel sur le terrain. La machine déclarée démarre et se juge elle-même dans un émulateur, et la vision dit qu'aucun client ne tourne dessus. Son texte de garanties dit quatre promises sur quatre, trois tenues dans l'émulateur ; la quatrième, survivre à une coupure, n'est pas tenue dans ce texte, qui ne porte aucune décision d'emplacement. La vision dit qu'elle attend le chien de garde sur la carte, et la carte est commandée.

Le terrain mène en vitesse. Le runtime contre lequel Softanza s'est mesurée était plus rapide sur chaque ligne, d'un facteur entre un et deux, et les deux mesures ont été faites sur l'ancien runtime.

Le terrain mène en images jugées par des personnes. Quarante et une images et sections de texte de la première partie de la galerie ont été jugées par un modèle : vingt justes, neuf fausses, douze incertaines. Le dossier dit qu'aucun humain ne les a regardées.

Là où je pense que le dossier se distingue, c'est que sa limite est une section d'une page, avec un titre. Chaque étape a un mot. Une fonction peut être construite et refuser encore jusqu'à ce qu'une personne nommée ait parlé. Et une exécution réelle qui n'a pas pu avoir lieu est rapportée non perçue, jamais comme un échec et jamais comme un passage.

## 7. La limite

Ce chapitre tout entier est une limite. En voici la somme dans les mots d'étape.

Ce qui est construit : les trois leçons qui sont prouvées. *Un faux ne part jamais* : le registre et la barrière de production. *Une organisation est jugée par son propre organigramme selon les règles d'un régulateur* : l'organigramme et ses validateurs. *L'autorité n'est pas la permission, et une décision garde son autorité du moment* : l'objet de gouvernance. Chacune a un fichier de la bibliothèque qui la porte, une garde qui se résout, et un bloc déjà gardé dans un chapitre voisin. La limite de chacune est dans les tableaux. Un bac à sable est lié et aucun adaptateur de paiement réel ne l'est ; le produit de la banque n'appelle pas le validateur d'organigramme. Le hub de l'organisation n'est pas construit, et le hors ligne est un manque.

Ce qui est conçu : la fiche de garanties en cinq lignes ; le runtime qui est celui du langage lui-même, faisant tourner la bibliothèque ; la machine déclarée sur une carte.

Ce qui est absent : toute plateforme client sur le moteur ; les déclarations des clients écrites comme celles de Softanza elle-même, en fichiers ; un mot de la banque ; l'usage du restaurant après le 25 août ; le hub de l'organisation ; un mécanisme hors ligne dans la bibliothèque ; une exécution réelle des paiements contre le bac à sable de la banque centrale ; le verdict d'une personne nommée sur tout cela.

La somme de toutes les cellules absentes est la ligne unique dont le chapitre 33 dit qu'elle reste due : *la solution a tourné sur le moteur propre de Softanza, et voici ce que l'utilisateur a dit.* Les déclarations des clients sont absentes. Le site dit qu'elles sont en cours d'écriture comme celles de Softanza elle-même. Le 8 octobre 2026, j'ai cherché un fichier de ces déclarations dans le dépôt du restaurant, dans la livraison de la banque et dans le dossier d'étude de l'organisation, et je n'en ai trouvé aucun. Le 9 octobre 2026, j'ai cherché de nouveau, en lecture seule, dans treize dépôts voisins de la bibliothèque. Ce sont celui du restaurant, le dépôt web du produit de la banque avec ses copies plus anciennes, celui de l'organisation, le dépôt central, celui du moteur, celui du site, et quatre autres projets du domaine de projets. J'ai cherché dans leur texte les classes propres de la bibliothèque pour une plateforme, un organigramme et une constellation, et, dans les noms de fichiers de cinq d'entre eux, des fichiers de déclaration. Les résultats sont les notes et les mémos de la bibliothèque, les données du site et, dans les copies plus anciennes du dépôt web du produit de la banque, une classe JavaScript d'organigramme qui est le code propre de cette application. Aucun fichier ne déclare la plateforme d'un client comme celle de Softanza elle-même ; le mot du chapitre pour ces déclarations est donc *absent*, et la ligne d'étape en tête le dit.

## 8. Six portes

**Le programmeur.** Votre démonstration est une répétition jusqu'à ce qu'une cible l'ait exécutée. Demandez à la portée si la ligne était native, répétée ou refusée, et écrivez le même mot à côté de vos propres affirmations.

**L'analyste.** Quand vous citez un projet, écrivez trois colonnes : l'affirmation, le document, et ce qui est absent. Ne remplissez pas la troisième de mémoire.

**Le concepteur.** Une fonction qu'aucune personne n'a vue ni entendue part fermée, et le dit. L'étape est un état de la conception et non une excuse.

**Le décideur.** Lisez le mot d'étape avant le témoignage. « Construit » est une affirmation sur une garde. « Tourne chez un client » est une affirmation sur un document, et vous pouvez le demander par écrit, avec un nom à côté.

**Le formateur.** Enseignez la différence entre un projet qui a instruit la bibliothèque et un projet qui tourne dessus. Le premier est prouvé ici, et le second est la ligne qui reste due. Non perçu est un état, pas un échec.

**L'agent.** Vous pouvez lire les tableaux et citer n'importe quelle cellule. Vous ne pouvez pas transformer une cellule absente en cellule présente. Si vous le faites, le prochain lecteur du dossier trouvera votre phrase et le fichier manquant côte à côte.

## 9. Exercice

Déclarez la surface d'un de vos projets : un service de courrier, un service de paiements, et un de plus de votre choix. Avant de lancer quoi que ce soit, écrivez la ligne que vous attendez sous chacune de trois questions : quels services sont non liés ; si le registre est sain ; quels services sont non liés une fois qu'un bac à sable est lié au service de courrier.

```haro exercise
oReg = new stzServiceRegistry("my-project")
oReg.DeclareMany([ :mail, :payments, :your_service ])
? @@( oReg.UnboundServices() )
#--> what you expect
? oReg.IsSound()
#--> what you expect
oReg.Bind(:mail, new stzMailSandbox())
? @@( oReg.UnboundServices() )
#--> what you expect
```

Puis, sur papier, faites le tableau de trois colonnes pour le projet que vous connaissez le mieux. Laissez vide ce que vous ne pouvez pas nommer. Sur la dernière ligne, écrivez qui l'a perçu, à quelle date, et ce qu'il a dit, ou le mot « non perçu » et pourquoi.

L'exercice n'a pas de réponse à vérifier d'abord. La question que pose le tuteur est : quelle cellule avez-vous remplie de mémoire ?

Le chapitre 32 se tourne vers la manière dont beaucoup d'esprits ont travaillé sur ce seul ouvrage, et vers la règle qu'ils gardent. Chaque loi cite l'incident qui l'a gagnée, et une loi nouvelle sans un échec daté derrière elle est une préférence.
