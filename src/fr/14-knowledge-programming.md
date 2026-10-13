---
id: knowledge-programming
part: 3
number: 14
title: La programmation de la connaissance
spine: false
narrations: [stz-knowledge-programming-narration.md, stz-bridging-minds-and-code.md, stz-rules-as-graph-rules-narration.md]
site: [offering]
guards: [knowledge_integration_narrated, provenance_survives_save_narrated, program_narrated]
stage:
  built: "un système comme un fichier texte brut de faits, avec des lois (unique, transitive, symétrique) et la source de chaque fait ; Prove avec ses étapes, un non aussi certain qu'un oui ; le mode strict ; le fichier écrit, relu et livré, d'un catalogue de cours à la mémoire d'un agent"
  designed: "des règles dans le fichier ; la dérivation sur n'importe quel graphe ; une requête qui joint ; plusieurs relations entre deux choses ; l'héritage de classes ; la validation au chargement"
  absent: "le dialogue fondateur de 2022, qui ne tourne pas ; Explain sur un graphe de connaissance ; la section des règles du fichier, que le lecteur saute"
status: draft
rulings: ["12.2", "12.6", "12.12", "12.13", "12.19"]
research: research/ch14.md
---

Dans ce chapitre, je prends les trois pratiques du terrain qui se rencontrent dans cette idée : la pile sémantique, la base de données de graphes de propriétés et les règles sur des faits. Je mets à côté d'elles un système qui est un fichier texte brut. J'exécute ce fichier : deux faits, une loi et une preuve avec ses étapes, puis une clinique en mode strict, où une rumeur refusée est gardée et nommée. J'écris le fichier, je le relis et je le montre à l'échelle, d'un catalogue de cours à la mémoire d'un agent. Je dis ce que j'ai décidé, qu'une entreprise se décrit dans un seul fichier et que le fichier est le programme. Je dis ce que j'ai refusé : un monde parallèle, une contradiction résolue en silence, la récupération. J'imprime la limite, un fichier qui à ce commit n'a pas de règles. Elle se tient à côté du principe : un système est un fichier, et y ajouter une ligne fait que le système sait davantage, sans rien coder ni entraîner.

## 1. Le concept, tel que le terrain le tient

Trois pratiques du terrain se rencontrent dans cette idée, et aucune n'est la même qu'elle.

La première est la pile sémantique : RDF, OWL et SPARQL. Un fait est un triplet de sujet, de prédicat et d'objet, écrit dans un vocabulaire partagé. Une ontologie dit quelles classes et quelles propriétés existent et ce qui en découle, et un raisonneur en dérive les conséquences. Ce sont des recommandations du W3C, de 2014, 2009 et 2013. Ce que le terrain demande à l'auteur d'une base de connaissance, c'est un langage d'ontologie à lui, un magasin et un langage de requête. Ils se tiennent d'ordinaire à côté de l'application et non dedans.

La deuxième est la base de données de graphes de propriétés, avec son langage de requête. Le dossier a une comparaison qui met de telles bases face à cette bibliothèque. C'est un texte de modèle gardé dans la bibliothèque, et il reconnaît au terrain l'échelle, la persistance et les transactions.

La troisième est les règles sur des faits, en Prolog et en Datalog. Des faits et des règles dans un seul programme, une requête par résolution. Le dossier ne nomme que Prolog, comme un langage à rejoindre, et non à reconstruire.

Une quatrième pratique se tient derrière le contraste, et le document de conception ne la nomme que pour la refuser. C'est la récupération, un tas de fragments de documents cherchés par similarité. (Connaissance générale, pas une étude du dossier.)

Ainsi, sur le terrain, la connaissance vit dans un magasin et sa logique dans un raisonneur, tous deux à côté du programme. Ici la connaissance est un fichier texte brut que le programme charge.

## 2. Le premier principe

**Un système est un fichier. Y ajouter une ligne fait que le système sait davantage, sans rien coder ni entraîner.**

Deux phrases du dossier le portent. La définition, dans le document de conception écrit à partir de ma directive du 13 juillet 2026 : l'intelligence est la capacité de calcul de dériver une connaissance nouvelle à partir d'une connaissance existante. Et ce que la vision de 2026 en garde : ajouter un fait augmente l'intelligence du système, sans changement de code et sans entraînement. Le chapitre 17 s'est ouvert sur la première, et je m'ouvre ici sur la seconde. Le document de conception du 13 juillet 2026 le dit déjà, presque dans les mêmes mots, et le chapitre garde son ouverture.

