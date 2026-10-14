---
id: the-environment
part: 5
number: 26
title: L'environnement
spine: false
narrations: [stzApp-building-your-first-app-narration.md, stz-emulating-the-whole-solution-narration.md, stz-system-dev-to-deploy-narration.md]
site: [zui]
guards: [gui_stzui_narrated, gui_profile_narrated, gui_tier_agreement_narrated, gui_accessibility_narrated, 05_stzapp_live_narrated, emulator_narrated]
stage:
  built: "l'interface comme texte avec un tribunal qui trouve l'élément ne servant aucun verbe ; deux projections de celle-ci, native et web, avec une table enregistrée des divergences et une page qui peut dire DISAGREE ; l'arbre d'accessibilité émis depuis la déclaration ; une page que le langage sert sur la boucle locale ; un monde qui propose et dont les propositions s'effacent quand on agit dessus ; des écrans déclarés comme intentions ; une surface de navigateur générée"
  designed: "le kit de shells avec deux shells ; le chrome comme genres fermés (colonne, ruban, rail, barre d'état), aucun encore classe de la bibliothèque ; la facette comme donnée ; un rail lié au focus ; des cellules d'état lues dans les tribunaux, avec une garde qui interdit qu'une cellule montre un état que le tribunal n'a pas émis"
  absent: "un IDE de cette famille ; une liste des vingt-deux verbes dans la bibliothèque et un refus d'un verbe inconnu ; une garde qui juge un shell contre les verbes ; un éditeur ; une latence mesurée"
status: draft
rulings: ["12.12", "12.23", "12.24", "12.25"]
research: research/ch26.md
---

Dans ce chapitre, je prends la forme que les environnements du terrain ont fini par prendre, une barre d'outils, une barre latérale, un éditeur et une barre d'état, et je lui oppose un motif en cinq marques. J'exécute les pièces que la bibliothèque a sous ces marques : un shell déclaré comme texte et jugé, deux projections, un ruban dans l'ordre d'une vie, un rail qui propose, une barre d'état qui dit la vérité. Je dis ce que j'ai décidé, porter les deux shells, et ce que j'ai refusé, dont un drapeau qui désactive l'arbre d'accessibilité. Et je dis où cela en est : à ce commit, un IDE de cette famille est absent, et les pièces qui le portent tournent. Le principe tient en une phrase : déclarer l'interface une fois, et chaque shell en est une projection qui peut ajouter des rendus, jamais des verbes.

## 1. Le concept, tel que le terrain le tient

Les environnements du terrain ont fini par prendre une forme. Une barre d'outils et un menu en haut, une barre latérale de fichiers, un éditeur, un terminal en dessous, et une barre d'état en bas. Depuis peu un assistant se tient dans un volet ou un terminal à côté du code, et l'humain approuve ses modifications. (Connaissance générale, signalée.)

Les études de terrain propres du dossier, datées, sont au nombre de trois. Le bloc-notes livré avec l'ancien langage hôte, mesuré le 12 août 2026 à trente-trois fichiers source et environ quatre mille lignes, sept volets ancrables, une configuration de quinze clés et aucun service de langage. Il existe, il est livré dans la boîte, et il fonctionne le jour de l'installation. Les éditeurs rapides, dans la spécification d'ergonomie de mars 2026, qui fixe pour son propre produit : de l'entrée à l'écran en moins de seize millisecondes sur tout matériel moderne, sans exception. Elle veut un chrome minimal, pas de barre d'état encombrée, pas de forêts de barres d'outils. Elle demande un essai à blanc avant un changement structurel, et des inspections qui disent pourquoi et proposent une correction. Et la barre d'état, telle que cette spécification l'écrivait : vingt-quatre pixels de haut, ne portant que l'état essentiel, avec cinq états de construction, dont l'un est *non vérifié*, pour un projet où aucune construction n'a encore tourné. L'état de « pas encore jugé » a son propre mot. Une barre verte par défaut serait le mensonge habituel du terrain. C'est mon point de vue.

Là où le terrain est silencieux, le chapitre répond. Le terrain ordonne ses barres d'outils par les fonctionnalités de l'outil, et non par la vie de la chose qu'on fait. Et il laisse la proposition d'un assistant atterrir comme une modification, l'approbation de l'humain étant une habitude. (Connaissance générale.)

## 2. Le premier principe

**Déclarer l'interface une fois. Chaque shell en est une projection, et une projection peut ajouter des rendus, jamais des verbes.**

L'en-tête de la bibliothèque pour son interface rédigée le dit : le fichier est le contrat, et le balisage natif et la page web en sont les projections. L'étude du dossier (ses sections 12.23 à 12.25) le lit comme une déclaration, deux projections, prouvées d'accord, reposant sur ma décision du 7 octobre 2026 : porter les deux. La phrase compagnon est celle de la constitution de l'interface, sur le site : un nouveau médium ajoute des rendus, jamais des verbes.

