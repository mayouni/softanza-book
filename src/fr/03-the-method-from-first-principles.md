---
id: the-method-from-first-principles
part: 1
number: 3
title: La méthode, depuis les premiers principes
spine: true
narrations: [stzstring-emptiness-narration.md, istrue-softanza-truth.md, stz-built-on-real-world-need.md]
site: [history, principles, estate, compare]
guards: [modality_narrated, wisecoding_narrated, wisecoding_rich_narrated]
stage:
  built: "le tribunal derrière chaque bloc de ce chapitre sauf celui de la vérité, et les mots d'étape que le site imprime sur chaque produit"
  designed: "le registre des concepts repensés comme données, avec une garde qui échoue quand un concept n'a pas de preuve"
  absent: "une page qui montre chaque concept repensé avec une preuve exécutée ; un fichier de tests pour le moteur de paradigme de la fusion de sections"
status: draft
rulings: ["12.19", "12.22", "12.29", "12.30"]
research: research/ch03.md
---

Dans ce chapitre, je montre la méthode que suit chaque chapitre après celui-ci. Je prends « depuis les premiers principes », le slogan du terrain, et je lui donne un sens étroit : un concept, la forme du terrain, une reconception en code qui s'exécute, et un tribunal qui la juge. Je montre le plus petit réexamen que je connaisse, la chaîne vide, puis les deux actes, déclarer et gouverner, chacun en quelques lignes. Je dis ce que j'ai refusé. D'abord une fonction sans besoin, et le code généraliste comme lieu de rencontre entre les personnes et les machines. Ensuite un titre qui regardait en arrière, la grille seule, et une lecture appelée recensement. Toute la méthode revient à une phrase : vous déclarez un monde dans un langage fait pour lui, et vous gouvernez la façon dont ce monde change.

## 1. Le concept, tel que le terrain le tient

Dans notre industrie, « depuis les premiers principes » est un slogan. Cela veut dire raisonner à partir du bas, non par analogie. Vous l'entendrez dans des conférences et le lirez dans des annonces de lancement, et on vous montrera rarement ce qu'il a produit.

Le terrain a bien une méthode pour les décisions derrière le logiciel, et c'est une bonne méthode. Une équipe écrit une courte fiche pour chaque décision qu'elle prend, composée du contexte, de la décision et des conséquences. Beaucoup d'équipes les appellent des fiches de décision d'architecture, d'après un billet de blog que Michael Nygard a écrit en 2011. Le terrain a aussi une méthode pour prouver ce que fait une fonction : un exemple écrit sous la fonction, que les outils peuvent exécuter comme un test. Python l'offre depuis 2001 avec son module doctest, qui s'exécute quand quelqu'un l'invoque, et Rust exécute par défaut les exemples de sa documentation comme des tests. Et quand le terrain compare un outil à un autre, il dessine une grille : des lignes de fonctions, une colonne par outil, des coches et des croix.

Le terrain a trois formes ; la méthode revient à une seule phrase.

## 2. Le premier principe

Voici la phrase à laquelle toute la méthode revient : **vous déclarez un monde dans un langage fait pour lui, et vous gouvernez la façon dont ce monde change.**

Deux actes. Tout le reste de ce livre est l'un d'eux, ou les deux ensemble.

## 3. La forme Softanza

« Depuis les premiers principes » peut se vérifier. Dans ce livre, cela a un sens étroit. Prenez un concept que tout le monde utilise, écrivez comment le terrain le tient, reconcevez-le, et laissez un code qui porte la reconception et un tribunal qui la juge. La page d'histoire du site s'intitule *Depuis les premiers principes*, et la bibliothèque est sur GitHub depuis le 12 mars 2022. L'expression n'est pas ici une décoration. C'est un ordre de travail.

Laissez-moi vous montrer le plus petit réexamen que je connaisse. Demandez à Python combien de fois la chaîne vide apparaît dans le mot « text », et il répond cinq : une avant chaque lettre et une à la fin. Demandez-lui si « text » contient la chaîne vide, et il dit oui ; JavaScript dit la même chose. (Python 3.13 et Node 22, exécutés le 8 octobre 2026.) C'est une convention d'implémenteurs, non un fait que quiconque dirait à voix haute. Softanza énonce une règle à la place, et la règle a un nom dans la narration qui l'argumente : le vide ne se compte pas, et le vide ne se contient pas. Que répond Softanza aux deux mêmes questions ? Exécutez-le :