Voyons maintenant la forme elle-même, un texte et ce qu'il fait quand on l'exécute.

## 3. La forme Softanza

Voici un système comme un texte. Deux faits : la farine est faite de mil, et le couscous de farine. Le couscous est-il fait de mil ? Demandez-le au graphe, puis ajoutez une ligne au fichier, une loi disant que *fait de* est transitif, et demandez de nouveau :

```haro
cFacts = 'knowledge "coop"' + nl + nl + "facts" + nl +
         "    flour | made-from | millet" + nl + "    couscous | made-from | flour" + nl
oA = new stzKnowledgeGraph("coop")
oA.ImportKnow(cFacts)
? oA.Prove([ "couscous", "made-from", "millet" ])[:narration]
#--> not derivable: no recorded fact or lawful chain gives 'couscous' made-from 'millet'
oB = new stzKnowledgeGraph("coop")
oB.ImportKnow(cFacts + nl + "ontology" + nl + "    made-from | transitive" + nl)
? oB.Prove([ "couscous", "made-from", "millet" ])[:narration]
#--> proved: couscous made-from flour made-from millet
```

Sans la loi, le graphe répond `not derivable` ; avec elle, `proved: couscous made-from flour made-from millet`. Le texte est le programme. Les deux mêmes faits, une ligne en plus, une capacité différente. Le bloc ne touche pas le disque : `ImportKnow` prend un texte, et prend un chemin quand la chaîne de caractères finit par l'extension du fichier.

Maintenant ajoutons un fait au graphe qui a la loi, et rien d'autre. Que répondent les deux graphes à la question plus longue ? Exécutez-le :

```haro
oB.KnowRelation("porridge", "made-from", "couscous")
? oB.Prove([ "porridge", "made-from", "millet" ])[:narration]
#--> proved: porridge made-from couscous made-from flour made-from millet
? oA.Prove([ "porridge", "made-from", "millet" ])[:narration]
#--> not derivable: no recorded fact or lawful chain gives 'porridge' made-from 'millet'
```

Le graphe qui a la loi prouve la chaîne plus longue et en écrit les étapes : `proved: porridge made-from couscous made-from flour made-from millet`. Le graphe sans la loi, qui n'a de plus jamais reçu le fait, répond toujours `not derivable: no recorded fact or lawful chain gives 'porridge' made-from 'millet'`, et je veux que vous remarquiez que ce non a deux causes, nommées dans sa propre ligne : aucun fait enregistré, et aucune chaîne que la loi permette. Un refus est aussi certain qu'une preuve, sur ce qui est enregistré et déclaré : le graphe dit « non dérivable », pas « faux ». Le commentaire de la bibliothèque sur `Prove` le dit : `a certain no is still certain`.

La même croissance atteint le modèle de domaine du chapitre 19. Rien n'est entraîné. Mais un modèle forgé à partir d'un graphe est un instantané. Le modèle apprend-il le fait nouveau quand le graphe l'apprend ? Exécutez-le :

```haro
oKB = new stzKnowledgeGraph("coop")
oKB.Know("couscous", "dish").KnowRelation("couscous", "contains", "semolina")
oDLM = StzDlmQ(oKB)
? oDLM.Ask("what is millet?")
#--> That is outside the 'coop' domain (I know 1 entities and 1 relations).
oKB.Know("millet", "grain").KnowRelation("couscous", "contains", "millet")
? oDLM.Ask("what is millet?")
#--> That is outside the 'coop' domain (I know 1 entities and 1 relations).
oDLM = StzDlmQ(oKB)
? oDLM.Ask("what is millet?")
#--> Millet is a grain.
? oDLM.Ask("couscous contains what?")
#--> Couscous contains semolina and millet.
```

Il ne l'apprend pas. La seconde réponse est l'ancien modèle qui refuse encore, `That is outside the 'coop' domain`, et seul le modèle forgé de nouveau répond `Millet is a grain.`

**Le fichier que la bibliothèque écrit.** Une clinique. Une relation déclarée unique, et un graphe en mode strict, où chaque fait a besoin de sa provenance. Que fait-il d'un fait sans source, d'un fait qui en a une, et d'un second, qui le contredit, venu d'une rumeur ? Et qu'écrit-il ensuite sur le disque ? Exécutez-le :

