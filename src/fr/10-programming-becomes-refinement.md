---
id: programming-becomes-refinement
part: 2
number: 10
title: La programmation devient raffinement
spine: false
narrations: [stzpolycode-refinement-centered_programming.md]
site: [refinement]
guards: [refinablecode_narrated, refine_deepening_narrated, gate_deepening_narrated]
stage:
  built: "le point de raffinement déclaré dans le source ; la barrière à cinq contrôles ; la cascade d'un point et d'une classe ; le retour en arrière par pas, par point de contrôle et jusqu'à zéro ; le plancher de confiance et le raffinement gouverné"
  designed: "l'expérience que décrit l'article : demander à un point de s'expliquer, appliquer un plan, un raffinement en une ligne ; la cascade du graphe de code jointe à la barrière ; le siège de raffinement de Haro"
  absent: "un historique sauvegardé : le fichier garde le source et rien de la ligne de temps"
status: draft
rulings: ["12.19", "12.23", "12.29"]
research: research/ch10.md
---

Dans ce chapitre, je dis ce que j'entends par raffiner plutôt que programmer. C'est un changement apporté à du code déclaré modifiable, proposé sous une forme typée, jugé par une barrière, enregistré comme un pas, et réversible. J'exécute la forme que la bibliothèque lui donne : le point de raffinement, la proposition, la barrière, la cascade, le plancher de confiance et le retour en arrière. Et j'imprime la barrière telle qu'elle est, cinq contrôles et non les quatre de ma conception. Je dis où le terrain mène et où la barrière s'arrête. Le principe est la phrase que j'ai écrite sur la quatrième de couverture du premier livre de cette maison d'édition : cessez de vouloir gouverner l'intelligence, et gouvernez le changement.

## 1. Le concept, tel que le terrain le tient

Le terrain a un nom pour changer une infrastructure avec une répétition : planifier, puis appliquer. Un outil calcule ce qui changerait, le montre, et ne l'applique que lorsque vous le dites. Terraform a rendu le schéma familier, et les contrôleurs d'admission du terrain appliquent la même idée à une requête avant qu'un cluster l'accepte. Plus récemment, le terrain a un nom pour une façon de travailler avec des agents d'IA qui écrivent du code : les spécifications d'abord, et l'agent remplit. Tout cela est une connaissance générale, pas une étude du dossier.

Ce que ces pratiques partagent, c'est l'endroit où elles se tiennent. Le plan et le contrôle d'admission portent sur l'infrastructure et sur les requêtes. Pour le code lui-même, une bonne part de la réponse du terrain à un changement reste un diff, un correctif de texte, et la relecture d'une personne. Cela marchait tant que chaque changement avait derrière lui une personne à qui poser la question. C'est un instrument faible quand la plupart des changements arrivent d'agents, en volume ; je tiens cela pour une vue, non pour un résultat.

À cet instrument faible, j'oppose une seule phrase.

## 2. Le premier principe

J'ai écrit la phrase sur la quatrième de couverture du premier livre de cette maison d'édition, et je n'en ai pas trouvé de meilleure : **cessez de vouloir gouverner l'intelligence, et gouvernez le changement.** L'en-tête de la bibliothèque dit la même chose sous la forme d'un type : un changement est une proposition typée, pas un diff.

Le reste du chapitre exécute cette phrase.

## 3. La forme Softanza

La pratique a changé de nom dans ma vie. Je disais que je programmais. Je dis maintenant de plus en plus que je raffine, et je veux dire par là quelque chose d'exact. Un raffinement est un changement apporté à du code qui a été déclaré modifiable, proposé sous une forme typée, jugé par une barrière, enregistré comme un pas, et réversible. Le premier livre de cette maison d'édition, *Refinement-Oriented Programming*, raconte la discipline à travers l'histoire d'une banque devant la lettre d'un régulateur. Ce chapitre dit ce que la bibliothèque en porte.

Il commence par déclarer où le code peut changer. Un point de raffinement est un bouton nommé, écrit dans le source sous forme de balise, avec son genre, sa valeur et ses bornes :

```haro
cSrc = 'vat_rate = <R:PARAM name="vat" value="0.20" min="0" max="0.25">' + nl +
       'sort_by  = <R:ALGO name="sort" value="quick" options="quick|merge|heap">'
o = new stzRefinableCode(cSrc)
? o.NumberOfPoints()
#--> 2
? @@( o.RefinementPoints() )
#--> [ [ "vat", "param", "0.20" ], [ "sort", "algo", "quick" ] ]
? o.KindOf("vat")
#--> param
```