```haro
? Q("text").Count("")
#--> 0
? Q("text").Contains("")
#--> FALSE
```

Il répond `0` et `FALSE`. Deux lignes, et une décision avec laquelle vous pouvez être en désaccord. Voilà à quoi ressemble un réexamen quand il est honnête : assez petit pour être lu, assez explicite pour être refusé.

Une lecture du dossier, faite en octobre 2026, a compté quarante-six concepts de cette sorte, en sept familles. Les deux premières sont les paradigmes, tels que la programmation orientée portée, la programmation de la connaissance et la programmation réactive reconçus, et les moteurs de paradigme, tels que la vérité, les quantificateurs et le temps. Les cinq autres sont les patrons et la réaction ; l'expression et la perception ; les données, le temps et le raisonnement ; le système, la livraison et les opérations ; et la bibliothèque qui se connaît elle-même. Quarante-six est une lecture et non un recensement ; la page de registre du site lui-même, lue le 9 octobre 2026, dit quarante-sept. Chaque concept de la liste a son propre article ou document de conception, et c'était le critère pour entrer dans la liste.

Voyons maintenant les deux actes, chacun en quelques lignes.

**Déclarer.** Une sorte de valeur est déclarée en une phrase, et chaque verdict à son égard est calculé et s'explique lui-même. Pourquoi -4 ne peut-il pas être un score ?

```haro
ConstrainQ("score").ToBeQ(:Number).AndQ().ToBeQ(:Positive).AndQ().ToBeQ(:Even)
? CanQ(42).BeA("score")
#--> TRUE
? CanQ(-4).BeA("score")
#--> FALSE
? Why()
#--> no: -4 is not positive (constraint 2 of 'score')
```

Remarquez la dernière ligne : `no: -4 is not positive (constraint 2 of 'score')`. Le verdict nomme la règle qu'il a appliquée, par son numéro ! Un verdict sur une sorte déclarée qui ne peut pas dire pourquoi n'est pas admis dans cette maison.

**Gouverner.** Une contrainte déclarée, une fois imposée, refuse un changement avant qu'il atterrisse. Ici la chaîne « hello » doit rester en minuscules. La mise à jour vers « HELLO » atterrit-elle ?

```haro
oName = new stzString("hello")
oName.EnforceConstraint("keep-lowercase", :Lowercase)
bRefused = FALSE
try
	oName.UpdateWith("HELLO")
catch
	bRefused = TRUE
done
? bRefused
#--> TRUE
? oName.Content()
#--> hello
```

La mise à jour a été refusée ! L'objet reste comme il était : il répond encore `hello`. Déclarer une contrainte et l'imposer sont deux actes, et la garde derrière ce bloc vérifie qu'une contrainte seulement déclarée reste passive.

Gouverner a aussi un côté qui fait face à la personne. Le système demande, et il ne vous laisse pas clore un monde qui n'est pas complet. Que dit-il quand vous essayez de conclure quand même ?

```haro
oKB = new stzKnowledgeGraph("restaurant")
oKB.Know("margherita", "dish").Know("tiramisu", "dish")
oKB.AddConversationQ("setup").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
aQ = oKB.AskInXT("setup")
? aQ[:why]
#--> every dish needs 'contains'
try
	oKB.ConcludeIn("setup", "world")
catch
	? cCatchError
done
#--> Can't conclude: 2 gap(s) remain -- the wise-coding loop is not done. Ask the next question.
```

Le but a été déclaré : chaque plat doit dire ce qu'il contient. L'écart entre le but et ce qui est connu génère la question, et la question porte sa raison. Conclure alors que deux écarts demeurent est refusé ! La ligne imprimée est `Can't conclude: 2 gap(s) remain -- the wise-coding loop is not done. Ask the next question.`, et ses derniers mots vous disent quoi faire ensuite. Le chapitre 18 parle de cette conversation. Ici il suffit de voir que gouverner n'est pas seulement refuser ; c'est demander.

