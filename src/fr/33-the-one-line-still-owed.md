---
id: the-one-line-still-owed
part: 7
number: 33
title: La ligne qui reste due
spine: true
narrations: [stz-built-on-real-world-need.md, stz-system-dev-to-deploy-narration.md, stz-emulating-the-whole-solution-narration.md, stz-service-virtualization-code-first-subscribe-later.md]
site: [customers, forged, platforms, estate]
guards: [full_scope_model_narrated, virtual_system_twin_narrated, service_delivery_narrated]
stage:
  built: "une plateforme déclarée construite, puis déployée, et refusée dans l'autre ordre ; le jumeau qui ne touche rien de réel ; la dernière porte qui refuse un faux service"
  designed: "le runtime propre à la langue, qui fait tourner la bibliothèque ; la fiche de garanties d'une solution en cinq lignes ; des hôtes réels et une vraie carte"
  absent: "une solution de client qui tourne sur le moteur Softanza, et le verdict d'une personne nommée à son sujet ; les déclarations des clients en fichiers"
status: draft
rulings: ["12.5", "12.10", "12.13", "12.21", "12.29", "12.30"]
research: research/ch33.md
---

## 1. Le concept, tel que le terrain le tient

Dans notre industrie, une plateforme est prouvée quand quelqu'un d'autre la fait tourner pour de bon. La page d'accueil montre les logos des entreprises qui l'utilisent ; une étude de cas en raconte une en deux pages. Une équipe qui croit à son propre produit l'utilise pour son propre travail, et un compilateur sérieux se compile lui-même. Les ingénieurs qui ont besoin d'une échelle en ont une : les niveaux de maturité technologique de la NASA, devenus plus tard une norme, où le niveau le plus haut est un système éprouvé à l'endroit pour lequel il a été construit.

Ce sont des épreuves raisonnables, et elles pointent toutes vers la même chose : la production. Ce qu'elles ne demandent pas, c'est qui l'a vu fonctionner, et ce que cette personne a dit.

## 2. Le premier principe

**Le dossier ne porte une solution que lorsqu'elle a tourné sur son propre moteur et qu'une personne nommée a dit ce qu'elle a vu.**

## 3. La forme Softanza

Ceci est le dernier chapitre, et il parle de quelque chose qui n'a pas eu lieu. Laissez-moi d'abord vous montrer le plancher sur lequel cela se tiendra, car le plancher existe.

Une solution est déclarée avant d'être construite, et la plateforme qui la porte refuse d'être déployée avant d'être construite :

```haro
oSol = new stzPlatformProfile("bank")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oPlatform = StzPlatformQ("bank")
oPlatform.SetProfile(oSol)
try
	oPlatform.Deploy()
catch
	? cCatchError
done
#--> stzPlatform.Deploy: the platform must be Build() before it can be deployed.
? oPlatform.IsDeployed()
#--> 0
oPlatform.Build()
oPlatform.Deploy()
? oPlatform.IsDeployed()
#--> 1
```

Avant que quoi que ce soit soit réel, la solution peut tourner sur un jumeau, une copie du système qui ne garde aucune référence à la réalité. Ici un fichier est écrit dans le jumeau, relu, et n'est nulle part sur le disque :

```haro
oTwin = new stzVirtualFileSystem()
oTwin.CreateFile("orders/today.txt", "3 couscous")
? oTwin.ContentOf("orders/today.txt")
#--> 3 couscous
? oTwin.OriginOf("orders/today.txt")
#--> virtual
? StzEngineFileExists("orders/today.txt")
#--> 0
```

Et à la dernière porte, une solution ne peut pas atteindre la production avec un faux service lié en elle, quel que soit celui qui le demande. Au chapitre 1 vous avez vu le registre refuser ; ici c'est la livraison elle-même qui refuse, avec une personne habilitée aux commandes :

```haro
oReg = new stzServiceRegistry("shop")
oReg.BindSandbox(:payments, new stzPaymentsSandbox())
oDel = new stzDelivery("shop")
oDel.AddBackend("api", "linux")
oDel.UseServicesQ(oReg)
oDel.DeployTo(StzDeploymentSiteQ("host1"), "api")
oDel.SetActor(HumanActor("dana"))
oDep = oDel.Deploy(:Production)
? oDep.WasCommitted()
#--> 0
? oDel.Log().EntriesOfLevel(:error)[2][:message]
#--> sandbox-in-production @ shop/payments
```