## 3. La forme Softanza

D'abord l'étape, avant les blocs. À ce commit, **un IDE de cette famille est absent**. Aucune classe de la bibliothèque n'est encore nommée pour un ruban, un rail, une colonne ou une barre d'état. La ligne d'étape propre de l'étude, proposée pour le site, le dit : aucun IDE de cette famille n'est livré aujourd'hui ; un shell l'est, pour le volet sonore. La fondation qui ferait du suivant une projection est spécifiée et pas encore construite. Ma lecture est d'accord, avec un ajout : la bibliothèque génère une surface de navigateur, celle de l'émulateur, et je la montre plus bas avec une perte.

La bibliothèque a les pièces sous chacune des cinq marques du motif. Les cinq sont un shell, deux projections, un ruban de facettes ordonné par la vie de la solution, un rail qui propose et une barre d'état qui dit la vérité. Elles tournent, et je les prends dans l'ordre.

### Un shell, déclaré comme texte, jugé par un tribunal

Le chrome est déclaré comme texte et jugé avant d'être montré. Le ruban est généré à partir de données, ici une simple liste ; la facette comme objet de bibliothèque est conçue et non construite. Les quatre noms de facettes sont quatre des cinq phases du corpus de conception du dossier : définir, architecturer, construire, gouverner, livrer. J'en ai pris quatre pour garder le bloc court. Chaque déclaration doit porter sa justification, et une déclaration sans elle est refusée. Quel élément ne sert aucun verbe ? Exécutez-le :

```haro
aFacets = [ "Define", "Build", "Govern", "Ship" ]
cTabs = ""
cIds = ""
for cF in aFacets
	cId = "tab_" + lower(cF)
	cIds += cId + ", "
	cTabs += 'DEFINE TEXT ' + cId + ' ( CONTENT "' + cF + '", ROLE tab, SATISFIES select ) RATIONALE "A facet."' + nl
next
cShell = 'DEFINE PANEL shell ( SIZE [640, 360], DIRECTION column, FONT "app", SATISFIES locate, CHILDREN [ribbon, work, status] ) RATIONALE "One shell, three bands."' + nl +
	'DEFINE BOX ribbon ( HEIGHT 32, DIRECTION row, ROLE tablist, SATISFIES discover, CHILDREN [' + cIds + '] ) RATIONALE "Facets, in the order of a life."' + nl + cTabs +
	'DEFINE BOX work ( HEIGHT fill, DIRECTION row, CHILDREN [page, rail] ) RATIONALE "The workspace and its rail."' + nl +
	'DEFINE TEXT page ( CONTENT "the work", SATISFIES read ) RATIONALE "What is being made."' + nl +
	'DEFINE BOX rail ( WIDTH 160, ROLE group, SATISFIES preview, CHILDREN [advice] ) RATIONALE "What the court proposes."' + nl +
	'DEFINE TEXT advice ( CONTENT "no proposal", SATISFIES understand ) RATIONALE "The rail, empty."' + nl +
	'DEFINE BOX status ( HEIGHT 24, ROLE status, SATISFIES understand, CHILDREN [state] ) RATIONALE "The truth of the build."' + nl +
	'DEFINE TEXT state ( CONTENT "clean", SATISFIES understand ) RATIONALE "The court verdict."'
oShell = new stzUiDocument(cShell)
? oShell.IsClean()
#--> 1
? len(oShell.Declarations())
#--> 12
? @@( oShell.Orphans() )
#--> [ "work" ]
```

`Orphans()` répond `[ "work" ]`, et `IsClean()` répond `1` sur les `12` déclarations.

La boucle de génération est celle du livre, et les rôles viennent de la liste fermée de la bibliothèque : `tablist`, `tab`, `group` et `status` y figurent.

### Les vingt-deux verbes

Chaque élément doit se rattacher à au moins un verbe, et un mot qui n'est pas l'un des vingt-deux est trouvé. Il y a une division du travail. La bibliothèque enregistre l'affirmation, avec `SATISFIES`, et trouve les éléments non rattachés, avec `Orphans()`. Elle ne détient pas la liste et ne refuse pas une intention inconnue : la garde affirme qu'une intention que personne n'a définie n'est pas une erreur. Donc la liste ci-dessous est saisie d'après la constitution, qui est dans son propre dépôt, et le livre la détient. Le tribunal refuse-t-il une intention qui n'est pas dans la liste ? Exécutez-le :

