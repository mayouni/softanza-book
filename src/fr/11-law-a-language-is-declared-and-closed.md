---
id: law-a-language-is-declared-and-closed
part: 3
number: 11
title: "Loi : un langage est déclaré et fermé, et ce qui le parle, personne ou modèle, est jugé par lui"
law: "a language is declared and closed, and whatever speaks it, person or model, is judged by it"
spine: true
narrations: [stznatural-vs-ring-naturallib.md, stz-near-natural-language-programming.md, stz-bridging-minds-and-code.md, stzlistex-pattern-matching-for-lists.md]
site: [languages]
guards: [multilingual_pack_narrated, semantic_resolver_narrated, literate_templates_narrated, question_narrated, structuredoutput_narrated, schema_grammar_narrated, constrained_decoding_narrated]
stage:
  built: "le vocabulaire de la couche naturelle comme données en cinq langues, avec ses refus ; le tribunal de la sortie structurée, son compilateur de grammaire et son échantillonneur ; les langages de motifs, qui acceptent un mot qu'ils ne connaissent pas"
  designed: "la forge qui produit l'analyseur, le tribunal et la grammaire d'un langage à partir de sa seule déclaration ; une grammaire émise pour chaque langage déclaré ; le style d'écriture comme grammaire déclarée"
  absent: "une couche naturelle fermée jusqu'au fond : une forme de liste atteint encore le code de l'hôte ; des classes de motifs qui refusent un mot qu'elles ne connaissent pas ; la lettre ɗ du hausa standard dans le paquet hausa"
status: draft
rulings: ["12.4", "12.10", "12.16", "12.19", "12.21", "12.27", "12.28", "12.29", "12.30"]
research: research/ch11.md
figures:
  - "10 of 10 against 2 of 10, one model of 135 million parameters, ten prompts: SOFTANZA_STRUCTURED_OUTPUT.md (C9) section 2.1"
---

Dans ce chapitre, j'énonce la loi de la partie III et je la fais tourner. Je commence par une phrase qui tourne parce que chaque mot est dans un dictionnaire que la bibliothèque possède, en anglais, en hausa, en français et en arabe. Je montre ce qu'elle dit d'un mot qu'elle ne connaît pas. Puis je déclare la forme d'une réponse comme un schéma, je juge des réponses contre lui, et je montre la seule chose qu'une grammaire ne peut pas tuer : une réponse fausse dans la bonne forme. Je dis quelles gardes le prouvent, où le terrain est en avance, et où la couche naturelle n'est pas encore fermée, puisque la loi doit le dire. La loi elle-même tient en une phrase : un langage est déclaré et fermé, et ce qui le parle, une personne ou un modèle, est jugé par lui.

## Ce que l'âge de l'IA change ici

Dans la partie II, l'âge a changé qui écrit le code. Ici, il change qui prononce la phrase. Une phrase d'un langage avait autrefois une personne derrière elle, quelqu'un à qui l'on pouvait demander ce qu'il voulait dire. Aujourd'hui l'auteur d'une phrase peut être un modèle, à qui l'on ne peut rien demander, et qui écrira une phrase fluide qu'elle soit vraie ou non.

La grammaire doit donc être fermée, et le tribunal, la partie qui accepte ou refuse une phrase selon sa grammaire, doit la lire. Un langage dont les phrases peuvent contenir n'importe quoi ne peut rien refuser, et un tribunal ne peut pas juger une phrase qu'il ne peut pas lire. La vision de la plateforme met tout le mouvement en une ligne, que j'ai ratifiée : les humains et les machines se rencontrent dans des langages déclarés, petits, fermés et jugés, pas dans du code généraliste.

C'est aussi là que l'ordre du livre se retourne. La couverture va du familier au nouveau : la programmation, les langages, l'intelligence. La logique du dossier va dans l'autre sens. Le premier acte est de déclarer un langage. La programmation, la discipline de la partie II, se passe à l'intérieur de langages déclarés : les formes du vocabulaire sont déjà une déclaration en Haro, dans une esquisse hors de la bibliothèque. L'intelligence, partie IV, est gouvernée par les deux : un modèle est tenu à une grammaire déclarée avant de parler, et sa phrase est jugée après. Le livre garde l'ordre de la couverture, donc ce chapitre est au milieu ; dans l'ordre du dossier, il viendrait en premier.

