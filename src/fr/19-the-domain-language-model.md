---
id: the-domain-language-model
part: 4
number: 19
title: Le modèle de langage de domaine
spine: false
narrations: [stz-service-virtualization-code-first-subscribe-later.md, stz-knowledge-programming-narration.md]
site: [languages, agentic]
guards: [dlm_narrated, structuredoutput_narrated, schema_grammar_narrated, knowledge_integration_narrated, constrained_decoding_narrated]
stage:
  built: "le premier échelon du modèle de domaine sans neurones ; ses faits rendus comme un corpus ; un vocabulaire fermé ; la complétion par consultation ; un lot en texte simple qui voyage avec ses tests ; un petit second échelon, un bigramme, exporté vers un fichier de modèle ; l'admission d'un fait par une loi"
  designed: "une grammaire dérivée d'une base de connaissances par un seul appel ; l'unité typée de prédiction validée en cinq étapes ; un second échelon dont le corpus est vérifié avant qu'il s'entraîne ; la fonderie qui l'agrandirait"
  absent: "un pipeline qui enchaîne les cinq étapes sur n'importe quelle unité ; un mot de fin de phrase pour le second échelon ; une complétion qui voit la phrase jusque-là"
status: draft
rulings: ["12.19", "12.26", "12.29"]
research: research/ch19.md
---

## 1. Le concept, tel que le terrain le tient

Un modèle de langage prédit le jeton suivant. Un jeton est un fragment de texte sans type, sans rôle et sans contrainte : il peut être la fin d'un mot, un espace, un crochet. Tout ce qu'un modèle dit est construit en choisissant des jetons l'un après l'autre, et tout ce qui rend le résultat utile, que ce soit une phrase valide, qu'elle soit vraie, qu'elle respecte un schéma, est vérifié après coup ou imposé de l'extérieur.

Le terrain a fait fonctionner cela avec trois outils. On adapte un modèle général à un domaine en l'entraînant davantage sur les documents du domaine. On lui donne les documents pertinents au moment de la question, récupérés par similarité. Et on contraint son décodage avec une grammaire, de sorte qu'il ne puisse pas produire une phrase malformée, comme l'a montré le chapitre 11. Tous trois gardent la même unité : le jeton.

## 2. Le premier principe

**La prochaine chose que dit le modèle est une unité vérifiable de votre monde, un fait que vos règles admettent ou refusent, jamais un jeton.** Et la barrière est la même pour tous les modèles de ce genre : les générations sont des propositions, et le graphe et ses règles décident de l'admission.

## 3. La forme Softanza

Je l'appelle un modèle de langage de domaine, et il a deux échelons. Le premier n'a aucun neurone et a été montré au chapitre 17 : il répond à partir de faits enregistrés, dit pourquoi, et refuse hors de son domaine. Le second est un petit modèle neuronal, facultatif, qui lui donne de la fluidité. Les deux aboutissent à la même barrière.

Commençons par l'origine du texte d'entraînement. Personne ne l'écrit. Chaque phrase est un fait de la base de connaissances, rendu, et le vocabulaire est fermé : chaque mot que le domaine contient, avec une première entrée pour l'inconnu.

```haro
oKB = new stzKnowledgeGraph("restaurant")
oKB.Know("margherita", "dish").
    Know("tiramisu", "dish").
    Know("chianti", "wine").
    KnowRelation("margherita", "contains", "tomato-sauce").
    KnowRelation("margherita", "contains", "mozzarella").
    KnowRelation("margherita", "pairs-with", "chianti")
oDLM = StzDlmQ(oKB)
? @@( oDLM.GenerateCorpus() )
#--> [ "margherita is a dish.", "tiramisu is a dish.", "chianti is a wine.", "margherita contains tomato-sauce.", "margherita contains mozzarella.", "margherita pairs-with chianti." ]
? @@( oDLM.Tokenizer() )
#--> [ "<unk>", "margherita", "tiramisu", "chianti", "dish", "wine", "contains", "pairs-with", "is", "a", "tomato-sauce", "mozzarella" ]
? @@( oDLM.Tokenize("margherita contains something-new") )
#--> [ 2, 7, 1 ]
```

