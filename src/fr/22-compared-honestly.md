---
id: compared-honestly
part: 4
number: 22
title: Comparé, honnêtement
spine: false
narrations: [stzgraph-vs-other-graph-libraries.md, stzexcis-performance-battle.md, stz-vs-qt-unicode-narration.md, stznatural-vs-ring-naturallib.md, stz-near-natural-language-programming.md]
site: [compare, code]
guards: [numeric_exactness_narrated, numeric_no_loss_narrated, semantic_resolver_narrated, engine_is_optimised_narrated]
stage:
  built: "cinq comparaisons, quatre exécutées des deux côtés avec la version de l'autre côté et la date, et la cinquième exécutée du côté Softanza seulement ; les quatre paires de code du site, ré-exécutées, trois d'entre elles des deux côtés ; trois études de terrain qui finissent sur ce que le terrain a et que la bibliothèque n'a pas, et un plan de culture qui imprime ses pertes"
  designed: "un registre de comparaisons comme données ; un tribunal des comparaisons dont la règle est qu'une ligne sans source ni date ne se publie pas ; les deux bancs d'essai ré-exécutés sur le moteur actuel"
  absent: "la collation selon la locale ; la casse selon la locale ; un comptage de graphèmes sur la chaîne publique ; une base de fuseaux horaires ; le banc d'essai du 7 juillet 2026 ré-exécuté ; la source de la matrice de couverture, que je n'ai pas pu localiser"
status: draft
rulings: ["12.10", "12.22", "12.29"]
research: research/ch22.md
---

Dans ce chapitre, je compare Softanza au terrain, et je dis comment une comparaison doit être faite avant de pouvoir être imprimée. Je montre cinq paires, la même tâche exécutée des deux côtés, avec la version de l'autre côté et la date sur la page et une ligne où l'autre côté mène. Je dis ce que j'ai refusé, la grille seule d'abord, et quelles gardes prouvent les blocs, puisque le tribunal des comparaisons est proposé et non construit. J'imprime la liste de ce que le terrain a et de ce qui manque à Softanza, à côté des gains. Le principe est celui-ci. Une comparaison ne vaut rien tant que la version de l'autre côté et la date ne sont pas sur la page, que l'autre côté n'a pas été exécuté, et que la perte n'est pas imprimée à côté du gain.

## 1. Le concept, tel que le terrain le tient

La comparaison, sur le terrain, est un genre du marketing avec quelques exceptions honnêtes. Le dossier nomme le genre : une page « Compare » pour chaque rival, et un bloc de comparaison sur chaque page de fonctionnalité. Sa forme la plus courante est la grille, avec des lignes de fonctionnalités, des colonnes d'outils, des coches et des croix.

Les exceptions honnêtes sont des pratiques et non des produits. Des bancs d'essai publiés avec la méthode, la machine et le mode de construction. Et des sections qui disent ce que l'autre outil a et qui nous manque. (Connaissance générale, et non étude du dossier. Je ne nomme aucun outil, puisque l'auteur n'en nomme aucun.)

## 2. Le premier principe

**Une comparaison ne vaut rien tant que la version de l'autre côté et la date ne sont pas sur la page, que l'autre côté n'a pas été exécuté, et que la perte n'est pas imprimée à côté du gain.**

Elle est faite de trois phrases du dossier. L'étude du 7 octobre 2026 : toute affirmation sur un autre outil est citée, datée et exécutée, et toute perte est publiée avec les gains. L'étude du domaine de projets sur un runtime de navigateur, exécutée le 8 août 2026 : les pertes sont publiées avec les gains. Et la page de couverture du site : une plateforme qui montre ses écarts est crue sur ses forces. La demande de l'auteur, telle que l'étude la rapporte, est un ton comparatif qui est « a motor force, to learn from the best and beat them when possible ». L'étude ajoute : avec « when possible » mesuré.

## 3. La forme Softanza

