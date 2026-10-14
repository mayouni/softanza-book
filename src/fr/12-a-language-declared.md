---
id: a-language-declared
part: 3
number: 12
title: Un langage, déclaré
spine: false
narrations: [stz-conditional-code-narration.md, stznatural-vs-ring-naturallib.md, stznatural-narration.md, stz-bridging-minds-and-code.md]
site: [languages]
guards: [structuredoutput_narrated, schema_grammar_narrated, constrained_decoding_narrated, 483_w_and_wf_forms_in_conditional_code, calc_column_engine_narrated]
stage:
  built: "dans la bibliothèque : une déclaration jugée au moment où elle est déclarée ; un tribunal et une grammaire issus d'une seule déclaration, avec la liste de ce que la grammaire a laissé tomber ; une machine à grammaire qui parcourt les octets et refuse en nommant ; une description pour une personne et un prompt pour un modèle d'IA à partir du même texte. Hors de la bibliothèque : une forge qui transforme une déclaration en tribunal et en grammaire, exécutée sur les propres langages du domaine de projets"
  designed: "la forge à l'intérieur de la bibliothèque ; sa liste complète de produits issus d'une seule déclaration (imprimeur, graphe de connaissance, porte naturelle, narration, runtime, un seul binaire statique) ; les projections d'un langage vers une application"
  absent: "la grammaire de la forge pour un mot de menu ; une garde qui affirme le refus d'une fonction hôte dans une condition ; le chiffre deux sur dix contre dix sur dix, qui demande un fichier de modèle que l'instantané ne contient pas"
status: draft
rulings: ["12.10", "12.21", "12.27", "12.29", "12.30"]
research: research/ch12.md
---

Dans ce chapitre, je prends une seule déclaration de la commande d'un restaurant et je la donne à trois lecteurs : une personne, un modèle d'IA et le tribunal. Je laisse la même déclaration produire une grammaire, et je montre où la grammaire et le tribunal s'accordent et où ils se séparent. Puis je quitte la bibliothèque pour la forge. C'est la machinerie qui transforme la seule déclaration d'un langage en son tribunal et sa grammaire, et je dis ce qu'elle a forgé et ce qu'elle n'a pas forgé. J'ai décidé que Haro est la langue des langues, et j'ai refusé une forme d'échappatoire ouverte. Le principe est une règle de Haro : déclarer un langage est aussi facile que déclarer une variable.

## 1. Le concept, tel que le terrain le tient

Deux familles d'outils permettent de déclarer un langage sur le terrain. La première est l'atelier de langages et le générateur d'analyseurs : JetBrains MPS, Xtext, Spoofax, et le `#lang` de Racket vous donnent de quoi définir un langage avec sa grammaire, son éditeur et ses vérifications. L'étude de terrain du domaine de projets lui-même, d'août 2026, dit pourquoi ils n'ont pas gagné. Ils dépendaient d'un écosystème, et les langages de Racket vivent et meurent à l'intérieur de Racket.

La seconde est le DSL interne : une bibliothèque dont les appels se lisent comme des phrases, alors que le fichier peut encore contenir n'importe quel code hôte. La même étude a la phrase que je retiens : la fermeture est le produit, et un DSL interne qui ne peut pas refuser du code hôte arbitraire est une API qui porte le costume d'un langage. Son groupe témoin, ce sont les langages fermés qui ont gagné : SQL, regex, Make, HTML et CSS, HCL, GraphQL, Markdown, CUE.

Pour la grammaire qu'un modèle doit respecter, le dossier nomme un seul outil : l'échantillonneur de grammaire d'une bibliothèque d'inférence locale bien connue, que la machine de la bibliothèque suit pour son encodage des éléments et son algorithme. Rien n'en est repris. (Connaissance générale, pas une étude du dossier : les fournisseurs de modèles proposent des modes de sortie structurée qui prennent un schéma JSON. Des bibliothèques ouvertes transforment un schéma ou une expression régulière en masque sur les jetons du modèle.)

Le chapitre 11 a dit ce qu'est un langage fermé, et ce qui a été perdu quand le terrain l'a laissé ouvert. Je le tiens pour acquis. Ce chapitre dit ce qui est nouveau : ce qui *produit* un langage fermé.

## 2. Le premier principe

**Déclarer un langage est aussi facile que déclarer une variable.**

