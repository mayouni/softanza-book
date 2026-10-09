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
  built: "le tribunal derrière chaque bloc de ce chapitre, et les mots d'étape que le site imprime sur chaque produit"
  designed: "le registre des concepts repensés comme données, avec une garde qui échoue quand un concept n'a pas de preuve"
  absent: "une page qui montre chaque concept repensé avec sa preuve ; un fichier de tests pour le moteur de paradigme de la fusion de sections"
status: draft
rulings: ["12.19", "12.22", "12.29", "12.30"]
research: research/ch03.md
---

## 1. Le concept, tel que le terrain le tient

Dans notre industrie, « depuis les premiers principes » est un slogan. Cela veut dire : raisonner à partir du bas, non par analogie. Vous l'entendrez dans des conférences et le lirez dans des annonces de lancement, et on vous montrera rarement ce qu'il a produit.

Le terrain a bien une méthode pour les décisions derrière le logiciel, et c'est une bonne méthode. Une équipe écrit une courte fiche pour chaque décision qu'elle prend : le contexte, la décision, les conséquences. Beaucoup d'équipes les appellent des fiches de décision d'architecture, d'après un billet de blog que Michael Nygard a écrit en 2011. Le terrain a aussi une méthode pour prouver ce que fait une fonction : un exemple écrit sous la fonction, exécuté par les outils chaque fois que le projet est construit. Python le fait avec son module doctest depuis 2001, et Rust exécute les exemples de sa documentation comme des tests. Et quand le terrain compare un outil à un autre, il dessine une grille : des lignes de fonctions, une colonne par outil, des coches et des croix.

## 2. Le premier principe

Voici la phrase à laquelle toute la méthode revient : **vous déclarez un monde dans un langage fait pour lui, et vous gouvernez la façon dont ce monde change.**

Deux actes. Tout le reste de ce livre est l'un d'eux, ou les deux ensemble.

## 3. La forme Softanza

« Depuis les premiers principes » peut se vérifier. Dans Softanza, cela a un sens étroit : prendre un concept que tout le monde utilise, écrire comment le terrain le tient, le reconcevoir, et laisser un code qui porte la reconception et un tribunal qui la juge. La page d'histoire du site s'intitule *Depuis les premiers principes*, et la bibliothèque est sur GitHub depuis le 12 mars 2022. L'expression n'y est pas une décoration. C'est un ordre de travail.

Laissez-moi vous montrer le plus petit réexamen que je connaisse. Demandez à Python combien de fois la chaîne vide apparaît dans le mot « text », et il répond cinq : une avant chaque lettre et une à la fin. Demandez-lui si « text » contient la chaîne vide, et il dit oui ; JavaScript dit la même chose. (Python 3.13 et Node 22, exécutés le 8 octobre 2026.) C'est une convention d'implémenteurs, non un fait que quiconque dirait à voix haute. Softanza énonce une règle à la place, et la règle a un nom dans la narration qui l'argumente : le vide ne se compte pas, et le vide ne se contient pas.

```haro
? Q("text").Count("")
#--> 0
? Q("text").Contains("")
#--> FALSE
```

Deux lignes, et une décision avec laquelle vous pouvez être en désaccord. Voilà à quoi ressemble un réexamen quand il est honnête : assez petit pour être lu, assez explicite pour être refusé.

Une lecture du dossier, faite en octobre 2026, a compté quarante-six concepts de cette sorte, en sept familles : les paradigmes, tels que le modèle mental, la programmation de la connaissance et la programmation réactive reconçus ; les moteurs de paradigme, tels que la vérité, les quantificateurs et le temps ; les patrons et la réaction ; l'expression et la perception ; les données, le temps et le raisonnement ; le système, la livraison et les opérations ; et la bibliothèque qui se connaît elle-même. Quarante-six est une lecture et non un recensement. Chaque concept de la liste a son propre article ou document de conception, et c'était le critère pour entrer dans la liste.

Voyons maintenant les deux actes, chacun en quelques lignes.

**Déclarer.** Une sorte de valeur est déclarée en une phrase, et chaque verdict à son égard est calculé et s'explique lui-même :

```haro
ConstrainQ("score").ToBeQ(:Number).AndQ().ToBeQ(:Positive).AndQ().ToBeQ(:Even)
? CanQ(42).BeA("score")
#--> TRUE
? CanQ(-4).BeA("score")
#--> FALSE
? Why()
#--> no: -4 is not positive (constraint 2 of 'score')
```

Remarquez la dernière ligne. Le verdict nomme la règle qu'il a appliquée, par son numéro. Une réponse qui ne peut pas dire pourquoi n'est pas admise dans cette maison.