## 1. Le concept, tel que le terrain le tient

Pour un programmeur qui travaille, un langage est un hôte généraliste, Python, JavaScript, Java. Un « langage de domaine » est d'ordinaire une bibliothèque dont les appels se lisent comme des phrases, alors que le fichier autour peut contenir n'importe quel code de l'hôte. L'étude que le domaine de projets a faite du terrain, écrite en août 2026, nomme ce qui est arrivé à ces conceptions. Les langages internes sont morts d'ouverture, parce qu'un fichier de construction n'est déclaratif que jusqu'au jour où quelqu'un y écrit du code arbitraire. Les ateliers de langage sont morts du poids de leurs outils. Et elle nomme les langages qui ont gagné : SQL, les expressions régulières, Make, HTML et CSS, les langages de configuration. Ils ont gagné parce qu'ils sont fermés.

L'ère des modèles a ajouté une pratique : quand un modèle écrit, ou bien l'on vérifie ce qu'il a écrit, ou bien l'on contraint sa sortie pendant qu'il écrit, avec une grammaire ou un schéma. L'implémentation de référence de l'échantillonnage contraint par une grammaire est un projet ouvert, et le dossier le dit là où il emploie le même algorithme. Et dans le langage commun du terrain aujourd'hui, « programmer en langage naturel » veut dire une seule chose : donner une consigne à un modèle.

## 2. Le premier principe

**Un langage est déclaré et fermé, et ce qui le parle, une personne ou un modèle, est jugé par lui.**

## 3. La forme Softanza

Une phrase peut-elle tourner sans qu'un modèle devine ce qu'elle veut dire ? Elle le peut, quand chaque mot est dans un dictionnaire que la bibliothèque possède :

```haro
Naturally("
    Make a string with 'hello niger' inside
    Spacify it and uppercase it
    @Box it while the box@ is rounded
    Display it on the screen
")
#--> ╭───────────────────────╮
#    │ H E L L O   N I G E R │
#    ╰───────────────────────╯
```

Quatre lignes d'anglais sont devenues une boîte arrondie autour de majuscules espacées.

Le dictionnaire est fait de données, indexées par des sens, pas par des mots anglais. Le même sens peut-il donc être dit dans une autre langue en ajoutant un bloc de données, pas de code ? Voici une même instruction en anglais, en hausa, en français et en arabe. La phrase en hausa est celle de la narration, et celle en français vient de la garde de la bibliothèque avec ses données changées. J'ai composé celle en arabe à partir du vocabulaire de la bibliothèque. Aucun locuteur natif n'a lu le hausa ni l'arabe pour autant que le dossier le montre :

```haro
? Naturally("Create a string with 'hello' and uppercase it").Result()
#--> HELLO
? NaturallyIn("hausa", "Yi rubutu dauke 'hello' Maida shi").Result()
#--> HELLO
? NaturallyIn("fr", "Crée une chaine avec 'hello' et mets la en majuscules").Result()
#--> HELLO
? NaturallyIn("ar", "أنشئ نصا بـ 'hello' ثم كبّره").Result()
#--> HELLO
```

Quatre langues, un seul sens, et `HELLO` quatre fois.

Et un programme redit ce qu'il a compris, dans sa propre langue. Une personne qui lit l'arabe peut vérifier la lecture que la machine fait de sa phrase sans lire une ligne de code.

```haro
o1 = NaturallyIn("ar", "أنشئ قائمة بـ [ 5, 3, 5 ] ثم أزل تكراراتها")
? @@( o1.Result() )
#--> [ 5, 3 ]
? o1.Understood()
#--> أنشئ قائمة بـ [ 5, 3, 5 ] -> أزل التكرارات
```

Le programme a redit `أنشئ قائمة بـ [ 5, 3, 5 ] -> أزل التكرارات` : la liste reçue, et la suppression des doublons.

Voici maintenant ce que la bibliothèque fait par règle : dire ce qu'elle n'a pas compris. Que fait-elle d'un verbe qu'elle ne connaît pas ? Écrivez-en un de travers et exécutez :