```haro
cShell = StzReplace(cShell, "DEFINE BOX work ( HEIGHT fill,", "DEFINE BOX work ( SATISFIES focus, HEIGHT fill,")
oShell = new stzUiDocument(cShell)
? @@( oShell.Orphans() )
#--> [ ]
aVerbs = [ "discover", "understand", "locate", "focus", "filter", "compare", "read", "scan", "scroll", "zoom", "select", "highlight", "preview", "mark", "act", "confirm", "cancel", "undo", "pause", "resume", "retry", "exit" ]
? len(aVerbs)
#--> 22
aStrangers = []
for cIntent in oShell.SatisfiedIntents()
	if not StzContains(aVerbs, cIntent)
		aStrangers + cIntent
	ok
next
? @@( aStrangers )
#--> [ ]
oOdd = new stzUiDocument(StzReplace(cShell, "SATISFIES preview", "SATISFIES transfer_funds"))
? oOdd.IsClean()
#--> 1
aStrangers = []
for cIntent in oOdd.SatisfiedIntents()
	if not StzContains(aVerbs, cIntent)
		aStrangers + cIntent
	ok
next
? @@( aStrangers )
#--> [ "transfer_funds" ]
```

Avec `SATISFIES focus` sur `work`, `Orphans()` répond `[ ]`, et la boucle sur la liste du livre aussi. Interrogé sur `transfer_funds`, `IsClean()` répond `1` ! La boucle sur la liste du livre répond `[ "transfer_funds" ]`.

`work` était une pure boîte de mise en page, et le tribunal compte aussi les conteneurs. Savoir si un conteneur doit être exempté des verbes appartient à la constitution, et non à la bibliothèque. Les familles, d'après la constitution : orientation, attention, information, sélection, action, et continuité. Et l'interprétation que je donne : la bibliothèque trouve l'étranger, et une liste que la bibliothèque ne détient pas ne peut pas le refuser. Le chapitre 25 a dit que la phrase-pont est appliquée à la main aujourd'hui. Je raconte ce retrait comme le refus qui est au centre de ce chapitre, dans la section 4 : la bibliothèque ne possède pas les verbes, la constitution les possède. Le texte de conception de la bibliothèque en dit encore vingt-quatre ; ce n'est pas la liste. Les vingt-deux sont imprimés dans le bloc ci-dessus, saisis d'après la constitution comme l'annexe C les imprime.

### Deux projections

Le même texte donne le balisage natif et la page web. Chaque élément déclaré est dans les deux, et les deux écrivent une propriété différemment exactement là où le profil enregistre une divergence. Combien de noms sont dans les deux ? Comptez-les :

```haro
cRml = oShell.ToRml()
cHtml = oShell.ToHtml()
nBoth = 0
for cName in oShell.Names()
	if StzContains(cRml, 'id="' + cName + '"') and StzContains(cHtml, 'id="' + cName + '"')
		nBoth++
	ok
next
? nBoth
#--> 11
? len(oShell.Names()) - 1
#--> 11
? StzContains(cRml, "--rmlui-direction")
#--> 1
? StzContains(cHtml, "--rmlui-direction")
#--> 0
```

Onze éléments et non douze : le panneau est la page elle-même, et non un `div`. Les deux dernières lignes montrent où les deux diffèrent. Le balisage natif contient `--rmlui-direction` (`1`), et la page web non (`0`). Le niveau natif met en page par la bibliothèque de mise en page du moteur, embarquée, et dessine par le volet graphique. Je n'ai pas ouvert de fenêtre.

### Le shell du navigateur

Le shell du navigateur est une page que le langage sert, sur la boucle locale. Une requête, un processus, aucun réseau au-delà de 127.0.0.1. Un second réacteur joue le client, donc c'est hors ligne par construction. Le gestionnaire lit une globale, parce que les lambdas de l'ancien langage hôte ne capturent pas les locales. Où vit la page ? Demandez au serveur :

```haro
$cShellPage = cHtml
oSrv = new stzAppServer()
oSrv.Get_("/", func oReq, oResp { oResp.Html($cShellPage) })
oSrv.Start(0, "127.0.0.1")
oClient = new stzReactor()
cCRLF = char(13) + char(10)
nJob = oClient.SubmitTcp("127.0.0.1", oSrv.Port(), "GET / HTTP/1.1" + cCRLF + "Host: local" + cCRLF + "Connection: close" + cCRLF + cCRLF)
? oSrv.ServeOne(3000)
#--> 1
cAnswer = oClient.AwaitTcp(nJob, 5000)
? StzContains(cAnswer, "200 OK")
#--> 1
? StzContains(cAnswer, 'id="status"')
#--> 1
? oSrv.Host()
#--> 127.0.0.1
oSrv.Stop()
```

`Host()` répond `127.0.0.1`. Le coût de cette forme est nommé dans le dossier. Un port lié localement est une surface et doit être traité comme tel. Selon les mots de la charte, l'intention de conception a été mesurée pour un studio de son et non pour un IDE. Le backend de la bibliothèque refuse déjà de quitter la boucle locale sans authentification, au moment de lier le port ; le serveur nu ci-dessus ne vérifie rien. Que fait le backend de `0.0.0.0` ? Essayez :