**Gouverner.** Une contrainte déclarée, une fois imposée, refuse un changement avant qu'il atterrisse :

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

La mise à jour a été refusée, et l'objet reste comme il était. L'erreur que la bibliothèque lève dit ce qui a été tenté, pourquoi cela a été refusé et que faire : corriger la nouvelle valeur, ou assouplir la contrainte. Déclarer une contrainte et l'imposer sont deux actes, et la garde derrière ce bloc vérifie qu'une contrainte seulement déclarée reste passive.

Gouverner a aussi un côté qui fait face à la personne. Le système demande, et il ne vous laisse pas clore un monde qui n'est pas complet :

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

Le but a été déclaré : chaque plat doit dire ce qu'il contient. L'écart entre le but et ce qui est connu génère la question, et la question porte sa raison. Conclure alors que deux écarts demeurent est refusé, et le refus vous dit quoi faire ensuite. Le chapitre 18 parle de cette conversation. Ici il suffit de voir que gouverner n'est pas seulement refuser ; c'est demander.

Encore un réexamen, parce que les moteurs de paradigme font aussi partie de la méthode. La vérité, dans le langage sous Softanza, est une affaire de zéros et de non-zéros, et une liste de mots compte comme vraie. Softanza garde cette vérité par défaut et vous laisse l'étendre par déclaration :

```haro
SetItemsMakingAListFalse([ "false", "wrong", "dangerous" ])
? IsTrue([ "hello", "this", "is", "wrong" ])
#--> TRUE
? IsTrueXT([ "hello", "this", "is", "wrong" ])
#--> FALSE
```

La réponse de l'hôte est inchangée. La réponse étendue lit votre déclaration. « La vérité devient une affaire de politique », dit la narration, et la politique est écrite là où vous pouvez la lire.

Voilà donc la méthode, sous la forme que vous rencontrerez dans chaque chapitre après celui-ci. Un concept tel que le terrain le tient. Le seul principe auquel le dossier revient. La reconception, en code qui s'exécute, avec sa promesse sous chaque bloc. La décision, et ce qui a été refusé. Le tribunal qui la prouve, par son nom. Le terrain, et où il mène. La limite, en trois mots d'étape : **construit** veut dire que le code existe et que ses gardes passent ; **conçu** couvre ce que le site appelle en construction, spécification et proposition ratifiée ; **absent** couvre un nom sans rien derrière lui pour l'instant, et ce que personne n'a nommé. Six portes, une pour chaque sorte de lecteur. Un exercice.

Et le livre est jugé comme la bibliothèque l'est. Chaque bloc qu'il contient s'est exécuté dans la bibliothèque la nuit où la page a été construite, au commit imprimé en haut de la page, et une page dont les promesses ne sont pas tenues ne se construit pas.

## 4. La décision, et ce que j'ai refusé

Il n'existe pas de fiche unique d'une décision appelée « la méthode ». La méthode a été décidée par morceaux, et les morceaux sont dans le dossier.

**J'ai refusé d'ajouter une fonction sans besoin.** Je l'ai écrit dans un article bien avant ce livre : « Je n'introduis de nouvelles fonctions que lorsqu'elles résolvent un problème tangible ou lorsque j'anticipe qu'elles répondront aux besoins des développeurs. » Les premiers principes sans cette règle produisent un musée. Avec elle, un réexamen doit mériter sa place : quelqu'un avait un problème auquel la forme du terrain ne répondait pas.

**J'ai refusé le texte libre comme lieu de rencontre entre les personnes et les machines.** La vision de la plateforme le dit en une ligne, que j'ai ratifiée : les humains et les IA se rencontrent dans des langages déclarés, petits, clos et jugés, et non dans du code généraliste. Déclarer est le premier acte parce qu'il rend le second possible. Un tribunal ne peut juger que la phrase d'un langage qu'il connaît.

**J'ai refusé un titre qui regardait en arrière.** Quand ce livre a été proposé pour la première fois, son titre était *Programming by Heart*, le slogan de la présentation de 2020. Je l'ai écarté comme dépassé : il nommait une posture, et le livre devait nommer ce qui était repensé. La proposition suivante était *Declare, Then Govern*. J'ai gardé à la place la propre phrase du site pour la couverture, et les deux verbes sont passés en quatrième de couverture, où vous les trouverez. Ils organisent chaque chapitre ; ils n'avaient pas besoin d'en être le nom.