```haro
o1 = Naturally("Create a string with 'softanza' Uppercse it")
? o1.Result()
#--> softanza
? @@( o1.Unresolved() )
#--> [ [ "Uppercse", "uppercase" ] ]
? o1.UnderstoodAll()
#--> 0
```

Le verbe mal orthographié n'est pas deviné. `Unresolved()` répond `[ [ "Uppercse", "uppercase" ] ]`, le mot rencontré à côté du mot que la bibliothèque pense que vous vouliez, et `UnderstoodAll()` répond `0` : le programme admet qu'il n'a pas tout compris. C'est le mode permissif : un mot inconnu est sauté et signalé. Un agent reçoit le mode strict, qui refuse, et un monde, une liste déclarée d'opérations permises, peut limiter ses phrases à cette liste :

```haro
try
	NaturallyStrict("Create a string with 'x' Fooify it")
catch
	? cCatchError
done
#--> Strict natural mode: not understood: 'Fooify' (did you mean 'boxify'?)
try
	NaturallyStrictIn("en", "Create a list with [ 3, 1 ] Reverse it", [ "METHOD_REMOVEDUPLICATES" ])
catch
	? cCatchError
done
#--> Operation not permitted in this world: METHOD_REVERSE
```

Le mode strict refuse `'Fooify'` et nomme tout de même le mot le plus proche : `did you mean 'boxify'?`. Dans ce monde, une phrase qui renverse une liste est refusée ! Le refus nomme l'opération : `Operation not permitted in this world: METHOD_REVERSE`.

L'autre direction du code naturel dans Softanza est la chaîne quasi naturelle, où la personne est l'analyseur et où la chaîne se lit comme une phrase. Quand elle répond non, dit-elle pourquoi ?

```haro
? IsQ().TheQ().LengthQ().OfQ("softanza").LessThanQ().TheQ().LengthQ().Of("Haro")
#--> 0
? Why()
#--> no: 8 is not less than 4
```

La chaîne a répondu `0`, et `Why()` a donné la raison : `no: 8 is not less than 4`. Un verdict dit pourquoi.

Voici maintenant la loi à son plus tranchant : un modèle. La bibliothèque déclare la forme d'une réponse comme un schéma. Que devient un schéma qui nomme un type que la bibliothèque n'a pas ? Il est jugé quand il est déclaré, avant qu'aucun modèle soit appelé :

```haro
try
	StzOutputSchemaQ([ [ :field = "x", :type = :colour ] ])
catch
	? cCatchError
done
#--> stzOutputSchema: unknown field type 'colour' (use string|number|boolean|oneof|list|structure).
```

Le refus nomme le type inconnu, `'colour'`, et liste les six qu'il accepte : `(use string|number|boolean|oneof|list|structure)`. Le schéma a été refusé avant qu'aucun modèle soit appelé ! Un schéma correct est un petit langage fermé. Le tribunal juge n'importe quelle réponse contre lui, quel qu'en soit l'auteur. Et le schéma émet sa grammaire, pour qu'un modèle puisse y être tenu pendant qu'il écrit :

```haro
oS = StzOutputSchemaQ([
	[ :field = "name", :type = :string ],
	[ :field = "age",  :type = :number, :must = [ [ ">=", 0 ], [ "<=", 130 ] ] ],
	[ :field = "mood", :type = :oneof,  :choices = [ "positive", "negative" ] ]
])
? oS.Accepts("name: Hadiza" + nl + "age: 41" + nl + "mood: positive")
#--> 1
? oS.Accepts("name: Hadiza" + nl + "age: 41" + nl + "mood: angry")
#--> 0
? oS.Accepts("name: Hadiza" + nl + "age: 900000" + nl + "mood: positive")
#--> 0
? oS.Accepts("name: Hadiza" + nl + "age: 62" + nl + "mood: positive")
#--> 1
? oS.ToGBNF()
#--> root ::= name-line age-line mood-line
#    name-line ::= "name: " text "\n"
#    age-line ::= "age: " number "\n"
#    mood-line ::= "mood: " ("positive" | "negative") "\n"
#    text ::= [^\n]+
#    number ::= "-"? [0-9]+ ("." [0-9]+)?
#    boolean ::= ("yes" | "no" | "true" | "false")
```

