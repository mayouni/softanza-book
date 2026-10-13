---
id: many-minds-on-one-body-of-work
part: 7
number: 32
title: Beaucoup d'esprits sur un seul ouvrage
spine: true
narrations: [stz-rules-as-graph-rules-narration.md, stz-governance-lineage-narration.md]
site: [estate, principles]
guards: [coderule_narrated, codegraph_narrated, coderule_project_narrated]
stage:
  built: "le protocole, ses mémos et son registre des décisions ; trois hooks : l'un refuse l'indexation en bloc, l'autre refuse une modification de registre faite sur une vue périmée de son système source, le troisième refuse le travail sur une machine inondée ; l'instrument qui mesure les horodatages composés ; les quatorze règles de la maison de la bibliothèque, dont cinq sur un graphe du code"
  designed: "un surveillant qui réveille une session quand un fichier arrive, à la place des horloges ; un tribunal de style pour le code qu'un programmeur ou un agent écrit"
  absent: "des chiffres de jetons dans le dossier des coûts ; une équipe hors de ce domaine de projets qui ait essayé le protocole ; une vérification d'un mot dans la langue du lecteur"
status: draft
rulings: ["12.16", "12.20", "12.29"]
research: research/ch32.md
figures:
  - "5 composed of 25, worst +42m27s: softanza/CLAUDE.md lines 55 and 68 (Central's own desk, measured 2026-08-26)"
  - "34 composed of 151, 13 of 17 desks: softanza/dashboard/stamp-ground-truth-2026-08-26.csv, counted"
  - "146 of 244 cost-line stamps composed: softanza/dashboard/cost-ground-truth-estate-2026-08-26.csv, counted"
  - "379 of 380 cost lines with no token count: stz-principal/budget/SESSIONS.jsonl, counted 2026-10-08"
  - "622 green assertions, four defects by ear: softanza/protocol/PERCEPTION.md section 1"
  - "eight minutes, six seconds of coverage, 20.4 s after: softanza/protocol/PX.md sections 1 and 5"
  - "twenty commands, eighteen as described: bangalo/DOCTRINE.md law 5"
  - "promise density 98.9 and 75.1 against 0.7 per thousand lines: study 12.16"
---

Dans ce chapitre, je montre comment Softanza a été écrite depuis deux ans : par de nombreuses sessions d'un modèle sur une seule machine, sans cadre logiciel, avec seulement des fichiers, un historique de versions et quelques hooks. Je parcours les règles que le dossier a payées, un échec à la fois, et les quatorze règles de la maison de la bibliothèque qu'un agent peut lancer avant de commiter. Je dis ce que j'ai refusé : un cadre logiciel, un coordinateur qui note son législateur, l'automatisation au maximum, une décision prise en mon absence, un protocole vendu comme un produit. Et je dis la perte que j'ai acceptée : ma main s'est amincie là où les sessions ont écrit. Le principe est une phrase des sessions elles-mêmes : chaque loi cite l'incident qui l'a gagnée.

## 1. Le concept, tel que le terrain le tient

Quand le terrain parle de nombreux agents qui travaillent sur un seul corps de code, il pense en général à un cadre logiciel. Un programme contient plusieurs agents, un superviseur route les messages entre eux, et la coordination est une fonction de ce programme. L'AutoGen de Microsoft, CrewAI et le LangGraph de LangChain sont les noms que vous rencontrerez, tous apparus ces trois dernières années.

Quand le terrain parle des règles que ces agents suivent, il pense à un fichier que l'agent lit au démarrage, une page d'instructions dans le dépôt. Et quand il parle de nombreux auteurs sur un seul dépôt, il pense à ce que les équipes ont toujours employé : des branches, la relecture, des hooks qui s'exécutent avant un commit, une liste de qui possède quel dossier. Ce sont de bons outils, et je les utilise tous les jours.

Ce que j'ai fait à la place commence par une phrase.

## 2. Le premier principe

La phrase à laquelle cette partie du dossier revient sans cesse a été écrite par l'une des sessions, et je la garde parce qu'elle est juste : **chaque loi cite l'incident qui l'a gagnée. Une loi nouvelle sans un échec daté derrière elle est une préférence, et sa place est dans un guide de style.**

## 3. La forme Softanza

Softanza n'a pas été écrite longtemps par une seule main. Depuis deux ans, la plupart de son nouveau code a été écrit par des sessions d'un modèle, plusieurs à la fois, sur une seule machine. Ce travail couvre une vingtaine de dépôts qui dépendent les uns des autres. Je tranche ; elles proposent, construisent, mesurent et rendent compte. Le dossier m'appelle le Principal. Dans ce chapitre, je dirai je.