C'est l'intitulé d'une règle de Haro, tranchée le 1er octobre 2026, et le noyau de la vision dit la même chose : l'époque rend la déclaration d'un langage aussi facile que celle d'une variable. L'autre moitié du chapitre a sa phrase, tirée de la doctrine de totalité de l'alphabet, ratifiée le 27 septembre : la malformation meurt à l'échantillonneur, la fausseté meurt au tribunal, et la non-terminaison est inexprimable.

Et celle que je dois porter à côté de chaque gain, tirée du contrat de la bibliothèque pour la sortie structurée : la structure tue la malformation, et non la fausseté.

## 3. La forme Softanza

Prenons une déclaration de ce à quoi doit ressembler la commande d'un restaurant. Elle a trois champs : un plat pris dans un menu fermé, une quantité entre 1 et 12, et une note facultative. Un seul texte est lu par trois lecteurs. Une personne lit une description. Un modèle lit une clause pour son prompt. Et le tribunal lit le même texte et juge une réponse. Que répond-il à un plat nommé pizza et à quarante portions ? Exécutez-le :

```haro
oO = StzOutputSchemaQ([
	[ :field = "dish",     :type = :oneof,  :choices = [ "margherita", "tiramisu" ] ],
	[ :field = "quantity", :type = :number, :must = [ [ ">=", 1 ], [ "<=", 12 ] ] ],
	[ :field = "note",     :type = :string, :optional = 1 ]
])
? oO.Describe()
#--> schema 'output' -- 3 field(s)
#      dish : oneof (margherita | tiramisu) [required]
#      quantity : number [required], must be at least '1', must be at most '12'
#      note : string [optional]
? oO.PromptClause()
#--> Answer with ONLY this structure, one field per line, nothing before it and nothing after it:
#
#    dish: <one of: margherita | tiramisu>
#    quantity: <number>
#    note: <text>
aV = oO.Verify([ :dish = "pizza", :quantity = 40 ])
? aV[:ok]
#--> 0
? aV[:findings][1][:message]
#--> field 'dish' is a closed enumeration (margherita | tiramisu) and the model answered 'pizza'.
? aV[:findings][2][:message]
#--> field 'quantity' must be at most '12', and the model answered '40'.
```

Le tribunal répond dans les mots de la déclaration : `field 'dish' is a closed enumeration (margherita | tiramisu) and the model answered 'pizza'.` Maintenant la même déclaration produit une grammaire. Le tribunal et la grammaire naissent d'un seul texte, et ils s'accordent sur la forme. Ils se séparent sur une valeur. Quarante portions ont la bonne forme : lequel des deux les laisse passer, et la bibliothèque dit-elle ce que la grammaire a laissé tomber ? Exécutez-le :

```haro
cG = oO.ToGBNF()
cGood  = "dish: margherita" + nl + "quantity: 2" + nl + "note: no basil" + nl
cBand  = "dish: margherita" + nl + "quantity: 40" + nl + "note: no basil" + nl
cShape = "dish: margherita" + nl + "quantity: many" + nl + "note: no basil" + nl
? StzGrammarAccepts(cG, cGood)
#--> 1
? oO.Accepts(cGood)
#--> 1
? StzGrammarAccepts(cG, cBand)
#--> 1
? oO.Accepts(cBand)
#--> 0
? StzGrammarAccepts(cG, cShape)
#--> 0
? oO.Accepts(cShape)
#--> 0
? len(StzFind("lessequal", oO.UnenforcedByGrammar())) > 0
#--> 1
```

La deuxième paire est l'enjeu du chapitre : la grammaire répond `1` et le tribunal répond `0` ! Je n'imprime pas la liste de ce que la grammaire a laissé tomber, parce que son texte porte, à un endroit, l'ancien nom du tribunal. Je vérifie qu'elle nomme la borne de l'intervalle.

On ne demande pas au modèle d'IA d'être prudent. L'échantillonneur demande à la grammaire, à chaque jeton candidat, si elle pourrait continuer. Ainsi un mot qui n'est pas au menu n'est pas refusé après avoir été dit. Peut-il seulement commencer ?

```haro
? StzGrammarCouldContinue(cG, "dish: t")
#--> 1
? StzGrammarCouldContinue(cG, "dish: p")
#--> 0
? StzGrammarCouldContinue(cG, "dish: margherita" + nl + "quantity: 2")
#--> 1
? StzGrammarCouldContinue(cG, "dish: margherita" + nl + "quantity: <")
#--> 0
```