La personne avait le droit de déployer. Le déploiement ne s'est pourtant pas exécuté, parce qu'un service de paiement qui est un bac à sable ne peut pas être ce par quoi un vrai client paie. Ce n'est pas une question d'autorité. C'est une question de ce qui est vrai.

Le plancher est donc là : déclarer, construire, répéter, refuser le faux, valider par un acteur gouverné. Maintenant l'absence.

Softanza a été utilisée. Je l'ai écrit au chapitre 1 et je m'y tiens, parce que l'étude qui a lu le dossier la première fois a écrit le contraire, qu'aucun utilisateur hors de mes propres projets n'avait été mesuré, et je l'ai corrigée. Une banque de Niamey a un produit d'évaluation d'organisation que j'ai construit à côté de la bibliothèque, installé sur son propre réseau sous licence, et le guide d'installation remis à la banque l'atteste. Un restaurant de Lyon a reçu la livraison d'une première version d'une plateforme de commerce de quartier et l'a éprouvée sur le terrain ; le dossier de ce projet s'arrête au 25 août 2026, avec un avenant clos le 4 août et un propriétaire qui a pris part à la première démonstration et mené une journée d'essais sur le terrain avec deux téléphones. Une organisation du Niger a son hub conçu. Le site énumère, projet par projet, la leçon que chacun a enseignée et le fichier de la bibliothèque qui la porte. La partie VI de ce livre raconte leurs histoires.

Et le site dit, dans la même page, sur quoi ces plateformes tournent aujourd'hui : des piles ordinaires. Celle de la banque est une application Python. Celle du restaurant est un ensemble de mondes web, chacun un seul fichier. Le hub de l'organisation n'est pas construit. Le site dit que leurs déclarations sont écrites comme celles de Softanza elle-même, pour que les faire passer sur le moteur Softanza soit un changement de moteur et non de plan. Les mots du site sont exacts : c'est un pas en avant, pas un pas accompli.

La ligne que le dossier ne porte pas encore est donc celle-ci : *la solution a tourné sur le moteur propre de Softanza, et voici ce que l'utilisateur a dit.*

Ce qui sépare d'ici cette ligne, lu dans le dossier et non composé :

1. **Les déclarations d'un client tournent sur le moteur au lieu de la pile ordinaire.** Le site dit que les déclarations sont en cours d'écriture ; je n'en ai trouvé aucun fichier, et le chapitre 31 dit où j'ai cherché ; le passage n'est pas fait.
2. **Le runtime propre à la langue fait tourner la bibliothèque sur le système du client.** Aujourd'hui les blocs de ce livre sont exécutés par le runtime de l'ancien langage hôte, version 1.27, et chaque page le dit sous sa ligne de preuve. Le runtime de pont censé le remplacer a été signalé le 5 octobre 2026 comme passant toutes les assertions que l'ancien runtime passe sur la bibliothèque, sauf une requête HTTP/2 qui a échoué une fois dans la passe ; sur chaque ligne stable, 3 461 des 5 112 programmes concordent avec l'ancien runtime. Son passage sous Linux est la prochaine étape. La charte de Haro a été ratifiée le 1er octobre 2026, et les étapes propres de Haro passent sur ses propres fixtures. Haro ne fait pas encore tourner la bibliothèque.
3. **La solution écrit sa fiche de garanties.** La vision demande à chaque solution cinq lignes, une pour chaque système auquel elle répond, technique, social, écologique, économique et culturel, jugées comme des fixtures, la machine en étant dérivée. Aucune solution n'en a écrit.
4. **Des hôtes réels et une vraie carte.** La vérification du déploiement contre un hôte réel ou un compte réel dépend de l'infrastructure. La machine déclarée démarre et se juge elle-même dans un émulateur ; des quatre promesses que fait son profil hébergé, l'émulateur peut en vérifier trois, et la quatrième attend un chien de garde sur une vraie carte. Aucun client ne fait tourner sur elle une charge de production.
5. **Une personne le perçoit, et le dossier dit qui.** Pas un compteur. Une personne, nommée, avec une date et ce qu'elle a dit.