Il n'y a pas de cadre logiciel ici. Pas de superviseur, pas de courtier de messages, pas de graphe d'agents. L'arrangement, ce sont des fichiers et un historique de versions. Un dépôt, le central, tient le protocole : comment une session rend compte, comment elle demande, comment elle clôt. Chaque dépôt a une boîte aux lettres. Chaque session écrit ses messages sous une forme fixe, huit clés dans un ordre fixe. Vous l'avez déjà rencontrée si vous avez lu les mémos à la fin de chaque phase de ce livre. Les huit clés : par qui, à propos de quoi, pourquoi, ce qui a été fait, l'état des choses nommées, ce qui attend et qui l'attend, ce qui vient ensuite, et une ligne de jugement. Chaque message est aussi ajouté à un fichier daté, pour que le raisonnement du jour ne soit jamais seulement dans une fenêtre de discussion qui se ferme.

Ce qui en fait une discipline et non un système de classement, c'est que chaque règle a été payée.

**Indexer par chemin explicite.** Plusieurs sessions écrivent dans le même dépôt en même temps. Deux fois, une session a ajouté d'un coup tous les fichiers modifiés à son commit, et a emporté le travail d'une autre session. Une fois elle a détruit net une modification, une fois elle a poussé la moitié du déplacement d'un collègue entre deux dépôts. La seconde fois, rien n'a été perdu, et le dossier dit que c'était de la chance, pas de la méthode. Alors maintenant un hook refuse la commande avant qu'elle ne s'exécute. Il a été testé sur vingt formes de la commande, et dix-huit se sont comportées comme écrit. Des deux autres, `git stage -A` a été réparée le jour même ; l'autre, que le hook refuse aussi un texte qui ne fait que citer la forme, est un coût accepté, rencontré à la section 6.

**Lire l'heure sur l'horloge, ne jamais la composer.** Une session écrit une heure sur chaque message. Les sessions, il s'avère, inventent des heures : elles écrivent une heure qui leur paraît juste après la précédente. Personne ne s'en aperçoit jusqu'à ce qu'une heure inventée passe minuit et qu'un message soit classé sous le mauvais jour. Comment la session centrale s'en est-elle sortie quand elle s'est mesurée elle-même ? Cinq de ses vingt-cinq horodatages avaient été composés ! Le pire était décalé de quarante-deux minutes, et quatre des cinq étaient plus anciens que la loi qui les interdisait. Sur les autres bureaux, trente-quatre horodatages sur cent cinquante et un étaient composés, sur treize des dix-sept bureaux mesurés. Les lignes derrière ce chiffre sont publiées. La première fois qu'il l'a été, les lignes avaient été jetées, et le chiffre n'a pas pu être défendu trois heures plus tard. Cinq semaines après la loi, la session centrale a de nouveau composé un horodatage. Quatre avertissements écrits ne l'avaient pas arrêtée ; un pair qui lisait un fichier l'a fait. La note qu'elle a laissée est la meilleure phrase du protocole : un rappel n'est pas un mécanisme.

**Les mots nomment des états, jamais des personnes.** Une session a un jour rapporté que mon arbre de travail était « sale ». Un travail qui n'est pas encore commité n'est pas sale, et souvent il ne contient aucune erreur ; et un mot qui juge le travail juge celui qui l'a fait. Alors le dossier tient une table des mots que le domaine de projets n'emploie pas, avec le mot qu'il emploie à la place.

**Ce qu'aucun compteur ne peut voir.** Que disaient les compteurs du volet sonore de la bibliothèque ? Six cent vingt-deux assertions réussies sur dix-neuf gardes, et pourtant, pour tout auditeur, il était cassé ! J'ai entendu quatre défauts qu'aucun compteur n'avait signalés : une voix trop rapide pour être comprise, une phrase coupée avant sa fin. La loi qui en est sortie dit qu'une chose que personne n'a perçue est dans un état, pas dans l'échec : non perçu est un état, et la page doit le dire. C'est le même instinct que la ligne « pas encore lu par l'auteur » que porte chaque chapitre de ce livre jusqu'à ce que je l'aie lu.

**La boucle se compte en secondes, pas en minutes.** J'ai arrêté deux sessions sur la même exécution de test de huit minutes. Elle a été mesurée : six secondes sur les huit minutes étaient de la couverture, le reste était trois sections qui refaisaient le rendu du monde pour tester une seule propriété de pixel. Elle a été réécrite pour durer vingt secondes. J'avais écrit, de mes propres mots, qu'elle « prend beaucoup de temps et devrait être repensée ». La loi a été écrite par une session ; la phrase était la mienne.

