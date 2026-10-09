---
id: law-the-code-adheres-to-the-way-a-person-thinks
part: 2
number: 5
title: "Loi : le code adhère à la façon dont une personne pense, et le tribunal le juge quel que soit celui qui l'a écrit"
law: "the code adheres to the way a person thinks, and the court judges it whoever wrote it"
spine: true
narrations: [stz-mental-mode-narration.md, stz-bridging-minds-and-code.md, stz-functions-as-linguistic-expressions.md, stzobject-history-narration.md, stz-near-natural-language-programming.md]
site: [learn, craft, principles]
guards: [coderule_narrated, testoor_promises_narrated, 05_containsemptystrings, 466_keeping_the_history_of_updates_of_a_softanza_objec]
stage:
  built: "les formes du vocabulaire dans des milliers de noms de méthodes ; les règles de la maison comme un tribunal sur le propre code de la bibliothèque ; la promesse lue par une machine dans la forme propre à la maison"
  designed: "un tribunal du style pour le code qu'un programmeur ou un agent écrit ; la grammaire d'écriture déclarée en Haro, pour qu'un modèle ne puisse écrire que dans elle"
  absent: "toute machine qui juge aujourd'hui le style d'un programme écrit avec la bibliothèque"
status: draft
rulings: ["12.2", "12.3", "12.14", "12.16", "12.17", "12.21"]
research: research/ch05.md
figures:
  - "promises per thousand lines, 98.9 / 75.1 / 52.5 / 0.7: study 12.16, measured at stzlib 93d7a39"
  - "fourteen house rules: StzCodeRuleNames(), run in chapter 32"
---

## Ce que l'âge de l'IA change ici

Pendant des années, la plupart du code écrit avec Softanza l'a été d'une seule main, et cette main était la mienne. Le style de la bibliothèque était simplement ma façon d'écrire. Puis les machines sont arrivées, et aujourd'hui la plupart du code, ici comme partout, est écrit par des modèles. La conception du plan de l'intelligence le dit en une phrase : la plupart de la programmation d'aujourd'hui est faite par des agents et des modèles de langage, pas par des humains.

Cela change ce qu'est un style. Un style qui vit dans les habitudes d'une seule personne meurt quand cette personne cesse d'écrire chaque ligne. Il doit devenir quelque chose à quoi l'on peut tenir une machine, et quelque chose qu'une machine peut vérifier, sinon il s'amenuise. Dans cette maison, il s'est amenuisé, et je vous montrerai où. Alors ce mouvement du livre, La programmation repensée, s'ouvre sur une loi qui a deux moitiés, et la seconde existe à cause de l'âge : le code adhère à la façon dont une personne pense, et le tribunal le juge quel que soit celui qui l'a écrit.

Il y a une dépendance à dire à voix haute. Ce livre suit l'ordre de sa couverture, du familier au nouveau : la programmation, puis les langages, puis l'intelligence. La logique propre du dossier va dans l'autre sens. Le premier acte est de déclarer un langage ; la programmation se passe à l'intérieur d'un langage déclaré ; l'intelligence est gouvernée par les deux. Les formes du vocabulaire sont déjà une déclaration en Haro, et l'usage que ce chapitre décrit, la scène, la chaîne, le paramètre nommé, la promesse sous chaque ligne, est destiné à en devenir une aussi. Lisez donc cette loi en sachant que la partie III la soutient.

## 1. Le concept, tel que le terrain le tient

Dans notre industrie, le « style de code » veut dire deux choses, et aucune ne concerne la façon dont une personne pense. La première est la mise en page et le nommage, imposés par des machines : le guide de style de Python depuis 2001, le formateur de Go depuis 2009, et les formateurs que tout projet moderne exécute avant un commit. Ils règlent les disputes sur les espaces et les majuscules, et ils y sont très bons. La seconde est l'interface fluide : des méthodes chaînées de sorte qu'une ligne se lise plus ou moins comme une phrase.

L'âge du code généré a ajouté une troisième pratique : vérifier après. Un modèle écrit, les tests et les linters lisent ce qu'il a écrit, et le modèle réessaie s'ils se plaignent. La ligne elle-même est jugée sur sa forme et son résultat. Savoir si elle suit l'ordre dans lequel celui qui l'a écrite raisonnait est une question que personne ne pose, parce que rien ne pourrait y répondre.

## 2. Le premier principe

Ma devise pour cela n'a pas changé depuis 2020 : **ce que vous pensez est ce que vous écrivez.**

## 3. La forme Softanza

