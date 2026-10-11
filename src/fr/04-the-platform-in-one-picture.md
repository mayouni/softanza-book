---
id: the-platform-in-one-picture
part: 1
number: 4
title: La plateforme en une image
spine: true
narrations: [stzApp-building-your-first-app-narration.md, stz-system-dev-to-deploy-narration.md, stz-emulating-the-whole-solution-narration.md, stz-vs-qt-unicode-narration.md]
site: [architecture, platform, platforms, areas]
guards: [00_stzapp_narrated, 06_stzsuperapp_narrated, full_scope_model_narrated, 01_platform_narrated, threat_model_narrated]
stage:
  built: "le moteur et ses bibliothèques ; la couche base ; les mondes, les constellations et les plateformes avec leurs gardes ; le sous-ensemble du moteur qu'une partie livre, pour le web"
  designed: "la couche max chargée par son fichier d'entrée ; la couche base s'appuyant sur la couche noyau ; un chargeur pour un seul domaine de la base ; un tribunal qui vérifie les couches contre leur contrat"
  absent: "un programme entier et son moteur emballés dans un seul fichier ; une plateforme cliente sur le moteur"
status: draft
rulings: ["12.2", "12.10", "12.12", "12.13", "12.15", "12.23", "12.29"]
research: research/ch04.md
---

Dans ce chapitre, je dessine toute la plateforme en une image, lue de bas en haut : le moteur, les couches, les zones, les mondes, les artisans du logiciel, et à côté de chaque étage son tribunal. Je la parcours étage par étage, avec à chaque étage un bloc que vous pouvez exécuter. Puis je dis ce que j'ai refusé en chemin : le calcul dans les faces, un drapeau pour choisir une couche, les mini-applications. L'image se résume en une seule idée à chaque altitude : rien n'est cru, tout est jugé.

## 1. Le concept, tel que le terrain le tient

Le terrain dessine une plateforme comme une pile de boîtes. Le noyau en bas, un runtime et ses bibliothèques au milieu, les applications au-dessus, et parfois une colonne sur le côté pour la sécurité ou les outils. À l'intérieur d'une même base de code, la même image devient une règle sur les dépendances : une couche interne ne sait rien des couches externes, et les flèches ne pointent que vers l'intérieur. Les trois crates standard de Rust, une pour le métal nu, une pour la mémoire, une pour un système d'exploitation complet, en sont la version la plus nette que je connaisse. Trois profondeurs du même langage, choisies par ce que la cible offre.

Pour les applications, l'image du terrain est un hôte. Une grande application embarque un runtime et fait tourner de petites applications à l'intérieur, qui partagent ses services et son magasin. Dans les deux images, le juge est à l'extérieur : une suite de tests à côté du code, une revue à côté du magasin. Dans les images que je connais, aucune ne dessine le tribunal comme une colonne debout à chaque étage.

## 2. Le premier principe

La pile de la plateforme se résume, dans la vision que j'ai ratifiée, en une seule idée à chaque altitude : **rien n'est cru, tout est jugé.**

## 3. La forme Softanza

Voici toute la plateforme en une image, lue de bas en haut. Chaque étage repose sur celui qui est dessous, et chaque étage est jugé par un tribunal à côté de lui. Les chiffres qu'elle porte ne sont pas tapés par moi : le build les lit, la nuit où cette page est faite, dans la bibliothèque et dans la carte des zones du site.

{{fig:platform-one-picture|La plateforme en une image. Chaque étage repose sur celui qui est dessous ; chacun est jugé par le tribunal à côté de lui ; l'architecte travaille à travers tous. Les chiffres sont lus au build dans le moteur de la bibliothèque, dans son arbre de tests et dans l'Atlas du site.}}

Parcourons-la, étage par étage, avec à chaque étage un bloc que vous pouvez exécuter.

