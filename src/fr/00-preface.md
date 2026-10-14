---
id: preface
part: 0
number: 0
title: Préface
spine: true
narrations: []
guards: []
status: draft
rulings: []
---

## Une question que vous avez déjà

Vous utilisez un outil qui écrit du code. Vous lui demandez une fonction, ou une fonctionnalité entière, et il répond en quelques secondes. Vient alors la question qu'aucun outil ne résout pour vous : ce code doit-il entrer dans mon système ?

Vous avez toujours eu des moyens de répondre. Vous lancez les tests. Le vérificateur de types est d'accord, ou il ne l'est pas. Un collègue relit le changement. Ces moyens ont été faits quand on écrivait le code lentement. Aujourd'hui une seule phrase peut produire mille lignes, et personne n'a le temps de relire mille lignes pour chaque phrase.

Le code est devenu bon marché. La confiance, non. Ce livre revient sans cesse à une phrase, celle sur laquelle repose chaque chapitre : **le changement arrive plus vite que la confiance.**

## L'idée, en deux gestes

D'abord vous **déclarez**. En texte simple, vous dites ce qu'est une chose : une application (je l'appelle un *monde*), un langage, un agent d'IA, un produit entier. Ensuite vous **gouvernez**. De votre déclaration vous obtenez un juge, que j'appelle un *tribunal*. Un tribunal est un validateur construit à partir de votre déclaration. Il rend un verdict, *tenu* ou *refusé*, et la raison, dans les mots de votre déclaration.

Chaque changement passe devant le tribunal avant d'entrer, quel qu'en soit l'auteur : vous, un collègue, un script ou un modèle d'IA. Le modèle peut toujours tout proposer. Il ne peut rien décider. On l'interroge aussi en dernier : tout ce que des règles peuvent décider, les règles le décident d'abord.

## Une déclaration, en vrai code

Voici le cas le plus petit. Vous ajoutez à votre système un agent d'IA, un programme qui surveille les niveaux de stock et réapprovisionne. Vous ne commencez pas par son code. Vous commencez par un court fichier texte qui dit ce qu'il est : son nom, la fréquence à laquelle il tourne, ce qu'il peut faire, et si ses actions peuvent être défaites. Ce fichier est une déclaration. Vous le chargez, et le tribunal le lit avant que l'agent puisse jamais tourner. Le fichier de cet agent omet quelque chose. Que dit le tribunal ?

```haro
cPia = "pia: 1
name: stock-watcher
kind: pi
reversibility: compensable
schedule:
  timer: 20
skills:
  - name: restock
    does: learn stock level ordered
"
oD = StzAgentDeclarationQ(cPia)
? oD.IsValid()
#--> 0
? oD.CiteFindings()
#--> [pia-coverage @ coverage] an agent must say WHAT IT COVERS. The engine loop refuses to schedule an agent with no coverage statement (law 18), so a file without one could never run and is refused here instead of at the first tick.
```

Lisez-le en trois parties. Le texte entre les guillemets est la déclaration. La ligne suivante la charge. Ensuite `?` imprime une réponse, et la ligne après `#-->` est ce que le bloc a imprimé quand je l'ai lancé. Le tribunal répond `0` : refusé. Il nomme la règle et donne la raison : un agent doit dire ce qu'il couvre, parce que le moteur ne planifiera pas un agent qui ne le dit pas, donc le fichier est refusé maintenant et non à sa première exécution. Quelques mots du fichier : `pia` nomme le format du fichier, `compensable` veut dire que ses effets peuvent être défaits par une action de compensation, et `law 18`, dans la raison du tribunal, est le numéro que le moteur donne lui-même à sa règle selon laquelle un agent sans couverture n'est jamais planifié.

Vous pourriez écrire ce contrôle dans votre propre CI. Ici personne n'a eu à le faire. Le tribunal des agents est livré avec la bibliothèque, donc la règle est celle de la bibliothèque, et les faits sont les vôtres, dans la déclaration. Un simple assert dans un script de démarrage juge un seul fait. Une déclaration tient dans un seul texte tous les faits sur l'agent, et le même tribunal la juge, qu'elle ait été écrite par une personne, un script ou un modèle d'IA. La règle peut aussi être la vôtre : le chapitre 2 a une règle que vous écrivez en quelques lignes sur deux faits, qu'un acteur est un modèle de langage et qu'il détient un effet, un pouvoir d'agir sur le monde comme envoyer un courrier, et le tribunal trouve la violation dans votre propre graphe d'agents. Cet exemple est petit exprès, et un schéma peut le vérifier aussi. Le livre ne soutient pas qu'un tribunal vérifie plus qu'un schéma. Il soutient qu'un seul tribunal, construit à partir de votre déclaration, se tient devant chaque acteur et donne sa raison. Il ne lit pas mille lignes générées pour les déclarer bonnes : il vérifie qu'un changement tient dans ce que vous avez déclaré, et le chapitre 24 montre un changement essayé sur une copie de votre système avant que rien ne soit validé. Pour une chose à vous, par exemple un langage que vous inventez, le chapitre 12 montre comment faire le tribunal, et dit jusqu'où cela est construit. Le chapitre 1 raconte une deuxième scène, avec un service de courrier, et le chapitre 2 relance ce bloc.

Vous direz que vous avez déjà des tests, des schémas et des contrôles de politique dans votre CI. C'est vrai. Aujourd'hui ces règles vivent à plusieurs endroits : des tests ici, un schéma là, un fichier de politique ailleurs, chacun écrit à la main après le code. Ici vous les énoncez une seule fois, dans la déclaration, et le tribunal en découle. Le chapitre 22 compare honnêtement les deux, et là où le terrain fait mieux, il le dit. Un tribunal juge ce que vous avez déclaré. Il ne peut pas juger ce que vous avez omis, et la limite de chaque chapitre dit où cela s'arrête.

## Ce qu'est Softanza

Une plateforme logicielle gouvernée. Vous déclarez ce que vous savez d'un monde, en texte clair ; un tribunal construit à partir de cette déclaration le garde ; et le modèle d'IA, quand il y en a un, vient en dernier. C'est la ligne de la couverture, et chaque chapitre la fait tourner. Matériellement, Softanza est trois choses, et pour chacune je dis jusqu'où elle existe.

- Une **bibliothèque** que vous appelez depuis du code. Vous écrivez quelques lignes de Haro comme celles ci-dessus, et vous les lancez avec la bibliothèque chargée. La bibliothèque tient les déclarations et les tribunaux qui en sont faits. Sa source est à github.com/mayouni/stzlib, et chaque bloc de code de ce livre a tourné sur un commit nommé de celle-ci. Si votre travail est en Python ou en TypeScript, vous l'utiliseriez aujourd'hui à côté de votre code, non dedans : par une seule porte gouvernée elle peut exécuter du code en six autres langages, Python, NodeJS (JavaScript), R, Julia, Prolog et C, qui avec l'hôte font les sept du chapitre 16.
- Un **moteur** sous la bibliothèque, écrit en Zig, un langage système. Il fait le calcul réel, une seule fois et en un seul endroit, pour que chaque langage qui lui parle obtienne le même comportement. Il tourne aujourd'hui, et les domaines de la bibliothèque y passent un à un : le chapitre 4 dit lesquels calculent encore dans le langage hôte.
- Un **langage**, Haro, fait pour tenir les déclarations. Pour l'instant il emploie la syntaxe de sa première facette, si bien que tout le code écrit jusqu'ici tourne sans changement. Son propre exécutable est en développement : il a une charte et un premier essai.

Le chapitre 4 dessine les trois en une seule image.

## Où il en est

Softanza n'est pas un projet de recherche, même s'il repose sur une recherche profonde. Des projets réels l'ont façonné : un restaurant, une banque et une organisation, et leurs retours ont façonné sa conception. Des parties de Softanza sont en production. D'autres sont en développement, comme il est normal pour une plateforme neuve et aussi ambitieuse. Chaque chapitre dit laquelle est laquelle.

## Ce qu'est ce livre

C'est un livre d'arguments, avec du code qui tourne. Pour chaque question sur la programmation, sur les langages et sur l'intelligence, je fais quatre choses. Je donne la réponse que donne d'ordinaire le terrain. Je donne la réponse que prend Softanza. Je donne la décision que j'ai prise, et ce que j'ai refusé. Et je donne la preuve : le code a tourné, et les tests qui le prouvent sont nommés. La troisième, la décision et ce que j'ai refusé, est la raison d'être de ce livre : le site montre ce qui est, et ce n'est qu'ici que vous trouverez ce qui a été refusé. Je dis aussi ce que le terrain fait déjà bien, pour que vous puissiez comparer.

Il compte sept parties et trente-trois chapitres. Vous n'avez pas besoin de connaître Softanza ni Zig. Il vous faut avoir écrit du code, et avoir ressenti le doute ci-dessus. Le site du projet tient ses preuves, avec leurs démonstrations, et son cours enseigne le même terrain par des exercices. Ce livre tient l'argument.

Chaque chapitre a six courtes portes, vers sa fin. Une porte est une entrée pour un genre de lecteur : le programmeur, l'analyste, le concepteur, le décideur, le formateur et l'agent. L'agent est un programme d'IA, parce que le livre est aussi publié sous forme de données qu'un programme peut lire. Entrez par la porte qui est la vôtre aujourd'hui.

## Comment le lire

Lisez d'abord neuf chapitres. Ils portent tout l'argument et peuvent se lire seuls : les quatre de la partie I, les deux derniers, et trois qui énoncent chacun une règle que le livre tient partout. Chapitre 5 : le code doit se lire comme une personne pense. Chapitre 11 : un langage est déclaré et fermé. Chapitre 17 : un programme est programmatique par défaut, ce qui veut dire que les règles et le code décident d'abord, et que le modèle d'IA vient en dernier. Le lecteur a un bouton qui n'affiche que ces neuf. Revenez aux autres quand l'un d'eux vous intéresse.

Chaque chapitre a les mêmes neuf parties, dans le même ordre. L'idée telle que le terrain la tient aujourd'hui. Le premier principe. La forme qu'elle prend dans Softanza, en code. La décision, et ce que j'ai refusé. Le tribunal : les tests nommés qui prouvent l'affirmation du chapitre. Le terrain, et ce qu'il fait mieux. La limite. Les six portes. Un exercice, auquel vous répondez avant de le lancer. Les chapitres 5, 11 et 17 s'ouvrent par une courte section de plus, sur ce que l'ère de l'IA change.

Un nom de plus que vous rencontrerez. Softanza vous pose la question à laquelle vous devez répondre, dans vos propres mots, et refuse de deviner la réponse à votre place. J'appelle cette pratique le wise coding. Le chapitre 18 la fait tourner, registre par registre.

## À quoi se fier

Chaque bloc de code de ce livre a été lancé dans la bibliothèque. Sous chaque titre, la page dit quand, à quel commit, et combien de blocs ont tenu leur promesse : combien ont imprimé ce que dit la ligne après `#-->`. Si un bloc imprime autre chose, la construction échoue, et la page avec elle. Les exercices sont à vous de les lancer.

Deux mots reviennent sur bien des pages. Le *dossier* est l'ensemble des dépôts, des sessions et des fichiers sur lesquels ce livre a tourné, au commit imprimé sous chaque titre. L'*étude* est ma propre étude de ce dossier, faite avant la rédaction des chapitres. Quand une page dit que le dossier ne contient pas de réponse, elle parle de ces fichiers, à ce commit.

Quand un chapitre dit ce qui n'est pas fini, il emploie trois mots et aucun autre. *Construit* : le code existe, un test existe, et un bloc a tourné. *Conçu* : un document le dit, et rien ne tourne. *Absent* : j'ai cherché et je n'ai rien trouvé, et je dis jusqu'où j'ai cherché. Le site du projet emploie cinq noms pour les mêmes choses, et le chapitre 3 montre comment ils se ramènent à ces trois-là.

Une remarque de plus. L'exécutable propre de Haro est encore en développement, donc les blocs marqués `haro` tournent aujourd'hui sur le runtime du langage pour lequel la bibliothèque a d'abord été écrite, version 1.27, et chaque page le dit. L'annexe H, l'histoire du projet, raconte comment on en est arrivé là. Dans le code, les noms propres de la bibliothèque, ses classes, ses fichiers et ses clés, portent encore le nom de ce langage, et le porteront jusqu'à ce que la bibliothèque en soit retirée ; la prose, non.

## À propos de ce brouillon

Les chapitres ont été rédigés avec des agents d'IA, à partir des propres fichiers du projet, et chaque bloc de code a été lancé. Je n'ai pas encore lu toutes les pages, et chaque chapitre porte en haut un bandeau qui le dit jusqu'à ce que je les aie lues. Là où les fichiers ne contenaient aucune réponse à une question, la page le dit en une phrase simple et n'en invente pas. L'édition française est une traduction des brouillons anglais, et chaque page française le dit. Cette préface a été écrite après les chapitres, et elle reste inachevée jusqu'à ce que j'écrive la mienne. C'est le deuxième livre de ma maison d'édition, AYOUNI. Le premier, *Refinement-Oriented Programming*, parle d'une discipline pour le logiciel à l'ère des agents d'IA, racontée à travers une banque.