Douze mots, et un mot hors du domaine est envoyé sur le premier. « Correct par construction » vaut ici dans le seul sens que le code lui donne : chaque phrase est un fait enregistré. Cela ne vaut pas encore dans le sens que la conception visait ; la section 7 dit où.

La complétion est contrainte au domaine : après une entité, seulement ses relations ; après une relation, seulement ses objets ; un fragment se complète en entités ; un mot que le domaine ne contient pas se complète en rien.

```haro
? @@( oDLM.Complete("margherita") )
#--> [ "contains", "pairs-with" ]
? @@( oDLM.Complete("contains") )
#--> [ "tomato-sauce", "mozzarella" ]
? @@( oDLM.Complete("tira") )
#--> [ "tiramisu" ]
? @@( oDLM.Complete("pizza") )
#--> [ ]
```

Je dois dire ce que c'est, parce que la garde qui le prouve l'appelle « the grammar spirit ». C'est une consultation dans les faits, non un décodage sous une grammaire compilée. Et elle voit un mot, pas la phrase jusque-là : `Complete("contains")` renvoie les objets de chaque fait `contains`, quel que soit son sujet.

La grammaire elle-même peut être dérivée de la base de connaissances, et ici le lecteur de ce livre doit écrire la dérivation. Il n'y a dans la bibliothèque aucun appel qui transforme une base de connaissances en grammaire, et la conception en fait la tâche du premier échelon. Mais les pièces se composent. Le vocabulaire du domaine devient les choix d'un schéma du chapitre 11, le schéma se compile en grammaire, et la grammaire n'a aucun chemin pour un mot hors du domaine :

```haro
aLex = oDLM.Lexicon()
acObjects = []
for aFact in oKB.Facts()
	if aFact[2] != "is-a" and find(acObjects, aFact[3]) = 0
		acObjects + aFact[3]
	ok
next
oS = StzOutputSchemaQ([
	[ :field = "subject",  :type = :oneof, :choices = aLex[:entities] ],
	[ :field = "relation", :type = :oneof, :choices = aLex[:relations] ],
	[ :field = "object",   :type = :oneof, :choices = acObjects ]
])
? oS.ToGBNF()
#--> root ::= subject-line relation-line object-line
#    subject-line ::= "subject: " ("margherita" | "tiramisu" | "chianti") "\n"
#    relation-line ::= "relation: " ("contains" | "pairs-with") "\n"
#    object-line ::= "object: " ("tomato-sauce" | "mozzarella" | "chianti") "\n"
#    text ::= [^\n]+
#    number ::= "-"? [0-9]+ ("." [0-9]+)?
#    boolean ::= ("yes" | "no" | "true" | "false")
cGood = "subject: margherita" + nl + "relation: contains" + nl + "object: mozzarella" + nl
cOut  = "subject: pizza" + nl + "relation: contains" + nl + "object: mozzarella" + nl
cLie  = "subject: tiramisu" + nl + "relation: contains" + nl + "object: mozzarella" + nl
? oS.Accepts(cGood)
#--> 1
? oS.Accepts(cOut)
#--> 0
? oS.Accepts(cLie)
#--> 1
? oDLM.Ask("tiramisu contains what?")
#--> I hold no 'contains' knowledge about 'tiramisu'.
```

Regardez ensemble les quatre dernières lignes. La grammaire accepte la phrase qui dit qu'un tiramisu contient de la mozzarella, parce qu'elle a la bonne forme et que chaque mot est dans le domaine. Le modèle la refuse, parce que le graphe ne tient aucun tel fait. Une grammaire est une barrière pour la forme ; la vérité appartient au graphe.

Un modèle de langage de domaine est un fichier qui voyage. Il est sauvegardé en texte simple, lisible et comparable par diff, sans binaire et sans poids, et un second modèle qui n'a jamais vu la base de connaissances peut répondre à partir de lui et exécuter ses propres tests :