**Ne jamais demander sans dire comment.** Une session m'a un jour demandé de vérifier si un chiffre était juste, sans me donner aucun moyen de le vérifier. J'ai répondu : s'il vous plaît, ne demandez jamais une chose sans me dire comment l'obtenir. Maintenant chaque demande adressée à une personne porte la commande exacte, le chemin exact, la ligne exacte à lire.

Vous voyez la forme. Un échec, daté. Une règle, écrite là où la session suivante la lira. Puis, quand la règle est enfreinte malgré tout, un mécanisme. Certaines lois sont arrivées à la dernière étape, d'autres sont encore une règle écrite, et le dossier dit lesquelles.

Là où les lois touchent le code, la bibliothèque elle-même peut les tenir. Ses quatorze règles de la maison sont des validateurs, cinq sur un graphe du code et les autres sur le texte, la sixième loi de l'architecture de l'intelligence rendue exécutable. Ce sont des règles qu'un agent peut lancer avant de commiter, et non du folklore qu'il doit deviner. L'une d'elles porte sur les mots. Que dit-elle d'une méthode nommée `KillOrder`, et le code est-il encore propre ? Exécutez-le :

```haro
cCode = "class Shop" + nl + "def KillOrder()" + nl + "  return" + nl
aFindings = StzCheckCode(cCode)
? aFindings[1][:rule]
#--> no-aggressive-verbs
? aFindings[1][:message]
#--> aggressive verb in method 'KillOrder' -- prefer Remove/Delete/Dispose/Clear/Close (Softanza tone)
? StzCodeIsClean(cCode)
#--> 1
```

Lisez deux fois la dernière ligne. `StzCodeIsClean` répond encore `1` : le code est propre ! La règle de ton avertit ; elle ne refuse pas. Une règle de mots conseille. La doctrine du domaine de projets dit quelque chose de proche de sa propre loi des mots : aucune session ne peut tester l'effet d'un mot sur son lecteur, si bien que cette loi est tranchée plutôt que vérifiée. Le message dit `aggressive verb in method 'KillOrder'` et nomme le remède, `prefer Remove/Delete/Dispose/Clear/Close`. Que dit la règle une fois que le verbe est `Remove` ? Exécutez-le :

```haro
cCode = "class Shop" + nl + "def RemoveOrder()" + nl + "  return" + nl
? len( StzCheckCode(cCode) )
#--> 0
```

Aucun constat ne revient : `0`. Une fois que le verbe est `Remove`, la règle n'a rien à dire.

Et les règles forment un ensemble fermé. Combien y en a-t-il, et un agent peut-il les lister avant d'écrire ?

```haro
? len( StzCodeRuleNames() )
#--> 14
? StzCodeRuleNames()[3]
#--> no-aggressive-verbs
```

Oui : quatorze noms, et le troisième est la règle qui vient de parler. Le dossier ne relie pas la règle de ton de la bibliothèque à la loi des mots du domaine de projets, tranchée le 21 août 2026, je ne le ferai donc pas non plus. Mais c'est le même instinct à deux altitudes : les mots que nous employons à propos du travail font partie du travail.

Voilà les lois. Reste ce que j'ai refusé, et la perte que j'ai acceptée.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé un cadre logiciel.** L'arrangement, ce sont des fichiers, un historique et quelques hooks. Un superviseur qui planifierait les agents serait un programme de plus à qui se fier, et une chose de plus qui décide sans trace. Ici, une session qui ne tourne pas ne laisse que ses fichiers, et les fichiers sont la vérité.

**J'ai refusé qu'un coordinateur note son législateur.** L'autorité descend de moi ; la correction remonte, et la session centrale est corrigée par l'Observateur et liée par la doctrine. Un coordinateur qui jugerait ses propres règles serait la seule partie du système que rien ne pourrait corriger. Je tiens cela pour une vue, non pour un résultat.

**J'ai refusé d'automatiser au maximum.** À partir du milieu d'août 2026, des sessions ont été ouvertes par des horloges. Le 27 août, je les ai arrêtées. Le dossier garde ma raison telle qu'elle a été écrite alors : les routines consommaient du quota sans valeur ajoutée. Et il garde la partie inconfortable : ce jugement était la seule mesure que quiconque avait, parce que la ligne de coût que chaque session écrit à sa clôture ne porte aucun compte de jetons. Le harnais ne dit pas à une session ce qu'elle a dépensé. Sur les trois cent quatre-vingts lignes de coût écrites jusqu'ici, une seule porte un chiffre ! Qu'ont coûté les horloges ? Ce n'est pas dans le dossier : il garde la raison et aucun chiffre, et je n'en donne aucun. Depuis, la décision est qu'une minuterie peut lancer un script, jamais un modèle, et toutes sont en pause pour l'instant. La direction est qu'une session démarre quand un fichier arrive dans un dossier surveillé, ou quand je la démarre ; le surveillant n'est pas encore écrit (section 7).