Un changement est alors une proposition. Elle nomme un point et une valeur ; si elle franchit la barrière, elle prend effet et est enregistrée comme un seul pas :

```haro
r = o.Refine("vat").To("0.22")
? r[:admitted]
#--> 1
? o.ValueOf("vat")
#--> 0.22
? o.NumberOfSteps()
#--> 1
```

L'admission s'imprime en `1` et `0`, non en `TRUE` et `FALSE` : c'est ainsi que ce verbe répond, et j'imprime l'exécution. Et que change une proposition qui ne franchit pas la barrière, et que dit la barrière ? Exécutez-le :

```haro
r2 = o.Refine("vat").To("0.99")
? r2[:admitted]
#--> 0
? r2[:why]
#--> constraint: 0.99 above max 0.25
? o.ValueOf("vat")
#--> 0.22
? o.Refine("sort").To("bubble")[:why]
#--> constraint: 'bubble' not in options quick|merge|heap
? o.Refine("ghost").To("1")[:why]
#--> structural: no refinement point 'ghost'
? o.NumberOfSteps()
#--> 1
```

Trois refus, et la ligne de temps n'a pas grandi d'un pas ! Le commentaire de la bibliothèque en fait une de ses lois : une proposition rejetée ne finit jamais modifiée. Chaque refus nomme d'abord son étape, `constraint` deux fois et `structural` une fois, comme dans `structural: no refinement point 'ghost'`, pour qu'une personne, ou un agent, puisse corriger la proposition sans lire un diff.

**La cascade** est ce que vous lisez à la place du diff. Avant le changement, demandez ce qu'il atteint. Il y a deux cascades, et elles sont séparées. Pour un point, c'est la ligne où il se trouve et les autres points de cette même ligne :

```haro
cPrice = 'price = <R:PARAM name="vat" value="0.20" min="0" max="0.30"> * <R:PARAM name="margin" value="1.1" min="1" max="2">' + nl +
         'floor = <R:PARAM name="floor" value="0.10" min="0" max="0.30">'
oc = new stzRefinableCode(cPrice)
aC = oc.Cascade("vat")
? aC[:lines][1]
#--> 1
? @@( aC[:alsoTouches] )
#--> [ "margin" ]
? oc.Cascade("floor")[:lines][1]
#--> 2
? len(oc.Cascade("floor")[:alsoTouches])
#--> 0
```

`vat` se trouve ligne 1 et touche aussi `[ "margin" ]` ; `floor` se trouve ligne 2, seul.

Pour une classe, la cascade est une propriété de la structure du code : qui en descend et qui hérite d'une méthode. La bibliothèque la calcule à partir du graphe de code, et elle peut analyser un texte sans toucher un fichier :

```haro
cCls = 'class Tariff' + nl +
       '	def Rate()' + nl +
       '		return 0.20' + nl +
       'class Invoice from Tariff' + nl +
       '	def Total()' + nl +
       '		return 1' + nl +
       'class Receipt from Invoice' + nl +
       '	def Print()' + nl +
       '		return 1' + nl +
       'class Quote from Tariff' + nl +
       '	def Rate()' + nl +
       '		return 0.18' + nl
g0 = new stzRingCodeGraph("")
g0.ScanSource(cCls, "world.ring")
g0.BuildGraph()
? @@( g0.Cascade("Tariff")[:descendants] )
#--> [ "Invoice", "Quote", "Receipt" ]
? g0.Cascade("Tariff")[:blastRadius]
#--> 3
? @@( g0.ImpactOf("Rate")[:inheritedBy] )
#--> [ "Invoice", "Receipt" ]
```

Changez le taux du tarif et trois classes sont dans le rayon d'impact. Deux d'entre elles héritent de la méthode, et `ImpactOf` les nomme : `[ "Invoice", "Receipt" ]`. La troisième, `Quote`, la redéfinit, de sorte qu'elle la possède et ne fait pas que l'hériter. C'est la différence que trace `ImpactOf`.

Comment un changement atteint-il ses dépendants ? Par une règle qui couvre plusieurs points, jugée sur l'état que le changement produirait. Si la règle échoue, la valeur est remise :

