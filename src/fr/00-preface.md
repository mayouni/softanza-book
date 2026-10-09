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

Ceci est le deuxième livre de la collection AYOUNI. Le premier, *Refinement-Oriented Programming*, racontait une discipline à travers une banque. Celui-ci raconte la plateforme qui se trouve en dessous : Softanza, une bibliothèque et un moteur, et un langage encore en construction, tous façonnés par une seule idée. Déclarez une chose, puis gouvernez-la. Une personne dit ce qu'est un langage, ce qu'est un monde, ce qu'est une solution, et un tribunal fait à partir de la déclaration juge celui qui la parle, personne ou modèle. Le chapitre 12 dit jusqu'où cela est construit : la bibliothèque juge une déclaration au moment où elle est déclarée, et la forge qui fait le tribunal et la grammaire d'un langage à partir de sa déclaration est construite hors de la bibliothèque.

Je l'ai écrit comme un document qui s'exécute. Chaque bloc de code qu'il contient, sauf les exercices, qu'il vous revient d'exécuter, a été exécuté dans la bibliothèque, à un commit que la page nomme, et jugé contre les lignes qui commencent par `#-->`, qui disent ce que le bloc a imprimé. Si un bloc n'imprime pas ce qu'il promet, la construction échoue, et la page avec elle. C'est pourquoi le livre n'est pas terminé le jour où il est écrit : il est terminé chaque fois qu'il s'exécute.

**Comment le lire.** Le livre compte sept parties et trente-trois chapitres. Neuf d'entre eux, la colonne, portent tout l'argument et peuvent être lus seuls : les quatre de la première partie, les trois qui énoncent chacun une loi (chapitres 5, 11 et 17), et les deux derniers. Le lecteur dispose d'un bouton qui n'affiche que la colonne. Lisez-la d'abord, et revenez au reste quand une de ses portes vous intéresse.

Chaque chapitre a les mêmes neuf éléments, dans le même ordre. Les trois chapitres qui énoncent une loi (5, 11 et 17) s'ouvrent sur une courte section de plus, sur ce que l'âge de l'IA change. Les neuf : le concept tel que le terrain le tient aujourd'hui ; le premier principe ; la forme qu'il prend dans Softanza, en code ; la décision, et ce que j'ai refusé ; le tribunal, qui est la liste des gardes qui le prouvent ; le terrain, avec ce qu'il possède et qui manque à Softanza ; la limite ; six portes, une pour le programmeur, l'analyste, le concepteur, le décideur, le formateur et l'agent ; et un exercice auquel vous répondez avant de l'exécuter. La forme de chaque chapitre place la limite en septième.

**Les trois mots d'étape.** Chaque limite est énoncée en trois mots et aucun autre. *Construit* : le code existe, une garde existe, et un bloc s'est exécuté. *Conçu* : un document le dit, et rien ne s'exécute. *Absent* : j'ai cherché, et je dis jusqu'où. Le site emploie cinq noms : construit, en construction, spécification, proposition ratifiée et nommé. Le chapitre 3 imprime comment ils se replient sur ces trois-ci.

**Ce que la page dit d'elle-même.** Sous chaque titre, une ligne dit quand les blocs se sont exécutés, à quel commit de la bibliothèque, et combien ont tenu leur promesse. Une deuxième ligne dit ce qui les a exécutés : le runtime de l'ancien langage hôte, celui sur lequel la bibliothèque tournait avant Haro, version 1.27. Haro, le langage dans lequel ce livre est écrit, n'a pas encore d'exécutable et n'exécute pas la bibliothèque, si bien que les blocs balisés `haro` tournent sur ce runtime plus ancien, et chaque page le dit. Les binaires du moteur sont copiés d'une construction faite dans une copie du même commit. Cette construction n'est pas épinglée, et la page dit à quel point elle est récente et quels commits du moteur l'ont suivie.

**Un brouillon est un brouillon.** Chaque chapitre porte un bandeau qui dit qu'il n'a pas été lu par l'auteur. Les questions auxquelles le dossier n'a pas pu répondre étaient autrefois marquées dans les pages. Il y a été répondu en mon nom, par des règles qui n'inventent rien : là où le dossier ne contient rien, la page le dit en une phrase simple et ne comble pas le vide. Ces réponses sont déléguées, et je peux revenir sur chacune en éditant la page. Vous voyez où le dossier s'arrête.

**Les trois médias.** Le site tient le dossier, avec ses lignes de preuve. Le cours, dans le programme d'éducation de la bibliothèque, enseigne le même terrain en quatre langues, dont le français, l'arabe et le haoussa sont des brouillons qu'aucun locuteur natif n'a relus (la page éducation du site, lue le 9 octobre 2026), et par des exercices jugés en exécutant le programme de l'apprenant. Ce livre tient l'argument. Là où ils diffèrent, la page le dit.

**Ce qui est dû.** Le dernier chapitre porte sur une ligne que le dossier ne porte pas encore : une solution qui a tourné sur le moteur propre de Softanza, et ce qu'un utilisateur nommé en a dit. Trois projets, un restaurant, une banque et une organisation, ont enseigné la bibliothèque, et aucun ne tourne encore dessus. J'ai écrit le chapitre avant que la ligne existe, et il faudra l'écrire de nouveau quand la ligne existera.

L'édition française existe comme traduction des brouillons anglais. Chaque page française le dit, et elle est relue une fois que j'ai marqué la page anglaise comme lue.

Le livre parle avec la voix de l'auteur, c'est pourquoi il dit « je ». Cette préface a été écrite après la première rédaction des chapitres, par la session qui les a rédigés, et elle n'a pas été relue depuis les modifications ultérieures des chapitres. Elle ne dit rien de la raison pour laquelle le livre a été écrit, puisque le dossier ne la dit pas. Elle reste une page de travail.