```haro
oT = new stzAppTopology("shell")
oT.AddDataset("notes", [ [ "first" ] ])
oT.SetDatasetColumns("notes", [ "text" ])
oBackend = new stzAppBackend("shell", oT)
bRaised = FALSE
try
	oBackend.StartOn("0.0.0.0", 0)
catch
	bRaised = TRUE
done
? bRaised
#--> 1
? oBackend.IsLive()
#--> 0
```

Il lève une erreur ! `bRaised` répond `1`, et `IsLive()` répond `0`.

### Une barre d'état qui dit la vérité

Une cellule d'état est une fonction du verdict du tribunal, donc elle ne peut pas dire *propre* d'un document que le tribunal a refusé. La fonction ci-dessous est celle du livre, au-dessus de `IsClean()` de la bibliothèque et de ses diagnostics. La classe de cellule d'état n'est pas encore dans la bibliothèque, et la garde qui interdit qu'une cellule montre autre chose que ce que le tribunal a émis est conçue. La spécification nomme aussi l'état avant toute construction, *non vérifié*, et ma fonction ne le porte pas. Que dit la cellule pour un enfant déclaré nulle part, et pour un rôle qui n'est pas dans la liste ? Exécutez-le :

```haro
? ShellStatus(cShell)
#--> clean
? ShellStatus(StzReplace(cShell, "[page, rail]", "[page, ghost]"))
#--> refused: DANGLING_REFERENCE
? ShellStatus(StzReplace(cShell, "ROLE status", "ROLE sttus"))
#--> refused: UNKNOWN_ROLE

func ShellStatus(cText)
	oD = new stzUiDocument(cText)
	if oD.IsClean()
		return "clean"
	ok
	return "refused: " + oD.Diagnostics()[1][:code]
```

La cellule répond `refused: DANGLING_REFERENCE` et `refused: UNKNOWN_ROLE`, et *propre* seulement pour le document que le tribunal a gardé.

Et ce que lit un lecteur d'écran est émis depuis la déclaration. Une région déclarée `ROLE status` est émise dans l'arbre d'accessibilité avec sa justification comme description, dans l'ordre de lecture, et aucun drapeau ne désactive l'arbre. La mise en page a besoin d'un fichier de police, et ce bloc utilise celle du système. Que dit l'arbre de la région d'état ? Demandez-lui :

```haro
oShell.UseFont("C:/Windows/Fonts/segoeui.ttf")
oP = oShell.ToPanel()
oT = new stzAccessibilityTree(oShell, oP)
? oT.NodeCount()
#--> 12
? oT.NodeOf("status")[:role]
#--> status
? oT.NodeOf("status")[:description]
#--> The truth of the build.
? @@( oT.ReadingOrder() )
#--> [ "window", "tablist", 'tab "Define"', 'tab "Build"', 'tab "Govern"', 'tab "Ship"', "group", 'label "the work"', "group", 'label "no proposal"', "status", 'label "clean"' ]
```

L'arbre répond `status`, et pour sa description `The truth of the build.`, la justification mot pour mot ! L'en-tête de la bibliothèque dit pourquoi : chaque toolkit garde l'accessibilité derrière un drapeau de performance, et c'est là que les utilisateurs n'obtiennent silencieusement rien. Donc ici il n'y a rien à garder derrière un drapeau et rien à oublier d'activer. Le même fichier dit ce qu'un lecteur d'écran peut manipuler, un agent d'IA peut le manipuler.

### Un rail qui propose

Un rail est une vue sur ce que le monde propose. Une pulsation propose et ne relie jamais. Un acte sur le monde efface une proposition, et la ligne d'état propre du monde compte à partir de la même liste que montre le rail. Que propose le monde, et que reste-t-il après un acte ? Exécutez-le :

```haro
oApp = StzAppQ("fieldvisits")
oApp.AddThingQ(:Client) { Has([ :name ]) }
oApp.AddThing(:Visit)
oApp.AddReactionQ(:Client).Unseen(90, :Days) { Propose(:Visit) }
oApp.AddInstance("amadou", :Client)
oApp.AddInstance("binta", :Client)
oApp.Live()
#--> [fieldvisits] is live -- 2 thing(s), 0 flow(s), 1 reaction(s), 0 goal(s); 2 proposal(s)
for aP in oApp.Proposals()
	? aP[1] + " " + aP[2] + " " + aP[3] + " " + aP[4]
next
#--> propose visit for amadou
#--> propose visit for binta
? oApp.Pulse()
#--> 0
? len(oApp.Proposals())
#--> 2
oApp.Relate("amadou", :visit, "visit-1")
oApp.Pulse()
for aP in oApp.Proposals()
	? aP[1] + " " + aP[2] + " " + aP[3] + " " + aP[4]
next
#--> propose visit for binta
```

