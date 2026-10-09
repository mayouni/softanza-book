---
id: the-mental-model-and-the-metaphors
part: 2
number: 6
title: Le modèle mental, et les métaphores
spine: false
narrations: [stz-mental-mode-narration.md, stzwalker-beyond-loops-the -walker-metaphor.md, stzwalker-walking-at-the-edge-narration.md, stz-conditional-code-narration.md, stz-bridging-minds-and-code.md]
site: [learn, craft]
guards: [00_yielder_narrated, 597_walker_basics, 611_checkw, 621_perform, 483_w_and_wf_forms_in_conditional_code, 495_walking_until_and_until_before]
stage:
  built: "le marcheur à une dimension, le vérificateur, le producteur et l'exécutant sur les listes ; le langage de condition compilé par le moteur, avec son jumeau en code hôte"
  designed: "les quatre métaphores comme modules natifs du moteur (seul le producteur en est un) ; un marcheur sur toute structure indexée"
  absent: "du code exécutable pour les trois modèles de l'article « Bridging Minds and Code » ; la table des bords de la narration du marcheur telle qu'écrite"
status: draft
rulings: ["12.3", "12.6", "12.14", "12.16", "12.17"]
research: research/ch06.md
---

## 1. Le concept, tel que le terrain le tient

Le terrain a un seul outil pour répéter une chose, la boucle, et une famille de cousins qui la cachent : l'itérateur, la compréhension, le flux avec son map, filter et reduce, la lambda qui porte une condition. Ce sont de bons outils, et ils partagent tous une habitude. Ils sont écrits dans le langage du mouvement de la machine : un index qui commence à zéro, un compteur qu'on incrémente, une variable qui accumule. Une personne qui lit la boucle doit retrouver la question qu'elle pose.

Le terrain a aussi un vocabulaire de métaphores pour la programmation, mais il les garde dans la documentation. Le code reste une boucle.

## 2. Le premier principe

**Dites le problème en mots simples, posez les mêmes questions dans le même ordre à n'importe quel objet, et quand vous écririez une boucle, nommez le mouvement que vous faites : marcher, vérifier, produire ou exécuter.** La page Craft du site le dit, dans les mots d'une session du 2 octobre 2026, tels que la page les donne le 9 octobre 2026 : « Une boucle cache quel mouvement elle fait. Softanza nomme les quatre mouvements, et une tâche est décomposée en eux à la place. » Cette phrase est celle du site, non la mienne ; la phrase ci-dessus est le principe de ce chapitre.

## 3. La forme Softanza

Le modèle mental compte sept étapes, et ce sont celles dans l'ordre desquelles une personne demande. Définir le problème en termes naturels et en prendre les mots-clés. Choisir l'objet qui tient les données. Demander s'il contient ce qui vous importe. Demander combien. Demander où. Agir sur ces positions, ou appeler le verbe qui le fait. Et célébrer, et recommencer. Au chapitre 5, vous avez exécuté ces étapes sur une liste de chaînes vides. Elles n'appartiennent pas à la liste. Les voici sur une chaîne, dans le même ordre :

```haro
o1 = new stzString("You and you")
? o1.ContainsCS("YOU", FALSE)
#--> TRUE
? o1.NumberOfOccurrenceCS("YOU", FALSE)
#--> 2
? o1.FindNthCS(2, "YOU", FALSE)
#--> 9
o1.ReplaceSection(9, 11, :With = "Me")
? o1.Content()
#--> You and Me
```

Contenir, compter, trouver, agir, et le même suffixe qui dit si la casse compte. Les trois questions que vous posez à une chaîne sont les trois que vous avez posées à une liste.

Quand les étapes se répètent, la boucle apparaît, et c'est là que la bibliothèque vous donne quatre métaphores à la place. Chacune nomme un mouvement.

**Le Marcheur se déplace le long d'une route.** Un marcheur est une carte de tout son voyage, construite à sa création : les positions qu'il visitera, les positions qu'il sautera, où il se tient, ce qui reste.

```haro
oWalker = Wk(1, 10, 2)
? @@( oWalker.Walkables() )
#--> [ 1, 3, 5, 7, 9 ]
? @@( oWalker.Unwalkables() )
#--> [ 2, 4, 6, 8, 10 ]
? @@( oWalker.Walk() )
#--> [ 1, 3 ]
? oWalker.CurrentPosition()
#--> 3
? @@( oWalker.RemainingWalkables() )
#--> [ 5, 7, 9 ]
```

