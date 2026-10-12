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

Dans ce chapitre, je prends les deux choses que le terrain appelle style de code et je pose la question qu'il ne pose pas : si une ligne suit l'ordre dans lequel celui qui l'a écrite a raisonné. J'exécute l'exemple fondateur dans la forme la plus proche qui s'exécute encore, puis le modèle mental sur une liste, les formes du verbe, le paramètre nommé, la scène et l'historique d'une chaîne, avec une promesse sous chaque question. Je dis ce que j'ai laissé aller, l'implémentation propre de la bibliothèque, et ce que j'ai refusé de laisser aller, le style du code écrit avec elle. Je montre le tribunal qui existe aujourd'hui, sur les propres classes de la bibliothèque, et celui qui n'est que conçu. La devise n'a pas changé depuis 2020 : ce que vous pensez est ce que vous écrivez.

## Ce que l'âge de l'IA change ici

Pendant des années, la plupart du code écrit avec Softanza l'a été d'une seule main, et cette main était la mienne. Le style de la bibliothèque était ma façon d'écrire. Puis les machines sont arrivées, et aujourd'hui la plupart du code, ici comme partout, est écrit par des modèles. La conception du volet de l'intelligence le dit en une phrase : la plupart de la programmation d'aujourd'hui est faite par des agents et des modèles de langage, pas par des humains.

Cela change ce qu'est un style. Un style qui vit dans les habitudes d'une seule personne meurt quand cette personne cesse d'écrire chaque ligne. Il doit devenir quelque chose à quoi l'on peut tenir une machine, et quelque chose qu'une machine peut vérifier, sinon il s'amenuise. Dans cette maison, il s'est amenuisé, et je vous montrerai où. Alors ce mouvement du livre, La programmation repensée, s'ouvre sur une loi qui a deux moitiés. La seconde existe à cause de l'âge : le code adhère à la façon dont une personne pense, et le tribunal le juge quel que soit celui qui l'a écrit. Par le tribunal, j'entends la machine qui juge un code selon les règles de la maison ; aujourd'hui elle ne juge que les propres classes de la bibliothèque, et la section 5 dit comment.

Il y a une dépendance à dire à voix haute. Ce livre suit l'ordre de sa couverture, du familier au nouveau : la programmation, puis les langages, puis l'intelligence. La logique propre du dossier va dans l'autre sens. Le premier acte est de déclarer un langage ; la programmation se passe à l'intérieur d'un langage déclaré ; l'intelligence est gouvernée par les deux. Les formes du vocabulaire sont déjà déclarées dans un prototype de Haro (sa charte, entrée du 3 octobre 2026). L'usage que ce chapitre décrit, la scène, la chaîne, le paramètre nommé, la promesse sous chaque ligne, est destiné à être déclaré aussi. Lisez donc cette loi en sachant que la partie III la soutient.

## 1. Le concept, tel que le terrain le tient

Dans notre industrie, le « style de code » veut dire deux choses, et aucune ne concerne la façon dont une personne pense. La première est la mise en page et le nommage, imposés par des machines : le guide de style de Python depuis 2001, le formateur de Go depuis 2009, et les formateurs que tout projet moderne exécute avant un commit. Ils règlent les disputes sur les espaces et les majuscules, et ils y sont bons. La seconde est l'interface fluide : des méthodes chaînées de sorte qu'une ligne se lise presque comme une phrase.

L'âge du code généré a ajouté une troisième pratique : vérifier après. Un modèle écrit, les tests et les linters lisent ce qu'il a écrit, et le modèle réessaie s'ils se plaignent. La ligne elle-même est jugée sur sa forme et son résultat. Savoir si elle suit l'ordre dans lequel celui qui l'a écrite raisonnait est une question pour laquelle je ne connais aucun outil.

## 2. Le premier principe

Ma devise pour cela n'a pas changé depuis 2020 : **ce que vous pensez est ce que vous écrivez.**

## 3. La forme Softanza

La diapositive fondatrice mettait toute l'idée sur une page. Sur la gauche, les quatre étapes de la pensée d'une personne : je prends le mot « softanza » ; je le mets en majuscules ; j'obtiens ses caractères ; je les joins avec une espace. Sur la droite, les mêmes quatre étapes en une ligne de code, comme si le texte de gauche avait été collé et exécuté.

Cette ligne exacte ne s'exécute plus. Son troisième maillon, une méthode qui transformait les caractères en une liste de chaînes en une seule étape, n'est pas dans la bibliothèque aujourd'hui. Il ne survit que dans des fichiers archivés et dans un échantillon de travail, sous la forme `CharsQRT`. Je vous le dis d'abord parce qu'un chapitre de loi qui cache son propre exemple fondateur ne mériterait pas votre confiance. Voici la forme la plus proche qui s'exécute, avec les quatre étapes toujours visibles, puis la forme que la bibliothèque offre comme un verbe dédié :