Il ne le peut pas : `dish: p` répond `0`. La dernière ligne est un échec que la mesure a trouvé dans un petit modèle : le substitut `<number>` répété là où doit se trouver un nombre. Et un jeton n'est pas un octet. Un morceau peut être valide comme préfixe et invalide comme complétion, et la machine reçoit le morceau entier. Que répond-elle à `yesterday`, qui commence comme `yes` ?

```haro
cY = 'root ::= "yes" "\n"'
? StzGrammarCouldContinue(cY, "y")
#--> 1
? StzGrammarCouldContinue(cY, "ye")
#--> 1
? StzGrammarCouldContinue(cY, "yesterday")
#--> 0
```

`y` et `ye` répondent `1`, et `yesterday` répond `0` !

Ce que la machine ne tiendra pas, elle le refuse en le nommant. Un langage fermé refuse ce qu'il ne peut pas porter, et n'approxime jamais. Une règle récursive à gauche est refusée par un code, de même qu'une règle citée et jamais définie. Une structure imbriquée est refusée par la grammaire. Le tribunal la lit-il quand même ?

```haro
? left(StzGrammarRefusal('root ::= tail' + nl + 'tail ::= tail "x" | "x"'), 7)
#--> GBNF-M7
? left(StzGrammarRefusal('root ::= greeting'), 7)
#--> GBNF-M4
? StzGrammarRefusal(cG) = ""
#--> 1
oNest = StzOutputSchemaQ([
	[ :field = "title",  :type = :string ],
	[ :field = "author", :type = :structure, :fields = [ [ :field = "name", :type = :string ] ] ]
])
? oNest.IsExpressibleAsGrammar()
#--> 0
try
	oNest.ToGBNF()
catch
	? len(StzFind("GBNF-F5", cCatchError)) > 0
done
#--> 1
? oNest.ParseOutput('{ "title":"T", "author":{"name":"Ada"} }')[:ok]
#--> 1
```

Le texte du refus de la structure imbriquée porte l'ancien nom du tribunal, donc je n'imprime que les codes. La dernière ligne est l'enjeu : le tribunal lit ce que la grammaire refuse d'écrire.

Le langage de déclaration est lui-même fermé. Une faute de frappe dans la loi est refusée au moment où la loi est déclarée. Le contrat de la bibliothèque dit pourquoi. Une clé comme `:requird = 0` laisserait un champ obligatoire sans un mot, et c'est la classe de faute de frappe qu'un tribunal ne doit pas tolérer dans sa propre loi. Que répond le tribunal à une telle clé ?

```haro
try
	StzOutputSchemaQ([ [ :field = "x", :type = :string, :requird = 0 ] ])
catch
	? cCatchError
done
#--> stzOutputSchema: unknown key ':requird' in field #1 (use :field, :name, :type, :required, :optional, :choices, :oneof, :of, :fields, :must, :note, :description).
```

La faute de frappe a été refusée sur-le-champ, et le message liste les clés permises !

Et une fonction hôte n'est pas un mot du langage fermé des conditions. Il y a deux façons de dire une condition, le langage fermé et la porte d'une fonction. Une racine carrée est un mot du langage d'expressions du moteur, et un sinus n'en est pas un. Que répond la forme textuelle au sinus, et que répond la forme fonction, qui exécute du code hôte ?

```haro
o = new stzList([ 4, 7, 10, 3, 8 ])
? @@( o.FindW('{ sqrt(@item) < 3 }') )
#--> [ 1, 2, 4, 5 ]
? @@( o.FindW('{ sin(@item) < 2 }') )
#--> [ ]
? @@( o.FindWF( func x { return sin(x) < 2 } ) )
#--> [ 1, 2, 3, 4, 5 ]
```

Ce que j'ai vu, et que la narration ne dit pas : le refus est silencieux et entier. La forme textuelle a imprimé `[ ]` et la forme fonction a imprimé `[ 1, 2, 3, 4, 5 ]` : rien de l'une, tout de l'autre. Une condition dont la branche gauche est vraie et dont la droite porte un sinus a imprimé `[ ]`. Une condition qui appelle une fonction de moi ne l'a jamais appelée. Une erreur de syntaxe a aussi imprimé `[ ]`. Le langage est fermé, et il refuse sans un mot. La couche naturelle du chapitre 11 dit pourquoi elle refuse, et celle-ci ne le dit pas.