Une boucle ne garde pas son itinéraire comme une valeur qu'on peut interroger. Un marcheur le fait, avant de bouger. Et il a une règle pour le bord de la route. Au-delà de la fin, quand la marche est en cours, il s'arrête en silence. Avant le début, il refuse :

```haro
oWalker = Wk(1, 10, 3)
? @@( oWalker.WalkNSteps(10) )
#--> [ 1, 4, 7, 10 ]
? @@( oWalker.Walk() )
#--> [ 10 ]
oWalker = Wk(1, 10, 3)
try
	oWalker.WalkBackward()
catch
	? cCatchError
done
#--> Can't walk backward! Already at the beginning of walkable positions.
```

Demandez dix pas à une marche qui en compte quatre et vous obtenez les quatre. L'article soutient que cela reflète notre façon de marcher dans le monde physique : on s'arrête quand on heurte un mur derrière soi, ce qui est une erreur, et on s'arrête simplement quand la route devant finit.

**Le Vérificateur demande oui ou non.** Tous, n'importe lequel, ou où :

```haro
o1 = new stzList([ "A", 5, "B", "C" ])
? o1.CheckW('{ isString(@item) and IsUppercase(@item) }')
#--> FALSE
? o1.ContainsW('{ isNumber(@item) }')
#--> TRUE
? @@( o1.FindW('{ isNumber(@item) }') )
#--> [ 2 ]
```

**Le Producteur produit des données neuves à partir des anciennes, et laisse les anciennes tranquilles.** **L'Exécutant est son pendant : il change les éléments là où la condition tient.** Mis côte à côte sur la même liste, le contraste est le point :

```haro
o1 = new stzYielder([ 1, -2, 3, -4, 5 ])
? @@( o1.Filter(:IsPositive) )
#--> [ 1, 3, 5 ]
? @@( o1.Map(:Abs) )
#--> [ 1, 2, 3, 4, 5 ]
? o1.Reduce(:Sum)
#--> 3
o2 = new stzList([ 1, "haro", 3, "python", 5, "ruby" ])
? @@( o2.YieldW('isString(@item)', 'upper(@item)') )
#--> [ "HARO", "PYTHON", "RUBY" ]
? @@( o2.Content() )
#--> [ 1, "haro", 3, "python", 5, "ruby" ]
o2.PerformW('isString(@item)', 'upper(@item)')
? @@( o2.Content() )
#--> [ 1, "HARO", 3, "PYTHON", 5, "RUBY" ]
```

Regardez les deux sorties de `Content()`, avant et après l'appel à `PerformW`. Le producteur a rendu les mots en majuscules et la liste n'a pas été touchée. L'exécutant a changé la liste. Le verbe vous dit lequel, si bien qu'une conception peut dire « cette étape ne fait que lire » et le penser.

Maintenant ce que les quatre partagent, qui est la dernière pièce du titre : une condition voyage à l'intérieur d'un argument. C'est une petite chaîne, au même emplacement que celui de find, de items, de contains, gardée dans une variable si vous voulez ; et elle a un jumeau qui prend une vraie fonction :

```haro
o1 = new stzList([ 3, 8, 5, 12, 1, 9 ])
cCond = '{ @item > 5 }'
? @@( o1.FindW(cCond) )
#--> [ 2, 4, 6 ]
? @@( o1.ItemsW(cCond) )
#--> [ 8, 12, 9 ]
? o1.ContainsW(cCond)
#--> TRUE
? @@( o1.FindWF( func x { return x > 5 } ) )
#--> [ 2, 4, 6 ]
```

La forme en chaîne est la condition W, W pour where ; la forme en fonction est WF. Elles se ressemblent et diffèrent d'une manière qui compte. Le moteur lit une condition W comme des données, dans un petit langage à lui : des littéraux, `@item`, l'arithmétique, les comparaisons, et une courte liste de fonctions. Il ne peut pas appeler votre code. Alors une condition qui essaie n'est pas exécutée :

```haro
o1 = new stzList([ 3, 8, 5, 12, 1, 9 ])
? @@( o1.FindW('{ @item > 5 and print("hacked") }') )
#--> [ ]
? @@( W('{ @item > 5 }') )
#--> [ "where", "{ @item > 5 }" ]
```

Rien n'a été imprimé. Une condition W peut être stockée, montrée à une personne et approuvée avant de s'exécuter, parce qu'elle ne peut pas s'échapper. Le jumeau WF exécute du code hôte, et la table propre de la bibliothèque dit qu'il n'est pas sûr avec une entrée à laquelle vous ne faites pas confiance.