```haro
d = new stzRefinableCode(cPrice)
d.DeclareDerivation("vat-above-floor",
	func oCode { return ring_number(oCode.ValueOf("vat")) >= ring_number(oCode.ValueOf("floor")) },
	"vat must not drop below floor")
? d.Refine("vat").To("0.30")[:admitted]
#--> 1
r3 = d.Refine("vat").To("0.05")
? r3[:admitted]
#--> 0
? r3[:why]
#--> derivation: rule 'vat-above-floor' violated -- vat must not drop below floor
? d.ValueOf("vat")
#--> 0.30
```

La règle a refusé le changement et s'est nommée : `derivation: rule 'vat-above-floor' violated -- vat must not drop below floor`. La valeur est toujours `0.30`.

Et qui l'a proposé ? Chaque proposition porte son origine, et un point peut fixer un plancher de confiance qui refuse une origine inférieure, sans refuser une personne. Qu'arrive-t-il à une proposition venue d'un modèle de langage quand le plancher du point exige une origine de confiance ? Exécutez-le :

```haro
d.TrustFloor("vat", :trusted)
r4 = d.Refine("vat").As(:llm).To("0.25")
? r4[:admitted]
#--> 0
? r4[:why]
#--> trust: posture :llm below the required floor for 'vat'
? d.ValueOf("vat")
#--> 0.30
? d.Refine("vat").As(:trusted).To("0.25")[:admitted]
#--> 1
? d.PostureOf(d.NumberOfSteps())
#--> trusted
```

La proposition du modèle a été refusée : `trust: posture :llm below the required floor for 'vat'`. Le point a gardé `0.30` ! La même proposition, venue d'une origine de confiance, a été admise, et le pas enregistre `trusted`.

Et qui peut tourner quel bouton ? C'est déclaré lui aussi : une permission, et un niveau d'autorité contre un niveau de risque. Prenez un acteur délégué et un bouton du troisième niveau. Exécutez-le :

```haro
gv = new stzRefinableCode(cPrice)
gv.SetGovernedBy(new stzGovernance("release-ops")).SetActor("release-bot")
gv.SetRiskFor("vat", 3).SetAllowRefine("vat").SetAuthorityLevel(:Delegated)
r5 = gv.Refine("vat").To("0.22")
? r5[:admitted]
#--> 0
? r5[:why]
#--> governance: refused: 'release-bot' holds 'delegated' authority (level 2) but 'refine-vat' is risk tier 3 (SHOULD does not cover it)
? gv.ValueOf("vat")
#--> 0.20
gv.SetAuthorityLevel(:Autonomous)
? gv.Refine("vat").To("0.22")[:admitted]
#--> 1
? gv.GovernanceQ().NumberOfDecisions()
#--> 1
```

L'acteur délégué a été refusé, `'release-bot' holds 'delegated' authority (level 2)`, et la valeur est restée `0.20`. La même proposition a été admise une fois l'acteur escaladé ! La décision est enregistrée : `NumberOfDecisions()` a imprimé `1`.

Enfin, un pas peut-il être repris ? La réversibilité fait partie du modèle de données : chaque pas admis garde sa valeur antérieure. Remontez jusqu'à un point de contrôle nommé, remontez jusqu'à zéro, avancez de nouveau :

```haro
t = new stzRefinableCode(cPrice)
t.Refine("vat").To("0.21")
t.Refine("vat").To("0.22")
t.Checkpoint("reviewed")
t.Refine("vat").To("0.28")
? t.ValueOf("vat")
#--> 0.28
t.RevertToCheckpoint("reviewed")
? t.ValueOf("vat")
#--> 0.22
? t.NumberOfSteps()
#--> 2
t.RevertTo(0)
? t.ValueOf("vat")
#--> 0.20
? t.CanRevert()
#--> 0
t.Redo()
? t.ValueOf("vat")
#--> 0.21
```

À zéro, `CanRevert()` a imprimé `0`. Un seul `Redo()`, et la valeur est `0.21`, le premier pas de nouveau.