### La forge, hors de la bibliothèque

Un langage déclaré une fois devrait donner son tribunal, sa bouche, sa voix et ses lecteurs. C'est la forge, et c'est là que l'étude de ce livre rencontre sa propre limite : la forge n'est pas dans la bibliothèque.

Je dirai ce que le dossier contient, et ce que j'ai observé le 8 octobre 2026 sur le runtime plus ancien, l'oracle. Le dossier est une charte et un spike dans un autre dépôt, en pur code du noyau qui tourne sur l'oracle. La forge lit une déclaration et écrit deux fichiers, un programme de tribunal et une grammaire. Les échelons du spike, entre le 1er et le 4 octobre 2026, ont forgé des tribunaux et des grammaires pour le langage machine du domaine de projets et pour un langage de flotte déclaré par-dessus. Ils ont fait de même pour le langage d'expressions et pour quatre lettres de plus de l'alphabet. Chacun a été jugé sur les cas propres du langage préexistant. Ces cas étaient sans adaptation pour le langage d'expressions (W) et pour Z, réexprimés pour F et A, et, pour Q, les réponses propres de l'ancien langage, relevées. Dans l'ordre : 117 sur 120 pour le langage machine, les trois restants étant les sortes du fichier de flotte. Puis 32 sur 32 pour le langage de flotte, 29 sur 29 pour W, 16 sur 16 pour Z, 25 sur 25 pour Q, 26 sur 26 pour F et 35 sur 35 pour A. C'est la méthode du chapitre 3, déclarer puis gouverner, appliquée à la forge elle-même.

J'ai fait tourner la forge sur un petit langage que j'ai écrit pour ce livre, la commande d'une table dans les mots de la salle à manger. C'est un exemple, écrit pour le livre et exécuté une fois, hors de la bibliothèque :

```text
DEFINE LANGUAGE order AS ( VERSION "0.2", GRAMMAR "0.2", COURT "none", EXTENSION ".order" )
  RATIONALE "A table's order, in the words of the dining room"
DEFINE MENU dishes AS ( WORDS [margherita, tiramisu, chianti],
  MESSAGE "the kitchen cooks margherita, tiramisu or chianti" ) RATIONALE "The kitchen's closed menu"
DEFINE RANGE portions AS ( MIN 1, MAX 12,
  MESSAGE "{value} portions is not an order: one to twelve" ) RATIONALE "A table orders between one and twelve"
DEFINE DECLARATION line AS ( VERB "ORDER", SEATS [dish: dishes, quantity: portions, note: text?] )
  RATIONALE "One line of an order: what, how many, and a word for the kitchen"
DEFINE REFUSAL unknown_verb AS ( MESSAGE "The dining room speaks only of orders." )
  RATIONALE "The closure speaks when an alien verb arrives"
```

La forge a imprimé qu'elle avait forgé une sorte et un refus, en une fraction de seconde d'horloge, et a écrit un tribunal d'environ 2,6 kilooctets. Que répond ce tribunal à un plat hors du menu, à quarante portions et à un verbe étranger ? Il a refusé les trois, dans les mots propres de la déclaration :

```text
DISH pizza          ->  order (line 2): the kitchen cooks margherita, tiramisu or chianti, not 'pizza'
QUANTITY 40         ->  order (line 3): 40 portions is not an order: one to twelve
DROP TABLE orders   ->  order (line 1): Unknown verb 'DROP': The dining room speaks only of orders.
```

Les refus sont les mots propres de la déclaration, écrits à côté de la grammaire. Même `DROP TABLE orders` a été refusé dans les mots de la salle à manger ! C'est toute la preuve du langage `order` : il a été exécuté une fois, hors de la bibliothèque, et ce n'est pas une déclaration du dossier.

Trois observations de plus, chacune une limite.

**Le méta-tribunal refuse l'échappatoire.** La déclaration du langage des déclarations liste les opérateurs et les opérandes qu'elle peut employer. Une déclaration qui listait `eval` parmi ses opérateurs, dans une fixture épinglée le 29 août 2026, a été refusée : `eval` n'est pas dans le menu fermé des opérateurs, une échappatoire est inexprimable, non interdite. Un appel hôte parmi les opérandes a été refusé de la même façon.