`Live()` imprime sa ligne, `2 proposal(s)` à sa fin, et le juge compare ce qui est imprimé. Avant l'acte, `Pulse()` répond `0` et le rail tient encore `2` propositions. Après l'acte, une ligne reste : `propose visit for binta`. "2 thing(s)" compte les deux choses, Client et Visit, et non les instances. Le chapitre 20 possède la loi sous le rail, la proposition, le plan et le tribunal.

Et un écran est une intention. Un endroit où le monde parle en verbes est celui de ses écrans. Cinq méthodes existent : `ToDiscover`, `ToUnderstand`, `ToFocus`, `ToSelect` et `ToAct`. Un sixième verbe, `ToCompare`, n'existe pas. Qu'est-ce qui répond quand un écran le demande ? Exécutez-le :

```haro
oW = StzAppQ("fieldvisits")
oW.AddThingQ(:Client) { Has([ :name ]) }
oW.AddScreenQ(:Home)  { ToDiscover(:Client) }
oW.AddScreenQ(:File)  { ToUnderstand(:Client) }
oW.AddScreenQ(:Pick)  { ToSelect(:Client) }
oW.AddScreenQ(:Edit)  { ToAct(:Client) }
oW.Explain()
#--> WORLD fieldvisits   lives in: memory (not persisted)
#      BEING
#        client (name)
#      MET FROM WITHOUT
#        screen home: discover client
#        screen file: understand client
#        screen pick: select client
#        screen edit: act client
try
	oW.AddScreenQ(:Side) { ToCompare(:Client) }
catch
	? cCatchError
done
#--> Error (R3) : Calling Function without definition: tocompare
```

C'est le runtime qui répond, `Error (R3) : Calling Function without definition: tocompare`, et aucun tribunal : le mot d'intention est stocké comme chaîne, et n'est vérifié contre aucune liste.

Voilà ce qui tourne ; je dis maintenant ce que j'en ai décidé, et ce que j'ai refusé.

## 4. La décision, et ce que j'ai refusé

**J'ai décidé de porter les deux shells.** Le 7 octobre 2026 on m'a demandé si la fondation prend le shell natif ou le shell du navigateur, et j'ai répondu : porter les deux. La conséquence que l'étude énonce est qu'un chrome est déclaré une fois, et que deux shells le projettent.

**J'ai décidé que la mécanique est celle de la bibliothèque et que l'IDE est celui du produit.** Le document de conception de la bibliothèque : la mécanique du paradigme est plateforme ; le livre, la marque, l'IDE sont produit, et ne fuient jamais. La fondation livre le raffinement comme verbe de bibliothèque disponible à tout programme.

**J'ai retiré le moteur d'interaction.** Le 26 mai 2026 mon commit a retiré vingt-deux modules inventés par une IA qui n'étaient pas dans le Softanza d'origine, parmi lesquels le module d'interaction. Je lis la date, le compte et la liste dans l'historique git de la bibliothèque, le commit `b70f3ad91`, et non dans l'arbre épinglé. Son texte de conception, qui dit vingt-quatre verbes et des lois appliquées par le moteur, est toujours dans l'arbre. La liste de la constitution en compte vingt-deux.

**J'ai refusé de résoudre des intentions à l'intérieur du langage du panneau.** Le panneau ne déclare aucun sens : il n'y a pas de `:Danger` et il ne peut jamais y en avoir. L'emplacement d'intention a été laissé délibérément non résolu. Plus haut, `IsClean()` a répondu `1` pour `transfer_funds` : le panneau ne juge aucun sens.

**J'ai refusé de rédiger le balisage, et j'ai refusé un moteur de script.** Le balisage natif est émis, jamais rédigé ; il n'y a pas de moteur de script ; flexbox seulement. C'est la raison pour laquelle le chrome est un fichier texte et non une classe.

**J'ai refusé un drapeau qui désactive l'arbre d'accessibilité.** Le bloc de l'arbre ci-dessus a imprimé `status` et `The truth of the build.` sans qu'aucun drapeau soit à activer.

**J'ai admis une lentille qui ne peut pas capturer.** La charte du domaine de projets pour ses produits : une vérité, dans des fichiers, et deux lentilles (les deux de la charte sont la paire de studios, et non deux shells). Ce que la charte a refusé, ce sont les cadres qui capturent le travail. Une lentille qui ne peut pas capturer est admissible. L'environnement est une projection de texte brut, et non un magasin.

**Une session a retiré une facette, et je l'ai rétablie.** La conception de référence consigne que la facette Connexions était de première classe dans le prototype de juin 2026, et qu'un agent d'IA l'a retirée par un raisonnement circulaire. Le retrait s'est propagé en cascade dans cinq documents. Je l'ai rétablie. Celui qui décide du ruban est l'auteur.