Le dernier pas est une loi du domaine de projets, et elle a été payée. Le volet sonore de la bibliothèque a un jour tenu des centaines d'assertions réussies alors qu'il était, à mon oreille, cassé. Depuis, un travail qui atteint une personne par un sens doit être perçu par une personne, et le dossier doit dire qui l'a perçu et ce qu'elle a dit. Et quand personne ne l'a fait, la loi le dit simplement : non perçu est un état, pas un échec. Un rapport peut être honnête et rester non perçu.

Le dossier tient déjà la forme de la ligne. Dans un autre plan, le 2 octobre 2026, le dossier dit que le Principal a écouté un son que la bibliothèque avait fait et a dit, dans les mots écrits : « yes it's real drum!! » (les mots sont écrits en anglais dans le dossier) Ce n'est pas une solution, et ce n'est pas un client. Mais c'est une personne, une date et une phrase, et c'est à cela que ressemblera la ligne unique.

Le dossier tient aussi le contraire, honnêtement. Les images que la bibliothèque dessine ont été jugées par un modèle, quarante et une images ou sections de texte, vingt justes, neuf fausses, douze incertaines, et le dossier dit qu'aucun humain ne les a encore regardées. L'exécution en réel du volet des paiements avec le compte de test de l'organisation a été reportée, par moi, et rapportée comme non perçue. Ni l'un ni l'autre n'est un échec. Les deux sont dus.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé qu'on me dise que les projets ne comptaient pas.** La première lecture du dossier a écrit qu'aucun utilisateur hors de mes propres projets n'avait été mesuré. C'était faux, et je l'ai dit : Softanza a été utilisée dans de vrais projets qui, sans être achevés, ont donné le retour qui a façonné sa conception. La lecture a été corrigée dans le dossier, sur place, avec la date. Ce qui l'a remplacée est plus petit et plus honnête : les utilisateurs existent et ont parlé ; ils n'ont pas encore tourné sur le moteur.

**J'ai refusé une référence sans document.** Le site ne compte un projet comme référence que lorsqu'un document le prouve, et il ne cite aucun nombre de pays ni aucun nombre de développeurs. Une leçon n'est listée que lorsqu'un fichier de la bibliothèque la porte.

**J'ai refusé de déplacer une plateforme en la réécrivant.** La plateforme d'un client passe sur le moteur comme un changement de moteur, non de plan. Les déclarations sont à écrire une fois, comme celles de Softanza elle-même, et le moteur en dessous change. Réécrire serait plus rapide à annoncer et plus lent à croire.

**J'ai refusé mon propre chiffre.** J'ai dit à voix haute, en pourcentage, jusqu'où le runtime de pont était arrivé. L'étude qui a lu le dossier a jugé que le chiffre ne devait pas être imprimé sans la garde qui le produit. Le mot d'étape est « en construction », et les lignes mesurées sont la preuve.

**J'ai refusé qu'un instrument tienne lieu de preuve d'une perception.** Une phase dont la preuve est entièrement un compteur n'est pas achevée quand la chose elle-même est quelque chose qu'une personne voit ou entend. Le compteur est un résultat. La personne est le verdict.

## 5. Le tribunal

Le plancher de ce chapitre repose sur trois gardes. `full_scope_model_narrated`, le socle commun de l'architecte, prouve qu'une solution est d'abord modélisée, qu'un déploiement avant une construction est refusé et consigné comme une erreur, et qu'un modèle ne peut pas effectuer le déploiement. `virtual_system_twin_narrated` prouve que la répétition ne touche rien de réel, que le plan se narre lui-même, et que valider est l'unique porte. `service_delivery_narrated` prouve qu'un déploiement en production avec un faux lié ne s'exécute pas du tout, avec chaque raison nommée, et que la barrière s'ouvre une fois le service réel.

Le tribunal du sujet de ce chapitre n'est pas une garde. C'est une ligne du dossier : qui, quand, et ce qu'il a dit. Cette ligne n'existe pas encore.