```haro
oCl = new stzKnowledgeGraph("clinic")
oCl.ConstrainRelation("treated-by", :Unique)
oCl.EnableStrictMode()
try
	oCl.AddFact("fatou", "treated-by", "dr-diallo")
catch
	? cCatchError
done
#--> Strict mode: every fact needs provenance -- use AddFactXT(s, p, o, [ :source = ..., :confidence = ... ]).
oCl.AddFactXT("fatou", "treated-by", "dr-diallo", [ :source = "registry", :confidence = 0.95 ])
? oCl.AddFactXT("fatou", "treated-by", "dr-sani", [ :source = "rumour", :confidence = 0.2 ])
#--> 0
oCl.WriteToKnowFile("clinic")
? read("clinic.zknw")
#--> knowledge "clinic"
#
#    facts
#        fatou | treated-by | dr-diallo
#
#    provenance
#        fatou | treated-by | dr-diallo | source | text | registry
#        fatou | treated-by | dr-diallo | confidence | number | 0.95
#
#    contradictions
#        fatou | treated-by | dr-diallo | dr-sani | rumour
#
#    ontology
#        treated-by | unique
```

Le fait nu est refusé avec la phrase propre de la bibliothèque, `Strict mode: every fact needs provenance`. Le fait avec sa source et sa confiance est admis. La rumeur est refusée, `0`, et le refus est gardé ! C'est ce que la bibliothèque écrit, un en-tête et jusqu'à quatre sections. Elles viennent dans cet ordre : les faits, la provenance quand un fait en porte, les contradictions quand l'une a été refusée, et l'ontologie quand une loi a été déclarée. Une ligne par enregistrement, les champs séparés par une barre. Une barre ou un saut de ligne à l'intérieur d'une valeur est échappé. La rumeur refusée est dans le fichier, nommée, et jamais résolue. Le commentaire du code sur la liste des contradictions le dit : `named, NEVER silently resolved`.

Le fichier se relit-il dans un graphe strict, avec la loi, la source de chaque fait et le refus à l'intérieur ? Chargez-le :

```haro
oBack = new stzKnowledgeGraph("clinic")
oBack.EnableStrictMode()
aR = oBack.ImportKnow("clinic.zknw")
? aR[:merged]
#--> 1
? @@( oBack.MetaOfFact("fatou", "treated-by", "dr-diallo") )
#--> [ [ "source", "registry" ], [ "confidence", 0.95 ] ]
? len(oBack.Contradictions())
#--> 1
? oBack.RelationHasLaw("treated-by", "unique")
#--> 1
remove("clinic.zknw")
? fexists("clinic.zknw")
#--> 0
```

Oui : un fait fusionné, la source et la confiance revenues, `[ [ "source", "registry" ], [ "confidence", 0.95 ] ]`, une contradiction, et la loi. Un fichier de ce genre a été écrit un jour sans sa provenance. L'export n'écrivait que les triplets nus, de sorte que la connaissance relue depuis le disque ne disait plus d'où elle venait. Un graphe strict ne pouvait pas charger son propre export. La correction, ce sont les deux sections ci-dessus. La garde qui la prouve est nommée à la section 5.

**Une loi qui se déclenche quand un fait est ajouté.** Sur le monde par défaut de la bibliothèque, celui qui est derrière le sucre syntaxique du langage naturel, une loi symétrique dérive le fait inverse au moment où le premier est ajouté, sans appel à une étape de dérivation. Personne n'a écrit qu'Ibrahim est marié à Amina. Le monde par défaut le sait-il ?

```haro
StzConstrainRelation("married-to", :Symmetric)
StzKnowRelation("amina", "married-to", "ibrahim")
? DefaultKnowledgeGraph().Query([ "ibrahim", "married-to", "amina" ])
#--> 1
```

Il répond `1`. Le fait inverse est là, et personne ne l'a écrit ! C'est le seul endroit où une loi déclarée se déclenche à l'ajout qu'une exécution de ce livre montre, et c'est le monde par défaut. La classe de graphe a aussi un interrupteur, `EnableAutoDerive`, qui lance les règles de dérivation après chaque arête ajoutée ; il est éteint par défaut, et je ne l'ai pas exécuté. Je montre la même loi sur un graphe d'instance à la section 7, où cela ne fonctionne pas.