Le chapitre 3 a dit « J'ai refusé la grille seule ». Ce chapitre est la méthode qui la remplace, avec ses preuves. Qu'a mesuré le dossier sur la grille ? L'étude a parcouru le texte de la bibliothèque à la recherche de tables dont l'en-tête nomme Softanza et au moins un autre outil. Elle a trouvé soixante-quatre tables, dans trente et un documents. Dans celles-ci, la colonne de Softanza porte 286 coches, 2 avertissements et 2 croix. Les autres colonnes portent 204 coches, 207 avertissements et 269 croix. Le jugement de l'étude est que c'est la forme d'une brochure, et que le dossier lui-même ne s'y fie pas. Je n'ai pas pu reproduire ces chiffres : un parcours plus étroit de ma main, avec une règle d'en-tête que j'ai écrite, a trouvé trente-sept tables dans vingt-neuf documents. L'étude n'imprime pas sa règle d'en-tête. Je cite ses nombres comme les siens, et datés.

La forme qui remplace la grille est une paire : la même tâche, les deux côtés exécutés, la version de l'autre côté sur la page, et une ligne où l'autre côté mène. J'en montre cinq. Quatre ont été exécutées des deux côtés, et la cinquième, le bloc cinq, du côté Softanza seulement. Les exécutions datent du 8 octobre 2026, entre 22 h 24 et 22 h 34, sur une machine Windows, et la construction du livre a ré-exécuté les blocs de Softanza le 9 octobre 2026 à 05 h 32. Tous tenus. L'autre côté est Python 3.13.15, et Node v22.20.0 avec son moteur V8 12.4 et ICU 77.1. R et Julia ne sont pas installés sur cette machine, et aucune paire ne s'en sert.

**Une : un entier est exact à toute taille.** Combien de chiffres garde le produit de deux nombres de vingt ? Exécutez-le :

```haro
oN = new stzNumber("12345678901234567890")
? oN.MultiplyByQ("98765432109876543210").Content()
#--> 1219326311370217952237463801111263526900
```

Quarante chiffres, exacts ! L'autre côté, Python 3.13.15, imprime les mêmes chiffres, `1219326311370217952237463801111263526900`, pour `12345678901234567890 * 98765432109876543210`. L'entier de Python est exact par défaut, et Softanza est à égalité avec lui. La ligne de Softanza est la plus longue : un littéral aussi long ne peut pas être un nombre natif, donc il est donné comme chaîne. L'autre côté, Node v22.20.0, imprime `1.219326311370218e+39`, parce que son nombre par défaut est un flottant de 64 bits. Il n'est exact que lorsqu'on le demande avec le suffixe `n`, un second genre de nombre. Donc où est le gain ? Sur le défaut de JavaScript, et non sur Python.

**Deux : des décimaux exacts.** `0.1` plus `0.2` fait-il `0.3` ici, et un prix multiplié par un taux garde-t-il ses centimes ? Exécutez-le :

```haro
? (new stzNumber("0.1")).AddQ("0.2").Content()
#--> 0.3
? (new stzNumber("19.99")).MultiplyByQ("0.15").Content()
#--> 2.9985
```

Il répond `0.3` et `2.9985` : les centimes sont gardés ! L'autre côté, Python avec des flottants, imprime `0.30000000000000004` et `2.9984999999999995`. Node imprime les deux mêmes, parce que JavaScript n'a pas de type décimal. Le module standard `decimal` de Python, importé et nourri de chaînes, imprime `0.3` et `2.9985` : à égalité avec Softanza, et au même coût par ligne. Donc Softanza gagne sur le défaut, puisqu'un nombre fait à partir d'une chaîne est un décimal exact, et est à égalité avec l'unique bibliothèque qui le fait délibérément. Le commentaire de la garde dit pourquoi : la valeur est stockée comme chaîne, et le calcul est fait sur des entiers mis à l'échelle par le moteur. Sa limite est dans les mots du dossier, et l'un d'eux est périmé. Les échelons pour les rationnels et pour les nombres complexes sont nommés dans le plan et, dans un commentaire de la garde des nombres qui ne sont pas perdus, « not built yet ». L'instantané contient une garde narrée pour chacun, `numeric_rationals_narrated` et `numeric_complex_narrated`, de sorte que ce commentaire est périmé et que je ne m'y fie pas. Je n'ai pas exécuté ces deux gardes.

**Trois : trier des mots accentués. Ici le terrain mène.** Softanza trie par point de code. Où cela place-t-il `étoile` ? Exécutez-le :

