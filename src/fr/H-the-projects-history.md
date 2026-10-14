---
id: the-projects-history
appendix: H
number: 108
title: "L'histoire du projet : de Ring à Haro"
status: draft
---

C'est l'unique page du livre qui nomme le langage dont Softanza est issu. Les chapitres ne le font pas, parce que la plateforme va là où ce langage ne peut pas la suivre. L'histoire a sa place ici, racontée une seule fois, avec gratitude.

## D'où il vient

Softanza est né sur Ring, un petit langage de script. J'ai écrit sa bibliothèque en Ring pendant des années. J'ai enseigné Ring, je l'ai promu sur le terrain, et j'ai passé neuf mois à écrire son livre, *Beginning Ring Programming*, publié par Apress en 2020. En 2021, j'ai décrit la bibliothèque à la communauté Ring pour la première fois. En 2022, la première présentation de Softanza l'appelait « le meilleur ami des programmeurs Ring existants ». La simplicité de Ring et son expressivité multiparadigme sont deux choses que Softanza garde, parce qu'elles n'ont jamais été le problème.

## Ce que des projets réels ont appris

Trois choses, et ce sont les raisons.

**Les limites sont apparues.** Des projets réels ont montré que Ring n'était pas adapté aux défis des applications modernes. Les limites sont en trois endroits : la performance, le typage fort et la facilité de construction. Les propres sessions du projet les ont mesurées.

**La direction ne pouvait pas être influencée.** La direction d'un langage appartient à son propriétaire, et la nôtre ne pouvait pas être influencée. Le projet a construit Ring++ pour résoudre ces trois difficultés sans quitter Ring, et il n'a pas reçu l'accueil que nous espérions.

**La gouvernance est une propriété de conception.** Une dépendance dont on ne peut pas influencer la direction, et dont on ne peut pas encadrer le comportement, échoue à la diligence que demandent les domaines régulés. La réponse de Softanza n'est pas l'indépendance pour elle-même, mais l'indépendance pour ses utilisateurs : un moteur écrit en Zig sans dépendance tierce, une machine virtuelle et un compilateur à nous, et des engagements que le projet fait déjà tourner comme des tests. Un noyau ouvert. Des chartes ratifiées en public. Chaque décision dans un registre daté. Chaque affirmation liée à sa preuve.

## Le chemin

Ring est le point de départ. Ring++ est le pont, en construction. Haro est la destination. Sous les trois se tient le moteur en Zig, qui fait le calcul une seule fois.

Aujourd'hui la bibliothèque tourne encore sur son premier runtime, version 1.27, et les blocs de ce livre tournent dessus. Haro emploie la syntaxe de ce premier runtime comme sa première facette, si bien que tout le code déjà écrit continue de fonctionner. Les tests narrés de la bibliothèque sont l'épreuve de cette promesse : Haro doit les faire tourner. Le chapitre 27 dit où en est le moteur, chiffres à l'appui.

## Remerciements

Softanza dit merci au langage dont il est issu, et va là où la souveraineté de ses utilisateurs l'exige.