Les trois modèles de l'article « Bridging Minds and Code », le sémantique, le mental et celui de l'expression, sont une seule idée en trois endroits. Le modèle sémantique est le monde du programme comme connaissance : une pomme est un fruit. Le modèle mental est ce que vous venez de faire : créer un objet, y stocker des données, y trouver des choses, agir sur les positions. Le modèle d'expression est le code qui le dit : choisir l'objet, taper le nom de l'action, continuer le flux d'actions, convertir le résultat en un autre objet, et continuer ainsi jusqu'à la réponse finale. Je les raconte en mots parce que le code de cet article ne s'exécute pas à ce commit, comme le dit la section 7.

## 4. La décision, et ce que j'ai refusé

**J'ai fait des métaphores un but de conception.** La présentation de 2022 liste les « métaphores centrées sur l'humain » comme l'un des sept buts de conception, et ses quatre fonctionnalités sont ces quatre. Un but est ce qui rend une fonctionnalité justifiable ou refusable, alors je n'ai pas laissé les métaphores comme une politesse de la documentation. Elles sont l'une des raisons pour lesquelles la bibliothèque a la forme qu'elle a.

**J'ai remplacé `eval` par un langage que le moteur possède.** L'emplacement de la condition était compilé en évaluant la chaîne comme du code, avec une forme étendue plus expressive mais plus lente à côté. J'ai retiré les deux. Le moteur lit maintenant la condition dans son propre petit langage, et la bibliothèque garde la forme en code hôte comme un verbe séparé, WF, avec son avertissement. J'ai refusé le code arbitraire venu d'un texte, et j'ai refusé de séparer la vitesse de l'expressivité : la forme étendue est retirée parce que la simple fait tout ce qu'elle faisait.

**J'ai gardé les sept étapes telles qu'écrites.** Quand le cours a été conçu, une lecture du noyau technique a trouvé cinq étapes : select, contains, count, find, apply. Le cours enseigne les sept comme la narration source les a. Personne ne renumérote la source.

**J'ai laissé la règle du bord être un principe de conception.** Avant le début est une erreur, et au-delà de la fin est ignoré. La narration donne sa raison en une phrase : cela reflète notre façon de marcher. Le dossier ne la date pas comme une décision, alors je la raconte comme la conception de la bibliothèque.

## 5. Le tribunal

Les quatre métaphores n'ont pas de garde unique. Le producteur en a une narrée, `00_yielder_narrated` : quatre opérations map, trois opérations filter et une somme. Le marcheur a `597_walker_basics`, des marcheurs nommés et ce qu'ils ont parcouru, et `495_walking_until_and_until_before`, une marche qui s'arrête sur une condition, y compris l'élément qui l'arrête, ou non. Le vérificateur a `611_checkw`, qui dit qu'une vérification est fausse quand un seul élément échoue. L'exécutant a `621_perform`, qui dit qu'il change la liste en place. `483_w_and_wf_forms_in_conditional_code` prouve qu'une condition W écrite avec des mots de curseur comme `@NextNumber` et la même écrite avec de l'arithmétique d'index brute comme `This[@i+1]` donnent les mêmes positions. `597_walker_basics` et `495_walking_until_and_until_before` testent les marcheurs nommés et les marches de la liste, par `StzListQ`, non le marcheur `Wk` des blocs ci-dessus. Aucune des gardes nommées ici ne couvre `Walkables`, `WalkNSteps` ni `WalkBackward` ; ces lignes reposent sur les exécutions gardées pour ce chapitre.

## 6. Le terrain, et où il mène

Le terrain mène en paresse. Un générateur produit l'élément suivant à la demande et peut être sans fin. Le marcheur construit une carte de tout son voyage à l'instant où il est fait. C'est un gain pour la prévoyance, vous pouvez demander quelles positions il sautera avant qu'il bouge, et une perte pour un parcours très grand ou sans fin.

Le terrain mène en ouverture. Une lambda porte n'importe quelle logique. Le langage W est borné exprès, et le prix de la borne est le second chemin, WF, qui a toute la puissance de l'hôte et aucune sécurité contre une entrée à laquelle on ne fait pas confiance. Il y a aussi un coût plus discret que j'ai mesuré une fois, sur un cas : une condition qui appelle quelque chose que le langage ne connaît pas donne une liste vide et aucune erreur.

Le terrain mène en portée et en outillage. Les itérateurs et les compréhensions sont dans tous les langages courants, avec le soutien des éditeurs, la vérification des types et une littérature. Ces quatre métaphores existent dans une seule bibliothèque.