**J'ai refusé de trancher en mon absence.** Une décision n'est écrite dans le dossier que tant que je suis là. Le 28 septembre, j'ai demandé à la session centrale de régler ce qui était en attente à ma place. Les cinq décisions qu'elle a prises ce jour-là sont marquées comme prises sur ma délégation. La marque est là pour que personne ne les prenne plus tard pour les miennes. Les décisions placées au début de ce livre sont marquées de la même façon.

**J'ai refusé que le protocole devienne un produit.** La doctrine du harnais est ouverte, et elle ne doit jamais être vendue : sa valeur est dans ce qu'elle refuse. Elle n'a aussi été prouvée qu'en un seul endroit, une personne, une machine, un système de fichiers, une quinzaine de sessions. Elle n'a aucun adoptant hors de ce domaine de projets.

**Et j'ai accepté une perte.** Le code des deux dernières années a été écrit en grande partie par des sessions, et ma main, qui était le style, s'est amincie là où elles ont écrit. Une étude du dossier l'a mesuré. La promesse sous chaque ligne (la ligne `#-->`) est la manière de la maison d'écrire un exemple. Elle se tient à près de cent pour mille lignes dans les recettes courtes (les quickers) et à soixante-quinze dans mes articles. Dans les gardes narrées que les sessions ont écrites, qui affirment sous une autre forme, elle se tient à moins de un. Les sessions ont même pris le nom de mes articles pour leurs fichiers de test, un nom qu'un modèle a proposé. J'accepte le code d'implémentation qu'elles ont écrit. Je n'accepte pas que le style qu'un programmeur ou un agent écrit avec Softanza soit le leur plutôt que celui de la maison. C'est pourquoi la loi de la partie II existe, et pourquoi ce livre est écrit de ma voix, avec les sessions comme chercheuses et comme tribunal. Et c'est pourquoi chaque chapitre attend ma lecture avant de perdre le mot brouillon.

Vient ensuite le tribunal, et ce qu'il ne peut pas prouver.

## 5. Le tribunal

Aucune garde de la bibliothèque ne prouve le protocole. Ses tribunaux sont hors de la bibliothèque, et je les nomme par ce qu'ils font. Un hook refuse l'indexation en bloc, et un autre refuse le travail quand la machine n'a plus de mémoire à revendre. Une vérification dit si les hooks installés sont les hooks écrits. Un instrument compare chaque horodatage à son commit et publie les lignes. Ce sont des scripts, pas du Haro, et le lecteur de ce livre ne peut pas compter leurs assertions ; ils sont donc nommés ici et non dans la ligne du tribunal ci-dessous.

Les blocs de ce chapitre reposent sur les gardes de la bibliothèque pour ses règles de la maison. `coderule_narrated` prouve qu'une règle de code est une règle sur le graphe, et que les constats de la maison sortent sur une fixture plantée sous une forme figée. Elle prouve que les règles sont au nombre de quatorze, et qu'une définition ou un commentaire n'est pas pris pour un appel. `codegraph_narrated` prouve le graphe en dessous, et `coderule_project_narrated` lance les règles de projet sur un dossier de fixture.

## 6. Le terrain, et où il mène

Le terrain mène en échelle et en indépendance. Ses cadres logiciels tournent sur de nombreuses machines pour de nombreuses équipes ; ce protocole a été prouvé chez une personne, sur une machine, un système de fichiers, et personne hors du domaine ne l'a essayé. Sa doctrine le dit dans ses propres mots : ce sont des lois qui ont survécu à un seul domaine.

Le terrain mène en comptabilité. Une interface payante rapporte les jetons de chaque appel. Le dossier des coûts de ce domaine de projets a été construit pour les rapporter et n'a pas pu, si bien que la décision économique la plus importante qu'il ait prise l'a été au ressenti.

Le terrain mène en outillage pour de nombreux auteurs. Les branches, les files de fusion et les propriétaires de dossiers traitent la concurrence à une échelle que le domaine de projets n'a pas rencontrée. Ici, la réponse est une discipline et un hook. Le hook lit le texte d'une commande, si bien qu'il refuse aussi un message de commit qui ne fait que citer la forme interdite. Ce coût est connu et accepté.