```haro
oDLM.AddGolden("what is margherita", "Margherita is a dish.")
oDLM.AddGolden("what is the weather today?",
	"That is outside the 'restaurant' domain (I know 3 entities and 2 relations).")
cFile = oDLM.Save("probe_dlm")
? cFile
#--> probe_dlm.zdlm
? read(cFile)
#--> dlm "restaurant"
#    entities
#        margherita | dish
#        tiramisu | dish
#        chianti | wine
#    relations
#        contains
#        pairs-with
#    facts
#        margherita | contains | tomato-sauce
#        margherita | contains | mozzarella
#        margherita | pairs-with | chianti
#    laws
#    goldens
#        what is margherita | Margherita is a dish.
#        what is the weather today? | That is outside the 'restaurant' domain (I know 3 entities and 2 relations).
oShipped = StzDlmQ("")
oShipped.LoadFrom(cFile)
? oShipped.Ask("what is tiramisu")
#--> Tiramisu is a dish.
? @@( oShipped.RunGoldens() )
#--> [ [ "total", 2 ], [ "passed", 2 ], [ "failed", [ ] ] ]
remove(cFile)
? fexists(cFile)
#--> 0
```

Le refus voyage avec le lot comme test golden, et le second modèle, qui n'a jamais vu le graphe, le passe. La section des lois est vide parce qu'aucune loi n'a été déclarée avant que le modèle soit forgé ; déclarez qu'une relation est unique, forgez de nouveau, et la ligne apparaît.

Maintenant le second échelon. C'est un petit modèle neuronal entraîné sur le corpus que vous avez vu, sans enseignant, et il peut être exporté comme fichier de modèle. J'en dirai la taille dans le même souffle que son résultat, parce qu'il est petit : une seule couche qui apprend à prédire le mot suivant à partir du précédent, sur douze mots, entraînée sur quinze paires.

```haro
oDLM.TrainNeuralRung(500)
? oDLM.NeuralWhy()
#--> neural bigram rung: 15 pairs over a 12-word vocab; trained 500 epoch(s), lr 0.50: loss 2.57 -> 0.70
? oDLM.NextToken("is")
#--> a
? oDLM.NextTokenConfidence("is")
#--> 1.00
cGguf = oDLM.ExportNeuralGguf("probe_bigram")
? cGguf
#--> probe_bigram.gguf
? StzEngineNeuralGgufInspect(cGguf)
#--> 2
remove(cGguf)
```

Le fichier contient deux tenseurs, un poids et un biais, et la bibliothèque sait le relire. Je ne prétends pas qu'un autre runtime le charge comme générateur de texte. Il s'entraîne en une fraction de seconde, hors ligne, et donne les mêmes nombres à chaque exécution.

Que dit un modèle comme celui-ci ? Il est fluide dans la grammaire du domaine, et il se trompe sur les faits. C'est la raison de la barrière :

```haro
aCorpus = oDLM.GenerateCorpus()
for cSeed in [ "tiramisu", "chianti", "margherita" ]
	cSaid = oDLM.NeuralGenerate(cSeed, 3)
	? cSaid + "  ->  " + ( find(aCorpus, cSaid + ".") > 0 )
next
#--> tiramisu is a wine  ->  0
#    chianti is a wine  ->  1
#    margherita contains mozzarella is  ->  0
```

« Tiramisu is a wine » est faux, parce que le tiramisu est un plat. « Chianti is a wine » est vrai. Et « margherita contains mozzarella is » est une phrase qui n'en finit pas, parce que le bigramme n'a aucun mot qui termine une phrase. Le test contre le corpus est une barrière grossière, et il refuserait un fait vrai que personne n'a enregistré. La vraie barrière est le graphe et ses lois :

```haro
oKB.ConstrainRelation("is-a", :Unique)
aVerdict = oKB.Admit("tiramisu", "is-a", "wine", [ :source = "rung 2" ])
? aVerdict[:admitted]
#--> 0
? aVerdict[:why]
#--> 'tiramisu' already bears 'is-a' (to 'dish'); the relation is :Unique
? @@( oKB.Contradictions() )
#--> [ [ [ "subject", "tiramisu" ], [ "relation", "is-a" ], [ "existing", "dish" ], [ "attempted", "wine" ], [ "source", "rung 2" ] ] ]
? oKB.Admit("pizza", "is-a", "dish", [ :source = "rung 2" ])[:why]
#--> admitted: 'pizza' is-a 'dish'
```