Encore un réexamen, parce que les moteurs de paradigme font aussi partie de la méthode. La vérité, dans le langage sous Softanza, est une affaire de vide et de non-vide, et une liste de mots compte comme vraie. Softanza garde cette vérité par défaut et vous laisse l'étendre par déclaration. Une fois « wrong » déclaré comme un élément qui rend une liste fausse, une liste qui le contient est-elle encore vraie ?

```haro
SetItemsMakingAListFalse([ "false", "wrong", "dangerous" ])
? IsTrue([ "hello", "this", "is", "wrong" ])
#--> TRUE
? IsTrueXT([ "hello", "this", "is", "wrong" ])
#--> FALSE
```

La réponse de l'hôte est inchangée : `TRUE`. La réponse étendue lit votre déclaration et dit `FALSE` ! « La vérité devient une affaire de politique », dit la narration, et la politique est écrite là où vous pouvez la lire.

Voilà donc la méthode, sous la forme que vous rencontrerez dans chaque chapitre après celui-ci. Un concept tel que le terrain le tient. Le seul principe auquel le dossier revient. La reconception, en code qui s'exécute, avec sa promesse sous chaque bloc. La décision, et ce qui a été refusé. Le tribunal qui la prouve, par son nom. Le terrain, et où il mène. La limite, en trois mots d'étape. Le premier, **construit**, veut dire que le code existe, qu'une garde existe et qu'un bloc a tourné. Le deuxième, **conçu**, couvre ce que le site appelle en construction, spécification et proposition ratifiée. Le troisième, **absent**, couvre un nom sans rien derrière lui pour l'instant, et ce que personne n'a nommé. Puis six portes, une pour chaque sorte de lecteur, et un exercice.

Et le livre est jugé comme la bibliothèque l'est. Chaque bloc qu'il contient s'est exécuté dans la bibliothèque la nuit où la page a été construite, au commit imprimé en haut de la page. Une page dont les promesses ne sont pas tenues ne se construit pas.

## 4. La décision, et ce que j'ai refusé

Il n'existe pas de fiche unique d'une décision appelée « la méthode ». La méthode a été décidée par morceaux, et les morceaux sont dans le dossier.

**J'ai refusé d'ajouter une fonction sans besoin.** Je l'ai écrit dans un article de la bibliothèque, qui ne porte pas de date. « Je n'introduis de nouvelles fonctions que lorsqu'elles résolvent un problème tangible ou lorsque j'anticipe qu'elles répondront aux besoins des programmeurs. » Les premiers principes sans cette règle produisent un musée. C'est mon point de vue, non un résultat. Avec elle, un réexamen doit mériter sa place : quelqu'un avait un problème auquel la forme du terrain ne répondait pas.

**J'ai refusé le code généraliste comme lieu de rencontre entre les personnes et les machines.** La vision de la plateforme le dit en une ligne, que j'ai ratifiée. Les humains et les IA se rencontrent dans des langages déclarés, petits, clos et jugés, et non dans du code généraliste. Déclarer est le premier acte parce qu'il rend le second possible. Un tribunal ne peut juger que la phrase d'un langage qu'il connaît.

**J'ai refusé un titre qui regardait en arrière.** Quand ce livre a été proposé pour la première fois, son titre était *Programming by Heart*, le slogan de la présentation de 2020. Je l'ai écarté comme dépassé : il nommait une posture, et le livre devait nommer ce qui était repensé. La proposition suivante était *Declare, Then Govern*. J'ai gardé à la place la propre phrase du site pour la couverture (le 8 octobre 2026, j'en ai changé un mot, pour « artisans du logiciel »). Les deux verbes sont passés en quatrième de couverture, où vous les trouverez. Ils organisent chaque chapitre ; ils n'avaient pas besoin d'en être le nom.

