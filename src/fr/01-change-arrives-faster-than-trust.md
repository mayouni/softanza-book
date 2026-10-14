---
id: change-arrives-faster-than-trust
part: 1
number: 1
title: Le changement arrive plus vite que la confiance
spine: true
narrations: []
site: [forged, agentic]
guards: [service_registry_narrated, safeworld_narrated, governance_crossing_narrated]
stage:
  built: le tribunal qui admet ou refuse un changement, pour une personne et pour une machine
  absent: une plateforme cliente qui tourne sur le moteur Softanza
status: draft
rulings: ["12.10", "12.11", "12.15", "12.28", "12.29"]
source: drafts/book-01-change-arrives-faster-than-trust.md
edits: ["section 5: one block, run by the book's runner (DECISIONS CH01-a)", "section 5: safeworld_narrated is in the agentic plane (CH01-b)"]
figures:
  - "seventy-six assertions: safeworld_narrated, counted at build (data/guards.json)"
  - "ninety-three percent: base holds 93.2 per cent of the lines, study 12.15, stzlib 93d7a39"
  - "a factor between one and two: Luau leads all six rows, 1.04 to 1.88 times, study 12.10 and the estate memo of 2026-09-13"
  - "twenty-two verbs, one hundred and twenty-two rules: the interface constitution, study 12.23"
---

## 1. Le concept, tel que le terrain le tient

Demandez à l'industrie ce qui a changé dans la programmation ces dernières années et vous obtiendrez une seule réponse, dite avec enthousiasme ou avec effroi : *les machines écrivent le code maintenant.*

L'image est familière. Un modèle d'IA propose une fonction, un fichier, une application entière. Une personne la relit, ou non. On ajoute des outils autour du modèle pour le rendre plus sûr : des linters qui lisent ce qu'il a écrit, des tests qu'il génère lui-même, des garde-fous qui attrapent le pire, un second modèle qui juge le premier. Le modèle est au centre. Tout le reste est une clôture bâtie autour de lui après coup.

Je ne crois pas que cette image se trompe sur les faits. Elle se trompe sur l'endroit où se tenir.

## 2. Le premier principe

Voici la phrase à laquelle je reviens sans cesse, et c'est la plus ancienne phrase de ce livre : **le changement arrive plus vite que la confiance.**

Le code est devenu bon marché. Mille lignes coûtent une phrase. Ce qui n'est pas devenu bon marché, ce qui est même devenu la chose la plus rare du logiciel, c'est la confiance que ces lignes font ce que leur auteur, humain ou machine, dit qu'elles font. Toutes les équipes que j'ai rencontrées ces deux dernières années ont plus de code qu'elles ne peuvent en relire et moins de confiance qu'avant. Le goulot de notre époque n'est pas l'écriture. C'est l'admission : décider ce qui peut entrer dans un système et y rester.

Aussi la question que pose Softanza n'est pas *comment générer mieux ?* C'est *comment admettre ?* Qui juge un changement, par quelle loi, avant qu'il s'exécute, et ce qu'on écrit du verdict pour que quelqu'un puisse le lire plus tard et en répondre.

Lorsque vous placez l'admission au centre, l'image se retourne. Le tribunal est au milieu. Le modèle est un auteur de propositions parmi d'autres, et il vient en dernier, après la personne, après les données, après la formule, après la phrase simple. Rien de ce qu'il dit n'entre dans le monde avant que le tribunal l'ait lu. Ce n'est pas une clôture bâtie autour d'un générateur. C'est un autre bâtiment.

## 3. La forme Softanza

Laissez-moi vous montrer plutôt que dire, par l'exemple, ce qui a toujours été ma façon préférée d'enseigner.

Une solution déclare qu'elle dépend d'un service de courrier. Pendant que je programme, je lie cette dépendance à un bac à sable : un objet qui capture chaque message et n'envoie rien, pour que mes tests puissent lire ce qui *serait* parti. Gratuit, hors ligne, déterministe. Puis je déplace la solution en production, le bac à sable toujours lié, comme on le fait à deux heures du matin avant une démonstration.