## 6. Le terrain, et où il mène

Le terrain mène en production. Les piles ordinaires font tourner de vraies charges pour de vrais utilisateurs aujourd'hui, y compris, selon la page même du dossier, l'application Python de la banque ; la première version du restaurant est faite de mondes web d'un seul fichier, et le hub n'est pas construit.

Le terrain mène en infrastructure réelle. Ses outils pilotent de vrais fournisseurs et de vrais hôtes chaque jour ; le déploiement de Softanza ne vérifie contre un hôte réel que lorsque l'infrastructure est là, et répète tout le reste.

Le terrain mène sur le matériel en service. Ses appareils tournent dans des boutiques et des cliniques ; la machine déclarée démarre dans un émulateur, et sa carte n'est pas encore en service.

Le terrain mène en vitesse. Le runtime auquel Softanza s'est mesurée était plus rapide sur chaque ligne, d'un facteur compris entre un et deux, et la note du domaine de projets a consigné la perte.

Là où je pense que le dossier se distingue, c'est dans ce qu'il ne se laisse pas dire. Chaque référence a un document. Chaque étape a un mot. Selon le document de conception, le déploiement émulé fait tourner le même artefact que celui qui est livré. Un faux ne peut pas être livré et un modèle ne peut pas valider. Et une perception est une ligne nommée, datée, citée, ce qu'un logo sur une page d'accueil ne porte pas.

## 7. La limite

Ce chapitre tout entier est une limite, je serai donc bref.

Ce qui est construit : le plancher. Déclarer, construire, déployer dans l'ordre ; répéter sur un jumeau ; refuser un faux à la dernière porte ; valider seulement par un acteur gouverné.

Ce qui est conçu : le runtime propre à la langue, qui fait tourner la bibliothèque ; la fiche de garanties d'une solution en cinq lignes ; la vérification sur des hôtes réels et sur une vraie carte.

Ce qui est absent : une solution de client qui tourne sur le moteur Softanza, le verdict d'une personne nommée à son sujet, et les déclarations des clients en fichiers (le chapitre 31 dit où j'ai cherché). Le dossier ne nomme aucun projet qui passe en premier sur le moteur, ni aucune personne qui le percevra ; je laisse les deux non écrits.

## 8. Six portes

**Le programmeur.** Votre code tourne aujourd'hui par la construction, la répétition et un déploiement gouverné. Ce que vous ne pouvez pas encore affirmer, c'est qu'un client le fait tourner sur le moteur, et le dossier ne vous laissera pas l'affirmer.

**L'analyste.** Demandez deux choses avant de compter un projet comme preuve : un document, et un verdict nommé.

**Le concepteur.** Ce que vous concevez est jugé en dernier par le sens d'une personne. L'opinion d'un modèle sur une image est un résultat ; celle d'une personne est le verdict.

**Le décideur.** Lisez le mot d'étape avant la promesse. Aujourd'hui le plancher est construit, et l'exécution chez un client est absente.

**Le formateur.** Enseignez que non perçu est un état et non un échec. Un rapport honnête peut être livré dessus, s'il le dit.

**L'agent.** Vous pouvez répéter un déploiement et l'expliquer. Vous serez refusé quand vous essaierez de l'effectuer, et le refus sera consigné (le chapitre 24 le montre).

## 9. Exercice

Déclarez une plateforme pour un projet qui est le vôtre, avec un serveur. Avant de lancer quoi que ce soit, écrivez la ligne que vous attendez sous chacune de trois questions : ce qui se passe quand vous lui demandez de déployer avant d'avoir construit ; ce qui se passe quand un assistant demande de déployer après la construction ; ce qui se passe quand une personne le demande.

```haro exercise
oSol = new stzPlatformProfile("my-project")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oP = StzPlatformQ("my-project")
oP.SetProfile(oSol)
# your three questions here, each with the line you expect under it
```

Lancez-le. Puis écrivez une ligne de plus, celle que votre propre projet doit encore, dans la forme du dossier : qui l'a perçu, à quelle date, et ce qu'il a dit. Si personne ne l'a fait, écrivez « non perçu », et dites pourquoi. Cette ligne est la fin de ce livre, et le début du suivant.
