---
id: the-guards-and-fixtures-cited
appendix: E
number: 105
title: Les gardes et les fixtures citées, par chapitre
status: draft
generated: guards
---

Une garde est un fichier de l'arbre de tests de la bibliothèque qui contient des assertions. Un chapitre qui dit « ceci est prouvé » nomme les gardes qui le prouvent, dans le préambule de sa source, et la construction lit chacune : elle trouve le fichier dans la bibliothèque au commit sur lequel le livre tourne, et compte les assertions qu'il contient. Une garde qui n'y est pas fait échouer la construction.

Cette annexe est cette lecture, chapitre par chapitre. Aucun chiffre n'y est tapé à la main. Elle est régénérée à chaque construction, si bien que les chiffres sont toujours ceux que la dernière construction a lus.

Deux choses à garder en tête. Un chiffre est le nombre d'appels d'assertion que le fichier contient, comptés dans son texte ; ce n'est pas une exécution. La plupart de ces gardes ne sont pas exécutées par le livre, parce qu'elles écrivent des fichiers, ouvrent des ports ou lancent des processus. Les quelques-unes que j'ai exécutées moi-même sont nommées dans les chapitres qui s'appuient sur elles, avec la date. Et les seules fixtures que le livre cite sont celles que lisent les gardes et les blocs : le dossier de cours du programme d'éducation de la bibliothèque, et les dossiers de données que ses gardes nomment. Les blocs du livre sont eux-mêmes les autres fixtures : chacun s'exécute dans la bibliothèque au commit nommé sous le titre de chaque chapitre.