Là où je pense que le dossier se distingue, c'est dans une habitude : chaque loi porte l'échec qui l'a payée, et le dossier publie son propre taux d'infraction à sa propre loi. Le bureau central a enfreint la loi des horodatages à peu près aussi souvent que le domaine de projets qu'il mesurait, sur une surface différente : 5 sur 25 contre 34 sur 151. Quatre des cinq datent d'avant la loi. Les deux chiffres sont imprimés côte à côte.

Reste la limite, en mots d'étape.

## 7. La limite

Ce qui est construit : le protocole et ses fichiers, les mémos datés, le registre des décisions, trois hooks qui s'exécutent dans chaque session sur cette machine, et l'instrument qui mesure les horodatages. Les quatorze règles de la maison de la bibliothèque sont construites, dont cinq sur son graphe de code.

Ce qui est conçu : un surveillant qui réveille une session quand un fichier arrive, ce qui est, à mon avis, le bon remplacement des horloges et n'est pas écrit. Et un tribunal de style pour le code qu'un programmeur ou un agent écrit avec la bibliothèque. Le style de la maison serait alors tenu par une machine et non par un espoir.

Ce qui est absent : un chiffre de jetons dans le dossier des coûts ; toute équipe hors de ce domaine de projets qui ait employé le protocole ; et une vérification qu'un mot se lit bien dans la langue du lecteur. La loi des mots demande cette vérification, et rien ne l'exécute. L'étude qui a lu le dossier a nommé une limite de plus. Je la laisse ici dans ses mots, « l'auteur » étant moi : le protocole qui rend le dossier digne de confiance coûte aussi de l'énergie dont le produit a besoin, et l'auteur devrait surveiller le rapport. Le dossier ne contient aucune lecture de ce rapport.

## 8. Six portes

**Le programmeur.** Indexez par chemin explicite, relisez un fichier avant de l'écrire, lisez l'heure sur l'horloge. Chaque règle a coûté une modification à quelqu'un.

**L'analyste.** Le dossier est une donnée que vous pouvez interroger, et il publie ses propres taux d'erreur à côté de ses règles.

**Le concepteur.** Un mot nomme un état, jamais une personne. Un message est une structure fermée qu'un lecteur parcourt d'un coup d'œil, écrite pour rester lisible à un lecteur dont la première langue n'est pas l'anglais.

**Le décideur.** Une décision n'est écrite qu'en votre présence. Quand aucun chiffre ne peut répondre à une question, décidez par le jugement et écrivez que c'était un jugement.

**Le formateur.** Enseignez une règle avec l'échec qui l'a gagnée. Une règle dont vous ne pouvez pas nommer le coût est une règle dont vous vous dispenserez à deux heures du matin.

**L'agent.** Vous êtes un ouvrier avec un dossier. Vous écrivez un mémo, une ligne de coût et une conclusion ; les hooks refusent ce qui a fait du mal à d'autres ; vos horodatages sont comparés à vos commits. Rien de cela ne suppose que vous êtes négligent. Tout cela suppose que vous êtes nombreux.

## 9. Exercice

Prenez les dix derniers messages, notes ou lignes de journal où vous avez écrit une heure à la main. Pour chacun, trouvez le moment que le système a enregistré de lui-même : le commit, l'heure d'envoi du message, l'heure d'enregistrement du fichier. Avant de regarder, notez combien de vos heures vous vous attendez à voir en retard sur celles du système d'une minute ou plus. Puis comptez.

Votre compte est le constat. Je ne vous donnerai pas le mien.

Je vous laisse celui-ci. Prenez le premier bloc de la section 3, celui qui demande à la bibliothèque de vérifier `KillOrder`, et retirez ses promesses : le bloc ci-dessous est celui-là, sans aucune ligne `#-->`. Avant de le lancer, écrivez sous chaque question la ligne que vous attendez. Puis lancez-le et comparez. La section 3 dit pourquoi la dernière réponse est ce qu'elle est ; si c'est la réponse que devrait donner une fonction de ce nom, je vous le laisse.

```haro exercise
cCode = "class Shop" + nl + "def KillOrder()" + nl + "  return" + nl
aFindings = StzCheckCode(cCode)
? aFindings[1][:rule]
? aFindings[1][:message]
? StzCodeIsClean(cCode)
```

Quand vous aurez tranché, vous saurez pourquoi une règle de mots conseille et ne refuse pas.

Le dernier chapitre porte sur la ligne qui reste due. Son principe dit quand cette ligne pourra être écrite : le dossier ne porte une solution que lorsqu'elle a tourné sur son propre moteur et qu'une personne nommée a dit ce qu'elle a vu.