**Un système à l'échelle.** Le programme d'éducation de la bibliothèque est un fichier de connaissance. Son catalogue, `program.zknw`, dit comment s'appelle le programme et quels cours et quelles langues il a. Quel est son nom, et quelles langues porte-t-il ? Demandez-le-lui :

```haro
oP = StzProgramQ("../../education/program")
? oP.Id()
#--> softanza-education
? @@( oP.Languages() )
#--> [ "en", "fr", "ar", "ha" ]
```

Il s'appelle `softanza-education`, et il a quatre langues. Ajouter un cours, c'est y ajouter une ligne, et la garde vérifie que chaque cours déclaré est un dossier et que chaque dossier est déclaré. Dans le module d'éducation, l'instantané tient quatre-vingt-dix-neuf fichiers de connaissance, comptés avec `find` le 8 octobre 2026. Ce sont des cours, des exercices, des mondes et des compétences, un monde de projet pour un apprenant, et les surcouches qu'une institution pose sur le noyau. La mémoire d'un agent est aussi un graphe de connaissance, sauvegardé par le même format, avec la provenance.

Voilà la forme. Voyons maintenant ce que j'ai décidé, et ce que j'ai refusé.

## 4. La décision, et ce que j'ai refusé

**J'ai décidé qu'une entreprise se décrit dans un seul fichier, et que le fichier est le programme.** Le document de conception enregistre ma directive : des entités, des relations, une ontologie de sémantiques propres au domaine, et des règles, dans un fichier lisible, comparable et modifiable à la main, validé au chargement. Je n'ai pas encore rencontré les deux derniers mots, et la section 7 dit où.

**J'ai décidé des extensions à quatre lettres.** `.zknw` pour la connaissance, et les autres de la famille ; les anciennes graphies se lisent encore. L'instantané écrit `.zknw` et lit encore `.stzknow`. Le fichier de règles n'a pas été renommé : le graphe écrit et lit toujours `.stzrulz`, bien que la famille lui donne quatre lettres. Je le rapporte comme le dossier l'a.

**J'ai refusé un monde parallèle.** La couche naturelle tenait autrefois ses entités dans des globales, et le document de conception l'a appelé le mauvais foyer, la mauvaise forme et un monde parallèle. La résolution est un graphe par défaut, unique, derrière le sucre syntaxique du langage naturel. Les anciennes globales existent encore, et le graphe grandit à côté : l'en-tête de la bibliothèque appelle cela une double écriture. La loi qui le sous-tend est que les globales de domaine nues sont interdites ; une forme globale ne peut exister que comme mince sucre sur une instance par défaut. Ainsi le dialogue de la loi symétrique ci-dessus est du sucre sur un graphe de la même classe que celui des premiers blocs.

**J'ai refusé de résoudre une contradiction en silence.** Le mode strict, où chaque fait a besoin de sa provenance, est une hygiène de la connaissance, sur option.

**J'ai refusé la récupération.** Le document de conception dit : pas de changement de code, pas d'entraînement, pas de mécanique RAG. C'est le même refus que celui du chapitre 17.

## 5. Le tribunal

`knowledge_integration_narrated` prouve que le monde répond à `WhatIs`, que le graphe a grandi à côté, et que la loi vit dans l'ontologie. Elle prouve que `Prove` narre d'abord la loi puis les maillons de la chaîne, avec une certitude de 1, et refuse ce qu'il ne peut pas prouver. Elle prouve que le fichier fait l'aller-retour. Elle prouve qu'une loi symétrique dérive l'arête inverse quand l'étape de dérivation est appliquée après l'ajout d'un fait par le graphe. Enfin, elle prouve que le mode strict admet un fait muni de provenance, refuse un fait nu, et refuse et enregistre une contradiction d'unicité.

`provenance_survives_save_narrated` prouve que la source et la confiance d'un fait survivent à une sauvegarde, qu'un graphe strict charge son propre export, et qu'une contradiction refusée survit. Elle prouve qu'une barre ou un saut de ligne dans une valeur est une donnée, et qu'un ancien fichier sans provenance se charge encore. Elle prouve que la mémoire d'un agent enregistre qui a appris un fait, et quand.