```haro
? @@( Q([ "zèbre", "étoile", "eau", "zoo" ]).SortedInAscending() )
#--> [ "eau", "zoo", "zèbre", "étoile" ]
```

Il répond `[ "eau", "zoo", "zèbre", "étoile" ]` : `étoile` en dernier, après `zoo` ! Le tri du terrain, conscient de la locale, place `étoile` entre `eau` et `zèbre`. L'autre côté, le `sorted` de Python, imprime la même liste : à égalité, et tous deux faux pour le français. Avec le module standard `locale` réglé sur `fr_FR.UTF-8`, trié avec `locale.strxfrm`, Python imprime `eau, étoile, zèbre, zoo`. Cela a fonctionné sur la machine de l'exécution. La locale doit exister sur l'hôte, et l'appel vaut pour tout le processus. Node, avec `Intl.Collator('fr')`, imprime le même ordre français, `eau, étoile, zèbre, zoo`, avec une bibliothèque intégrée. Donc le terrain mène : JavaScript avec un argument, Python avec la locale de l'hôte. Softanza n'a pas de collation. Le plan de culture du 18 août 2026 dit que le tri est le tri ordinal du moteur. Et la page de couverture note l'internationalisation partielle, contre profonde pour deux autres plateformes, avec une note : un pari délibéré contre la grande bibliothèque internationale.

Ce bloc est un écart épinglé. Sa promesse enregistre la réponse actuelle de la bibliothèque, de sorte que la page échoue le jour où la bibliothèque gagne la collation. C'est voulu. La règle propre du plan de culture dit qu'épingler un écart connu n'est légitime que lorsque l'assertion échoue le jour où l'écart est comblé, et lorsque l'étiquette le dit.

**Quatre : la majuscule turque. Le terrain mène.** Que répond la méthode quand on lui donne la locale turque ? Exécutez-le :

```haro
? Q("istanbul").UppercasedInLocale("tr_TR")
#--> ISTANBUL
```

Elle répond `ISTANBUL` : la locale a été acceptée et ignorée ! Python imprime `ISTANBUL` : à égalité, puisque la bibliothèque standard n'a pas de casse selon la locale. Node, avec `toLocaleUpperCase('tr')`, imprime `İSTANBUL`. Le turc a besoin de la majuscule pointée. C'est la perte la plus digne d'être imprimée, et ce n'est pas que le moteur manque de turc. C'est que la méthode prend une locale et, aujourd'hui, répond en majuscule simple sans le dire ; honorer la locale, ou refuser, est l'étape suivante. Le commentaire de la source dit : majuscule simple quand elle n'a pas de règle. Le plan de culture a mesuré la même chose le 18 août 2026 et l'a appelée l'équivalent en code de la fausse barre de progression. Sa loi est la raison de ce chapitre : pas de façades. Une opération honore la culture qu'on lui a donnée, ou elle refuse. Je tiens cela pour une vue, non pour un résultat, et la loi du plan de culture dit la même chose.

**Cinq : une instruction dans votre langue.** Une instruction en langage naturel est guidée par un dictionnaire et locale : pas de réseau, pas de modèle, pas de clé. Que fait-elle de la phrase, et qu'a-t-elle compris ? Exécutez-le :

```haro
o1 = Naturally("Make a list holding [ 3, 1, 3 ] then drop its duplicates")
? @@( o1.Result() )
#--> [ 3, 1 ]
? o1.Understood()
#--> create a list with [ 3, 1, 3 ] -> remove duplicates
```

Elle répond `[ 3, 1 ]`, et dit ce qu'elle a compris : `create a list with [ 3, 1, 3 ] -> remove duplicates`. Je n'ai pas exécuté l'autre côté. L'équivalent du terrain de « prends cette phrase et fais-le » est un appel de modèle. Ce qu'il lui faut, c'est un modèle. Un modèle hébergé demande un réseau, un compte, une clé et un coût par jeton ; un modèle local demande un modèle téléchargé et un GPU ou un processeur patient. Il lui faut une invite, et une vérification que la réponse est ce qui a été demandé, et la réponse n'est pas garantie d'être la même deux fois. La propre paire du site de ce genre écrit l'autre côté comme un commentaire, qui dit qu'il n'y a pas de pendant sans un modèle de langage externe.