La diapositive fondatrice de 2022 mettait toute l'idée sur une page. À gauche, les quatre étapes de la pensée d'une personne : je prends le mot « softanza » ; je le mets en majuscules ; j'obtiens ses caractères ; je les joins avec une espace. À droite, les mêmes quatre étapes en une ligne de code, comme si le texte de gauche avait été collé et exécuté.

Cette ligne exacte ne s'exécute plus. Son troisième maillon, une méthode qui transformait les caractères en une liste de chaînes en une seule étape, n'est pas dans la bibliothèque aujourd'hui ; il ne survit que dans un fichier archivé. Je vous le dis d'abord parce qu'un chapitre de loi qui cache son propre exemple fondateur ne mériterait pas votre confiance. Voici la forme la plus proche qui s'exécute, avec les quatre étapes toujours visibles, puis la forme que la bibliothèque offre comme un verbe dédié :

```haro
? StzListOfStringsQ( StzStringQ("softanza").UppercaseQ().Chars() ).ConcatenatedUsing(" ")
#--> S O F T A N Z A
? StzStringQ("softanza").UppercaseQ().Spacified()
#--> S O F T A N Z A
```

L'idée est intacte ; le maillon fluide a été perdu. Une demande part vers la bibliothèque pour le rétablir.

Le modèle mental est la même idée au niveau d'un problème. Vous dites le problème en mots simples. Vous choisissez l'objet qui tient les données. Puis vous demandez, dans l'ordre : contient-il ce qui m'importe, combien, où. Ensuite vous agissez sur ces positions, ou vous appelez le verbe qui le fait pour vous :

```haro
o1 = new stzList([ "A", "", "B", "", "", "C" ])
? o1.ContainsEmptyStrings()
#--> TRUE
? o1.CountEmptyStrings()
#--> 3
? @@( o1.FindEmptyStrings() )
#--> [ 2, 4, 5 ]
o1.ReplaceEmptyStrings(:With = "~")
? @@( o1.Content() )
#--> [ "A", "~", "B", "~", "~", "C" ]
```

Contenir, compter, trouver, agir. Chaque ligne est une étape de pensée, et les noms sont les mots que vous emploieriez pour la dire.

La forme du verbe dit ce qui arrive à l'objet. Le participe passé vous donne une copie changée et laisse l'objet tranquille ; le verbe simple agit sur l'objet ; le verbe avec Q agit et rend l'objet, pour que l'étape suivante puisse suivre :

```haro
o1 = new stzString("RIxxNxG")
? o1.Removed("x")
#--> RING
? o1.Content()
#--> RIxxNxG
o1.Remove("x")
? o1.Content()
#--> RING
? Q("rixxnxg").RemoveQ("x").UppercaseQ().Spacified()
#--> R I N G
```

Un paramètre est nommé, et le nom se lit comme de l'anglais. Vous n'avez pas besoin de retenir quel argument vient en second :

```haro
? Q("I love Haro").Replaced("love", :With = "♥")
#--> I ♥ Haro
o2 = new stzList([ "tea", "rice", "fish" ])
o2.SwapItems(:AtPositions = 1, :And = 3)
? @@( o2.Content() )
#--> [ "fish", "rice", "tea" ]
```

Quand plusieurs questions sont posées à une même chose, elles sont posées à l'intérieur de sa scène, un bloc d'accolades autour de l'objet, pour que l'objet soit nommé une seule fois et que les questions se lisent comme une liste :

```haro
Q("haro php HARO ruby Haro") {
	? NumberOfOccurrence(:Of = "haro")
	#--> 1
	? NumberOfOccurrenceCS(:Of = "haro", :CS = FALSE)
	#--> 3
	? @@( FindAllCS("haro", FALSE) )
	#--> [ 1, 10, 20 ]
}
```

Et les étapes de la pensée peuvent être relues. Un objet élevé avec son historique garde le résultat de chaque étape de sa chaîne :

```haro
? @@( Qh(12500).AddQ(500).RetrieveQ(1500).DivideByQ(500).MultiplyByQ(2).History() )
#--> [ 12500, 13000, 11500, 23, 46 ]
```

L'article qui a raconté cela le premier promettait quatre valeurs, sans la première, et une somme courte d'une unité. La garde derrière le bloc énonce la règle d'aujourd'hui : la valeur initiale, puis le résultat de chaque étape. Le livre prend la réponse de l'exécution, pas celle de l'article.

Remarquez la ligne sous chaque question. Ce n'est pas un commentaire. C'est une promesse, ce que la ligne doit imprimer, et dans cette maison elle est la forme d'un exemple depuis le premier jour : une courte histoire, quelques questions, et les réponses écrites dessous. C'est la première moitié de la loi, rendue visible : le code suit l'ordre de la pensée, et chaque étape dit ce qu'elle attend.