```haro
? StzListOfStringsQ( StzStringQ("softanza").UppercaseQ().Chars() ).ConcatenatedUsing(" ")
#--> S O F T A N Z A
? StzStringQ("softanza").UppercaseQ().Spacified()
#--> S O F T A N Z A
```

L'idée est intacte ; le maillon fluide a été perdu. Une demande part vers la bibliothèque pour le rétablir.

Le modèle mental est la même idée au niveau d'un problème. Vous dites le problème en mots simples. Vous choisissez l'objet qui tient les données. Puis vous demandez, dans l'ordre : contient-il ce qui m'importe, combien, où ? Ensuite vous agissez sur ces positions, ou vous appelez le verbe qui le fait pour vous. Prenez une liste qui contient des chaînes vides. En contient-elle, combien, et où ? Exécutez :

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

La liste répond `TRUE`, puis `3`, puis `[ 2, 4, 5 ]`. Contenir, compter, trouver, agir. Chaque ligne est une étape de pensée, et les noms sont les mots que vous emploieriez pour la dire.

La forme du verbe dit ce qui arrive à l'objet. Que fait chaque forme à l'objet ? Par convention de la bibliothèque, le participe passé vous donne une copie changée et laisse l'objet tranquille. Le verbe simple agit sur l'objet. Le verbe avec Q agit et rend l'objet, pour que l'étape suivante puisse suivre :

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

Quand plusieurs questions sont posées à une même chose, elles sont posées à l'intérieur de sa scène, un bloc d'accolades autour de l'objet. L'objet est nommé une seule fois, et les questions se lisent comme une liste :

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

Les étapes de la pensée peuvent-elles être relues ? Un objet élevé avec son historique garde le résultat de chaque étape de sa chaîne :

```haro
? @@( Qh(12500).AddQ(500).RetrieveQ(1500).DivideByQ(500).MultiplyByQ(2).History() )
#--> [ 12500, 13000, 11500, 23, 46 ]
```

Cinq valeurs, la valeur de départ comprise, et la chaîne se termine à 46 ! L'article qui a raconté cela le premier promettait quatre valeurs, sans la première, et une valeur finale courte d'une unité, 45. La garde derrière le bloc énonce la règle d'aujourd'hui, sur une chaîne de texte : la valeur initiale, puis le résultat de chaque étape. Le livre prend la réponse de l'exécution, pas celle de l'article.

Remarquez la ligne sous chaque question. Ce n'est pas un commentaire. C'est une promesse, ce que la ligne doit imprimer. Dans cette maison, elle est la forme d'un exemple depuis le premier jour : une courte histoire, quelques questions, et les réponses écrites dessous. C'est la première moitié de la loi, rendue visible : le code suit l'ordre de la pensée, et chaque étape dit ce qu'elle attend.

Maintenant la seconde moitié. Une règle qu'une personne doit retenir est du folklore ; je le tiens pour une vue, non pour un résultat. La bibliothèque transforme ses règles de maison en validateurs, dont cinq sur quatorze s'exécutent sur le graphe du code, pour qu'une personne ou un agent puisse vérifier une classe avant qu'elle n'atterrisse. Ici une classe enfreint la convention de la maison selon laquelle un verbe finissant en Q rend l'objet. Cette règle a besoin des instructions de retour, que le graphe ne modélise pas, et elle s'exécute donc comme un passage sur le texte. Que dit le tribunal de la classe ? Exécutez :

```haro
cCode = "class Basket" + nl + "def Add(x)" + nl + "	return x" + nl + "def AddQ(x)" + nl + "	return 42" + nl
? StzCodeIsClean(cCode)
#--> FALSE
? StzCheckCode(cCode)[1][:rule]
#--> q-returns-object
```

Le tribunal répond `FALSE`, et nomme la règle : `q-returns-object`. Il n'a pas demandé qui avait écrit la classe ! C'est toute la seconde moitié. Et la promesse sous chaque question est lue elle aussi par une machine : l'exécuteur de la bibliothèque juge une promesse comme une affirmation sur ce que la ligne a imprimé. La plus ancienne forme d'exemple de la maison est aussi sa plus récente forme de test.

