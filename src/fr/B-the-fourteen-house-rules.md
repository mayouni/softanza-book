---
id: the-fourteen-house-rules
appendix: B
number: 102
title: Les quatorze règles de la maison
status: draft
guards: [coderule_narrated]
rulings: ["12.16"]
---

La bibliothèque a un tribunal sur son propre code. Il lit une classe comme un graphe et la juge selon des règles, chacune écrite après que la bibliothèque a fait quelque chose qu'elle n'aurait pas dû faire. Cette annexe énumère les quatorze, et en montre trois qui se déclenchent.

Il y a deux quatorze dans ce livre, et ce sont deux ensembles différents. Les quatorze **règles de la maison** de cette annexe sont des règles du code de la bibliothèque : elles forment un tribunal, et elles s'exécutent. Les quatorze **règles d'écriture**, au chapitre 7, sont une lecture de la manière dont le style s'écrit. Ce sont des lectures du code, énoncées comme des règles, et aucune machine ne les juge. La coïncidence du nombre est une coïncidence.

La liste est fermée et la bibliothèque peut l'imprimer :

```haro
? len( StzCodeRuleNames() )
#--> 14
? StzCodeRuleNames()[2]
#--> q-returns-object
? StzCodeRuleNames()[14]
#--> value-called-as-function
```

Voici trois d'entre elles, déclenchées sur du code que j'ai planté. Une méthode qui écrit sur la console est un avertissement, le code reste donc propre. Une méthode qui ne diffère d'une autre que par la casse est une erreur, puisque le langage hôte ne distingue pas les deux et que le fichier ne se chargerait pas. Et une classe qui définit `Len()` masque la fonction propre de l'hôte, et elle est refusée :

```haro
cSay = "class Door" + nl + "def Say()" + nl + "	? 'hello'" + nl + "	return 1" + nl
? StzCheckCode(cSay)[1][:rule]
#--> library_prints
? StzCheckCode(cSay)[1][:severity]
#--> warning
? StzCodeIsClean(cSay)
#--> 1
cBox = "class Box" + nl + "def Size()" + nl + "	return 1" + nl + "def size()" + nl + "	return 2" + nl
? StzCheckCode(cBox)[1][:rule]
#--> no-case-collision
? StzCodeIsClean(cBox)
#--> 0
cLen = "class Box" + nl + "def Len()" + nl + "	return 1" + nl
? StzCheckCode(cLen)[1][:rule]
#--> no-len-method
? StzCodeIsClean(cLen)
#--> 0
```

Une note sur l'orthographe, qu'un programme qui lit les constats doit connaître. La liste emploie des traits d'union : `library-prints`. Un constat de huit des quatorze revient avec des tirets bas : `library_prints`. Les constats des règles sur le graphe du code gardent leurs traits d'union. Je donne ce que l'exécution a imprimé.

### Les quatorze

| # | Règle | Ce qu'elle refuse | Gravité |
|---|---|---|---|
| 1 | `no-len-method` | définir `Len()` sur une classe : elle masque la fonction native de l'hôte et casse tous les appelants | erreur |
| 2 | `q-returns-object` | une méthode nommée avec un `Q` final qui ne renvoie pas un objet à chaîner | erreur |
| 3 | `no-aggressive-verbs` | les noms de méthode qui commencent par un verbe violent : le ton Softanza | avertissement |
| 4 | `engine-first` | du code nouveau qui prend les fonctions de chaîne orientées octets de l'hôte là où les formes du moteur existent | avertissement |
| 5 | `q-has-plain-twin` | un mutateur chaînant sans jumeau simple : `Q` chaîne, et le simple agit | avertissement |
| 6 | `no-case-collision` | deux méthodes d'une même classe qui ne diffèrent que par la casse : l'hôte ne distingue pas la casse, le fichier ne se charge donc pas | erreur |
| 7 | `dead-knob` | un attribut qu'un setter écrit et que rien ne lit : un réglage qui ne peut rien changer | erreur |
| 8 | `setter-resets-on-reject` | un setter qui répond à une valeur qu'il n'aime pas en écrasant ce qui était déjà là | selon la source |
| 9 | `setter-only-moves-one-way` | `max()` ou `min()` contre l'attribut même qu'on règle : un cliquet qui avale l'autre sens | erreur |
| 10 | `misspelled-name` | une méthode portant une faute d'orthographe connue alors que le nom correct n'existe pas | avertissement |
| 11 | `library-prints` | une méthode de classe qui écrit sur la console pendant qu'elle travaille ; les méthodes dont le but est d'afficher sont exemptées | avertissement |
| 12 | `empty-method-body` | une méthode déclarée qui ne fait rien ; plus sévère pour un prédicat, qui alors ne répond rien, lu comme faux | avertissement |
| 13 | `writes-a-mutable-constant` | affecter à `true`, `false`, `null`, `nl`, `tab` ou `cr` : dans l'hôte ce sont des globales ordinaires | erreur |
| 14 | `value-called-as-function` | appeler le résultat d'un appel, la forme que laisse un balayage | erreur |

J'ai déclenché les lignes 6, 11 et 1 ci-dessus, et les lignes 2, 7, 9, 10, 12 et 13 dans la recherche pour le chapitre 7. Les gravités des lignes 3, 4, 5, 8 et 14 sont les déclarations de la source, et je ne les ai pas déclenchées.

### Ce que le tribunal ne juge pas

Aucune des quatorze n'est une règle d'écriture. Aucune machine ne juge, aujourd'hui, le style d'un programme écrit avec la bibliothèque. C'est la limite du chapitre 7, et c'est la raison pour laquelle les quatorze autres sont dans ce livre sous la forme d'une table avec leur état, et non d'un tribunal.

### Les quatorze autres : les règles d'écriture, et où en est chacune

Lu d'après la décision de l'étude sur le style, avec l'état de chacune au commit sur lequel ce livre tourne.

| # | Règle d'écriture | État |
|---|---|---|
| 1 | Une valeur est élevée à son objet par `Q()` ou par un élévateur typé | tourne |
| 2 | Une scène est un bloc entre accolades sur un seul objet | tourne |
| 3 | Chaque ligne imprimée porte sa réponse sous `#-->` | jugée par une machine |
| 4 | Un paramètre est nommé, et le nom se lit comme de l'anglais | tourne, et dans n'importe quel ordre |
| 5 | Une chaîne reflète l'ordre de la pensée, un pas par ligne | tourne |
| 6 | La forme du verbe dit ce qui arrive | tourne |
| 7 | Les suffixes et les préfixes sont petits et veulent dire chacun une seule chose | en partie |
| 8 | Une fonction a des variantes pour la manière dont une personne la dit | en partie |
| 9 | La précision plutôt que la généralité, quand cela ne coûte rien | en partie |
| 10 | Le code voyage dans un argument comme une petite chaîne | le siège tourne ; la marque sur le nom d'un paramètre est retirée |
| 11 | Les petits langages littéraux vivent dans des chaînes | tourne sous une forme |
| 12 | Une phrase peut être presque naturelle | pas comme le deck l'a écrit |
| 13 | Une fonction peut être nommée dans n'importe quelle langue humaine | ne tourne pas |
| 14 | Un commentaire parle avant le code, de la voix du maître | tourne |