Maintenant la seconde moitié. Une règle qu'une personne doit retenir est du folklore. La bibliothèque transforme ses règles de maison en validateurs qui s'exécutent sur le graphe du code, pour qu'une personne ou un agent puisse vérifier une classe avant qu'elle n'atterrisse. Ici une classe enfreint la convention de la maison selon laquelle un verbe finissant en Q rend l'objet :

```haro
cCode = "class Basket" + nl + "def Add(x)" + nl + "	return x" + nl + "def AddQ(x)" + nl + "	return 42" + nl
? StzCodeIsClean(cCode)
#--> FALSE
? StzCheckCode(cCode)[1][:rule]
#--> q-returns-object
```

La règle ne se soucie pas de qui a écrit la classe. C'est toute la seconde moitié. Et la promesse sous chaque question est lue elle aussi par une machine : l'exécuteur de la bibliothèque juge une promesse comme une affirmation sur ce que la ligne a imprimé, de sorte que la plus ancienne forme d'exemple de la maison est aussi sa plus récente forme de test.

Les chapitres de cette partie prouvent la loi, chacun d'un côté. Le chapitre 6 raconte le modèle mental et les quatre métaphores qui remplacent les boucles : marcher, vérifier, produire, exécuter. Le chapitre 7 raconte le style d'écriture comme quatorze règles, et les sept buts de conception comme sa moitié architecturale. Le chapitre 8 raconte les formes que peut prendre le nom d'une fonction, et la portée nommée dans le verbe. Le chapitre 9 raconte les motifs de pensée : la machine qui réagit à ce qu'elle reconnaît, la programmation réactive en mots simples, et les moteurs de la vérité, de la quantité et du temps. Le chapitre 10 raconte comment la programmation devient raffinement.

## 4. La décision, et ce que j'ai refusé

**J'ai laissé aller l'implémentation de la bibliothèque.** Le code que les modèles ont écrit à l'intérieur de la bibliothèque est accepté comme bon. Il ne ressemble pas au mien. Ses variables locales portent des soulignés des deux côtés, des centaines de fois par millier de lignes, parce que le langage sous-jacent à Softanza laisse la variable locale d'une bibliothèque écraser la globale d'un appelant, et que la convention l'empêche. Je n'ai pas demandé l'ancien style là, et je refuserais une campagne pour l'imposer.

**J'ai refusé de laisser aller le style du code écrit avec Softanza.** Chaque ligne qu'un programmeur, une personne ou un agent, écrit avec la bibliothèque doit prendre le style historique : la scène, la chaîne une étape par ligne, le paramètre nommé, la forme du verbe, la promesse sous chaque question. C'est la ligne que j'ai tracée quand j'ai vu ce qui s'était passé.

Ce qui s'est passé est mesurable. Une étude du dossier a compté la promesse sous chaque ligne, par millier de lignes. Dans les courtes recettes que la maison garde, il y en a près de cent. Dans mes articles, soixante-quinze. Dans les tests classiques, cinquante-deux. Dans les gardes que les sessions ont écrites, moins d'une : elles affirment sous une autre forme, un appel qui nomme l'attente, qu'elles ont adoptée parce que l'exécuteur de l'époque ne savait pas distinguer un bloc qui avait échoué d'un bloc qui n'avait jamais tourné. Cet écart est comblé maintenant ; l'exécuteur lit la promesse comme une affirmation. L'étude qui les a comptées recommande que la forme classique, un titre, les questions et les promesses dessous, devienne la forme unique pour les nouveaux blocs de test, les blocs convertis restant tels qu'ils sont ; le dossier contient cette recommandation, et aucune décision de moi à ce sujet.

**J'ai refusé de réécrire le code quand le langage a changé de nom.** Quand le langage sous-jacent est devenu Haro, le code de mes articles a été renommé et rien d'autre. Les formes sont l'atout ; le nom est une étiquette.

**Les formes du vocabulaire sont devenues des données, et trois anciennes fonctionnalités ont été refusées comme grammaire.** En Haro, les formes que peut prendre un verbe sont déclarées une fois et générées, et les noms livrés de la bibliothèque sont jugés contre la déclaration. La conception de ce travail refuse trois choses que le diaporama de 2022 comptait comme des fonctionnalités : des noms qui tolèrent une faute d'orthographe, des paramètres dans n'importe quel ordre, et des noms de méthodes dans d'autres langues humaines. Elles restent possibles dans la bibliothèque ; elles ne font pas partie de la grammaire à laquelle une machine est tenue. Le refus est écrit dans le fichier des principes du langage, comme son septième principe, marqué conçu ; le livre l'imprime comme celui de la conception, et le dossier ne dit pas qu'il est le mien.