**La grammaire de la forge ne tient que la forme.** Un siège de menu ressort comme un identifiant général, donc la grammaire forgée laisse passer `pizza`. Le compilateur de schémas de la bibliothèque, dans les blocs ci-dessus, ferme le même menu en une alternance. Sur le langage machine du domaine de projets, la grammaire forgée accepte une référence pendante que le tribunal refuse. Le dossier nomme une différence entre la bouche et le tribunal, la part qu'une grammaire hors contexte ne peut pas dire : les noms en double, les références pendantes. Je n'ai trouvé aucun enregistrement qui énonce le manque du menu comme un manque.

**La vision n'a pas rattrapé.** Le texte de la vision, daté entre le 27 septembre et le 5 octobre 2026, dit que la forge n'a pas forgé. Le fichier des principes, daté du 1er octobre 2026, dit que la forge n'existe pas. Le même dépôt a construit le spike le même jour et forgé pour plusieurs langages. La phrase vraie a donc deux côtés. La forge a forgé des tribunaux et des grammaires pour plusieurs langages, hors de la bibliothèque, et elle n'a pas forgé la liste complète que le principe promet. Et le texte de la vision n'a pas été mis à jour. Dans les mots d'étape du livre, la forge est construite hors de la bibliothèque et conçue pour la bibliothèque, et la limite du chapitre 11 le dit de même.

### Les facettes d'un langage déclaré

Par facette, j'entends ici une surface d'un langage déclaré. La charte liste ce que la forge produit à partir d'une déclaration, et je donne à chacune un mot d'étape :

| facette | ce que c'est | étape |
|---|---|---|
| le texte | la déclaration, simple et fermée, avec une justification exigée sur chaque déclaration | construit à l'extérieur ; l'analogue de la bibliothèque est la déclaration de schéma |
| le tribunal | le juge généré pour le langage, qui parle dans les mots propres de la déclaration | construit à l'extérieur ; l'analogue de la bibliothèque est `Verify` et `Accepts` |
| la bouche | la grammaire pour un modèle d'IA contraint | construit dans la bibliothèque pour les schémas ; construit à l'extérieur pour les langages déclarés, la forme seulement |
| le prompt | l'instruction qu'un modèle d'IA lit, réglée par la mesure | construit dans la bibliothèque ; inconnu pour les langages déclarés |
| la lecture de la personne | une description pour un humain | construit dans la bibliothèque (`Describe`) |
| la voix | le langage qui narre une exécution, une phrase, un refus ; jamais stocké et jamais relu par l'analyse | construit à l'extérieur ; l'analogue de la bibliothèque est `Understood()` |
| les langues | une langue humaine comme fichier de données | construit à l'extérieur pour deux langues ; construit dans la bibliothèque pour cinq paquets (chapitre 11) |
| les projections | le monde rendu à une application, un serveur, une page, un appareil | conçu |
| les faces | une seconde syntaxe de Haro | conçu ; le chapitre 16 la raconte |

Le mot *facette* a d'autres sens dans ce livre, et je définis le mien ici : une surface d'un langage déclaré. Le deuxième sens est une syntaxe de Haro pour un programmeur d'un autre langage : le tableau l'appelle une *face*, et le chapitre 16 la raconte. Le troisième est un onglet du ruban de l'environnement, une phase d'une vie, celui du chapitre 26.

## 4. La décision, et ce que j'ai refusé

**J'ai décidé que Haro est la langue des langues.** L'en-tête de la charte me cite, du 1er octobre 2026 : Haro est une langue des langues, dans laquelle les artisans du logiciel définissent un langage pour leur domaine et programment avec lui, ou laissent leurs agents d'IA le faire. La charte enregistre un renversement : sa première décision, en tant que socle généraliste sous la famille des langages déclarés, a été renversée. Le reste de cette ratification était mon « suivez vos recommandations » sur sept décisions, et ce sont des décisions par délégation.

**J'ai décidé de déclarer, et non d'écrire.** L'acte du noyau : déclarer un langage. Ce fut une extraction et non une invention : les premiers langages ont été déclarés après qu'ils tournaient déjà et avaient des consommateurs.