```haro
oReg = new stzServiceRegistry("my-solution")
oReg.Bind(:mail, new stzMailSandbox())
oReg.SetPhase(:emulated)
? oReg.IsSound()
#--> 1
oReg.SetPhase(:production)
? oReg.IsSound()
#--> 0
? oReg.Findings()[1][:message]
#--> still bound to a SANDBOX in a production phase -- a fake must never ship
```

Le registre ne la déclare pas saine. En phase émulée il répond un ; en production il répond zéro, et la ligne suivante dit pourquoi : un faux ne doit jamais être livré. Le faux est refusé par son nom, et un service déclaré et jamais lié lève une erreur au moment où on le demande, au lieu de ne rien faire en silence. Je n'ai pas eu à me souvenir de le vérifier. La phase a décidé de ce qui revient, et la vérification est imposée, non mémorisée.

C'est toute la philosophie en une petite scène. L'expression est libre : liez ce que vous voulez, aussi longtemps que vous voulez. L'admission est gouvernée : la barrière lit la phase et la liaison, et refuse.

Maintenant une deuxième scène, parce que la première n'a pas de modèle d'IA dedans et que vous attendez le modèle.

Prenons un restaurant pour illustration : un agent d'IA qui connaît son monde propose de passer une commande. Dans Softanza, l'agent ne la passe pas. Il propose un plan. Un atelier répète le plan sur un jumeau du système, une copie qui ne garde aucune référence vers le réel, et enregistre chaque opération qu'il effectuerait. Un tribunal lit la répétition à la lumière des règles que le restaurant a déclarées : qui peut commander, ce qui peut être commandé, ce qu'un fournisseur doit confirmer. Alors seulement un acteur gouverné valide, et la validation est enregistrée avec son acteur et son issue. La garde qui prouve cette séquence, `safeworld_narrated`, répète dans un jumeau des fichiers, planifie et laisse un acteur valider ; elle compte soixante-seize assertions au moment où j'écris, dont aucune ne parle d'un restaurant, et le site montre une exécution enregistrée du même mécanisme.

Remarquez ce que le modèle a fait et n'a pas fait. Il a proposé. Il n'a pas décidé, pas écrit, pas envoyé. Il était un auteur de propositions à côté des registres de réponse. Trois d'entre eux, une option choisie, une structure de données donnée, une phrase dite, sont construits aujourd'hui et ouverts à la personne avant même que le modèle soit appelé ; deux autres, une formule écrite et un exemple montré, ne sont pas encore construits (chapitre 18). J'appelle cela *programmatique par défaut, le modèle en dernier*. C'est la phrase sous chaque chapitre de la partie IV.

Et une troisième scène, la plus petite, parce qu'elle montre la même loi au niveau d'une seule ligne. La plateforme est jugée sur l'allure de son code et sur ce qu'il répond :

```haro
o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? @@( o1.FindAll("tea") )
#--> [ 1, 3, 6 ]
? @@( o1.DuplicatesRemoved() )
#--> [ "tea", "rice", "fish" ]
```

La question est dite comme elle est pensée : trouver tout, retirer les doublons. Et les deux lignes sous les deux questions ne sont pas mon commentaire. Ce sont des promesses que la bibliothèque a tenues la nuit où ce chapitre a été construit. Si elle cesse de les tenir, cette page échoue. La même loi, l'admission avant la confiance, appliquée à un paragraphe.

## 4. La décision, et ce que j'ai refusé

Chaque chapitre de ce livre porte cette section, et j'ai promis dans la préface que c'est la raison d'être du livre. Soyons donc concret sur les décisions derrière ce premier chapitre, car elles n'ont pas été confortables.

**J'ai refusé de mettre le modèle d'IA au centre.** Quand les modèles d'IA sont arrivés, c'était le geste évident, et j'avais les pièces pour le faire : une couche naturelle, un graphe de connaissances, une classe d'agent. J'aurais pu brancher un modèle dans chacune et livrer un Softanza qui « parle ». Je ne l'ai pas fait, et j'ai écrit ce refus dans l'architecture comme une loi : l'esprit est programmatique par défaut, et un modèle ne peut que proposer. J'ai renoncé à un peu de mode par ce choix. Je crois avoir gardé la plateforme.