Les chapitres de cette partie prouvent la loi, chacun d'un côté. Le chapitre 6 raconte le modèle mental et les quatre métaphores qui remplacent les boucles : marcher, vérifier, produire, exécuter. Le chapitre 7 raconte le style d'écriture comme quatorze règles qui lui sont propres, et non les quatorze règles de la maison du tribunal plus bas, et les sept buts de conception comme sa moitié architecturale. Le chapitre 8 raconte les formes que peut prendre le nom d'une fonction, et la portée nommée dans le verbe. Le chapitre 9 raconte les motifs de pensée : la machine qui réagit à ce qu'elle reconnaît, la programmation réactive en mots simples, et la ligne de temps, la grille et les opérations profondes. Le chapitre 10 raconte comment la programmation devient raffinement.

## 4. La décision, et ce que j'ai refusé

**J'ai laissé aller l'implémentation de la bibliothèque.** Le code que les modèles ont écrit à l'intérieur de la bibliothèque est accepté comme bon. Il ne ressemble pas au mien. Ses variables locales portent des soulignés des deux côtés, des centaines de fois par millier de lignes, parce que le langage sous-jacent à Softanza laisse la variable locale d'une bibliothèque écraser la globale d'un appelant, et que la convention l'empêche. Je n'ai pas demandé l'ancien style là, et je refuserais une campagne pour l'imposer.

**J'ai refusé de laisser aller le style du code écrit avec Softanza.** Chaque ligne qu'un programmeur, une personne ou un agent, écrit avec la bibliothèque doit prendre le style historique. Ce style, c'est la scène, la chaîne une étape par ligne, le paramètre nommé, la forme du verbe, et la promesse sous chaque question. C'est la ligne que j'ai tracée quand j'ai vu ce qui s'était passé.

Ce qui s'est passé est mesurable. Une étude du dossier a compté la promesse sous chaque ligne, par millier de lignes. Dans les courtes recettes que la maison garde, il y en a près de cent. Dans mes articles, soixante-quinze. Dans les tests classiques, cinquante-deux. Dans les gardes que les sessions ont écrites, moins d'une. Elles affirment sous une autre forme, un appel qui nomme l'attente. Elles l'ont adoptée parce que les comparaisons nues des anciennes suites imprimaient 0 ou 1, ce qui ne distingue pas un bloc qui a échoué d'un bloc qui n'a jamais tourné. Cet écart est comblé maintenant ; l'exécuteur lit la promesse comme une affirmation. L'étude qui les a comptées recommande que la forme classique, un titre, les questions et les promesses dessous, devienne la forme unique pour les nouveaux blocs de test, les blocs convertis restant tels qu'ils sont. Le dossier contient cette recommandation, et aucune décision de moi à ce sujet.

**J'ai refusé de réécrire le code quand le langage a changé de nom.** Quand le langage sous-jacent est devenu Haro, le code de mes articles a été renommé et rien d'autre. Les formes sont l'atout ; le nom est une étiquette.

**Les formes du vocabulaire sont devenues des données, et trois anciennes fonctionnalités ont été refusées comme grammaire.** En Haro, les formes que peut prendre un verbe sont déclarées une fois et générées, et dans le prototype du langage les noms livrés de la bibliothèque sont jugés contre la déclaration. Sa charte rapporte 584 des 595 orthographes livrées de la classe de chaînes en accord (entrée du 3 octobre 2026). La conception de ce travail refuse trois choses que le dossier comptait comme des fonctionnalités : des noms qui tolèrent une faute d'orthographe, des paramètres dans n'importe quel ordre, et des noms de méthodes dans d'autres langues humaines. Le diaporama fondateur comptait les deux dernières ; la narration des formes comptait la première. La tolérance aux fautes et l'ordre libre restent dans la bibliothèque, en partie ; les noms multilingues ne survivent que dans un fichier archivé. Aucune des trois ne fait partie de la grammaire à laquelle une machine est tenue. Le refus est écrit dans le fichier des principes du langage, comme son septième principe, marqué conçu ; le livre l'imprime comme celui de la conception, et le dossier ne dit pas qu'il est le mien.

**J'ai choisi les buts avant les lois.** La conception de 2022 tenait sept buts, l'expressivité, la flexibilité, la fiabilité, la cohérence, les métaphores humaines, les abstractions pratiques et la maniabilité, et chaque fonctionnalité en servait un. Les règles de fonctionnement d'aujourd'hui sont des lois payées par des incidents, qui disent comment et non pourquoi. Le chapitre 7 remet les buts à côté des lois.

## 5. Le tribunal