**Le moteur.** En bas se trouve un moteur écrit en Zig : un ensemble de bibliothèques derrière une interface C, une par domaine, regroupées par la couche qui les charge. Selon la règle de conception du moteur, le moteur fait le calcul ; la bibliothèque au-dessus lui donne un vocabulaire. Un petit exemple rend la division visible. Demandez au langage sous-jacent à Softanza la longueur du mot arabe pour la paix, puis demandez-la au moteur. Que compte chacun ? Exécutez-le :

```haro
? len("سلام")
#--> 8
? Q("سلام").NumberOfChars()
#--> 4
? Q("مرحبا بالعالم").Script()
#--> arabic
```

Le langage compte des octets et répond `8`. Le moteur compte des lettres et répond `4`, et il connaît l'écriture : `arabic`. Quatre lettres, pas huit !

Le moteur a aussi sa propre porte, sous chaque classe. Les nombres trop grands pour l'arithmétique de la machine sont additionnés exactement, par le moteur lui-même :

```haro
a = StzEngineBigIntFromString("99999999999999999999999999999999")
? StzEngineBigIntToString( StzEngineBigIntAdd(a, StzEngineBigIntFromString("1")) )
#--> 100000000000000000000000000000000
```

**Les couches.** Au-dessus du moteur, la bibliothèque est découpée en trois couches, selon la profondeur de capacité. Le noyau, avec le préfixe `stk`, est léger et parle directement au moteur, pour les petits appareils et les petits binaires. La base, `stz`, est la couche riche, où vivent le vocabulaire et ses formes, assez pour la plupart des solutions. Le max, `stx`, est destiné aux innovations les plus fortes. Une couche se choisit par le fichier qu'un programme charge, et le même verbe veut dire le même acte au noyau et à la base :

```haro
o1 = new stkList([ "one", "and", "one", "makes", "two", "ones" ])
? o1.FindFirst("one")
#--> 1
o2 = new stzList([ "one", "and", "one", "makes", "two", "ones" ])
? o2.FindFirst("one")
#--> 1
```

**Les zones.** À travers les couches, la bibliothèque est cartographiée par l'Atlas du site en zones regroupées en bandes, et chaque zone en voies. Chaque voie est notée d'émergente à forte, la plupart avec la ligne qui le prouve. L'Atlas dit ce qui existe, et à quel point c'est bien. La règle de conception du moteur est qu'un verbe veut dire le même acte sur toute structure qui l'admet. Ici elle tient pour une paire, une chaîne et une liste : sur une chaîne, il répond des positions de caractères ; sur une liste, des positions d'éléments :

```haro
? @@( Q("tea rice tea").FindAll("tea") )
#--> [ 1, 10 ]
? @@( Q([ "tea", "rice", "tea" ]).FindAll("tea") )
#--> [ 1, 3 ]
```

**Les mondes.** Au-dessus de la bibliothèque, l'unité n'est pas un module mais un monde : une application est un monde vivant de sens, avec ses choses, ses relations et ses règles. Un monde se déclare, et il peut s'expliquer lui-même :

```haro
oApp = new stzApp("FieldVisits")
oApp {
    AddThingQ(:Account) { Has([ :number, :chapter, :balance ])  IsTrue(:balance, "@ >= 0") }
    AddThingQ(:Client)  { Has([ :code, :name, :city ])  Owns(:Account) }
    AddRelation(:Account, :belongsTo, :Client)
}
oApp.Explain()
#--> WORLD FieldVisits   lives in: memory (not persisted)
#      BEING
#        account (number, chapter, balance)
#            true when balance @ >= 0
#        client (code, name, city)
#      RELATIONS
#        client owns account
#        account belongsto client
oApp.Live()
#--> [FieldVisits] is live -- 2 thing(s), 0 flow(s), 0 reaction(s), 0 goal(s); 0 proposal(s)
```

Les mondes se composent en constellation. Ici un restaurant et son fournisseur de produits sont deux mondes, et un lien entre eux déclare l'unique traversée permise. Que devient une traversée qu'aucun lien ne déclare ? Exécutez-le :