**J'ai refusé une forme d'échappatoire ouverte.** Aucune clause, aucun opérateur ni opérande ne désigne du code hôte, des appels, une évaluation ou des entrées et sorties. Inexprimable, non interdit. Deux fixtures épinglent le refus, et je les ai relancées.

**J'ai refusé la logique dans la surface de déclaration.** La déclaration déclare et ne calcule pas. L'alphabet n'est délibérément pas Turing-complet, et c'est sa puissance et non sa pauvreté. C'est mon point de vue.

**J'ai refusé le langage naturel comme surface de déclaration.** Le langage naturel demande, et il ne déclare jamais. Un brouillon peut être proposé, et le tribunal décide, et l'humain ratifie.

**J'ai refusé un seul texte pour déclarer et pour calculer.** La programmabilité et la fermeture n'occupent jamais la même surface. Le code de calcul n'atteint un monde déclaré que par les portes que la forge génère, et le chapitre 16 parle de la porte.

**J'ai refusé de laisser la moitié grammaire mettre le tribunal à la retraite.** Le contrat dit que le tribunal ne part pas à la retraite quand le décodage contraint arrive. Et ce que la grammaire ne peut pas exprimer, elle le refuse, et ne l'aplatit ni ne l'approxime jamais.

**J'ai refusé une seconde face comme un second sens.** Une face épelle le graphe ; elle ne lui donne jamais le sens de Python ou de JavaScript. C'est le mémo d'une session, qui propose et ne tranche rien, et sa question de savoir combien de faces avant l'annonce est la mienne, et sans réponse dans le dossier.

Vient ensuite le tribunal, et les gardes qui sont derrière lui.

## 5. Le tribunal

`structuredoutput_narrated` prouve qu'une déclaration est jugée quand elle est déclarée, avec un type inconnu, une clé inconnue et un menu vide refusés. Elle prouve que deux formes de transmission sont lues et que rien n'est deviné, qu'il n'y a pas de crédit partiel, que l'imbrication fonctionne, et qu'une nouvelle tentative tient dans un seul budget. Dans sa dixième scène, elle prouve qu'un mensonge est laissé passer exprès. `schema_grammar_narrated` prouve que la déclaration se compile en grammaire, et qu'une énumération fermée devient une alternance fermée. Elle prouve que l'optionnel et l'arité des listes sont traités, que les contraintes non imposées sont listées par champ et par opérateur, et qu'une structure imbriquée est refusée avec un code nommé. `constrained_decoding_narrated` prouve que la machine parcourt une grammaire octet par octet, qu'un préfixe n'est pas un tout, et que `yesterday` est refusé. Elle prouve que le substitut écrit par le modèle ne peut pas être atteint, que les refus sont nommés, que la structure n'est pas la vérité, et qu'une grammaire sur une session en flux est refusée. Ses deux scènes qui demandent un modèle génératif le disent. `483_w_and_wf_forms_in_conditional_code` prouve que les deux formes d'une condition donnent les mêmes positions. Elle n'affirme pas le refus du langage fermé, et aucune garde ne l'affirme.

Aucune garde de la bibliothèque ne teste une forge, puisqu'il n'y en a pas. La garde de la forge est à l'extérieur : le spike passe vingt-trois étapes en 367,5 secondes le 4 octobre 2026, d'après son propre fichier. Je ne l'ai pas lancé. Et la première exécution du méta-tribunal lui-même fut de vingt-huit sur vingt-huit le 29 août 2026. Le lecteur de gardes du livre ne résout que les gardes de l'arbre de tests de la bibliothèque, donc celles-ci ne peuvent pas être nommées dans le front matter.

Le premier essai est valide dans deux cas sur dix quand on vérifie après coup, et dans dix sur dix quand il est contraint. Ce chiffre est un nombre dans un commentaire de ces gardes. On ne peut pas le reprendre ici : les scènes réelles demandent un fichier de modèle génératif, et l'instantané ne contient, dans son dossier des modèles, qu'un fichier de somme de contrôle. Le chapitre 11 porte le chiffre, et j'y renvoie.

## 6. Le terrain, et où il mène

Les ateliers de langages mènent sur l'outillage. L'étude de terrain le dit elle-même : ils restent supérieurs sur les axes que la conception abandonne délibérément, l'outillage projectionnel, l'intégration à l'éditeur et la profondeur des macros. Et le pari que ces axes sont les mauvais est nommé comme un pari.

