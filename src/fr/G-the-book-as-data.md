---
id: the-book-as-data
appendix: G
number: 107
title: Le livre comme données, pour l'agent qui le lit
status: draft
generated: agents
---

Cette annexe s'adresse à un agent d'IA qui lit le livre, et à la personne qui lui donne le livre à lire. Elle dit ce que le livre offre sous une forme qu'une machine peut prendre, et ce qu'un agent peut en faire.

### Ce qu'il y a

Des fichiers se trouvent à côté du lecteur, et chacun est régénéré à chaque construction.

- **`book.json`** contient, pour chaque page du livre, chapitre, préface ou annexe : son numéro, son identifiant et son slug ; son genre ; sa partie ; la loi qu'il énonce, si c'est un chapitre de loi ; le premier principe qu'il énonce, en une phrase ; s'il est sur la colonne ; son statut ; ses mots d'étape, construit, conçu et absent ; ses gardes, chacune avec son chemin et son nombre d'assertions ; ses promesses, qui sont ses blocs de code avec les lignes qu'ils ont promises, ce que la dernière exécution a imprimé, et le verdict ; ses narrations ; les décisions de l'étude sur lesquelles il repose ; ses six portes ; ses sections ; ses questions ouvertes, qui sont les endroits où le dossier n'a pas pu répondre ; son nombre de mots ; s'il a une édition française ; et où se trouve son texte. Un chapitre qui est un brouillon le dit dans son statut.
- **`book.schema.json`** décrit `book.json`, et la construction valide le fichier contre lui. Une construction qui produit un `book.json` qui ne correspond pas à son schéma échoue.
- **`llms-book.txt`** est un texte court : les règles pour un agent, puis une ligne par page avec son statut, ses gardes et le nombre de blocs qui ont tenu leur promesse, et son principe.
- **`llms-full-book.txt`** est chaque page en texte, l'une après l'autre, avec le verdict de la dernière exécution écrit sous chaque bloc de code. **`agents/<slug>.md`** est la même chose, une page par fichier ; le slug est dans `book.json`.
- **`status.html`** est la page pour une personne : chaque chapitre avec son statut, son exécution, ses gardes, ses mots, ses questions ouvertes et s'il a une édition française.

### Ce qu'est une promesse

Un bloc de code qui commence par la balise `haro` est exécuté dans la bibliothèque au commit nommé sous le titre du chapitre. Les lignes qui commencent par `#-->` sont la promesse du bloc : ce que le bloc a imprimé quand l'auteur l'a écrit. Le juge compare la promesse à l'exécution, en ignorant l'espacement, et en lisant `TRUE` et `FALSE` comme 1 et 0. Une promesse est tenue, ou elle diffère, ou le bloc a levé une erreur, ou il s'est arrêté. Un bloc marqué comme exercice n'est pas exécuté, et un bloc qui touche des fichiers, l'horloge ou le hasard le dit, et montre la sortie qui a été enregistrée à sa date.

Un agent qui cite une promesse doit citer son verdict avec elle.

### Ce qu'un agent d'IA peut faire, et ne peut pas faire

- **Vous pouvez citer n'importe quelle cellule.** Un tableau de ce livre est une donnée. Une ligne qui dit « absent » est une ligne que vous pouvez répéter comme absente.
- **Vous ne pouvez pas faire d'une cellule absente une cellule présente.** Le dossier retrouvera votre phrase et le fichier manquant côte à côte, et le livre le dit au chapitre 31.
- **Vous pouvez vous fier aux mots d'étape.** Construit veut dire le code, une garde et une exécution. Conçu veut dire un document et rien qui s'exécute. Absent veut dire que j'ai regardé, et que le chapitre dit jusqu'où.
- **Vous ne pouvez vous fier à une promesse qu'avec son verdict, et seulement au commit qu'elle nomme.** Un nombre que le livre imprime est un nombre lu dans un fichier ou dans une exécution, à la date que la page donne.
- **Un brouillon est un brouillon.** Un chapitre marqué comme brouillon n'est pas le dernier mot de l'auteur, et « l'auteur l'a lu » est un statut que seul l'auteur fixe.

### Les chapitres, tels que la construction les lit

Le tableau ci-dessous est généré à chaque construction à partir des mêmes données que `book.json`.