**J'ai choisi les buts avant les lois.** La conception de 2022 tenait sept buts, l'expressivité, la flexibilité, la fiabilité, la cohérence, les métaphores humaines, les abstractions pratiques et la maniabilité, et chaque fonctionnalité en servait un. Les règles de fonctionnement d'aujourd'hui sont des lois payées par des incidents, qui disent comment et non pourquoi. Le chapitre 7 remet les buts à côté des lois.

## 5. Le tribunal

`coderule_narrated` prouve qu'une règle de la maison est une règle sur le graphe du code, que les constats sortent sur du code planté, que le code propre passe, et que les règles sont quatorze. `testoor_promises_narrated` prouve que la promesse est jugée par une machine dans la forme propre à la maison, chaque règle plantée dans les deux sens : le mensonge qu'elle doit attraper, et la vérité qu'elle ne doit pas accuser. `05_containsemptystrings` est les étapes du modèle mental sur la même liste, un bloc classique gardé comme une garde. `466_keeping_the_history_of_updates_of_a_softanza_objec` prouve l'historique d'une chaîne.

## 6. Le terrain, et où il mène

Le terrain mène sur l'application des règles. Tout langage courant a un formateur et un linter qui s'exécutent à chaque commit par défaut. Le tribunal qui jugerait le style d'un programme écrit avec Softanza est une spécification ; celui qui existe juge les propres classes de la bibliothèque.

Le terrain mène en portée et en gens. Il y a un marché du travail pour ses outils et aucun encore pour celui-ci, et les générateurs du terrain sont les plus grands qui existent.

Le terrain mène aussi, aujourd'hui, sur les propres pages de Softanza. L'étude qui a mesuré le dossier a trouvé que les blocs de code du site ne portent ni paramètre nommé ni scène : un dialecte réduit de la bibliothèque, montré à chaque visiteur et à chaque agent qui apprend du site. Un style qui n'est pas montré n'est pas appris.

Là où je pense que Softanza se distingue, c'est dans ce à quoi le style est lié. Un formateur juge la forme d'une ligne ; une interface fluide rend une ligne agréable. Ici la ligne est liée à une étape de pensée, la forme du verbe est un contrat sur l'objet, et la promesse sous la ligne est l'exemple, le test et la documentation à la fois.

## 7. La limite

Ce qui est construit : les formes du vocabulaire, dans des milliers de noms de méthodes ; les règles de la maison comme un tribunal sur le propre code de la bibliothèque ; la promesse jugée par une machine.

Ce qui est conçu : un tribunal du style pour le code qu'un programmeur ou un agent écrit avec la bibliothèque, qui lirait un argument positionnel là où un argument nommé existe, une question sans promesse, une chaîne sur une ligne au-delà de deux étapes ; et la grammaire d'écriture déclarée en Haro, pour que la sortie d'un modèle y soit tenue avant d'être écrite.

Ce qui est absent : toute machine qui juge, aujourd'hui, le style d'un programme écrit avec la bibliothèque. La chaîne de la diapositive fondatrice ne s'exécute pas telle qu'écrite. Dans ce livre, la discipline porte le nom de sa devise : ce que vous pensez est ce que vous écrivez.

## 8. Six portes

**Le programmeur.** Vos lignes suivent votre raisonnement : sélectionner, contenir, compter, trouver, agir. Chaque question porte sa promesse, et un tribunal la lit que vous l'ayez écrite ou qu'un agent l'ait fait.

**L'analyste.** La méthode part de votre problème en mots simples. Les mots-clés que vous employez deviennent les noms des étapes.

**Le concepteur.** La forme du verbe est un contrat d'interface : le participe passé ne touche jamais l'objet.

**Le décideur.** Un style auquel une machine peut être tenue peut être relu but par but, non ligne par ligne, ce qui est la seule lecture qu'une personne puisse donner à des centaines de milliers de lignes.

**Le formateur.** Le cours enseigne la discipline entière, et dans l'ordre : formuler, puis exprimer, puis être jugé.

**L'agent.** Vous serez corrigé par la bibliothèque, non par le folklore. Écrivez la question, puis la promesse dessous.

## 9. Exercice

Prenez la liste `[ "tea", "", "rice", "", "fish", "" ]`. Écrivez dans l'ordre les questions du modèle mental, une ligne chacune : contient-elle des chaînes vides, combien, où. Puis un acte, avec un paramètre nommé. Sous chaque question, écrivez la ligne qu'elle doit imprimer, avant d'exécuter quoi que ce soit.

Exécutez. Puis demandez à un agent de résoudre le même problème, et jugez sa réponse avec deux questions seulement : chaque ligne suit-elle une étape de pensée, et chaque question porte-t-elle sa promesse.