La fausse proposition est refusée avec sa raison, et le refus est gardé, avec sa source : le second échelon du modèle. Un fait nouveau est admis. C'est tout le principe en sept lignes : une proposition, une loi, un refus avec son pourquoi, et le refus au dossier.

La conception décrit l'unité de prédiction en trois niveaux. Un jeton est un fragment sans type. Un plongement est un vecteur sans rôle. Et un chunk est un nœud typé d'un graphe, avec une étiquette, une charge utile et des arêtes : une déclaration, une relation, une contrainte. Un chunk est validé en cinq étapes avant d'entrer dans le graphe : type, motif, intégrité du graphe, conformité, et contribution constructive. Je le raconte comme conception, parce qu'il n'y a pas de chunk dans la bibliothèque. Ce qui existe, ce sont des pièces : le tribunal du chapitre 11 vérifie le type et la forme d'un texte ; l'admission ci-dessus impose une loi, ce qui est la conformité ; et ajouter deux fois un fait est une opération sans effet inoffensive, ce qui est une petite forme de la dernière étape. Rien ne les enchaîne.

## 4. La décision, et ce que j'ai refusé

Le 13 juillet 2026, j'ai tranché sur ce point. Le concept d'un modèle de langage de domaine avait été conçu pour l'un des produits du domaine de projets ; je l'ai donné à la fondation ouverte, pour que tout projet Softanza qui fournit une base de connaissances puisse livrer son propre modèle gratuitement aux utilisateurs de son domaine. Le format est `.zdlm`. Le plancher est le premier échelon, dans chaque modèle ; le second est une fluidité facultative. Le dossier tient la décision qu'un modèle se livre gratuitement, et aucun texte de licence. Je dis « gratuit » comme le mot de cette décision : un fichier simple, dans la fondation ouverte, sans redevance de licence ni compteur.

**J'ai refusé le jeton comme unité.** L'unité est un chunk du monde, qu'un graphe peut admettre ou refuser.

**J'ai refusé un enseignant que je ne peux pas voir.** La conception antérieure de l'idée employait un grand modèle commercial pour écrire son corpus d'entraînement. J'ai posé une loi contre cela, et le corpus de ce modèle est rendu à partir des faits propres du domaine : la deuxième loi de la bibliothèque dit qu'une capacité n'exige jamais rien de payant ni de distant.

**J'ai refusé le neuronal d'abord.** La découverte dont part la section est que le modèle canonique n'est pas neuronal. Une revue du produit antérieur a archivé un transformeur de un à trois milliards de paramètres, au profit d'une prédiction à base de règles, au motif que l'hallucination est impossible quand le modèle ne peut pas générer de texte presque valide. Le premier échelon a donc zéro entraînement et zéro coût, et l'échelon neuronal vient en second.

**J'ai refusé que la forme tienne lieu de vérité.** La grammaire dit que la structure tue la malformation, pas la fausseté. La vérité appartient au graphe, à ses lois, et à une personne.

## 5. Le tribunal

`dlm_narrated` prouve le modèle forgé à partir d'un graphe, ses réponses avec leur pourquoi, son refus hors du domaine, la complétion, le lot en texte simple avec ses goldens, le tokeniseur fermé et le second échelon avec son fichier de modèle. Une de ses assertions sur le second échelon vérifie seulement que la phrase générée commence par un préfixe fixe, de sorte qu'elle passerait aussi sur la fausse phrase ci-dessus. `structuredoutput_narrated`, `schema_grammar_narrated` et `constrained_decoding_narrated` prouvent le tribunal du chapitre 11, le compilateur de grammaire et l'échantillonneur ; la dernière a deux scènes qui exigent un fichier de modèle génératif, que cette machine ne détient pas, de sorte qu'une partie seulement a tourné pour cette page. `knowledge_integration_narrated` prouve la dérivation et le refus par une loi. Et je dois dire que l'admission que je montre dans le dernier bloc n'est appelée par son nom dans aucune garde : on l'atteint par la conversation, et par la forme stricte d'ajout d'un fait, que la garde affirme bien.