`coderule_narrated` prouve qu'une règle de la maison est une règle sur le graphe du code, que les constats sortent sur du code planté, que le code propre passe, et que les règles de la maison de la bibliothèque sont quatorze. `testoor_promises_narrated` prouve que la promesse est jugée par une machine dans la forme propre à la maison, chaque règle plantée dans les deux sens : le mensonge qu'elle doit attraper, et la vérité qu'elle ne doit pas accuser. `05_containsemptystrings` est les étapes du modèle mental sur la même liste, un bloc classique gardé comme une garde. `466_keeping_the_history_of_updates_of_a_softanza_objec` prouve l'historique d'une chaîne.

## 6. Le terrain, et où il mène

Le terrain mène sur l'application des règles. La plupart des langages courants ont un formateur et un linter, et la plupart des projets les exécutent avant un commit ou en intégration continue. (Connaissance générale, non une étude du dossier.) Le tribunal qui jugerait le style d'un programme écrit avec Softanza est une spécification ; celui qui existe juge les propres classes de la bibliothèque.

Le terrain mène en portée et en gens. Il y a un marché du travail pour ses outils et aucun encore pour celui-ci, et les générateurs du terrain sont les plus grands qui existent.

Le terrain mène aussi, aujourd'hui, sur les propres pages de Softanza. L'étude qui a mesuré le dossier a trouvé que les blocs de code du site ne portent ni paramètre nommé ni scène : un dialecte réduit de la bibliothèque, montré à chaque visiteur. Un agent qui apprendrait du site apprendrait ce dialecte. Je n'ai pas mesuré de nouveau les blocs du site. Un style qui n'est pas montré n'est pas appris.

Là où je pense que Softanza se distingue, c'est dans ce à quoi le style est lié. Un formateur juge la forme d'une ligne ; une interface fluide rend une ligne agréable. Ici la ligne est liée à une étape de pensée, la forme du verbe est un contrat sur l'objet, et la promesse sous la ligne est l'exemple, le test et la documentation à la fois.

## 7. La limite

Ce qui est construit : les formes du vocabulaire, dans des milliers de noms de méthodes ; les règles de la maison comme un tribunal sur le propre code de la bibliothèque ; la promesse jugée par une machine.

Ce qui est conçu : un tribunal du style pour le code qu'un programmeur ou un agent écrit avec la bibliothèque. Il lirait un argument positionnel là où un argument nommé existe, une question sans promesse, une chaîne sur une ligne au-delà de deux étapes. Et la grammaire d'écriture déclarée en Haro, pour que la sortie d'un modèle y soit tenue avant d'être écrite.

Ce qui est absent : toute machine qui juge, aujourd'hui, le style d'un programme écrit avec la bibliothèque. La chaîne de la diapositive fondatrice ne s'exécute pas telle qu'écrite. Dans ce livre, la discipline porte le nom de sa devise : ce que vous pensez est ce que vous écrivez.

## 8. Six portes

**Le programmeur.** Vos lignes suivent votre raisonnement : sélectionner, contenir, compter, trouver, agir. Chaque question porte sa promesse, et un tribunal la lit que vous l'ayez écrite ou qu'un agent l'ait fait.

**L'analyste.** La méthode part de votre problème en mots simples. Les mots-clés que vous employez deviennent les noms des étapes.

**Le concepteur.** La forme du verbe est un contrat d'interface : par convention de la bibliothèque, le participe passé ne touche pas l'objet. Un tribunal pour cette règle est conçu, non construit.

**Le décideur.** Je tiens cela pour une vue, non pour un résultat : un style auquel une machine peut être tenue peut être relu but par but, non ligne par ligne, ce qui est la seule lecture qu'une personne puisse donner à des centaines de milliers de lignes.

**Le formateur.** Enseignez la discipline entière, et dans l'ordre : formuler, puis exprimer, puis être jugé.

**L'agent.** Vous serez corrigé par la bibliothèque, non par le folklore. Écrivez la question, puis la promesse dessous.

## 9. Exercice

Prenez la liste `[ "tea", "", "rice", "", "fish", "" ]`. Écrivez dans l'ordre les questions du modèle mental, une ligne chacune : contient-elle des chaînes vides, combien, où. Puis un acte, avec un paramètre nommé. Sous chaque question, écrivez la ligne qu'elle doit imprimer, avant d'exécuter quoi que ce soit.

Exécutez. Puis demandez à un agent de résoudre le même problème, et jugez sa réponse avec deux questions seulement : chaque ligne suit-elle une étape de pensée, et chaque question porte-t-elle sa promesse.

Le chapitre suivant est le modèle mental, et les métaphores. Là où vous écririez une boucle, il vous demande de nommer plutôt le mouvement que vous faites : marcher, vérifier, produire ou exécuter.