Une perte de plus, qui n'est pas un bloc. Une chaîne d'un emoji de famille, cinq points de code, reliés par des liants, montre où la chaîne publique n'expose pas encore ce que le moteur sait. La classe compteur répond `1` pour le comptage de graphèmes ; `NumberOfChars` répond `5` et `NumberOfBytes` répond `18` ; et `GraphemeCount()` sur la chaîne elle-même lève une erreur, parce que la méthode n'est pas définie. Le moteur sait, et la chaîne ne le dit pas. Le `len` de Python donne `5`, et le `.length` de Node donne `8`.

Voilà la forme, cinq paires et une perte de plus ; ce que j'ai refusé pour y arriver vient ensuite.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé la grille seule.** Deux cent quatre-vingt-six coches dans la colonne de Softanza contre deux cent soixante-neuf croix dans les autres colonnes, c'est la forme d'une brochure.

**J'ai refusé de garder un chiffre phare qui ne se reproduit pas.** La note du domaine de projets du 13 septembre 2026 a remesuré le runtime sous la bibliothèque contre un runtime rapide du terrain sur six noyaux appariés. Appariés veut dire algorithme et tailles identiques des deux côtés, chaque côté dans son idiome rapide, sommes de contrôle inter-langages affirmées avant tout nombre, minima sur des exécutions répétées. Le terrain mène sur chaque ligne, d'un facteur entre 1,04 et 1,88. La note dit que l'affirmation à retirer est que le runtime le bat, au présent, sur x64. Le chiffre phare n'a jamais été remesuré après que le prototype, que la note appelle « spike », est devenu un produit. La note a demandé à l'auteur de corriger les notes propres du runtime. Le chiffre phare a été retiré dans la note du domaine de projets du 13 septembre 2026, et je n'en dis pas plus.

**J'ai refusé une rétractation qui supprime ses preuves.** Les notes propres du runtime du 29 août 2026 ont rétracté une table publiée dans l'autre sens, une perte sur un téléphone. L'exécution avait eu lieu sur les cœurs lents du téléphone alors que le pair tournait sur des cœurs rapides. Les notes gardent la table, barrée, et disent qu'une rétractation qui supprime ses propres preuves n'est pas une rétractation. Donc le dossier a retiré un gain et retiré une perte. La règle est de reproduire avant d'imprimer. Imprimer des pertes n'est pas la règle. C'est mon point de vue, et les deux retraits que garde le dossier, un gain et une perte, sont ce qui le soutient.

**J'ai refusé une comparaison qui ne peut pas être refaite.** Le paquet de passage de relais du même jour, le 13 septembre 2026, dit que les noyaux du prototype sont morts avec l'arbre de travail. C'est pourquoi une session extérieure a dû reconstruire la mesure à partir de prose.

**J'ai refusé une façade.** Les blocs trois et quatre.

**J'ai refusé la grande bibliothèque internationale.** La table du plan de culture dit qu'elle est tuée, une décision prise et en vigueur dans la première couche. Le coût, ce sont les blocs trois et quatre. La page de couverture l'imprime comme un pari délibéré.

**J'ai refusé de comparer sur le terrain le plus fort de l'outil.** L'étude du domaine de projets sur un runtime de navigateur a trois règles d'honnêteté. Chaque langage reçoit du code idiomatique ; les pertes sont publiées avec les gains ; chaque moteur est une construction de production. Elle dit, de sa propre page, que sans elles c'est du marketing. Son tableau de score a neuf scénarios, quatre gagnés et cinq perdus. Ce n'est pas une barrière de régression : ses nombres servent à apprendre, et non à barrer.

Le tribunal qui tiendrait ces refus vient ensuite, et il est proposé, non construit.

## 5. Le tribunal

Le tribunal des comparaisons est proposé et non construit. Le plan de l'étude le nomme : une ligne de comparaison sans source ou sans date ne se publie pas. Une paire de code dont l'autre côté n'a pas été exécuté, ou l'a été dans une construction de débogage, ne se publie pas non plus. Je n'ai trouvé aucun fichier dans la bibliothèque ou le site qui l'implémente. Donc qu'existe-t-il ? Quatre gardes, qui prouvent les blocs et touchent à la méthode.