**J'ai mis à la retraite le langage sur lequel je suis né.** Softanza a été écrit pendant des années sur un petit langage de script chaleureux que j'aime et que j'ai supplié, bien avant l'ère des LLM, de faire du langage naturel exécutable sa première préoccupation. Il ne l'a pas fait, et c'est son droit. En 2026, j'ai décidé que le langage ne serait pas porté plus loin : le runtime sous Softanza est en train d'être remplacé par un runtime qui nous appartient, écrit en Zig, une charte et un spike pour l'instant, portant l'ancienne surface pour que chaque ligne que j'ai écrite puisse continuer à s'exécuter, sous un nouveau nom, **Haro**. L'ancienne surface reste parce que le code est le patrimoine ; l'ancien runtime s'en va parce que la souveraineté sur le runtime est l'un des engagements que j'ai pris. Cette décision n'a pas été gratuite. Elle est au chapitre 27 avec ses chiffres, y compris celui que je ne voulais pas : notre runtime est plus lent que celui contre lequel nous l'avons mesuré, d'un facteur entre un et deux, sur chaque ligne. J'ai consigné la perte dans le mémo du domaine de projets du 13 septembre. Un livre qui cache cela ne mérite pas votre confiance, et une plateforme non plus.

**J'ai refusé de laisser quoi que ce soit entrer dans BASE sans un tribunal, et j'ai échoué.** Les trois couches de la bibliothèque, NOYAU, BASE et MAX, devaient garder le fondement petit et les innovations au-dessus. Sous la pression du temps, j'ai laissé tout aller dans BASE : quatre-vingt-treize pour cent du code s'y trouve aujourd'hui, et la règle de dépendance est tenue au niveau du moteur et rompue au niveau de l'héritage. Je le dis au premier chapitre, non au dernier, parce que la discipline que je m'apprête à prêcher pendant trente-deux chapitres est une discipline que j'ai enfreinte, et l'étude du dossier m'a pris sur le fait. C'est à cela que sert un tribunal, et celui des couches n'est encore que proposé.

**J'ai refusé une seconde intégration.** Quand quelqu'un demande « et Python, et JavaScript, et mon langage », la réponse est une porte, à gouverner, et jamais un autre runtime hôte cousu dans la plateforme. Les sept langages du dossier, l'hôte et six runtimes derrière une seule porte, ont été choisis pour sept couches d'une solution, et le chapitre 16 les compte. La porte est la réponse à « et le langage X », et c'est une seule réponse, pas vingt.

Ce qui a été refusé fait autant partie de Softanza que ce qui a été construit. Vous ne trouverez pas les refus sur le site, parce que le site montre ce qui est. Vous les trouverez ici, dans chaque chapitre, sous ce titre.

## 5. Le tribunal

Qu'est-ce qui prouve ce chapitre ? Trois choses, et je vous les donne par leur nom pour que vous puissiez les vérifier plutôt que me croire.

Le refus d'un faux en production par le registre de services est une garde, `service_registry_narrated`, dans le volet système. La suite proposer, répéter, juger et valider de l'agent d'IA est `safeworld_narrated`, soixante-seize assertions, dans le volet agentique, à côté de `governance_crossing_narrated`, dans le volet système, pour la traversée elle-même. Les blocs de code de cette page ont été exécutés par l'exécuteur propre du livre à l'intérieur de la bibliothèque la nuit où cette page a été construite, et sa sortie est montrée telle qu'elle est venue.

Trois gardes pour un chapitre de philosophie peuvent sembler peu. Ce sont les trois bonnes, parce que ce sont les trois endroits où la philosophie rencontre un verdict.

## 6. Le terrain, et où il mène

Je ne ferai pas semblant que le terrain n'a rien. Il a, ces trois dernières années, construit les générateurs de code les plus capables de l'histoire, et je les utilise chaque jour. La réponse de l'industrie au problème de la confiance est un vrai travail : tests générés, robots de revue, moteurs de politiques, bacs à sable pour agents d'IA, sorties structurées, un second modèle pour noter le premier. Là où le terrain mène, et il mène nettement, c'est dans les générateurs eux-mêmes. Softanza ne construit pas les grands générateurs et ne les concurrence pas ; là où il entraîne, il entraîne de petits modèles liés à un seul domaine, dont chaque réponse sera vérifiée par une grammaire. Le terrain mène aussi en échelle : ses outils de revue lisent des volumes de code généré contre lesquels rien dans Softanza n'a été exécuté.