`program_narrated` prouve que le programme compte ses cours, et que chaque cours déclaré est un dossier et chaque dossier est déclaré. Elle prouve que les textes se lisent de la même façon depuis un checkout avec d'autres fins de ligne.

Voilà ce que prouvent les gardes. Ce que le terrain fait mieux vient ensuite.

## 6. Le terrain, et où il mène

La comparaison de graphes du dossier dit elle-même où les solutions traditionnelles gagnent : les systèmes à grande échelle qui ont besoin de stockage et de traitement distribués, et les applications où la performance est critique. Son tableau place Softanza à l'échelle de l'entreprise, de quelques centaines à quelques milliers de nœuds, dans un seul processus. C'est le résumé honnête de la perte : le terrain mène en échelle, en persistance, en transactions et en outillage. (La ligne de la comparaison sur la persistance est antérieure au fichier ; le graphe de connaissance en écrit un maintenant.)

Le terrain mène en normes et en portée, en connaissance générale. Une base de connaissance en RDF peut être partagée avec n'importe quel outil qui lit les formats du W3C, reliée à des vocabulaires publics et interrogée à travers des magasins. D'après le dossier, un fichier de connaissance est lu par cette bibliothèque et par rien d'autre. Un raisonneur pour un langage d'ontologie riche fait ce que trois lois et une déclaration de classe ne font pas. Le terrain mène en expressivité des règles : Prolog et Datalog dérivent des faits nouveaux à partir de règles arbitraires. Ici, dans les exécutions que j'ai gardées, une seule sorte de loi dérive un fait, et seulement sur le monde par défaut. Le terrain mène en requêtes à plusieurs étapes, puisque SPARQL et Cypher joignent des motifs. Et en relations multiples entre deux choses.

Voici où je pense que cela se distingue, avec les limites mesurées à côté. La connaissance est un fichier texte qu'une personne peut lire, modifier, comparer et livrer avec le programme. Chaque réponse est prouvable avec ses étapes, et un non est aussi certain qu'un oui. Ce qu'un fait affirme voyage avec sa source et ses refus. Et le même format porte un cours, le projet d'un apprenant et la mémoire d'un agent. Rien de cela n'a besoin d'un magasin, d'un serveur, d'un modèle ni d'un entraînement.

Les pertes sont imprimées. La limite du chapitre vient ensuite, avec ses exécutions.

## 7. La limite

La limite de ce chapitre est celle que la ligne de structure porte déjà : *entités, relations, une ontologie, règles*. Le fichier à ce commit n'a pas de règles. Voici le fichier avec une section de règles. Qu'en fait le lecteur ?

```haro
cRules = 'knowledge "pairs"' + nl + nl + "facts" + nl + "    margherita | pairs-with | chianti" + nl + nl +
         "rules" + nl + "    pairs-with | symmetric" + nl
oRul = new stzKnowledgeGraph("pairs")
aM = oRul.ImportKnow(cRules)
? aM[:merged]
#--> 1
? len(oRul.Ontology())
#--> 0
```

Le fichier fusionne, `1`, et l'ontologie est vide, `0`. L'analyseur reconnaît l'en-tête `rules`, et n'a de gestionnaire pour aucune des lignes qui le suivent. Elles sont écartées : l'ontologie en tient `0`, et aucun refus ne revient. La même loi sous l'en-tête `ontology` donne une ontologie de longueur 1. Les règles vivent ailleurs, comme données dans une règle attachée à un graphe, ce qui est le sujet des chapitres 29 et 30, et dans un fichier séparé qui nomme des fonctions de règle. Dans ce fichier il y a des faits et des lois. J'imprime « faits et lois », et j'envoie les règles à ces deux chapitres. Le fichier unique qui contient des règles, que promet la conception, n'est pas là, et la section 7 imprime ce manque comme la limite du chapitre.

La loi n'est pas non plus dérivée sur un graphe d'instance. Prenons la même loi symétrique et le même fait que sur le monde par défaut. L'inverse y est-il ?

```haro
oSy = new stzKnowledgeGraph("pairs")
oSy.ConstrainRelation("pairs-with", :Symmetric)
oSy.KnowRelation("margherita", "pairs-with", "chianti")
? oSy.RelationHasLaw("pairs-with", "symmetric")
#--> 1
? oSy.Query([ "chianti", "pairs-with", "margherita" ])
#--> 0
```