`numeric_exactness_narrated` prouve l'arithmétique décimale exacte, les entiers au-delà de 2 puissance 53, le produit de quarante chiffres, et la division exacte quand elle se termine. `numeric_no_loss_narrated` prouve qu'un nombre n'est pas détruit en entrant, et que l'échelle de représentation est observable. Son commentaire final nomme encore comme non construits les échelons des rationnels et des nombres complexes, et il est périmé (voir le bloc deux). `semantic_resolver_narrated` prouve que les paraphrases se résolvent en opérations canoniques par le lexique local, et la phrase du bloc cinq est l'un de ses cas. Elle ne passe pas à ce commit : je l'ai exécutée le 8 octobre 2026 et elle s'arrête sur une erreur levée par une fonction de découpage de chaîne, avant sa fin. Donc la page compte ses assertions et ne prétend pas à son verdict. `engine_is_optimised_narrated` prouve que le moteur est compilé avec optimisation, par une barrière de temps : c'est la garde propre de la bibliothèque pour la règle de la construction de production.

Aucune garde n'affirme les blocs trois et quatre comme des écarts épinglés. Aucune garde n'existe pour une paire de code dont l'autre côté n'a pas été exécuté. Je range les deux parmi les demandes.

Le tribunal n'est pas construit, mais le dossier tient déjà la liste de ce que le terrain a, et elle suit.

## 6. Le terrain, et où il mène

Le dossier tient déjà la liste de ce que le terrain a et de ce qui manque à Softanza. Je l'imprime, par fichier et par date, à côté des gains.

**La performance, face au terrain, 29 juillet 2026.** Pas de magasin de séries temporelles, pas de langage de requête, pas de tableaux de bord : par conception, le volet exporte. Pas de contexte distribué au-delà de HTTP. Un échantillonnage honnête, là où celui du terrain est plus fin aujourd'hui. Des décennies d'intégrations, que les titulaires possèdent. Les mots propres de l'étude sont que sur l'étendue les titulaires gagnent décisivement, et que le volet ne les concurrence pas et ne devrait pas feindre de le faire. Quatre pertes sont barrées avec la phase qui les a fermées.

**L'analyse d'incident, face au terrain, 1er août 2026.** L'échelle, la rétention et la recherche, là où borné veut dire oublier. Pas de télémétrie de l'hôte, du noyau ou du réseau. Un petit ensemble de détections livrées face au corpus d'une communauté. Le flux de travail d'un centre d'opérations. Et les jointures non câblées, que l'étude appelle le plus grand écart honnête du système, listées et non cachées.

**L'étude des extensions, 16 août 2026.** Le terrain est en avance sur la granularité des permissions, sur la résolution des dépendances, sur la distribution et sur la signature. L'en-tête de l'étude dit que c'est de l'analyse et non des règles.

**Le plan de culture, 18 août 2026.** Chaque ligne a été vérifiée dans cette session en l'exécutant. La casse prend une locale sur quatre niveaux et ne l'honore pas encore. La collation, la mise en forme des chiffres, les calendriers non grégoriens et les fuseaux horaires sont absents. Le statut du plan était alors non commencé.

**L'étude du domaine de projets sur le runtime de navigateur, 8 août 2026.** Quatre lignes sur neuf gagnées, cinq pour les pairs, et l'opcode de boucle fusionné d'un pair reste en avance d'une génération de conception.

**Le runtime face à un pair rapide, 13 septembre 2026.** Six noyaux, les sommes de contrôle d'abord, le pair en avance sur chaque ligne.