Voilà la barrière sous la forme que la bibliothèque lui donne. Cinq contrôles, dans l'ordre où le code les exécute. La structure de la proposition, puis les contraintes du point, puis la gouvernance, puis la confiance de l'origine, et enfin la dérivation entre les points. Je les ai exécutés plus haut dans l'ordre du récit, non dans celui du code. L'en-tête du fichier appelle cela une barrière à quatre étapes sur une ligne et à cinq sur une autre. Le code numérote ses contrôles 1, 2, 3, 4 et 4b. Le contrôle de confiance a été ajouté aux quatre le 16 juillet 2026, et le compte de la conception n'a pas été changé. Je rapporte ce qui tourne : cinq contrôles.

Derrière la barrière se tiennent des décisions, et ce que j'ai refusé.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé de gouverner l'intelligence.** Une bonne part de l'approche du terrain pour les agents d'IA est de rendre le modèle plus sûr : alignement, garde-fous, une consigne qui demande confirmation ; cela aussi est une connaissance générale. J'ai refusé ce cadre. La sortie d'un modèle est ce qu'elle est, de quelque modèle que ce soit, et l'intelligence de la génération suivante ne restera pas immobile pour que je la gouverne. Le changement est ce qui reste, et c'est lui qui atteint le monde. La barrière se tient donc là où le changement arrive, et elle ne demande qu'une chose : qu'est-ce qui est proposé, d'où, et le code dit-il que ce point peut changer ainsi.

**J'ai refusé le diff comme unité.** Un diff est un changement de texte. Un raffinement est une proposition typée sur un point déclaré, avec un genre, des bornes et une origine. J'ai gardé le diff comme artefact, et je l'ai refusé comme ce qu'il faut relire.

**J'ai fait porter le verbe à la bibliothèque, et laissé l'environnement ailleurs.** Le raffinement comme verbe de bibliothèque, le point, la barrière, la cascade et le retour en arrière, appartient au socle commun ouvert. L'environnement dans lequel une équipe vit avec lui au jour le jour, les écrans, le mode réel, le livre, est un produit. Il ne déborde pas dans la bibliothèque.

**J'ai imprimé la barrière telle qu'elle est.** J'avais écrit la conception avec quatre étapes, et le code a cinq contrôles. Une page qui citerait ma conception et pas mon code aurait tort, et c'est le code qui tourne.

## 5. Le tribunal

`refinablecode_narrated` prouve le point déclaré, la proposition qui passe, les deux refus qui laissent le source entier (bornes et options), la cascade, le retour en arrière et le fichier sauvegardé. `refine_deepening_narrated` prouve la ligne de temps avec ses points de contrôle et son rétablissement, et le plancher de confiance. `gate_deepening_narrated` prouve le refus d'un point inconnu, la dérivation entre les points avec son annulation, et le refus gouverné avec sa filiation.

Vient ensuite le terrain, et où il mène.

## 6. Le terrain, et où il mène

Le terrain mène en infrastructure, où planifier et appliquer sont la pratique quotidienne de nombreuses équipes et où l'application parle à de vrais fournisseurs ; c'est une connaissance générale, comme dans la section 1. La barrière de Softanza porte sur le changement apporté au code, que le terrain traite par une relecture.

Les outils du terrain mènent en étendue : ils ne sont liés ni à une bibliothèque, ni à un langage, ni à un bouton déclaré. La barrière de Softanza juge ce que le code a déclaré comme point. Un changement apporté à un endroit qui n'a jamais été déclaré n'est pas un raffinement ici ; il est hors de la barrière.

Et sur la confiance, une bonne part de l'approche du terrain est faite pour passer à l'échelle de n'importe quel modèle d'IA. La mienne repose sur une déclaration par point.

Voyons maintenant où la barrière s'arrête.

## 7. La limite

Ce qui est construit : le point de raffinement, la barrière avec ses cinq contrôles, la cascade d'un point et d'une classe, le retour en arrière, le plancher de confiance et le raffinement gouverné. Les gardes de la section 5 les couvrent, avec deux exceptions. La cascade d'une classe n'a pas de garde ici, parce que la garde du graphe de code scanne un chemin vivant de l'arbre de travail de la bibliothèque. Et aucune garde n'affirme les autres points d'une ligne.

Ce qui est conçu, et absent de la bibliothèque par son nom : l'expérience que décrit l'article d'origine. La classe que cet article nomme, `stzPolyCode`, n'est pas dans la bibliothèque à ce commit. Le raffinement en une ligne du document de conception, un point qui s'explique, un plan qui est appliqué, ne sont pas dans la bibliothèque. La cascade du graphe de code et la cascade de la barrière ne sont pas jointes. Et Haro a une barrière dans un spike écrit uniquement dans l'ancien langage hôte, son propre siège de raffinement n'étant pas construit.