La loi est enregistrée, `1`, et l'arête inverse n'y est pas, `0` ! L'en-tête de la classe le dit : `only :unique and :transitive are acted on here` ; la symétrie est seulement enregistrée. Quatre autres limites, chacune avec son exécution.

**Une seule relation entre deux choses.** Le graphe stocke une arête par paire de nœuds. Admet-il une seconde relation entre les deux mêmes entités, `amina` et `bread` ? Exécutez-le :

```haro
oShop = new stzKnowledgeGraph("shop")
oShop.KnowRelation("amina", "sells", "bread")
aV = oShop.Admit("amina", "buys", "bread", [ :source = "till" ])
? aV[:admitted]
#--> 0
? aV[:why]
#--> Can't add fact: 'amina' and 'bread' already carry the edge 'sells' (stzGraph stores one edge per node pair).
```

La seconde relation est refusée, `0`, avec la phrase propre de la bibliothèque, `Can't add fact: 'amina' and 'bread' already carry the edge 'sells' (stzGraph stores one edge per node pair)`. Un modèle de connaissance qui ne peut pas tenir *vend* et *achète* entre les deux mêmes entités est une vraie limite. Le code le dit : `known limitation, revisit with multi-edge support`.

**Une question à deux étapes ne répond qu'à sa première étape.** `QueryPath` suit-il son second motif, et le prédicat d'une requête peut-il être une variable ? Exécutez-le :

```haro
oQ = new stzKnowledgeGraph("coop2")
oQ.KnowRelation("amina", "sells", "couscous").KnowRelation("couscous", "made-from", "flour")
? @@( oQ.QueryPath([ [ "amina", "sells", "?p" ], [ "?p", "made-from", "?m" ] ]) )
#--> [ "couscous" ]
? @@( oQ.Query([ "amina", "?p", "?o" ]) )
#--> [ ]
```

Le chemin répond `[ "couscous" ]`, la première étape et rien de plus : `QueryPath` ignore le reste de ses motifs, donc ce n'est pas encore une requête à plusieurs étapes. Le prédicat variable répond `[ ]`.

**Une ligne qui n'est pas un fait.** Quatre lignes, dont trois ne sont pas des faits : deux champs, quatre champs, et aucune barre. Que refuse le lecteur ?

```haro
cBad = 'knowledge "t"' + nl + nl + "facts" + nl + "    a | likes | b" + nl + "    c | likes" + nl +
       "    d | likes | e | f" + nl + "    g likes h" + nl
oT = new stzKnowledgeGraph("t")
aBad = oT.ImportKnow(cBad)
? aBad[:merged]
#--> 1
? @@(aBad[:refused])
#--> [ ]
```

Rien. Le fichier fusionne, `1`, et la liste des refus est `[ ]` ; le lecteur se tait et les trois lignes disparaissent ! Le document de conception promet que le fichier est « validé au chargement ». À ce commit l'analyseur ne garde qu'une ligne ayant exactement trois champs.

**Le dialogue fondateur de 2022.** La narration raconte la programmation de la connaissance par un dialogue : une pomme comme fruit et comme entreprise, un propriétaire, des relations demandées comme des questions. À ce commit sa première ligne ne tourne pas. Le texte, que je montre et ne lance pas, est `@Q("Apple").IsA(:Fruit)`. Le 8 octobre 2026 il s'est arrêté sur `Calling Function without definition: @isfruit` ; je n'ai pas gardé cette exécution comme bloc. La classe de chaîne de caractères lit le prédicat comme du langage naturel et cherche une fonction de ce nom. Deux autres formes s'arrêtent ailleurs. Les lignes de promesse de la narration sont périmées. La forme la plus proche qui tourne garde le sens. Le monde connaît-il un nom à deux significations ?

```haro
StzKnow(:Apple, :Company)
StzKnow(:Apple, :Fruit)
? @@( WhatIs(:Apple) )
#--> [ "company", "fruit" ]
```

Il connaît les deux : `[ "company", "fruit" ]`.

L'étude du dossier dit déjà que le dialogue a été gardé en marge, et que le centre s'est déplacé vers le fichier. Le chapitre garde le fichier comme ouverture, et le dialogue de 2022 reste en marge.