**Le banc d'essai de chaînes du 7 juillet 2026**, et la bataille polyglotte, dans une narration datée du 18 avril 2025 : l'ancien langage hôte est arrivé dernier sur sept dans deux manches sur trois. Il est arrivé dernier au total aussi. Les deux portent des réserves que le dossier ultérieur y a mises. Je n'ai pas ré-exécuté le banc d'essai. La construction par défaut du moteur était une construction de débogage jusqu'au 26 juillet 2026, et le fichier de construction propre de la bibliothèque dit que toute bibliothèque partagée qu'elle avait jamais chargée était compilée sans optimisation. Donc le banc d'essai a probablement tourné sans optimisation. C'est une inférence, et je l'énonce comme telle. Le même commentaire dit que, sur le travail de chaînes, de listes et de matrices, ce changement n'achète qu'environ quinze pour cent. Donc le mode de construction est une réserve sur les nombres et non une excuse pour eux. Je n'ai pas pu lire ici le mode de construction du moteur, et l'horloge du langage hôte résout dix à quinze millisecondes. Le banc d'essai est donc cité ici comme un dossier daté, avec cette réserve, et non comme une mesure présente.

**La matrice de couverture.** Trente domaines en sept groupes, face à quatre autres plateformes, lue le 17 septembre 2026. Le bilan de Softanza est sept profonds, quatorze solides, sept partiels, deux absents, présent dans vingt-huit sur trente. Je l'ai recompté à partir des lignes et il correspond. Les deux lignes absentes sont les mathématiques symboliques (« no computer algebra ») et le paquet, la construction et le déploiement (« a library, not a registry »). Parmi les sept lignes partielles se trouve l'internationalisation, « a deliberate bet against ICU », et la ligne neuronale est « inference only; no training foundry ». Les bilans stockés de deux des autres plateformes ne correspondent pas à leurs propres lignes, d'un en deux endroits. Je n'imprime que le bilan de Softanza. La matrice cite un fichier boussole comme source des notes. Je n'ai pas pu localiser le fichier dans l'instantané, dans la copie de travail ni dans le dépôt du domaine de projets.

**La comparaison de graphes, une narration datée du 26 décembre 2025.** Un modèle l'a écrite, et le dit dans sa signature. Sa colonne pour Softanza se note elle-même d'une croix sur le passage à l'échelle et sur les transactions et d'un avertissement sur la performance, et sa conclusion énumère où les solutions traditionnelles gagnent.

Là où Softanza se distingue, selon le dossier, sans un nombre : le SLA ; l'acte gouverné ; l'événement typé ; la seule ligne de la matrice sur la gouvernance et l'exécution sûre. Deux de plus : des nombres exacts par défaut, face à deux flottants ; une instruction qui se résout localement. Et une méthode qui imprime chacun d'eux à côté d'une perte.

Voilà la liste ; je dis maintenant où ce chapitre s'arrête.

## 7. La limite

Ce qui est construit : quatre des cinq paires, exécutées des deux côtés, et la cinquième du côté Softanza. Les quatre paires de code du site sont construites aussi. Je les ai ré-exécutées le 8 octobre 2026, trois d'entre elles des deux côtés (la quatrième a un commentaire pour son autre côté). Ma note de la nuit dit que les sorties concordaient. Le sont aussi les études de terrain de la bibliothèque sur la performance, l'analyse d'incident et les extensions, avec leurs sections de pertes, et le plan de culture, qui imprime ses pertes. Le sont aussi le harnais du banc d'essai de chaînes et la garde que le moteur est optimisé.

Ce qui est conçu ou proposé : un registre de comparaisons comme données ; un tribunal des comparaisons ; la ré-exécution des deux bancs d'essai. L'étude tient les trois. Quand j'ai rédigé ce chapitre, le 8 octobre 2026, je les ai cherchés dans la bibliothèque et dans le site et n'ai rien trouvé. Le site, lu le 9 octobre 2026, imprime maintenant cinq règles pour comparer, la première étant « Cite or do not publish ». Il imprime aussi une liste des neuf lignes où Softanza est partiel ou absent, avec les plateformes qui y sont profondes. Il dit, dans une ligne marquée conçu, qu'un registre de comparaisons n'est pas encore tenu comme données. Il ne nomme pas le tribunal.

Ce qui est absent : une colonne *comparé* sur l'Atlas, sur le registre des innovations et sur les narrations. Absent du site : les études de terrain, les soixante-quatre grilles elles-mêmes (il en donne maintenant le nombre, et rien de plus), les deux bancs d'essai et la table du runtime. Absent de la bibliothèque : la collation selon la locale ; la casse selon la locale ; un comptage de graphèmes sur la chaîne publique ; une base de fuseaux horaires. Et absent encore : la ré-exécution du banc d'essai du 7 juillet 2026, et la source de la matrice de couverture.