Le code généré rend bon marché aussi la fabrication indisciplinée de langages, et c'est pourquoi le tribunal est le cœur et non un accessoire. Je tiens cela pour une vue, non pour un résultat.

Le décodage contraint : le terrain l'a construit le premier, et l'implémentation de référence est celle d'une autre bibliothèque. Ce que le dossier ajoute, c'est l'appariement : une grammaire et un tribunal issus d'une seule déclaration, et la liste de ce que la grammaire a laissé tomber.

Une grammaire sur-approxime un tribunal. Les noms en double, les références pendantes et la cohérence d'un menu ne sont pas hors contexte. Je l'ai observé dans les deux sens plus haut : une plage que la grammaire ne peut pas porter, et une référence qu'elle ne peut pas porter.

Le code qu'une forge émet doit être lu par quelqu'un. Le style de famille dont hérite chaque langage déclaré a un test de réussite : apprendre le deuxième langage devrait prendre une soirée, parce que c'est le premier langage avec d'autres verbes. C'est une exigence de conception et non une mesure. Aucun apprenant n'a été chronométré dans le dossier que j'ai lu.

La limite vient ensuite, au bord d'un second langage fermé.

## 7. La limite

La bibliothèque a deux langages de formules fermés, et ils se comportent différemment au bord. Un lecteur qui croit que le langage fermé des conditions, celui du chapitre 11 et de la condition ci-dessus, couvre toutes les formules se trompera à table. La colonne calculée d'un tableau retombe, d'après son propre en-tête, sur le chemin d'évaluation classique quand le moteur ne peut pas compiler une formule. Le mot `sin` que la condition a refusé s'exécute-t-il ici ?

```haro
o1 = new stzTableAggregator([
	[ :A, [ 0, 1, 4 ] ],
	[ :B, [ 2, 4, 20 ] ]
])
o1.AddCalculatedCol(:SINE, 'sin(@(:A))')
? @@( o1.Col(:SINE) )
#--> [ 0, 0.84, -0.76 ]
```

Le sinus que la condition a refusé, le tableau l'a calculé, et il a imprimé `[ 0, 0.84, -0.76 ]` ! J'ai aussi vu, et je ne le montre pas, une seconde chose. Sur une autre table d'essai, avec A égal à 1, 3 et 10 et B égal à 2, 4 et 20, j'ai écrit une formule `@(:A) + HostBonus(@(:B))`. La fonction de moi qui s'y trouve multiplie par mille. La formule a imprimé `[ 2001, 4003, 20010 ]` : une fonction hôte définie par l'utilisateur s'est exécutée de l'intérieur d'une chaîne de formule. Et une formule qui nomme une fonction qui n'existe pas a levé l'erreur propre de l'hôte. Le second langage fermé est donc ouvert à son bord. Aucune garde n'affirme l'un ou l'autre comportement.

Ce qui est construit : dans la bibliothèque, une déclaration jugée quand elle est déclarée ; un tribunal et une grammaire issus d'elle ; la liste de ce que la grammaire a laissé tomber. Une machine à grammaire qui dit qu'elle est contrainte ; un prompt et une description issus du même texte. Le build compte 151 assertions dans trois gardes narrées. Deux petits langages fermés de conditions, avec des limites. Les langues de la couche naturelle comme données.

Ce qui est construit, mais hors de la bibliothèque : une forge d'une déclaration vers un tribunal et une grammaire, dans le dépôt de la charte de Haro.

Ce qui est conçu : la forge qui produit, à partir d'une seule déclaration, l'analyseur, le tribunal, l'imprimeur, la grammaire, le graphe de connaissance, la grammaire de requête, la porte naturelle, la narration, le runtime et un binaire statique. D'après ma lecture de la charte, le spike a montré le tribunal, la grammaire, un runtime qui parcourt la déclaration, une grammaire de requête, une narration et le tribunal de la lettre naturelle. Je n'ai pas trouvé montré un imprimeur pour les phrases déclarées, un graphe de connaissance forgé à partir d'une déclaration, ni le binaire statique unique par langage. La bibliothèque qui a une forge : rien en elle ne déclare ni ne forge un langage. Une grammaire pour chaque langage déclaré livrée dans la bibliothèque : promise dans le noyau, non livrée. Et les projections : le monde rendu à une application, un serveur, une page, un appareil.