**J'ai refusé la grille seule.** Les documents de la bibliothèque contiennent des dizaines de grilles de comparaison, et dans celles-ci la colonne de Softanza gagne presque chaque ligne. Un lecteur qui ne voit que ces grilles a raison d'en demander davantage qu'une grille. L'honnêteté du dossier est ailleurs : dans les sections des études de terrain intitulées « ce que le terrain a et qui manque à Softanza, honnêtement », et dans des chiffres mesurés. Quand le runtime sous Softanza a été mesuré de nouveau en septembre 2026 contre celui auquel il était comparé, le résultat annoncé auparavant ne s'est pas reproduit. La perte a été consignée le jour même, dans une note interne. C'est la règle que suit ce livre : une perte est imprimée à côté du gain, dans la même section.

**J'ai refusé d'appeler une lecture un recensement.** Les quarante-six concepts sont une lecture du dossier par une session, non une liste que j'ai tranchée ligne par ligne. L'annexe A imprime le registre de quarante-six lignes tel que l'étude le donne, avec la colonne propre au livre, comme annexe de travail : les lignes n'ont pas été tranchées une à une.

Voilà les cinq refus ; voyons maintenant le tribunal qui juge les blocs ci-dessus.

## 5. Le tribunal

Les trois blocs des deux actes reposent sur deux gardes. `modality_narrated` prouve qu'une sorte déclarée peut être inspectée, qu'un verdict nomme la contrainte qui a échoué, et qu'une sorte inconnue n'autorise jamais en silence. Elle prouve aussi qu'une contrainte imposée refuse une mauvaise mise à jour avant qu'elle atterrisse, tandis qu'une contrainte déclarée reste passive. `wisecoding_narrated` prouve la conversation. Elle prouve des écarts calculés à partir du but déclaré, une question qui dit pourquoi elle est posée, des réponses admises, et une loi qui refuse à travers la conversation et atteint une personne. Et elle prouve que conclure avec des écarts ouverts est refusé. Sa sœur, `wisecoding_rich_narrated`, porte les cas plus riches de la même boucle.

Le réexamen du vide repose sur `612_dealing_in_emptiness_in_softanza.ring`, un test de la bibliothèque écrit en scénarios, chaque ligne énonçant le résultat qu'elle attend. Le réexamen de la vérité repose sur sa narration et sur l'exécution de ce livre, et sa garde est l'étape suivante. Le fichier de la bibliothèque qui lui est consacré, `04_truth_in_softanza.ring`, fixe la liste des mots faux par affectation et n'appelle jamais la fonction, de sorte qu'il ne prouve pas le bloc.

Le tribunal est nommé ; vient ensuite le terrain, et où il mène.

## 6. Le terrain, et où il mène

Le terrain mène en adoption. Les fiches de décision sont un standard léger que beaucoup d'équipes utilisent, avec des modèles et des outils autour. L'élément décision de ce livre existe dans ce livre et dans une étude du dossier, et pas encore comme donnée dans la bibliothèque. Les exemples de la documentation peuvent être exécutés par l'outil standard de Python, et Rust les exécute par défaut. Les promesses de Softanza sont jugées par les exécuteurs propres de la maison, qu'aucun outil extérieur ne lit encore. Et le terrain compare par grille, comme les pages du dossier le font aussi ; une grille seule est un début, et c'est pourquoi la section 4 demande la perte à côté du gain.

Là où je pense que Softanza se distingue, c'est en un seul endroit : le réexamen est mené jusqu'au bout. Je tiens cela pour une vue, non pour un résultat. La décision est écrite, la reconception s'exécute, la promesse est jugée à la construction, et le mot d'étape dit jusqu'où chaque pièce est allée. Une fiche de décision ne s'exécute pas. Un exemple ne dit pas ce qui a été refusé. Ici, ils sont un seul objet.

## 7. La limite

Ce qui est construit : le tribunal derrière chaque bloc de ce chapitre sauf celui de la vérité, et les cinq mots d'étape que le site imprime sur chaque produit.

Ce qui est conçu : le registre des concepts repensés comme données, une ligne par concept avec son article, son code, sa garde et son étape. À côté, une garde qui échoue quand un nouveau concept arrive sans ligne. Les deux sont aujourd'hui une spécification.