Et quelque chose qui n'est pas reproduit : les soixante-quatre, les six cent quinze et les trente et un de l'étude, que mon parcours n'a pas reproduits, et les comptes de symboles.

La méthode est plus stricte que le dossier auquel elle est appliquée. Des comparaisons plus anciennes de la bibliothèque précèdent ses règles et ne satisfont pas encore l'une d'elles ou plus. Le banc d'essai de chaînes a probablement tourné sur un moteur de débogage. La bataille polyglotte n'a ni versions ni dates dans son texte, et dit que ses temps sont relatifs à un environnement informatique précis. La grille de graphes n'a ni versions, ni dates, ni sources pour ses cellules. La grille de charge cognitive d'un autre article de conception avance des chiffres de soixante à soixante-dix pour cent sans méthode imprimée à côté. Cet article finit ensuite sur un positionnement honnête qui nomme quatre choses sur lesquelles la bibliothèque ne concurrence pas.

Six portes suivent, une pour chaque lecteur de cette page.

## 8. Six portes

**Le programmeur.** Copiez une paire. Exécutez les deux côtés dans vos propres versions, gardez la sortie telle qu'elle est venue, et ajoutez la ligne où l'autre outil est en avance.

**L'analyste.** La matrice de couverture n'est une aide à l'achat que parce qu'elle montre deux lignes absentes et sept partielles dans ses propres couleurs. Lisez celles-là d'abord.

**Le concepteur.** La perte va dans le même bloc et dans la même typographie que le gain. Le mot d'étape fait partie de l'interface.

**Le décideur.** Demandez à tout fournisseur, celui-ci compris, la version de l'autre côté, la date, si cela a été exécuté, et la ligne qu'ils perdent. La note du 13 septembre 2026 est un modèle de chiffre phare retiré.

**Le formateur.** Une paire de code est une leçon sur ce que coûte une ligne. L'apprenant écrit la sortie de l'autre côté avant de l'exécuter.

**L'agent.** Quand vous répétez une affirmation sur un autre outil, portez sa version et sa date, et dites si vous ne l'avez pas exécutée. Le registre qui rendrait cela vérifiable par un agent est proposé et non construit.

## 9. Exercice

Choisissez une tâche où vous croyez que votre propre outil est en avance, et une où vous croyez que l'autre l'est. Faites une comparaison qui obéit aux trois règles : la version de l'autre côté et la date, les deux côtés exécutés, la perte imprimée.

```haro exercise
? YourSide(the_input)
#--> the line your tool prints
```

Sous elle, écrivez comme texte : le nom et la version de l'autre outil, la date, la ligne exacte qu'il imprime, et une ligne de la forme « ici l'autre mène parce que... ». Un lecteur vérifie les trois lignes de texte, puisqu'un lanceur ne le peut pas.

Une variante qu'une machine peut juger : prenez les cinq lignes de l'autre côté du bloc trois et prédisez, avant d'exécuter, l'ordre que chacune imprime. Je ne vous dirai pas quel ordre est le bon.

Je vous laisse celui-ci. Voici le bloc trois, sa promesse retirée :

```haro exercise
? @@( Q([ "zèbre", "étoile", "eau", "zoo" ]).SortedInAscending() )
```

Sous lui, écrivez la promesse qu'attendrait un lecteur français, l'ordre que donne le tri conscient de la locale du terrain à la section 3, comme une ligne `#-->`, et exécutez-le. Je n'imprime pas le verdict. Lisez-le, puis lisez les sections 3 et 7 pour apprendre pourquoi ce bloc est un écart épinglé et non une faute du tri. Quand vous aurez résolu cela, vous saurez pourquoi le bloc trois promet la réponse actuelle de la bibliothèque et non celle du terrain.

Le chapitre 23 se tourne vers l'architecte, et vers un monde, une constellation et une plateforme. Là, la solution est déclarée en mondes, en liens et en une enveloppe avant que rien en soit construit, et chaque traversée entre eux est gouvernée.