Et je n'imprimerai pas la comparaison que fait la bibliothèque elle-même des marcheurs avec les boucles et les itérateurs. Sa table a treize lignes, toutes en faveur du marcheur, aucune exécutée. Une table sans aucune perte est la forme d'une brochure.

## 7. La limite

Ce qui est construit : le marcheur à une dimension, dans la couche max, et les marches sur les listes ; le vérificateur comme `CheckW`, `ContainsW` et `FindW` ; le producteur comme une classe adossée au moteur, et comme `YieldW` ; l'exécutant comme `PerformW` ; et le langage de condition W compilé par le moteur.

Ce qui est conçu : les métaphores comme modules natifs du moteur. La conception du moteur marque les quatre comme prévus ; seul le producteur a un fichier de moteur. Et un marcheur qui ne porte plus du tout sur les listes mais sur toute structure indexée.

Ce qui est absent ou cassé à ce commit, d'après mes exécutions :

- La table de l'article sur la marche au bord ne tient pas. Un pas unique plus grand que l'intervalle lève une erreur là où la table promet le silence, et un chemin de directions mêlées lève une erreur là où elle promet l'acceptation. Les deux principes tiennent dans les cas montrés plus haut. Le livre énonce le principe et n'imprime que les cas qui s'exécutent ; la table n'est pas imprimée.
- Le code de l'article « Beyond Loops » diffère par endroits. L'historique d'un marcheur est une liste de marches ; une marche en arrière ne prend plus d'argument ; la direction s'imprime « backward » là où l'article dit « reverse ». L'exécution de l'article par le site a gardé dix blocs sur dix-huit.
- Les trois modèles de « Bridging Minds and Code » : aucun de ses codes ne s'exécute tel qu'écrit ; dans l'exécution du site, douze blocs ont levé une erreur et un a différé. Alors je les ai racontés en mots.
- Le getter `EmptyStrings()` de l'article du modèle mental n'existe pas.
- La classe dédiée du vérificateur lève une erreur quand on lui demande `ContainsW`, et le marcheur de chaînes n'a pas la marche en arrière avec condition.
- Et « pas d'eval » n'a pas tout atteint. Le résolveur quasi naturel, l'autre direction du chapitre 13, évalue encore du code hôte. Il en va de même de `StringsW` et de `ItemsWhere` sur la liste, et de `ContainsW` sur la classe dédiée du vérificateur : chacun appelle encore `eval` sur une chaîne de condition. Ce que j'ai dit plus haut, que le moteur lit une condition W et ne peut pas l'exécuter comme du code, vaut pour le chemin du moteur et non pour ces trois.

## 8. Six portes

**Le programmeur.** Posez les quatre mêmes questions à n'importe quel objet, et quand vous tendez la main vers une boucle, nommez le mouvement : marcher, vérifier, produire ou exécuter.

**L'analyste.** Dites le problème en mots simples, et les verbes que vous avez employés sont les étapes : « sont-ils tous », « lesquels », « donne-moi les grands », « rends-les négatifs ».

**Le concepteur.** Le producteur ne change jamais la liste et l'exécutant la change, et le verbe vous dit lequel.

**Le décideur.** Une condition W est une chaîne que le moteur lit et ne peut pas exécuter comme du code, si bien qu'elle peut être stockée, montrée et approuvée. Le prix est un petit langage, et un appel qu'il ne connaît pas donne une liste vide, non une erreur.

**Le formateur.** Le livre d'autoformation a déjà l'ordre : trouver, puis appliquer, puis marcher, demander, produire et agir.

**L'agent.** Écrivez la condition comme la chaîne, non comme du code. Quand la réponse est vide, vérifiez les mots de la condition avant de croire au vide.

## 9. Exercice

Prenez la liste `[ 4, 9, 12, 7, 20, 3 ]`. Quatre phrases sont données. Une : sont-ils tous au-dessus de 2 ? Deux : donnez-moi, comme une nouvelle liste, ceux au-dessus de 8, doublés. Trois : rendez négatifs ceux au-dessus de 8, dans la liste elle-même. Quatre : quelles positions sont 2, 4 et 6 ?

Pour chacune, dites d'abord quel mouvement c'est, marcher, vérifier, produire ou exécuter, et écrivez sous la ligne que vous allez écrire ce que vous attendez qu'elle imprime. Puis écrivez la ligne, avec la condition comme une chaîne partout où il y a une condition, et exécutez-la. Après la deuxième et la troisième, imprimez de nouveau la liste. Dites, avant de regarder, dans laquelle des deux la liste a changé.