Ce qui est absent : une page qui montre chaque concept avec une preuve exécutée (le site a une page de registre, lue le 9 octobre 2026, qui les liste chacun avec ses preuves). Un fichier de tests pour le module du moteur de l'un des moteurs de paradigme, la fusion de sections : il n'en a pas en propre, bien que ses méthodes de fusion s'exécutent dans `base/test/string/289_content.ring` et `max/test/stzListOfPairsTest.ring`. Et quelques réexamens où l'article va un pas au-delà du code d'aujourd'hui. L'article sur les quantificateurs demande si toutes vos notes `AreGreaterThan` la moyenne, et cette méthode s'écrit autrement dans la bibliothèque aujourd'hui. Ses quantificateurs plus conviviaux, certains, la plupart et peu, tirent au hasard, de sorte qu'ils ne portent aucune promesse aujourd'hui. Le registre est une lecture, et une lecture peut manquer un concept qui ne vit que dans un seul article.

Là s'arrête ce chapitre ; six portes suivent, une pour chaque sorte de lecteur.

## 8. Six portes

**Le programmeur.** Chaque affirmation que vous faites peut porter sa promesse. Une contrainte imposée refuse une mauvaise mise à jour au point de mise à jour de l'objet (`Update()` pour une chaîne ou un nombre, `_SetContent()` pour une liste).

**L'analyste.** Votre règle est une déclaration, et son verdict nomme la règle qui a échoué, par son numéro.

**Le concepteur.** Le mot d'étape fait partie de l'interface. Un produit qui n'existe pas encore le dit, en un mot que vous pouvez vérifier.

**Le décideur.** Demandez à chaque fournisseur la perte à côté du gain. Le chapitre 1 en imprime une, avec sa date : le runtime sous Softanza est derrière celui auquel il était comparé, de 1,04 à 1,88 fois, mesuré le 13 septembre 2026.

**Le formateur.** Chaque réexamen a un article qui l'argumente : le concept, la forme du terrain, la reconception. C'est un programme de cours, ordonné par famille.

**L'agent.** Vous apprenez cette plateforme à partir de la plateforme, et elle vous corrige. Un verdict qui dit pourquoi est écrit pour vous autant que pour une personne.

## 9. Exercice

Choisissez un défaut de votre propre langage que vous n'avez jamais questionné : ce que compte la chaîne vide, ce qui compte comme vrai, ce que veut dire « la plupart ». Avant d'exécuter quoi que ce soit, écrivez en une phrase la règle que vous croyez juste. Puis écrivez deux promesses sous la forme que vous avez rencontrée : la ligne que votre langage imprime aujourd'hui, et la ligne que votre règle doit imprimer.

```haro exercise
? YourDefault(the_input)
#--> what your language prints today
? YourRule(the_input)
#--> what your declared rule must print
```

Exécutez les deux. Je ne vous dirai pas quelle règle est juste. Si votre règle et votre langage divergent, vous avez trouvé une décision que quelqu'un a prise pour vous, et vous pouvez maintenant la prendre vous-même.

Je vous laisse celui-ci, volontairement. Reprenez le bloc de la section 3 qui gouverne une chaîne, changez un seul mot, `EnforceConstraint` pour `AddConstraint`, et exécutez-le tel qu'il est donné ci-dessous. Je n'en imprime aucune sortie.

```haro exercise
oName = new stzString("hello")
oName.AddConstraint("keep-lowercase", :Lowercase)
bRefused = FALSE
try
	oName.UpdateWith("HELLO")
catch
	bRefused = TRUE
done
? bRefused
? oName.Content()
```

Regardez ce qu'il imprime : si la mise à jour a été refusée, et ce que l'objet contient. Lisez ensuite la section 3, juste après le bloc, et la section 5, sur la garde qui le vérifie : la page dit pourquoi. Quand vous aurez les deux lignes, vous saurez pourquoi une contrainte déclarée n'est pas une contrainte imposée.

Le chapitre 4 dessine la plateforme en une image, sous une seule idée à chaque altitude : rien n'est cru, tout est jugé.