## 6. Le terrain, et où il mène

Le terrain mène en échelle. Entraîner et servir des modèles de toute taille est une pratique mûre ; ce second échelon est une seule couche sur douze mots, et les étapes qui le feraient devenir plus, un corpus validé, la déduplication, un tokeniseur entraîné, un réseau plus grand, la quantification, ne sont pas faites. Je ne rivalise pas avec les grands modèles.

Le terrain mène en fluidité, ce qui est le but d'un modèle. Un premier échelon qui répond à partir des faits dira « I hold no knowledge about that » là où un modèle général écrirait quelque chose de plausible, et pour un client la chose plausible est souvent plus utile. La réponse propre du dossier est le second échelon, et son état présent est la table ci-dessus.

Là où je pense que ceci se distingue, c'est dans ce qu'est la sortie. La réponse d'un modèle général est du texte, et chaque vérification sur elle se fait après coup. Ici chaque réponse du premier échelon porte son pourquoi et une certitude de un, et chaque proposition du second rencontre une barrière qui peut la refuser avec une raison. Un modèle qui ne peut dire que ce que le domaine contient, et une barrière qui se souvient de ce qu'elle a refusé : voilà ce qu'une banque, un ministère ou une école peut signer.

## 7. La limite

Ce qui est construit : le premier échelon et ses réponses ; les faits rendus comme corpus, avec un vocabulaire fermé ; la complétion par consultation ; le lot qui voyage avec ses tests ; un second échelon qui s'entraîne en une fraction de seconde et exporte un petit fichier de modèle ; et l'admission d'un fait par une loi.

Ce qui est conçu, et la page doit dire chaque point :

- La grammaire dérivée d'une base de connaissances par un seul appel. La composition du chapitre 19 est celle du lecteur, pas celle de la bibliothèque.
- Le corpus du second échelon validé par la grammaire du premier avant d'être admis. La conception le dit ; le code rend les faits directement, sans une telle vérification. Ainsi « correct par construction » vaut pour le texte d'entraînement, et non pour ce que dit le modèle.
- La validation en cinq étapes d'un chunk. Aucune n'existe comme pipeline.
- Les étapes de la fonderie au-delà du bigramme.

Ce qui est absent : un mot de fin de phrase pour le second échelon, ce qui explique qu'une de ses phrases n'en finisse pas ; et une complétion qui voit la phrase jusque-là, ce qui explique qu'une complétion après une relation énumère les objets de chaque fait de cette relation. Le premier échelon répond aussi à une question reformulée avec le type, comme l'a montré le chapitre 17, là où la loi de cette partie dit qu'il devrait refuser.

## 8. Six portes

**Le programmeur.** Un modèle est un fichier que vous pouvez lire, comparer par diff et tester : ses faits, ses lois et ses goldens.

**L'analyste.** Un fait que vous ajoutez fait que le modèle en sait plus, et une loi que vous ajoutez le fait refuser davantage, sans entraînement.

**Le concepteur.** Le refus du modèle fait partie de son contrat : le test golden dit ce qu'il doit refuser de répondre.

**Le décideur.** Le modèle ne peut dire que ce que le domaine contient, et la barrière garde la trace de ce qu'elle a refusé et pourquoi.

**Le formateur.** Le premier échelon est un modèle qu'un apprenant peut lire en entier. Le second est assez petit pour être entraîné devant une classe.

**L'agent.** Ce que vous proposez est un fait que le graphe peut admettre ou refuser, avec une raison que vous pouvez lire.

## 9. Exercice

Forgez un domaine à vous avec trois entités et deux relations. Avant d'exécuter quoi que ce soit, écrivez ce que vous attendez de trois appels : la complétion d'une entité, la complétion d'une relation, et la réponse à une question sur une chose que le domaine ne contient pas. Puis déclarez qu'une relation est unique et proposez, sous forme de fait, quelque chose qui la contredit.

Exécutez-le. Puis écrivez une phrase de la bonne forme et de la mauvaise vérité, et dites lequel de la grammaire et du graphe la refuse, et lequel ne la refuse pas.