Là où je crois que Softanza se tient seul, c'est dans l'ordre des choses. Le terrain ajoute l'admission à un générateur. Softanza ajoute un générateur à un tribunal. Dans le terrain, un modèle d'IA écrit dans votre langage et des outils le vérifient ensuite ; ici, le modèle ne peut écrire que dans un langage que vous avez déclaré, dont la grammaire est close et dont le tribunal est destiné à naître avec lui, de sorte que, pour les langages dont la grammaire est compilée aujourd'hui, une phrase invalide ne peut pas du tout être prononcée. Dans le terrain, le dialogue avec un système est un prompt ; ici, le système demande, et la réponse peut être un exemple, une formule ou une phrase avant d'être jamais un modèle. Dans le terrain, la trace d'une décision est un journal ; ici, c'est une transcription avec un locuteur et une certitude, dont on répond pour toujours.

Ce sont des affirmations, et chacune a son chapitre et sa garde. Je les liste ici pour que vous sachiez où va l'argument, et pour que vous puissiez me le faire tenir.

## 7. La limite

La limite honnête de ce chapitre est aussi la limite honnête de toute la plateforme, et je la mets sur la première page à dessein.

Softanza a été utilisé. Une banque à Niamey fait tourner une plateforme d'évaluation dont la construction a façonné Softanza, sous licence, attestée par le guide d'installation que nous avons livré. Un restaurant à Lyon fait tourner une plateforme pour le commerce de quartier dont le propriétaire a fait seul la première démonstration, sur son propre téléphone, avec une application de messagerie comme ligne d'assistance. Une organisation au Niger a son hub conçu. Leurs leçons sont dans le code, par nom de fichier, dans la partie VI.

Mais les plateformes clientes tournent aujourd'hui sur des piles ordinaires. Celle de la banque est une application Python ; celle du restaurant est un ensemble de mondes web d'un seul fichier ; le hub de l'organisation n'est pas construit. Leurs déclarations sont en cours d'écriture comme celles de Softanza elle-même, de sorte que les faire passer sur le moteur Softanza soit un changement de moteur et non de plan. Ce passage est l'étape suivante. Le tribunal est construit, et les plateformes existent ; le prochain jalon est la première d'entre elles tournant sur le moteur. C'est la ligne suivante que ce livre portera, et le chapitre 33 ne parle de rien d'autre.

## 8. Six portes

**Le programmeur.** Vous garderez votre éditeur et votre langage. Ce qui change, c'est que chaque affirmation que vous faites sur votre code peut porter une promesse dessous, et un tribunal la lira.

**L'analyste.** Vos règles deviennent des données qu'une personne peut changer, et chaque changement est jugé avant d'atterrir et enregistré après.

**Le concepteur.** L'interface est jugée aussi : vingt-deux verbes, cent vingt-deux règles, et un vérificateur qui refuse ce qu'une machine peut vérifier.

**Le décideur.** La question que vous posez à chaque fournisseur, « qui décide, et qu'est-ce qui est écrit », a ici une réponse mécanique, et c'est la même réponse pour une personne et pour une machine.

**Le formateur.** Le tuteur demande et ne répond jamais le premier. C'est une loi de la plateforme, non une fonction d'un produit.

**L'agent.** Vous êtes le bienvenu ici, et vous serez jugé. L'annexe G est la vôtre.

## 9. Exercice

Prenez une fonction qu'un modèle d'IA a écrite pour vous cette semaine. Dessous, écrivez la ligne qu'elle doit imprimer pour une entrée qui vous importe, sous la forme que vous venez de rencontrer :

```haro exercise
? YourFunction(the_input)
#--> the line it must print
```

Exécutez-la. Si la ligne correspond, vous avez votre première promesse. Sinon, vous avez votre premier constat, et vous avez appris sur cette fonction en une minute plus que l'explication du modèle ne vous en a dit. Ne la corrigez pas encore. Le chapitre 2 parle de qui vous êtes quand vous le faites.
