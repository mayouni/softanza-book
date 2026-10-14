---
id: the-projects-history
appendix: H
number: 108
title: "L'histoire du projet : de Ring à Haro"
status: draft
---

C'est l'unique page du livre dont la prose nomme le langage dont Softanza est issu ; les noms propres de la bibliothèque, dans le code, le portent encore, jusqu'à ce que la bibliothèque en soit retirée. Les chapitres ne le font pas, parce que la plateforme va là où ce langage ne peut pas la suivre. L'histoire a sa place ici, racontée une seule fois, avec gratitude.

## D'où il vient

Softanza est né sur Ring, un petit langage de script. J'ai écrit sa bibliothèque en Ring pendant des années. J'ai enseigné Ring, je l'ai promu sur le terrain, et j'ai passé neuf mois à écrire son livre, *Beginning Ring Programming*, publié par Apress en 2020. En 2021, j'ai décrit la bibliothèque à la communauté Ring pour la première fois. En 2022, la première présentation de Softanza l'appelait « le meilleur ami des programmeurs Ring existants ». La simplicité de Ring et son expressivité multiparadigme sont deux choses que Softanza garde, parce qu'elles n'ont jamais été le problème.

## Ce que des projets réels ont appris

Trois choses, et ce sont les raisons du passage à Haro.

**Les limites sont apparues.** Des projets réels ont montré que Ring n'était pas adapté aux défis des applications modernes. Les limites sont en trois endroits : la performance, le typage fort et la facilité de construction. Les propres sessions du projet les ont mesurées, et le dossier garde les lignes avec leurs reproductions. Le chapitre 27 imprime la mesure de la première : le moteur à moins de 2x d'un pair rapide du terrain sur chaque ligne, ce que l'ancien runtime n'a jamais été. Sa mémoire se tient à côté de celle de l'ancien runtime.

**La direction ne pouvait pas être influencée.** La direction d'un langage appartient à son propriétaire, et nous ne pouvions pas influencer celle du nôtre. Le projet a construit Ring++ pour résoudre ces trois difficultés sans quitter Ring, et il n'a pas reçu l'accueil que nous espérions.

**La gouvernance est une propriété de conception.** Une dépendance dont on ne peut pas influencer la direction, et dont on ne peut pas encadrer le comportement, échoue à la diligence que demandent les domaines régulés. La réponse de Softanza n'est pas l'indépendance pour elle-même, mais l'indépendance pour ses utilisateurs : un moteur écrit en Zig sans dépendance tierce, une machine virtuelle et un compilateur à nous, et des engagements que le projet fait déjà tourner comme des tests. Un noyau ouvert. Des chartes ratifiées en public. Chaque décision dans un registre daté. Chaque affirmation liée à sa preuve.

## Le chemin

Ring est le point de départ. Ring++ est le pont, en construction. Haro est la destination. Sous la bibliothèque se tient le moteur en Zig, quel que soit celui des trois qui est au-dessus : chaque fonctionnalité est implémentée une seule fois, dans le moteur, et le chapitre 27 dit la règle.

Aujourd'hui la bibliothèque tourne encore sur son premier runtime, version 1.27, et les blocs de ce livre tournent dessus. Haro emploie la syntaxe de ce premier runtime comme sa première facette, si bien que tout le code déjà écrit continue de fonctionner. Les gardes de la bibliothèque sont l'épreuve de cette promesse : Haro doit les faire tourner. Le chapitre 27 dit où en est le moteur, chiffres à l'appui.

## Remerciements

Softanza dit merci au langage dont il est issu, et va là où la souveraineté de ses utilisateurs l'exige.