Ce qui est absent : la grammaire de la forge pour un mot de menu, que j'ai vue ne tenir que la forme, plus haut, et le chiffre de deux sur dix contre dix sur dix, repris. Et tout enregistrement que la forge tourne sur le runtime de Haro. Au moment où la vision a été écrite, le langage n'existait pas ; les exécutions de la charte sont sur le runtime plus ancien et sur l'oracle.

Les six portes suivent, du programmeur à l'agent.

## 8. Six portes

**Le programmeur.** Vous déclarez la forme en quelques lignes et vous en tirez son tribunal, sa grammaire et son prompt. Ce que vous n'obtenez pas, c'est un moyen d'exécuter une fonction hôte depuis la déclaration : le langage n'a pas de mot pour cela.

**L'analyste.** La déclaration est du texte brut dans les mots du domaine, et le tribunal répond dans ces mots.

**Le concepteur.** Le refus est déclaré à côté de la grammaire, dans la voix du domaine, et n'est pas rédigé par runtime. Un concepteur choisit ce que dit un menu fermé quand il est rompu.

**Le décideur.** Une seule déclaration produit la bouche et le tribunal, et la forge elle-même publie où ils sont en désaccord. La forge est aujourd'hui hors de la bibliothèque. Ne l'achetez pas comme livrée.

**Le formateur.** Le lecteur peut prédire, octet par octet, ce que l'échantillonneur permettra, et apprend qu'une grammaire tue la malformation et non la fausseté.

**L'agent.** Vous ne parlez que la grammaire qu'on vous a remise. Une phrase que vous rédigez est une proposition que le tribunal juge. Votre bouche est la forme, et vos faussetés sont celles du tribunal et d'une personne.

## 9. Exercice

Écrivez, à la main, une grammaire pour une ligne de commande de déjeuner : `dish: ` puis l'un de deux plats de votre choix, puis un saut de ligne. Avant de rien exécuter, écrivez vos prédictions comme des promesses :

```haro exercise
cG = 'root ::= ...'     # your grammar here
? StzGrammarAccepts(cG, "dish: <your first dish>" + nl)
#--> ?
? StzGrammarAccepts(cG, "dish: <a dish not on your menu>" + nl)
#--> ?
? StzGrammarCouldContinue(cG, "dish: <the first letters of your first dish>")
#--> ?
? StzGrammarAccepts(cG, "dish: <the first letters of your first dish>")
#--> ?
? StzGrammarRefusal(cG) = ""
#--> ?
```

Ajoutez ensuite un nombre à la ligne, `quantity: ` et des chiffres, et écrivez une sixième prédiction : votre grammaire accepte-t-elle `quantity: 4000` ? Exécutez-la. La leçon est la troisième, la quatrième et la sixième. La machine sait déjà qu'un préfixe pourrait continuer et n'est pas encore une phrase, et elle ne peut pas savoir que le nombre est trop grand. Notez, en une phrase, qui dans votre restaurant doit refuser quarante portions, puisque la grammaire ne le peut pas.

Je vous laisse celui-ci. La section 3 termine sa série de conditions sur un refus sans un mot, et la section 4 dit pourquoi le calcul reste hors de la surface qui déclare. Prenez les deux lignes qui posent à la liste la même question sous les deux formes, et changez une seule chose : écrivez un autre nombre à la place du 2, le même dans les deux lignes. Je n'imprime rien dessous.

```haro exercise
o = new stzList([ 4, 7, 10, 3, 8 ])
? @@( o.FindW('{ sin(@item) < 2 }') )
? @@( o.FindWF( func x { return sin(x) < 2 } ) )
```

Exécutez-les pour plusieurs nombres. Cherchez un nombre pour lequel les deux formes impriment la même chose, et dites si l'impression seule vous apprend laquelle des deux a refusé et laquelle a répondu. Quand vous l'aurez fait, vous saurez ce que coûte un langage fermé qui refuse sans un mot.

Le chapitre suivant passe à la phrase naturelle, dans deux directions et sous une seule discipline. Une phrase s'exécute parce que chacun de ses mots est dans un dictionnaire que la bibliothèque possède, et ce que la bibliothèque ne connaît pas, elle le refuse, avec la raison.