**J'ai accepté le shell du navigateur avec son coût, non mesuré.** La charte de l'IDE de la porte d'entrée a choisi un onglet de navigateur, construit avec le moteur, sans étape d'installation, et a nommé la perte.

**Le motif a été appris en six efforts sur deux ans, dont un seul construit**, compte l'étude. Ce compte est celui de l'étude.

Vient ensuite le tribunal, avec les gardes derrière ces pièces et celles qui manquent.

## 5. Le tribunal

`gui_stzui_narrated` prouve la clôture du tribunal du panneau, une référence pendante, un doublon, une boîte orpheline, un panneau manquant, la justification obligatoire et un aller-retour. Elle prouve, à la scène 13, l'emplacement d'intention : `SATISFIES`, `Orphans()`, et qu'une intention que personne n'a définie n'est pas une erreur. `gui_profile_narrated` prouve que le profil est de la donnée, avec trois divergences enregistrées. Elle prouve qu'un document a deux projections et que chaque élément déclaré est dans les deux, et que la fixture émet une page qui se vérifie elle-même. La moitié navigateur de cette garde est une procédure à reproduire. `gui_tier_agreement_narrated` prouve qu'une même liste d'affichage rendue en vectoriel et en pixels s'accorde au pixel près. Ce n'est pas du HTML contre du natif. `gui_accessibility_narrated` prouve l'arbre émis depuis la déclaration. `05_stzapp_live_narrated` prouve qu'un monde vivant propose et qu'agir efface. `emulator_narrated` prouve la surface générée de l'émulateur.

Trois gardes sont à venir : une qui juge un shell contre les vingt-deux verbes, une qui vérifie qu'une cellule d'état ne montre que ce qu'un tribunal a émis, et une qui dit que les deux projections d'un chrome s'accordent dans le navigateur. L'étude en note l'absence, et je n'ai rien trouvé de contraire.

**La vérification des deux projections peut échouer, et elle a échoué.** La fixture de la bibliothèque est une page et non une assertion : elle porte la projection web et les boîtes que la mise en page native a produites. Un script les compare et imprime une bande de verdict. Un exécuteur ne peut pas la juger, donc je l'ai lue à la main le 8 octobre 2026. Sur le chrome du premier bloc, onze boîtes avec du texte dans chaque région, la bande disait "AGREE on every declared box of 11". Sa note disait que quatre boîtes de largeur automatique diffèrent, ce qui est deux modeleurs de texte et non le profil. Sur le même chrome à trois bandes avec des régions vides, la bande disait "DISAGREE on 1 declared boxes of 3". La cause est dans la projection web : une boîte vide est émise comme `<div id="body"/>`. Un analyseur HTML la lit comme une balise ouvrante, si bien que les frères qui suivent s'y imbriquent. Le niveau natif n'est pas touché. La fixture l'attrape ! Les gardes de la bibliothèque pas encore, puisque leur propre vitrine n'a pas de boîte vide : en ajouter une est l'étape suivante. Un espace de travail vide est le premier état du motif. Donc la bande dit la vérité dans les deux sens, ce qui est la cinquième marque du chapitre en une seule image, et la projection web a un cas à corriger sur cet état exact.

Du tribunal, je reviens au terrain, et à l'endroit où il mène.

## 6. Le terrain, et où il mène

Les éditeurs rapides fixent une barre que le dossier écrit comme loi pour son propre produit : de l'entrée à l'écran en moins de seize millisecondes, un démarrage à froid en moins de quatre cents, sans exception. Le dossier ne l'a pas encore mesurée sur l'un ou l'autre shell : un chiffre de latence est absent, et c'est l'étape suivante.

Un changement de texte invalide tout le document. Une valeur liée qui change refait la mise en forme de chaque chaîne, là où une couleur n'en refait qu'une. Les éditeurs du terrain appliquent des patchs, et le terrain mène ici aujourd'hui. (Connaissance générale.)

Le navigateur coûte ce qu'il coûte : l'accès aux fichiers par le modèle du navigateur, un port à garder, et une latence non mesurée. Le shell natif coûte un système de fenêtres, et un GPU pour le chemin raster.

Le terrain a un service de langage (connaissance générale), et le dossier a un contrat ; le service est l'étape suivante. Le modèle de l'explorateur lit le fichier de monde que le service émettrait, et il n'est chargé par aucun fichier d'entrée : un bloc qui l'appelle sans un chargement écrit à la main échoue.

L'éditeur rapide du terrain traite la barre d'état comme de l'encombrement. Le motif en garde une et lui demande d'être vraie. C'est un pari, et je le tiens pour une vue, non pour un résultat ; le corpus propre du dossier plaide pour le côté du terrain dans le même souffle.

Reste la limite.

## 7. La limite