Ce qui est construit, et où cela s'arrête : les limites de la barrière telle qu'elle est.

- Elle vérifie les contraintes de trois genres de point, un paramètre, un algorithme et une bibliothèque. Un point d'un autre genre, un bloc de code par exemple, est analysé et passe sans contrôle ; les contrôles pour ces genres sont l'étape suivante.
- Une posture de confiance inconnue se classe comme de confiance : le code lui donne le rang le plus haut. Une proposition venue d'une origine que le code ne connaît pas franchit donc un plancher de confiance.
- Une dérivation est appliquée à titre provisoire et restaurée en cas d'échec. Je dis donc « ne finit jamais modifié », pas « jamais touché ».
- Le fichier sauvegardé contient le source rendu ; l'historique, les postures, la ligne de temps et le rechargement sont absents, et c'est l'étape suivante. La réversibilité vit dans l'objet en cours d'exécution ; la porter dans le fichier est encore à venir. La bibliothèque écrit ce fichier avec le suffixe `.zrfn`, tel que livré. La charte de Haro, ratifiée le 1er octobre 2026, retient le suffixe `.rfn` pour la phrase de raffinement de Haro, et laisse `.zrfn` à l'extraction de la bibliothèque par balises de commentaire, la forme que ce chapitre a exécutée.

## 8. Six portes

**Le programmeur.** Déclarez les endroits qui peuvent changer, et proposez-leur des changements sous forme de propositions typées. Un refus nomme son étape.

**L'analyste.** La règle qui couvre plusieurs points, c'est à vous de la déclarer, et la barrière la juge sur l'état que le changement produirait.

**Le concepteur.** La cascade est ce que vous lisez à la place du diff : pour un point, quelle ligne et quels points sur elle ; pour une classe, quelles classes héritent. Ce sont deux cascades, pas encore une seule.

**Le décideur.** Qui peut tourner quel bouton est une permission et une autorité contre un niveau de risque, et la décision est enregistrée avec son autorité du moment.

**Le formateur.** Reculez d'un pas, remontez jusqu'à un point de contrôle nommé, remontez jusqu'à zéro, avancez de nouveau. Un apprenant peut essayer sans crainte parce que chaque pas garde sa valeur antérieure.

**L'agent.** Vous pouvez proposer. Votre origine est sur la proposition, et un point peut fixer un plancher que votre origine ne franchit pas.

## 9. Exercice

Prenez deux réglages d'un de vos programmes : un taux et un plafond, par exemple, avec une règle selon laquelle le taux doit rester sous le plafond. Déclarez-les comme des points, avec des bornes, et déclarez la règle qui les couvre. Avant de rien exécuter, écrivez sous chaque proposition si elle est admise et, sinon, à quelle étape elle est refusée. Proposez un changement du taux au-dessus du plafond, et un autre depuis une origine que vous déclarez comme un modèle d'IA, contre un plancher que vous fixez. Puis remontez jusqu'à zéro et avancez d'un pas.

Exécutez-le. Si vous vous êtes trompé sur l'étape, vous avez trouvé un endroit où votre propre barrière est en désaccord avec votre propre attente.

Je vous laisse celui-ci. La section 7 dit ce que la barrière fait d'une origine que le code ne connaît pas, et le bloc de confiance de la section 3 est celui à exécuter. Ses premières lignes sont ci-dessous, et `d` est l'objet de ce bloc, alors exécutez d'abord la section 3 ; changez une seule chose, et remplacez `:llm` par un nom de votre choix, que le code n'a jamais appris.

```haro exercise
d.TrustFloor("vat", :trusted)
r4 = d.Refine("vat").As(:yourorigin).To("0.25")
? r4[:admitted]
```

Exécutez-le, et lisez ce que fait la barrière en regard de ce que dit la section 7. Je ne vous dirai pas si la barrière a raison. Quand vous aurez tranché, vous saurez ce que le plancher de confiance fait d'une origine qu'il n'a jamais rencontrée.

Le chapitre suivant énonce une loi : un langage est déclaré et fermé, et ce qui le parle, une personne ou un modèle, est jugé par lui. Ici, la chose jugée était un changement ; là, c'est ce qui parle.