```haro
oResto = StzAppQ("resto")
oResto.AddThingQ(:dish) { Has([ :name, :price ]) }
oSupplier = StzAppQ("supplier")
oSupplier.AddThingQ(:crate) { Has([ :produce, :qty ]) }
oCon = new stzSuperApp("acme-group")
oCon.AddWorld("resto", oResto)
oCon.AddWorld("supplier", oSupplier)
oCon.Bond("resto", "supplier", "order-produce")
oCon.GovDeclareRisk("order-produce", 2)
oCon.GovGrant("resto", "order-produce")
oCon.GovSetAuthority("resto", :Delegated)
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 1
? oCon.CallAcross("resto", "supplier", "raid-kitchen")
#--> 0
? oCon.Why()
#--> no bond declares 'raid-kitchen' from 'resto' to 'supplier'.
```

La traversée déclarée répond `1`. L'autre répond `0`, et la constellation donne sa raison en une ligne : `no bond declares 'raid-kitchen' from 'resto' to 'supplier'.` Toute autre traversée est refusée avec sa raison.

Le socle commun est le sol partagé d'une constellation, ce sur quoi chacun de ses mondes se tient. Il tient une identité, une session et un magasin. C'est un monde comme les autres, le monde zéro, et non un genre particulier de nœud. Le chapitre 23 le montre et dit où le code reste en deçà.

Et une plateforme est l'enveloppe autour d'une solution : ses parties, les systèmes sur lesquels elles tournent, et l'ordre dans lequel elle est construite, répétée et déployée. Vous la verrez refuser de déployer avant d'être construite au chapitre 33. Voici ce qu'elle fait des couches, pour le web : une partie d'une solution ne livre que les groupes du moteur dont elle a besoin, et seulement ceux qui appartiennent à Softanza. Le téléphone ci-dessous demande quatre capacités. Combien de groupes du moteur livre-t-il ? Exécutez-le :

```haro
oDelivery = new stzDelivery("my-shop")
oDelivery.AddSuperApp(:phone, :Android)
oDelivery.AddBackend(:api, :LinuxServer)
oDelivery.NeedsIn(:phone, [ :Unicode, :PivotTable, :ConstraintSolver, :Regex ])
oPlan = oDelivery.Plan()
? @@( oPlan.EngineCapsFor(:phone) )
#--> [ "pivottable", "constraintsolver" ]
? @@( StzWasmGroupsFor( oPlan.EngineCapsFor(:phone) ) )
#--> [ "aggregation", "solver" ]
```

Deux : `aggregation` et `solver`. Le système propre du téléphone gère l'une des deux autres, Unicode, et Softanza livre l'autre, Regex, comme une construction dans le langage propre de la cible.

**Les artisans du logiciel.** En haut se trouvent les six portes du chapitre 2 : le programmeur, l'analyste, le concepteur, le décideur, le formateur et l'agent. Et une personne travaille à travers chaque étage, du moteur à l'organisation : l'architecte de plateforme. Le dossier nomme cette personne en trois endroits sans lien entre eux, et aucun autre rôle ne traverse toutes les bandes de l'Atlas.

**Le tribunal.** À côté de chaque étage se tient son juge. Le moteur a ses tests et les contrats entre les étages. Les couches ont les gardes narrées. La plupart des voies des zones portent une ligne de preuve. Les mondes ont leurs liens et leurs normes, l'ordre de construction et de déploiement, et le refus d'un faux en production. Les interfaces des artisans du logiciel ont une constitution de verbes et de règles à laquelle chaque élément doit remonter. Et au-dessus de tout cela, le modèle de menaces de la plateforme énumère ses garanties, chacune liée à la garde qui la prouve. Sa propre garde échoue quand une ligne nomme une garde qui n'existe plus.