Ce qui est conçu : des règles dans le fichier ; la dérivation sur n'importe quel graphe ; une requête à plusieurs étapes ; plusieurs relations entre deux choses ; l'héritage de classes. `DefineClass` écrit un fait, et aucun héritage n'en découle. Le plus proche qui a tourné, dans un essai antérieur dont je n'ai pas gardé l'exécution, est de déclarer `is-a` transitif et d'énoncer la classe comme un fait de cette relation. Et l'hygiène de la connaissance de la conception au-delà de la provenance, les requêtes bornées, les graphes à portée et la révision avec retour arrière, n'a aucune méthode de ce nom.

Ce qui est absent ou cassé : `Explain()` sur un graphe de connaissance, qui appelle `ApplyInference`, une fonction définie nulle part. Et `ValidateOntology()`, qui renvoie 1 quel que soit le contenu de l'ontologie, comme son propre commentaire le dit, `known defect`.

Une note sur l'histoire du document de conception. Son amendement du 22 août 2026 dit qu'aucun fichier de connaissance n'existe nulle part dans l'arbre, et que c'est de l'hygiène et non un manque. À ce commit ce n'est plus vrai : il y en a quatre-vingt-dix-neuf, tous dans le module d'éducation.

Voilà la limite, imprimée. Voyons maintenant les six portes.

## 8. Six portes

**Le programmeur.** Une classe et un fichier texte : `Know`, `KnowRelation`, `ConstrainRelation`, `Prove`, `Query`, `WriteToKnowFile`, `ImportKnow`. Le fichier est comparable et se livre avec le programme.

**L'analyste.** La page de l'offre le nomme : ce que vous déclarez, ce sont les entités, les règles et les flux de votre organisation, dans un fichier de connaissance en texte brut. Lisez « règles » comme la limite ci-dessus. Pour commencer, dans le cours : le chapitre intitulé « Enseigner un monde ».

**Le concepteur.** Le dossier est silencieux. Ni la page de l'offre ni l'étude ne relient le fichier de connaissance à la porte du concepteur, et je n'en invente pas.

**Le décideur.** Le fichier est du texte brut qu'un responsable peut lire. Chaque fait peut porter une source et une confiance. Une affirmation refusée est gardée, nommée et jamais résolue. Une réponse vient avec sa preuve, et un non est certain. La deuxième loi de la conception dit qu'aucune capacité ne doit exiger rien de payant ni de distant. Je n'ai pas exécuté le fichier hors ligne.

**Le formateur.** Tout le programme d'éducation est fait de fichiers de connaissance. Un apprenant enseigne un monde, puis l'interroge, et la garde du projet vérifie le fichier du monde, le fichier de l'agent et une réponse imprimée. Une institution s'adapte par surcouche, jamais par fourche.

**L'agent.** Votre mémoire est un graphe de connaissance avec provenance, et votre monde est un fichier que vous chargez et interrogez.

## 9. Exercice

Voici un monde avec deux faits, et une question à laquelle il ne peut pas encore répondre. Votre promesse est la ligne qui prouve que la classe 3b fait partie du primaire, avec la chaîne écrite en entier. Changez le monde, et non la question.

```haro exercise
cWorld = 'knowledge "school"' + nl + nl + "facts" + nl +
         "    class-3b | part-of | grade-3" + nl +
         "    grade-3 | part-of | primary" + nl
oW = new stzKnowledgeGraph("school")
oW.ImportKnow(cWorld)
? oW.Prove([ "class-3b", "part-of", "primary" ])[:narration]
# this prints a refusal. Your promise: the line proving that class-3b is part of primary,
# with the chain written out. Change the world, not the question.
```

Exécutez-le et voyez ce qui s'imprime. Si vous changez la question pour demander au sujet du grade 3, il prouvera quelque chose, et ce ne sera pas la ligne que vous avez promise. Puis posez la question inverse, si le primaire fait partie de la classe 3b, une fois que votre monde a sa loi, et voyez si la loi ajoute un fait dans le mauvais sens. Je ne vous dis pas la ligne à ajouter.

Le chapitre suivant porte sur les langages de motifs : un motif est une règle sur la forme des données, écrite comme des données, et la même habitude sert tous les genres de données. Ici, une loi sur une relation était une ligne dans un fichier ; là, la règle porte sur la forme des données elles-mêmes.