**La projection web ne porte pas encore de rôles, d'étiquettes ni d'intentions.** `ToHtml` n'émet qu'un identifiant, un style et le texte. L'arbre qui porte les rôles est un artefact séparé, comme le bloc ci-dessus le montre, donc un shell de navigateur devrait déduire à partir de `div` nus ce que le shell natif émet. Le plan lui-même dit que la bibliothèque d'accessibilité qu'il adopte n'a pas d'adaptateur web.

**Le centre de contrôle de la bibliothèque elle-même imprime des constantes là où le motif demande des verdicts.** L'émulateur génère une surface de navigateur, une grille de parties avec des pastilles d'état et des badges de fidélité, une fenêtre d'appareil et une console pour chaque partie. Ses mots d'état sont des constantes de la classe d'appareil et du gabarit, et ils ne sont pas mesurés. Voici un plan avec une partie firmware et une capacité GPIO, et aucune pompe nulle part. Que dit sa page ? Construisez-la et lisez-la :

```haro
oPlan = new stzDelivery("greenhouse")
oPlan.AddFirmware(:node, :ESP32)
oPlan.NeedsIn(:node, [ :GPIO ])
oEmu = new stzEmulator(oPlan)
oEmu.CompileEngineQ(FALSE)
oEmu.SetOutDirQ("_emu")
oEmu.Build()
cH = read("_emu/index.html")
? StzContains(cH, "needs a look")
#--> 1
? StzContains(cH, "2 approximated")
#--> 1
? StzContains(cH, "parts healthy")
#--> 1
? StzContains(cH, "Ready to ship.")
#--> 1
StzDirDeleteAll("_emu")
```

La partie reçoit "2 approximated" et, dans le détail de la grille, un texte sur la temporisation de la pompe et le bruit des capteurs : le texte de la démonstration de serre, renvoyé pour n'importe quel microcontrôleur. L'en-tête dit "parts healthy" et la bannière dit "Ready to ship." pour le même plan, à partir de littéraux ! Un plan avec seulement un backend imprime aussi "parts healthy" et "Ready to ship.", et ni "needs a look" ni "2 approximated" (lu dans la source, non exécuté). "Deploy to production" est une alerte. La moitié véridique est réelle : la fidélité est imprimée, et la console refuse un verbe que le sous-ensemble du moteur de la partie n'a pas. C'est de la narration dans la bibliothèque, que je n'ai pas exécutée.

Voilà la perte contre la page de la bibliothèque elle-même. Elle se tient à côté de « une barre d'état qui dit la vérité » de la section 3 : le motif demande qu'une cellule d'état soit une fonction de ce qu'un tribunal a émis. Et la page propre de la bibliothèque imprime ses mots à partir de littéraux. La demande de dériver ces mots du plan est ouverte, et c'est l'étape suivante.

**`ToPanel` a besoin d'un fichier de police et lève une erreur sans lui.** L'arbre d'accessibilité et la fixture ont besoin d'un panneau mis en page, donc les blocs qui les utilisent dépendent d'une police système.

**`Orphans()` compte les conteneurs.** Savoir si une boîte de mise en page seule doit servir un verbe est une règle que la constitution doit énoncer.

Ce qui est construit : l'interface comme texte avec un tribunal ; quatre genres fermés, une liste fermée de dix-neuf rôles, un ensemble fermé de champs, une justification obligatoire, un aller-retour jusqu'à un point fixe. Deux projections, avec une table enregistrée de trois divergences et une page qui peut dire DISAGREE. L'arbre d'accessibilité, et un pont qui atteint l'interface d'un vrai lecteur d'écran sous Windows, lu et non exécuté par moi. Une valeur déclarée change et l'écran suit, avec le focus conservé. Une page hébergée sur la boucle locale, et un backend qui refuse de quitter la boucle locale sans signature. Un monde qui propose, des écrans déclarés comme intentions, une surface de navigateur générée. Et un shell binaire, le banc d'écoute du volet sonore, en environ sept cents lignes de Zig, que j'ai lues et pas construites.

Ce qui est conçu : le kit de shells avec deux shells ; le chrome comme genres fermés nommés pour la colonne, le ruban, le rail et la barre d'état, aucun encore classe de la bibliothèque. La facette comme donnée, avec son groupe, sa place dans la vie, ses genres d'artefacts, son tribunal et son profil. Le rail lié au focus, et les cellules de gouvernance lues dans les tribunaux, avec une garde qui interdit qu'une cellule montre un état que le tribunal n'a pas émis.

Ce qui est absent : un IDE de cette famille. Une liste des vingt-deux verbes dans la bibliothèque, et tout refus d'un verbe inconnu : `transfer_funds` passe le tribunal. Une garde qui juge un shell contre les verbes. Un éditeur. Une latence mesurée. Je raconte le motif comme conçu, avec les pièces qui tournent comme preuve : le tribunal du chrome, les deux projections, l'arbre d'accessibilité, la page hébergée sur la boucle locale. Aucun IDE de cette famille n'est livré aujourd'hui.