Les parties II à IV de ce livre sont des repensées, et chacune est une boîte de cette image. La partie V assemble l'image en usage.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé le calcul dans les faces.** Le moteur est le produit. Le langage au-dessus ajoute de la beauté, pas du calcul : des milliers de méthodes qui se lisent comme des phrases, et les algorithmes en dessous, en un seul endroit. La règle est que chaque fonctionnalité est implémentée une fois, dans le moteur. La migration n'est pas terminée, et le contrat des couches liste le nombre, la liste, l'objet, le graphe, les statistiques et le naturel comme encore en Ring.

**J'ai retiré l'ancien framework, sans repli.** La bibliothèque reposait sur un grand framework C++ pour son texte, ses dates et ses fichiers. Quand le moteur l'a remplacé, tous les chemins passant par le framework ont été retirés : pas de repli, pas de drapeau de fonctionnalité gardé au cas où.

**J'ai choisi la souveraineté comme un verdict sur chaque dépendance, non comme « chaque ligne est à nous ».** Le moteur embarque et épingle un ensemble de bibliothèques tierces, la figure les compte. Le dossier définit le mot en une ligne : rien que quelqu'un d'autre puisse retirer. C'est le test. Une bibliothèque dont la source est épinglée dans l'arbre le passe.

**J'ai refusé un drapeau pour choisir une couche.** La première manière de choisir une couche était un drapeau. Elle ne pouvait jamais fonctionner, parce que le langage sous-jacent charge à la compilation tous les fichiers qu'il voit, si bien que les trois couches se chargeaient à chaque appel. L'échec de l'une était l'échec de toutes. Le drapeau a été retiré plutôt que gardé comme un interrupteur qui ne fait rien en silence. La raison a été écrite là où le prochain lecteur se tiendra : une couche se choisit par le fichier que l'on charge.

**J'ai laissé tout aller dans la base, et je le dis.** Sous la pression du temps, les domaines ont atterri dans la base pendant que le moteur, les volets comme la sécurité et la performance, et les clients avançaient. C'était le choix agile, et il n'est défendable que tant que la dette est visible. Alors la figure dessine la base au plus large, et le chapitre 27 raconte la dette avec ses chiffres.

**J'ai refusé les mini-applications.** La super-application du terrain est un hôte qui fait tourner de petites applications. Celle de Softanza est un graphe gouverné de mondes : des mondes, pas des mini-applications ; des liens et des normes, pas un conteneur.

## 5. Le tribunal

`00_stzapp_narrated` prouve qu'un monde est déclaré et rendu visible. `06_stzsuperapp_narrated` prouve la constellation : des mondes qui se joignent, le socle commun comme monde zéro, des traversées barrées par des normes avec le lien nommé comme raison, un monde retiré qui rompt ses liens. `full_scope_model_narrated`, le terrain d'entente de l'architecte, prouve la solution modélisée d'abord, les portées qui refusent ce qu'une cible interdit, et l'ordre de construction et de déploiement. `01_platform_narrated` prouve les devoirs de la plateforme. `threat_model_narrated` lit le modèle de menaces de la plateforme et échoue quand une garantie nomme une garde qui n'existe plus.

## 6. Le terrain, et où il mène

Les trois profondeurs de Rust sont imposées par son compilateur et employées chaque jour sur le métal nu. La règle de Softanza est tenue au moteur et aux fichiers d'entrée, et rompue là où la base devrait s'appuyer sur le noyau, comme le montre la section 7.

Les bibliothèques de texte du terrain mènent sur la locale : la propre carte de Softanza dit que l'écart net de ses chaînes est la couche de locale des composants internationaux. Sa zone de locale est un pari délibéré contre ces composants : sans collation, sans règles de pluriel et sans fuseaux horaires.

Les hôtes de super-applications du terrain servent de vrais utilisateurs à une échelle que cette plateforme n'a jamais rencontrée. Le dossier les nomme comme le modèle qu'il a refusé et ne mesure rien contre eux, alors je n'en mesurerai pas non plus.