Regardez les quatre verdicts. La première réponse a imprimé `1`. La deuxième, avec `mood: angry`, et la troisième, avec `age: 900000`, ont imprimé `0` : le tribunal les a refusées. La quatrième a imprimé `1` de nouveau. Hadiza a quarante et un ans dans la première réponse et soixante-deux dans la quatrième, et le tribunal accepte les deux ! Une grammaire tue les phrases mal formées, pas les phrases fausses. Le dossier le dit en cinq mots (dans l'original anglais) : structure tue l'informe, pas le faux. Ce livre dit la même chose : la vérité d'une réponse n'est pas l'affaire de la grammaire. Le dossier dit que la vérité demande la réversibilité, un auditeur et un Principal, la personne qui tranche. Une grammaire est la barrière, pas le juge de tout.

Un gabarit est aussi un contrat. Une phrase avec un trou non rempli est refusée avant de tourner :

```haro
try
	NaturallyWith("Create a string with {#1} and {#2} it", [ "x" ])
catch
	? cCatchError
done
#--> Unfilled template hole! The narration still contains a {#n} slot with no value for it.
```

Et les motifs sont de petits langages à part entière, mais pas encore fermés : le chapitre 15 montre les classes de motifs acceptant sans se plaindre un mot qu'elles ne connaissent pas. La forme d'une liste est déclarée, pas écrite comme une boucle :

```haro
? Lx("[@N, @S]").Match([42, "hello"])
#--> 1
? Lx("[@N, @S]").Match(["hello", 42])
#--> 0
? Lx("[@N, [@N2], @N]").Match([1, [2, 3], 4])
#--> 1
? Lx("[@N, [@N2], @N]").Match([1, [2], 4])
#--> 0
```

Deux formes ont correspondu, deux non, et aucune boucle n'a été écrite.

Les chapitres de cette partie prouvent la loi de cinq côtés. Le chapitre 12 raconte un langage déclaré : la forge (la machinerie qui produit l'analyseur, le tribunal, l'imprimeur et la grammaire d'un langage à partir de sa seule déclaration), la grammaire fermée sans échappée vers l'hôte, et le tribunal né avec la grammaire. Il raconte aussi la grammaire émise pour qu'un modèle ne puisse dire que des phrases valides, et ses surfaces. Le chapitre 13 raconte les deux directions du code naturel, la machine comme analyseur et la personne comme analyseur, dans une seule discipline. Le chapitre 14 raconte la programmation par la connaissance, un fichier qui est un système. Le chapitre 15 raconte les langages de motifs, l'expression régulière élevée aux listes, aux nombres, aux tables, aux matrices, au temps et aux graphes. Le chapitre 16 raconte les sept langages que Softanza atteint par une seule porte gouvernée, et pourquoi une porte n'est pas une surface.

## 4. La décision, et ce que j'ai refusé

**J'ai choisi l'acte : déclarer un langage.** Pas « utilisez notre langage ». Déclarez le vôtre : le langage de votre domaine, dans vos mots. C'est le noyau de la plateforme, et c'est la raison d'être de cette partie.

**J'ai refusé l'échappée ouverte.** Le méta-langage qui déclare les langages du domaine de projets vit hors de cette bibliothèque. Sa règle fondatrice refuse de définir toute forme qui laisserait une phrase atteindre le code de l'hôte, appeler une fonction, évaluer une chaîne ou toucher un fichier. Pas interdit : inexprimable. Un langage interne qui ne peut pas refuser le code arbitraire de l'hôte est, selon les mots de l'étude de terrain du domaine de projets, une API déguisée en langage.

**J'ai refusé le langage naturel comme façon de déclarer.** Le langage naturel demande ; il ne déclare jamais. Un modèle peut rédiger une déclaration, et, par la règle de la vision, qui est conçue et pas encore construite, le brouillon n'entre dans le monde que comme une proposition : le modèle propose, le tribunal décide, une personne ratifie.

**J'ai tenu la promesse de 2020 et changé son mécanisme.** Ma première diapositive promettait un langage naturel exécutable. La vision de 2026 a jugé ce slogan : il promettait plus qu'un tribunal ne peut défendre, parce qu'une phrase naturelle peut être ambiguë et qu'un mensonge peut être grammatical. Le naturel reste donc à la porte, là où une phrase demande ou rédige, et l'exécution appartient à des langages fermés qu'un tribunal peut juger. J'ai construit la couche naturelle ainsi bien avant que la vision le nomme. Seuls les mots définis dans le dictionnaire sont interprétés. Tout autre mot est sauté et signalé, ou refusé en mode strict, jamais deviné.

**J'ai sorti la gouvernance de la bibliothèque et gardé les refus dedans.** En juillet 2026, un kit pour gouverner les agents a atterri dans la couche naturelle. Je l'ai retiré le jour même : le mode strict, les refus, le pourquoi et le compris appartiennent à la bibliothèque ; un produit pour gouverner les agents, non. Et j'ai retiré un ensemble de marqueurs : leur chiffre de l'ordre des lettres avait été inversé par son propre inventeur, de mémoire, et ils répétaient des sens. Un langage qu'une personne parle ne marque jamais une référence de cette façon. Une chaîne non grammaticale qui tourne est un bogue.

**J'ai refusé un second plongement.** Le chapitre 1 énonce cette décision ; j'ajoute seulement ici qu'une porte apporte un runtime étranger, qu'une surface apporte une syntaxe familière sur la même grammaire, et que le chapitre 16 raconte la différence.

## 5. Le tribunal

`multilingual_pack_narrated` prouve les langues comme données : les paquets, les programmes en français et en arabe, un paquet ajouté à l'exécution, et le programme qui se paraphrase dans sa propre langue. `semantic_resolver_narrated` prouve le mot inconnu avec sa suggestion, le mode strict, et la liste d'autorisation sous laquelle tout ce qui est hors liste est grammaticalement impossible. Elle ne passe pas à ce commit. Ma recherche pour le chapitre 13 l'a exécutée deux fois le 8 octobre 2026, et la demande L45 du mémo du 9 octobre en consigne le résultat. Elle s'arrête sur une erreur levée par une fonction de découpage de chaîne, avant la fin. La page compte donc ses assertions et ne revendique pas son verdict. `literate_templates_narrated` prouve qu'un gabarit est un contrat. `question_narrated` prouve qu'un verdict par oui ou non enregistre son pourquoi. `structuredoutput_narrated` prouve le tribunal de la sortie structurée, y compris le mensonge qu'il laisse passer. `schema_grammar_narrated` prouve le compilateur de grammaire, et `constrained_decoding_narrated` l'échantillonneur qui y tient un modèle.

Sept gardes prouvent la loi ; la section suivante dit où le terrain est en avance.

## 6. Le terrain, et où il mène

Le terrain mène en outils. Les ateliers de langage restent en avance sur les axes auxquels la conception du domaine de projets a délibérément renoncé : l'outillage projectionnel (des éditeurs qui comprennent un langage pendant que vous tapez), l'intégration aux IDE, la profondeur macro-théorique. L'étude du domaine de projets le dit dans ses propres mots : c'est un pari, et il est nommé comme tel. Je tiens ce pari pour une vue, non pour un résultat.

Le terrain a construit le décodage contraint le premier. L'échantillonneur de Softanza suit l'algorithme de l'implémentation de référence et n'embarque rien. Mesurées sur un seul petit modèle de cent trente-cinq millions de paramètres, sur dix consignes, les réponses étaient valides du premier coup deux fois sur dix quand on les vérifiait après coup. Tenu à la grammaire, le modèle était valide dix fois sur dix. C'est un seul petit modèle et dix consignes, et rien dans le dossier n'en mesure un grand.

Et l'âge coupe dans les deux sens. Le code généré rend aussi bon marché la fabrication négligente de langages. C'est pourquoi le tribunal n'est pas un accessoire d'un langage déclaré. Il en est le cœur. C'est mon point de vue.

## 7. La limite

Ce qui est construit : la couche naturelle, son vocabulaire comme données en cinq langues, l'anglais, le hausa, le français, l'arabe et le turc, et ses refus. Construits aussi : le tribunal de la sortie structurée avec son compilateur de grammaire et son échantillonneur, et les langages de motifs. Ceux-ci acceptent encore un mot qu'ils ne connaissent pas.

Ce qui est conçu : la forge qui produirait, à partir de la seule déclaration d'un langage, son analyseur, son tribunal, son imprimeur (la partie qui réécrit une phrase) et sa grammaire pour un modèle. La forge est construite hors de la bibliothèque et conçue pour la bibliothèque : une première esquisse en a été construite hors de la bibliothèque en octobre 2026. La bibliothèque ne peut pas encore l'exécuter. Le texte de la vision dit que la forge n'a pas encore forgé (fabriqué les parties d'un langage à partir de sa déclaration). L'esquisse a depuis forgé des tribunaux et des grammaires pour plusieurs langages, jugés par les propres fixtures de ces langages, et la vision ne l'a pas rattrapée. Le chapitre 12 la raconte avec ses limites. Une grammaire pour chaque langage déclaré est promise et pas livrée.

Ce qui est absent, et la loi doit le dire. La couche naturelle n'est pas fermée jusqu'au fond. Une forme, une liste écrite entre crochets, est encore remise à l'hôte pour être évaluée. Une fonction de l'hôte à l'intérieur des crochets s'exécute-t-elle ? Essayez-en une :

```haro
? @@( Naturally("Create a list with [ upper('x'), 1 ] and remove its duplicates").Result() )
#--> [ "X", 1 ]
```

La fonction `upper` n'est pas un mot du dictionnaire naturel, et la liste est revenue `[ "X", 1 ]`. Elle s'est exécutée quand même ! Le dossier connaît déjà cette échappée et a acheminé sa réparation. Tant que la réparation n'est pas arrivée, « la couche naturelle est un langage fermé » est vrai de ses mots et pas de ses listes, et ce livre le dira.

Et le paquet hausa ne lit pas encore la lettre ɗ, qu'emploie l'orthographe standard du hausa. Le paquet l'a stockée dans un encodage cassé. Quand je l'ai sondé le 8 octobre 2026 sur l'instantané précédant ce commit, une phrase écrite correctement échouait sans un mot de plainte. Le hausa de ce chapitre est écrit sans le crochet, comme le paquet le lit aujourd'hui. Le dossier ne tient aucune lecture des phrases du paquet par un locuteur du hausa. Les phrases en langue étrangère imprimées dans ce chapitre viennent de la narration et des gardes de la bibliothèque, ou sont composées à partir de son vocabulaire. Aucun locuteur natif ne les a lues pour autant que le dossier le montre.

Voilà les limites ; la section suivante ouvre six portes sur elles.

## 8. Six portes

**Le programmeur.** Vous continuez d'écrire du code. Ce que vous déclarez est une grammaire fermée, et le tribunal juge votre phrase et celle d'un agent par les mêmes règles.

**L'analyste.** Les mots de votre domaine deviennent un paquet de données, et le système les comprend ou les refuse avec la raison.

**Le concepteur.** Les refus font partie du langage : ce qui est hors liste est refusé en mode strict, donc il n'a jamais besoin d'un avertissement.

**Le décideur.** Un modèle tenu à une grammaire déclarée répond dans la bonne forme. Il peut encore répondre une fausseté dans la bonne forme, et le dossier imprime cette limite avec le résultat.

**Le formateur.** Une phrase en hausa, en français ou en arabe s'exécute et redit ce qu'elle a compris, de sorte qu'un apprenant lit la lecture que la machine fait de ses propres mots.

**L'agent.** Vous ne pouvez parler que le langage déclaré. Le mode strict est votre posture, et votre brouillon est, par la règle de la vision (conçue), une proposition que le tribunal juge.

## 9. Exercice

Déclarez, avec `StzOutputSchemaQ`, un enregistrement de trois champs tiré d'un domaine que vous connaissez : une demande de prêt, par exemple, avec un montant dans une fourchette, une devise tirée d'une liste fermée, et un objet en texte libre. Avant de rien exécuter, écrivez trois réponses qu'un modèle pourrait donner : une que le tribunal doit accepter, une qu'il doit refuser à cause de sa forme, et une qu'il acceptera bien qu'elle soit fausse. Sous chacune, écrivez votre prédiction comme une promesse.

Exécutez-le. La troisième réponse est la leçon de ce chapitre. Écrivez, en une phrase, qui dans votre domaine doit la juger, puisque la grammaire ne le peut pas.

Le chapitre 12 est *Un langage, déclaré*. Son principe : déclarer un langage est aussi facile que déclarer une variable.