**J'ai refusé la grille seule.** Les documents de la bibliothèque contiennent des dizaines de grilles de comparaison, et dans celles-ci la colonne de Softanza gagne presque chaque ligne. Un lecteur qui ne voit que ces grilles a raison de les escompter. L'honnêteté du dossier est ailleurs : dans les sections des études de terrain intitulées « ce que le terrain a et qui manque à Softanza, honnêtement », et dans des chiffres mesurés. Quand le runtime sous Softanza a été mesuré de nouveau en septembre 2026 contre celui auquel il était comparé, le résultat annoncé auparavant ne s'est pas reproduit, et la perte a été publiée le jour même. C'est la règle que suit ce livre : une perte est imprimée à côté du gain, dans la même section.

**J'ai refusé d'appeler une lecture un recensement.** Les quarante-six concepts sont une lecture du dossier par une session, non une liste que j'ai tranchée ligne par ligne. [AUTHOR: Approuvez-vous le registre de quarante-six lignes comme l'annexe A du livre en l'état, ou le trancherez-vous d'abord ligne par ligne ?]

## 5. Le tribunal

Les quatre blocs des deux actes reposent sur deux gardes. `modality_narrated` prouve qu'une sorte déclarée peut être inspectée, qu'un verdict nomme la contrainte qui a échoué, qu'une sorte inconnue n'autorise jamais en silence, et qu'une contrainte imposée refuse une mauvaise mise à jour avant qu'elle atterrisse tandis qu'une contrainte déclarée reste passive. `wisecoding_narrated` prouve la conversation : des écarts calculés à partir du but déclaré, une question qui dit pourquoi elle est posée, des réponses admises, une loi qui refuse à travers la conversation et atteint une personne, et la conclusion avec des écarts ouverts refusée. Sa sœur, `wisecoding_rich_narrated`, porte les cas plus riches de la même boucle.

Les réexamens du vide et de la vérité reposent sur les tests classiques de la bibliothèque, les blocs numérotés avec leurs réponses écrites dessous, que la maison a gardés comme sa première forme de test.

## 6. Le terrain, et où il mène

Le terrain mène en adoption. Les fiches de décision sont un standard léger que beaucoup d'équipes utilisent, avec des modèles et des outils autour ; l'élément décision de ce livre existe dans ce livre et dans une étude du dossier, et pas encore comme donnée dans la bibliothèque. Les exemples de la documentation sont exécutés par les outils standard de Python et de Rust dans chaque projet qui en écrit ; les promesses de Softanza sont jugées par les exécuteurs propres de la maison, qu'aucun outil extérieur ne lit. Et l'habitude du terrain de comparer par grille n'est pas pire que celle du dossier, qui montre la même faiblesse sur ses propres pages.

Là où je pense que Softanza se distingue, c'est en un seul endroit : le réexamen est mené jusqu'au bout. La décision est écrite, la reconception s'exécute, la promesse est jugée à la construction, et le mot d'étape dit jusqu'où chaque pièce est allée. Une fiche de décision ne s'exécute pas. Un exemple ne dit pas ce qui a été refusé. Ici, ils sont un seul objet.

## 7. La limite

Ce qui est construit : le tribunal derrière chaque bloc de ce chapitre, et les cinq mots d'étape que le site imprime sur chaque produit.

Ce qui est conçu : le registre des concepts repensés comme données, une ligne par concept avec son article, son code, sa garde et son étape, et une garde qui échoue quand un nouveau concept arrive sans ligne. C'est aujourd'hui une spécification.

Ce qui est absent : une page qui montre le registre entier avec ses preuves ; un fichier de tests pour l'un des moteurs de paradigme, la fusion de sections, qui n'en a pas en propre ; et quelques réexamens qui ne s'exécutent pas comme leur article l'a écrit. L'article sur les quantificateurs demande si toutes vos notes `AreGreaterThan` la moyenne, et cette méthode s'écrit autrement dans la bibliothèque aujourd'hui ; ses quantificateurs plus conviviaux, certains, la plupart et peu, tirent au hasard, de sorte qu'ils ne peuvent pas porter une promesse. Le registre est une lecture, et une lecture peut manquer un concept qui ne vit que dans un seul article.

## 8. Six portes

**Le programmeur.** Chaque affirmation que vous faites peut porter sa promesse, et une contrainte déclarée refuse une mauvaise mise à jour à l'unique endroit où les mises à jour se font.

**L'analyste.** Votre règle est une déclaration, et son verdict nomme la règle qui a échoué, par son numéro.

**Le concepteur.** Le mot d'étape fait partie de l'interface. Un produit qui n'existe pas encore le dit, en un mot que vous pouvez vérifier.

**Le décideur.** Demandez à chaque fournisseur la perte à côté du gain. Ici elle est imprimée, avec sa date.

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