Et l'Atlas lui-même imprime où Softanza est faible : la zone binaire est un plan sans code livré, le volet de l'extensibilité (greffons, interface de fonctions étrangères, embarqué) est surtout prévu, la zone du système a peu de voies fortes. Une carte qui imprime ses zones faibles est la seule sorte qui vaille la peine d'être lue.

## 7. La limite

Ce qui est construit : le moteur et ses bibliothèques, la couche base, les mondes, les constellations et les plateformes avec leurs gardes, et, pour le web, le sous-ensemble du moteur qu'une partie livre.

Ce qui est conçu, ou construit et inaccessible. Les propres classes de la couche max sont écrites et chargées par aucun fichier d'entrée. Que répond le runtime quand vous en demandez une ? Exécutez-le :

```haro
try
	o3 = new stxString("one and one")
catch
	? cCatchError
done
#--> Error (R11) : Error in class name, class not found: stxstring
```

Le runtime répond : `Error in class name, class not found: stxstring`. La classe est écrite, et aucun fichier d'entrée ne la charge.

Le contrat des couches dit que la couche base s'appuie sur le noyau, par héritage ou par délégation. Elle ne fait ni l'un ni l'autre pour les domaines communs : les deux partagent le moteur et implémentent deux fois ces domaines. La couche noyau elle-même est cassée contre le moteur aujourd'hui : ses classes de chaîne et de caractère appellent des noms du moteur qu'aucun fichier du moteur n'enregistre, comme le rapporte l'étude du site sur les racines du livre. Le bloc de la section 3 ne montre que des listes. Un chargeur qui amène un domaine de la base sans les autres n'est pas construit. Un tribunal qui lit le contrat des couches contre l'arbre et échoue en cas de dérive est une spécification, proposée dans cette étude du site. Ce qui est construit, ce sont deux implémentations qui partagent un moteur ; la ligne du contrat selon laquelle la base s'appuie sur le noyau est conçue.

Ce qui est absent : un programme entier et son moteur emballés dans un seul fichier sans aucune dépendance, et une plateforme cliente qui tourne sur le moteur.

## 8. Six portes

**Le programmeur.** Vous choisissez votre profondeur par le fichier que vous chargez, et un verbe veut dire le même acte sur une chaîne et sur une liste.

**L'analyste.** L'Atlas vous dit, voie par voie, où la plateforme est forte et où elle émerge. Construisez sur les voies fortes.

**Le concepteur.** Votre interface a un tribunal à elle, les verbes et les règles de la constitution, dans la même colonne que les gardes du code.

**Le décideur.** Posez deux questions à chaque étage : qu'y a-t-il dessous, et qui le juge. La réponse du moteur à la première est une liste écrite de bibliothèques épinglées.

**Le formateur.** L'image est la carte du livre. Chaque repensée des parties II à IV est une boîte de cette image.

**L'agent.** L'image existe comme des données que vous pouvez lire, l'Atlas comme un fichier, et chaque étage où vous écrivez a un tribunal qui vous lira.

## 9. Exercice

Dessinez votre propre solution comme ce chapitre dessine Softanza : des étages, et un tribunal à côté de chacun. Pour chaque boîte, écrivez le fichier qui la déclare et la garde qui la juge, et mettez dessus un mot d'étape : construit, conçu ou absent.

Puis déclarez-en deux parties avec `stzPlatformProfile`, et avant d'exécuter quoi que ce soit, écrivez la ligne que vous attendez quand vous lui demandez de déployer avant de construire. Exécutez-le. Une boîte sans tribunal à côté est votre première trouvaille.

Le chapitre suivant quitte l'image pour le code écrit à l'intérieur d'elle, et énonce la première loi : le code adhère à la façon dont une personne pense, et le tribunal le juge quel que soit celui qui l'a écrit. Son principe tient en une phrase : ce que vous pensez est ce que vous écrivez.