## 8. Six portes

**Le programmeur.** Vous écrivez le shell comme texte, et un tribunal vous dit l'unique boîte qui ne sert aucun verbe avant que quoi que ce soit soit dessiné. Le même fichier est une fenêtre native et une page, et la bibliothèque a une page qui dit quand elles divergent.

**L'analyste.** Le ruban est l'ordre de la vie de votre solution, et non celui des fonctionnalités d'un outil. La cellule d'état lit le tribunal, et vous pouvez demander au monde ce qu'il propose avant qu'on lui demande d'agir.

**Le concepteur.** Votre interface a une constitution de vingt-deux verbes et une grammaire fermée qui ajoute des rendus et jamais des verbes. Chaque élément doit dire quel verbe il sert, et la bibliothèque trouve déjà ceux qui n'en disent aucun.

**Le décideur.** Demandez de tout environnement trois choses. Sa barre d'état lit-elle un tribunal ? Son assistant vit-il dans un volet et propose-t-il ? Et qui juge que les deux shells s'accordent ? Ici les réponses sont : conçu ; conçu, avec la loi du rail construite en dessous au chapitre 20 ; et une page qui se vérifie elle-même, qui a attrapé le cas de la boîte vide dès sa première exécution, d'après la garde.

**Le formateur.** L'exercice est une prédiction : dites ce que le tribunal répondra avant de l'exécuter. Le mot d'état qui est une constante est une leçon sur la différence entre une étiquette et une vérité.

**L'agent.** Le shell est un fichier texte que vous pouvez lire et écrire, et l'arbre que lit un lecteur d'écran est l'arbre que vous pouvez lire. Vos propositions apparaissent dans un rail et ne valident nulle part.

## 9. Exercice

Un exercice, en trois mouvements.

1. Écrivez un shell à vous en cinq éléments : une barre de titre, un ruban de trois facettes tirées de la vie de votre propre solution, une zone de travail, un rail, une barre d'état. Avant d'exécuter quoi que ce soit, écrivez sur papier quel verbe parmi les vingt-deux chaque élément sert, et laquelle de vos boîtes vous vous attendez à ce que le tribunal appelle orpheline.
2. Exécutez `IsClean()` et `Orphans()`, et comparez avec votre papier. Puis cassez le fichier de trois façons : un enfant déclaré nulle part, un rôle qui n'est pas dans la liste, et une intention qui n'est pas l'une des vingt-deux. Pour chacune, écrivez ce que votre fonction d'état répondra, et si la bibliothèque, la fonction du livre, ou personne ne l'attrapera.
3. Émettez la page, ouvrez-la, et écrivez la ligne que la bande de la fixture imprimera pour une version avec une zone de travail vide. Puis regardez. La page vient de `ToFixture`, qui prend la boîte que `BoxOf` rapporte pour chaque nom sur le panneau mis en page par `ToPanel` ; `gui_profile_narrated` a la boucle, et un fichier de police est nécessaire.

```haro exercise
oMine = new stzUiDocument('DEFINE PANEL shell ( SIZE [640, 360], DIRECTION column, CHILDREN [bar] ) RATIONALE "Mine."' + nl + 'DEFINE TEXT bar ( CONTENT "mine", SATISFIES understand ) RATIONALE "Mine too."')
# under each line, write what you expect before you run it
? oMine.IsClean()
? @@( oMine.Orphans() )
```

Si une promesse casse, ne la changez pas : expliquez d'abord la sortie.

Je vous laisse celui-ci. Le `ShellStatus` de la section 3 est la fonction du livre, et je ne l'ai pas gardée contre le cas ci-dessous : celui que la section 3 a passé par `IsClean()`, et que la section 7 range parmi les absents. Exécutez la ligne et lisez le mot que la cellule donne. Puis faites refuser par la cellule un étranger aux vingt-deux, comme le fait la boucle du livre, avec la boucle sur la liste que la section 3 contient déjà, et sans demander à la bibliothèque une liste qu'elle ne possède pas (la section 4 dit pourquoi).

```haro exercise
# the book's own call, with the one change of the second block of section 3
? ShellStatus(StzReplace(cShell, "SATISFIES preview", "SATISFIES transfer_funds"))
```

Quand la cellule sera juste, vous saurez ce que la bibliothèque trouve, et ce que seule une liste qu'elle ne tient pas peut refuser.

Chaque shell de ce chapitre est une projection, et le chapitre 27 descend sous elles toutes : trois couches, un moteur, Haro. Là, chaque fonctionnalité est implémentée une fois, la surface est la promesse, et le runtime est la partie qu'on mesure, et qu'on n'affirme jamais.
