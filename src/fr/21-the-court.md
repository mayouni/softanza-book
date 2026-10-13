---
id: the-court
part: 4
number: 21
title: "Le tribunal : promesses, perception, sécurité et performance"
spine: false
narrations: [stz-security-ledger-narration.md, stz-governance-lineage-narration.md, stz-perf-governed-loop-narration.md, stz-honest-stopwatch-narration.md, stz-security-drill-narration.md]
site: [security, offering]
guards: [testoor_promises_narrated, threat_model_narrated, security_ledger_narrated, secretstore_narrated, secret_narrated, stopwatch_narrated, tracing_tail_narrated, governed_loop_narrated, security_sentinel_narrated]
stage:
  built: "la promesse jugée comme une affirmation sur un arrêt ; le volet de sécurité avec son registre, sa sentinelle, son exercice, sa réponse et ses secrets, et sa table de garanties liées à des gardes ; le volet de performance avec son instrument et sa boucle gouvernée ; la loi de la perception, adoptée"
  designed: "les routes, l'horloge et la météo, et la perception pour le lanceur de promesses ; le volet des extensions ; la négociation autour d'un plan rejeté"
  absent: "un verdict humain sur une image de la galerie ; sept des huit traditions musicales entendues par une personne qui en vient ; un vrai coffre et un vrai bac à sable comme preuves ; un magasin de séries temporelles"
status: draft
rulings: ["12.13", "12.16", "12.19", "12.20", "12.22", "12.26", "12.29"]
research: research/ch21.md
---

Dans ce chapitre, je reprends le tribunal du chapitre 5, qui juge quiconque a écrit le code. J'en montre quatre, chacun par quelque chose qu'il refuse : les promesses, la perception, la sécurité et la performance. Je fais parcourir au voyageur un fichier de trois promesses, et je demande au dossier combien des huit traditions musicales une personne a entendues. Je modifie un registre scellé et je lis quelle entrée la chaîne nomme, et je laisse un modèle proposer un plan de performance qu'il ne peut pas valider. Je dis ce que j'ai refusé, sept choses en tout, dont le mot « narration » pour ce qui ne peut pas mentir, une seconde bibliothèque d'assertions, un sixième état pour un arrêt, une garantie sans garde. Le principe tient les quatre tribunaux ensemble : une affirmation ne vaut que ce que vaut le tribunal qui peut la refuser, et là où aucun tribunal ne voit, le dossier le dit.

## 1. Le concept, tel que le terrain le tient

Quatre pratiques du terrain sont quatre tribunaux, et on les voit rarement comme un seul.

La première est l'exemple qui s'exécute. Le doctest de Python exécute la session interactive trouvée dans une docstring et compare le texte imprimé. Rust exécute les exemples de sa documentation, et Go a des exemples testables avec une sortie attendue dans un commentaire. L'exemple est la spécification. Sa faiblesse est que la comparaison est du texte contre du texte, et que c'est le harnais qui décide ce qu'est un échec.

La deuxième est le test d'instantané. Une capture d'écran ou un arbre rendu est stocké et comparé à l'exécution suivante. Il prouve que l'image d'aujourd'hui égale celle d'hier.

La troisième est l'audit contre une liste. Les listes du terrain sont celles de l'OWASP, du NIST et des cadres de conformité. Pour la détection et la preuve, la chaîne d'outils est l'agrégateur de journaux, le format de règles, l'orchestration des réponses.

La quatrième est l'instrument. Micrometer, OpenTelemetry, Prometheus et les profileurs de chaque runtime mesurent un programme de l'extérieur. (Connaissance générale, et non étude du dossier, sauf là où je nomme le fichier.)

## 2. Le premier principe

**Une affirmation ne vaut que ce que vaut le tribunal qui peut la refuser. Et là où aucun tribunal ne voit, le dossier le dit.**

Le dossier la tient en deux phrases qui se rejoignent. Le modèle de menace : chaque garantie nomme la garde qui la prouve, et une garantie sans garde est listée comme un risque ouvert. Et la loi de la perception : une comparaison prouve l'identité et jamais la justesse, et si une personne est le dernier consommateur, une personne est la dernière barrière. Sous les deux se trouve la doctrine que la bibliothèque répète dans chaque volet : l'expression est libre, et l'admission est gouvernée.

## 3. La forme Softanza

Le chapitre 5 a parlé du tribunal qui juge quiconque a écrit le code. Ce chapitre a quatre tribunaux, un par genre d'affirmation. Je montre chacun par quelque chose qu'il refuse.

### Le tribunal des promesses

Une promesse, dans ce livre, est la ligne `#-->` sous une expression, et c'est une affirmation sur un arrêt du programme. L'outil qui la lit, appelé le voyageur (il appartient au volet nommé Testoor), dit qu'une promesse est tenue, divergente, non atteinte ou non jugée. Une promesse qui se dispute avec elle-même, de la prose après une valeur, n'est jamais accusée. Que dit le voyageur d'une promesse vraie, d'une promesse fausse et d'une promesse qui se dispute avec elle-même ? Exécutez-le :

```haro
write("tour.haro", '? 1 + 1' + nl + '#--> 2' + nl +
	'? 1 + 1' + nl + '#--> 3' + nl +
	'? "C"  #--> "C" but should be "sm_AS"' + nl)
oTour = TravellerQ().Silent().Walk("tour.haro")
aClaims = oTour.Records()[1][:run][:stops][1][:claims]
? aClaims[1][:state]
#--> kept
? aClaims[2][:state]
#--> diverged
? aClaims[3][:state]
#--> unjudged
? oTour.ExitCode()
#--> 1
remove("tour.haro")
```

Il dit `kept`, `diverged` et `unjudged`, et le code de sortie est `1`. Ce code est celui du lanceur, et non celui du langage.

Une promesse peut être que la ligne lève une erreur. Cela se lit comme une levée d'erreur promise. Quand elle survient, comment la tournée finit-elle ? Exécutez-le :

```haro
write("raise.haro", '? "before"  #--> before' + nl +
	'? Boom()  #--> ERROR: boom happened' + nl +
	'func Boom()' + nl + char(9) + 'raise("boom happened")' + nl)
oRaise = TravellerQ().Silent().Walk("raise.haro")
aRun = oRaise.Records()[1][:run]
? aRun[:stops][1][:claims][2][:state]
#--> kept
? aRun[:end]
#--> finished
? oRaise.ExitCode()
#--> 0
remove("raise.haro")
```

La promesse est `kept`, la fin est `finished` et le code de sortie est `0` ! Le processus du langage s'est terminé sur une erreur, et la tournée a fini comme elle avait dit qu'elle le ferait.

Chaque règle de ce juge a été apprise en regardant le harnais accuser la bibliothèque à tort. L'en-tête de la garde le dit. Une promesse courte `6` s'est un jour cachée à l'intérieur d'un `[ 6, 28 ]` plus loin, et c'est pourquoi la règle sur les graphies existe. Le juge propre à ce livre est une copie du juge du site, plus lâche que le voyageur.

### Le tribunal de la perception

La phrase du dossier est qu'une comparaison prouve l'identité, et qu'elle ne prouve jamais la justesse. La bibliothèque tient le cas. Un tracé en barres dessinait des barres verticales pour des données horizontales pendant que tous ses soixante-treize exemples continuaient de passer. C'est pourquoi les tracés comparent désormais l'image exactement. Cela rend l'identité stricte ; cela n'en fait pas la justesse. La justesse est une personne.

Donc un monde déclaré porte son état de perception. Huit traditions musicales sont déclarées comme données dans la bibliothèque. Combien d'entre elles une personne a-t-elle entendues ? Demandez au dossier :

```haro
nUnheard = 0
for cName in StzSoundUniverses()
	if StzSoundUniverseQ(cName).Listener() = "UNPERCEIVED"
		nUnheard++
	ok
next
? len(StzSoundUniverses())
#--> 8
? nUnheard
#--> 7
? left(StzSoundUniverseQ("tunisian").Listener(), 5)
#--> HEARD
```

Il répond `8`, `7` et `HEARD` : huit déclarées, et sept d'entre elles non perçues ! Une seule est entendue, et le dossier de celle-ci porte un nom, une date et un verdict. Le compteur de ce bloc ne fait que compter les non entendues ; aucun compteur ne décide du verdict. L'unique tradition qui a été entendue l'a été par moi le 26 septembre 2026, à travers cinq exemples originaux, et mon verdict a été « far from being qualified ». Laquelle des parties échoue, l'accord, le phrasé, le rythme ou le timbre, je ne l'ai pas encore dit. Ces mots sont les miens, et ils sont l'unique perception enregistrée qui soit un refus.

La loi est celle du domaine de projets, c'est-à-dire de l'ensemble des projets de l'auteur, adoptée le 25 septembre 2026 sur instruction de l'auteur. Elle exige que le dossier nomme celui qui perçoit et cite le verdict. Sa troisième exigence est celle que j'emporte avec moi : non perçu est un état, pas un échec. Elle refuse aussi deux choses. Elle ne dit pas qu'un humain doit garder chaque commit, parce qu'elle lie à la granularité d'une phase. Et elle ne dit pas qu'elle se généralise à partir d'un volet sans preuve supplémentaire, et elle a été retenue un mois pour ce motif.

La galerie d'images est l'endroit où elle n'est pas satisfaite. La bibliothèque tient quatre-vingt-quinze jugements d'images et de sections de texte, dans trois fichiers d'index, commités le 5 octobre 2026. Chacun est d'un modèle, lisant l'image ou lisant le texte que le programme a imprimé. Aucun ne porte de nom humain. Le premier index le dit en une phrase : aucun humain n'a regardé ces images. Le registre des constats se termine par une ligne que je répète : un verdict humain sur un échantillon est encore dû. Le dossier ne tient aucun verdict humain sur une image de la galerie. Elle reste non perçue.

### Le tribunal de la sécurité

Le volet de sécurité part d'une affirmation. Le modèle de menace suppose qu'un modèle de langage détourné passera, et le rend inoffensif. Le modèle ne détient jamais la capacité, et donc un LLM trompé ne peut toujours pas agir. Le document n'essaie pas de détecter chaque invite malveillante.

La preuve de ce qui s'est passé est une chaîne de hachage. Modifiez n'importe quelle ligne après la première, et la chaîne dit quelle entrée s'est rompue. Si j'en modifie une, quelle entrée nomme-t-elle, et une mauvaise clé déclenche-t-elle la même accusation ? Exécutez-le :

```haro
oLed = StzSecurityLedger(256)
oLed.Record(StzSecurityRefusal("auth.login.failed", HumanActor("admin"), "user:admin", "wrong credentials"))
oLed.Record(StzSecurityRefusal("secret.reveal.refused", LLMActor("advisor"), "secret:payments-key", "actor is not effectful"))
oLed.SealTo("evidence.txt", "the-evidence-key")
? StzVerifySealedLedger("evidence.txt", "the-evidence-key")[:why]
#--> chain intact over 2 entries
? StzVerifySealedLedger("evidence.txt", "another-key")[:why]
#--> the chain is intact but the SEAL does not match this key
write("evidence.txt", StzReplace(read("evidence.txt"), "actor is not effectful", "routine maintenance"))
? StzVerifySealedLedger("evidence.txt", "the-evidence-key")[:why]
#--> the chain breaks at entry 2 -- that record (or one before it) was edited
remove("evidence.txt")
```

Le vérificateur répond `chain intact over 2 entries`, puis `the SEAL does not match this key`, puis `the chain breaks at entry 2`. La chaîne a nommé la rupture ! Une mauvaise clé et une ligne modifiée sont deux accusations différentes. Remarquez quelle entrée j'ai choisi de modifier : la deuxième. Une modification de la première entrée n'est pas détectée. Le vérificateur contrôle le texte de chaque entrée contre l'empreinte de l'entrée qui la précède, et la première n'en a aucune avant elle. Cela a caché ma première tentative. La narration énonce la limite dans ses propres mots : ce n'est pas une protection contre un attaquant qui exécute déjà du code dans le processus.

Un secret est la même loi appliquée à une clé. Son seul visage public est son descripteur. Une main qui peut valider peut le lire. Que répond le tribunal quand un modèle de langage demande ? Exécutez-le :

```haro
StzOpenSecurityLedger(64)
oKey = new stzSecret("deploy-key")
oKey.FromLiteralQ("ssh-ed25519-AAAA")
? oKey.Descriptor()
#--> <secret 'deploy-key' (secret) from literal>
? oKey.Reveal(HumanActor("ops"))
#--> ssh-ed25519-AAAA
try
	oKey.Reveal(LLMActor("planner"))
catch
	? cCatchError
done
#--> Refused: actor 'planner' (posture sandboxed) may not reveal secret 'deploy-key'. Only an effectful, non-sandboxed actor can read a secret.
? len(StzSecurityLedgerQ().Refusals())
#--> 1
StzCloseSecurityLedger()
```

Il répond `Refused: actor 'planner' (posture sandboxed) may not reveal secret 'deploy-key'`. Le tribunal a refusé le modèle, et le registre compte `1` refus sans que personne n'ait appelé le registre ! C'est la loi du chapitre 17, qu'un modèle ne détient pas la capacité de produire des effets, appliquée à une clé, avec le dossier en plus.

Qu'est-ce que la table de garanties lie à une garde ? La méta-garde du modèle de menace vérifie que le document existe avec ses sections, et que chaque ligne de garantie contient une preuve. Une preuve est le chemin d'une garde, une exécution de fuzzing, un contrôle de nomenclature logicielle ou un manuel d'exploitation. Elle vérifie que chaque chemin de garde dans les lignes existe sur le disque, et qu'une fausse ligne plantée, avec une garantie sans preuve, est attrapée. Elle n'exécute pas les gardes, et elle ne vérifie pas qu'une garde affirme ce que dit sa ligne. Cela, c'est le travail de la barrière de sécurité. Donc « chacune liée à une garde » est, exactement, « chacune nomme au moins une preuve, et tout fichier de garde qu'elle nomme existe ».

À ce commit, la table tient 43 garanties. Le site dit 38, sur trois pages. Les deux sont vrais de leurs dates : le document avait 38 lignes le 30 septembre 2026, et les lignes de 39 à 43 ont été ajoutées le 5 octobre. Le nombre du site est au site de le mettre à jour.

### Le tribunal de la performance

Un instrument doit un nombre. Le chronomètre honnête donne un nombre issu d'une horloge qui ne va que vers l'avant. Il exclut une pause, et il expédie deux spans d'une même trace dans un seul lot pour un collecteur d'observabilité. Si je le mets en pause 200 millisecondes, la pause compte-t-elle dans le temps écoulé ? Exécutez-le :

```haro
w = StzStopwatchXT("import-orders")
w.Lap("parsed")
w.Pause()
StzEngineTimeSleepMs(200)
w.Resume()
w.Stop()
? isnumber(w.ElapsedMs())
#--> 1
? w.ElapsedMs() < 200
#--> 1
? w.Record()[:running]
#--> 0
w2 = StzStopwatchXT("notify-customer")
w2.JoinTrace(w.TraceParent())
w2.Stop()
? w2.TraceId() = w.TraceId()
#--> 1
oBatch = StzOtelBatch("shop")
oBatch.AddSpan(w).AddSpan(w2)
? Q(oBatch.ToJson()).NumberOfOccurrence(w.TraceId())
#--> 2
```

La pause n'a pas compté : `w.ElapsedMs() < 200` a imprimé `1`, et `w.Record()[:running]` a imprimé `0`, parce que le chronomètre s'était arrêté. Le second chronomètre a rejoint la trace du premier : `w2.TraceId() = w.TraceId()` a imprimé `1`, et le JSON du lot contient l'identifiant de trace `2` fois, pour deux spans.

Prudence sur ce que cela ne prétend pas. La narration dit que le chronomètre rejoint reçoit un nouveau span. J'ai vérifié : il reçoit la même trace, comme le montre le `1` ci-dessus, et le même identifiant de span, que ce bloc n'imprime pas. La phrase tient pour l'écho du serveur, que je n'ai pas exécuté, et non pour le chronomètre. Je la range parmi les demandes.

L'instrument n'est pas la fin du tribunal. Le jugement et l'action vivent à l'intérieur du programme. Un plan de performance est proposé par une machine, et seul un acteur effectif le valide. Que se passe-t-il quand un modèle demande à le valider, puis quand une personne le fait ? Exécutez-le :

```haro
oPlan = StzPerfPlan("relieve-queue")
oPlan.Propose(:ScaleUp, "nlp", "queue.depth: measured 900 (must be <= 100)")
oFleet = new FakeFleet
? oPlan.MayCommit(LLMActor("advisor"))
#--> 0
? oPlan.ExecuteOn(oFleet, LLMActor("advisor"))
#--> 0
? oFleet.CallCount()
#--> 0
? oPlan.ExecuteOn(oFleet, HumanActor("mansour"))
#--> 1
? oFleet.CallCount()
#--> 1
oPlan.Show()
#--> Perf plan relieve-queue -- 1 proposed action(s).
#      1. scaleup 'nlp' -- queue.depth: measured 900 (must be <= 100)
#    Audit (2):
#      #1 REFUSED scaleup 'nlp' by advisor -- actor is not effectful -- expression is free; admission is governed
#      #1 COMMITTED scaleup 'nlp' by mansour -- queue.depth: measured 900 (must be <= 100)

class FakeFleet
	aFleetCalls = []
	def ScaleUp(pcTag)
		aFleetCalls + [ "scaleup", pcTag ]
	def CallCount()
		return len(aFleetCalls)
```

Le parc, ici, est un double de répétition, tout objet qui répond aux mêmes verbes effectifs. La boucle est prouvée contre le double et non contre un vrai parc. Un modèle qui demande à valider est refusé avant toute tentative : `ExecuteOn` a imprimé `0` et `CallCount` a imprimé `0`, donc le double a compté zéro appel ! Pour la personne, `ExecuteOn` a imprimé `1` et `CallCount` a suivi avec `1`. La même action est jugée deux fois, et l'audit garde les deux jugements : `REFUSED scaleup 'nlp' by advisor -- actor is not effectful -- expression is free; admission is governed`, et `COMMITTED scaleup 'nlp' by mansour`.

Les quatre tribunaux ont parlé, et maintenant je dis ce que j'ai refusé.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé le mot pour la chose qu'il n'était pas.** La structure de ce livre et le bilan de clôture de l'étude appellent les articles des « narrations qui ne peuvent pas mentir ». Ma propre décision du 7 octobre 2026, le 12.20 de l'étude, dit que « narration » nomme les articles sous le dossier de documentation de la bibliothèque, et non les suites exécutables. Le lanceur du site annote un article et ne décide plus s'il est montré. Le propre dossier du site du 8 octobre 2026, exécuté sur un autre commit que celui de ce livre, dit que sur 135 articles 55 se sont exécutés. Sur les 423 blocs de ceux-ci, 123 ont tenu leur promesse. Donc les articles peuvent dériver. Ce qui ne peut pas mentir, ce sont les gardes exécutables, et la construction de ce livre, qui échoue quand un bloc ne tient pas sa promesse.

**J'ai refusé une seconde bibliothèque d'assertions.** Les décisions du lanceur de promesses refusent une seconde bibliothèque, une réécriture des fichiers de test, et un pourcentage de couverture avant qu'il y ait des routes. Elles refusent un double écrit pour la production d'une plateforme, et le mot « vérifié » sur une affirmation perceptive sans un nom et une phrase.

**J'ai refusé de plier non jugé ou non perçu en réussite ou échec.** Un arrêt a cinq états et pas de sixième : tenue, divergente, non atteinte, non jugée, non perçue. Un lanceur qui plie non jugé ou non perçu en réussite ou échec a tort. Je tiens cela pour une vue, non pour un résultat.

**J'ai refusé d'analyser une preuve altérée.** Un outil qui vérifie, avertit, puis analyse quand même apprend à ses utilisateurs à ignorer l'avertissement. C'est mon point de vue.

**J'ai refusé de tout détecter.** Les détections sont déclarées. La sentinelle ne parle que sur les transitions : silence, une alarme après cinq mauvais mots de passe, et rien de nouveau après un sixième, puisque l'histoire n'a pas redémarré. Elle n'écrit pas ses propres déclenchements dans le registre, parce que des détections sur des événements de détection invitent des boucles de rétroaction.

**J'ai refusé de concurrencer l'écosystème du terrain.** L'étude de performance du 29 juillet 2026 dit que le volet ne concurrence pas Grafana, Datadog ni l'écosystème d'OpenTelemetry, et ne devrait pas feindre de le faire. Il exporte.

**J'ai refusé une garantie sans garde.** La dernière règle du modèle de menace est qu'une garantie n'est ajoutée qu'avec sa garde.

Voyons maintenant les gardes qui prouvent ce qui s'est exécuté.

## 5. Le tribunal

`testoor_promises_narrated` prouve chaque règle de promesse plantée dans les deux sens. Un mensonge est divergent ; deux mensonges sont tous deux attrapés ; un mensonge court ne se cache pas dans une liste plus loin ; les graphies d'une valeur vraie sont toutes tenues. Une levée d'erreur attendue est honorée ; la prose est non jugée ; un programme qui ne compile pas n'est pas divergent ; une levée d'erreur en cours de route laisse les promesses suivantes non atteintes. `threat_model_narrated` prouve la méta-garde décrite plus haut, y compris son pendant négatif. `security_ledger_narrated`, `secretstore_narrated` et `secret_narrated` prouvent la chaîne et le sceau, le magasin et le secret. `security_sentinel_narrated` prouve la sentinelle déclenchée sur les fronts. `stopwatch_narrated` et `tracing_tail_narrated` prouvent l'instrument et le lot. `governed_loop_narrated` prouve le plan, le contrôle préalable, la validation et l'audit.

La construction compte 11 assertions dans `threat_model_narrated`, un compte statique de ses appels d'assertion. Les autres sont aussi comptées par la construction, et non exécutées ici. Le volet de performance a douze gardes. Je n'imprime pas leur somme, parce que la construction les compte.

## 6. Le terrain, et où il mène

Les sections honnêtes propres du dossier, chaque perte à côté de son gain.

**En performance.** Il n'y a pas de base de données de séries temporelles, pas de langage de requête et pas de tableaux de bord. Par conception, le volet exporte. Sa réponse d'échantillonnage est faite d'anneaux bornés qui abandonnent le plus ancien, ce qui est honnête et plus grossier que l'échantillonnage en tête ou en queue. Le contexte distribué s'arrête à HTTP. L'écosystème d'intégrations et d'auto-instrumentation pour chaque cadre est celui du terrain. Le profileur est coopératif : il voit ce que vous encadrez, là où un profileur natif voit tout. Le gain qu'il revendique est que le jugement et l'action vivent à l'intérieur du programme : des budgets qui font échouer la construction, un réglage qui passe la gouvernance, une surveillance qui se facture elle-même.

**En sécurité.** Le registre est un anneau borné, et borné veut dire oublier. Il n'y a pas de télémétrie de l'hôte, du noyau ou du réseau. Les détections sont déclarées et non apprises, un écart en partie comblé par une détection de taux le 30 septembre 2026. La propre comparaison du dossier est qu'un corpus de règles au format du terrain est plus grand que huit détections livrées. Il n'y a pas de flux de travail d'un centre d'opérations de sécurité. Le plus grand écart, dans les mots du dossier, est qu'une détection ne peut voir que ce qu'une jointure émet. Le gain est que l'événement est typé à la naissance, là où la porte refuse, de sorte qu'aucun analyseur ne se tient entre ce que le programme savait et ce que le détecteur juge.

**En promesses.** Les doctests du terrain vivent dans la chaîne d'outils de l'hôte et répondent réussite ou échec (connaissance générale). Le juge de la maison a cinq états. Là où le terrain mène, c'est en instruments : la note de lancement de Testoor, le volet qui tient le voyageur, a les instruments de couverture de toute sorte à zéro, et la couverture de routes est planifiée.

**En perception.** Les services d'instantanés visuels du terrain sont mûrs et automatiques (connaissance générale). La loi de la maison dit qu'une perception ne remplace pas un nombre, et qu'aucun nombre ne la remplace.

L'étude du dossier donne le ton que j'essaie de faire résonner. Une grille de deux cent quatre-vingt-six coches contre deux cent soixante-neuf croix est, dans ses mots, la forme d'une brochure.

Voyons maintenant où le chapitre s'arrête.

## 7. La limite

Ce qui est construit : les promesses comme arrêts ; le volet de sécurité, avec son registre, sa sentinelle, son exercice, sa réponse, son attestation et ses secrets ; le volet de performance de sa première phase à sa dernière ; la loi de la perception, adoptée. Et les tables de verdict déclarées pour la voix chantée et les huit univers. La table de garanties tient 43 lignes qui nomment 57 fichiers de garde distincts, aucun ne manquant.

Ce qui est conçu :

- Les routes et la carte du lanceur de promesses, son horloge et sa météo, ses excursions, sa perception et sa mutation, et ses tournées héritées. Tout cela est planifié. L'état *non perçu* est nommé dans l'en-tête du lanceur, et le lecteur n'en assigne aucun.
- La négociation autour d'un plan rejeté, que le modèle de menace appelle conception seulement.
- Le volet des extensions : les extensions ne sont pas livrées, et le code étranger n'est pas encore gouverné.

Ce qui est absent :

- **Un verdict humain sur une image de la galerie.** Zéro sur quatre-vingt-quinze. La deuxième exigence de la loi, un nom, une date et ce qu'ils ont dit, n'y est pas satisfaite. Le chapitre dit non perçu, et ne dit pas vérifié.
- Sur les huit traditions musicales, sept non entendues.
- Un vrai coffre et un vrai bac à sable comme preuves. Le résolveur de coffre est testé contre un remplaçant, sur un vrai HTTP. Il n'y a pas d'adaptateur de gestion de clés dans le nuage.
- Les chemins sur les systèmes POSIX, non vérifiés, en attendant une machine Linux ; le fuzzing planifié ; l'intégration continue ; les commits signés, que l'auteur a différés pour la phase de développement.
- Un magasin de séries temporelles. Un pourcentage de couverture, qui est refusé tant qu'il n'y a pas de routes.

Trois autres choses ont leur place ici, trouvées en exécutant le tribunal.

**Les nombres de l'exercice diffèrent selon la source.** La mesure de réactivité du modèle de menace vient de trois exécutions. C'est une détection en un peu plus de trois cent cinquante millisecondes, et un confinement en un peu plus de cinquante. Le site imprime 395 et 50, d'un rejeu du 1er octobre. Ils diffèrent parce que l'exercice mesure une horloge. Une forme d'attaque, en boucle locale, sur une seule machine, lancée à la demande. Quel que soit le nombre que vous imprimez, vous nommez sa source.

**Un défaut possible dans le juge de promesses, que je signale et sur lequel je n'ai rien construit.** Un fichier dont la première promesse est un mensonge et la dernière une levée d'erreur promise lit le mensonge comme non atteint et la levée d'erreur comme tenue. La tournée est brisée, avec zéro divergente, et le code de sortie est 1. Je l'ai reproduit deux fois. Chaque règle seule se comporte comme la garde la plante. Savoir si une divergence au-dessus d'une levée d'erreur promise devrait se lire *divergente* est une question pour le volet Testoor, qui tient le voyageur.

**Des comptes qui ne s'accordent pas entre les sources.** La clôture de l'étude dit 387 gardes narrées. Mon `find` sur l'instantané épinglé dit 529 fichiers ainsi nommés. Le compte propre de la construction est celui qu'il faut utiliser, et aucun des deux autres.

Six portes suivent, une pour chaque lecteur.

## 8. Six portes

**Le programmeur.** Vos exemples portent déjà leur sortie attendue. Le voyageur les lit comme des promesses et dit tenue, divergente ou non jugée, et la prose qui se dispute avec elle-même n'est jamais accusée.

**L'analyste.** Le modèle de menace est une table que vous pouvez lire : chaque ligne avec la garde qui la prouve et sa limite honnête. Le jugement de performance est déclaré avant que le code ne s'exécute.

**Le concepteur.** Une image ou un son est une affirmation que seule une personne peut clore. La galerie dit qu'un modèle a regardé et qu'aucun humain ne l'a fait. Votre verdict est une ligne nommée dans le dossier.

**Le décideur.** La question de savoir qui a décidé, et ce qui est écrit, a une réponse mécanique dans les deux volets. La même action est refusée pour le modèle et validée pour l'humain, les deux dans un seul audit, et la preuve est scellée de sorte qu'une modification soit nommée.

**Le formateur.** La règle du tuteur rencontre le tribunal. Prédisez le verdict d'une promesse avant que le voyageur ne la parcoure.

**L'agent.** Vous pouvez proposer un plan de confinement ou un plan de réglage et vous ne pouvez valider ni l'un ni l'autre. Votre refus est lui-même un événement enregistré. Ne dites pas à une personne qu'une image est juste. Dites « non perçu ».

## 9. Exercice

Prédisez, par écrit, avant d'exécuter quoi que ce soit. Le fichier ci-dessous contient trois promesses. Quel état aura chacune ?

```haro exercise
write("mine.haro", '? 2 * 3' + nl + '#--> 6' + nl +
	'? 2 * 3' + nl + '#--> 7' + nl +
	'? "ok"  #--> "ok" but see why' + nl)
# before you run: which state will each of the three promises have?
oMine = TravellerQ().Silent().Walk("mine.haro")
aMine = oMine.Records()[1][:run][:stops][1][:claims]
# your three predictions, then:  ? aMine[1][:state]   ? aMine[2][:state]   ? aMine[3][:state]
remove("mine.haro")
```

Exécutez-le. Les états sont tenue, divergente et non jugée. Puis ajoutez une quatrième ligne qui lève une erreur, promettez-la avec `#--> ERROR:`, et prédisez d'abord comment la tournée finira. Ne changez pas votre prédiction pour la faire correspondre à ce que vous voyez. Expliquez d'abord la sortie.

Je vous laisse celui-ci. Voici le bloc de la levée d'erreur de la section 3 avec un seul changement : sa première promesse est maintenant un mensonge.

```haro exercise
write("raise.haro", '? "before"  #--> after' + nl +
	'? Boom()  #--> ERROR: boom happened' + nl +
	'func Boom()' + nl + char(9) + 'raise("boom happened")' + nl)
oRaise = TravellerQ().Silent().Walk("raise.haro")
aRun = oRaise.Records()[1][:run]
# what does the tour say of each promise, how does it end, what is the exit code?
? aRun[:stops][1][:claims][1][:state]
? aRun[:stops][1][:claims][2][:state]
? aRun[:end]
? oRaise.ExitCode()
remove("raise.haro")
```

Exécutez-le. Lisez ce que le voyageur dit du mensonge, ce qu'il dit de la levée d'erreur, comment la tournée finit et quel est le code de sortie, puis comparez avec ce que chacune des deux promesses a donné seule à la section 3. La section 7 dit pourquoi je ne peux pas vous le dire : c'est un défaut possible du juge de promesses, que j'ai signalé sans rien construire dessus, et que j'ai laissé non corrigé exprès. Quand vous saurez dire ce que le tribunal répond ici, vous connaîtrez la question que la section 7 confie au volet Testoor.

Le chapitre 22 est *Comparé, honnêtement*. Son principe est celui-ci : une comparaison ne vaut rien tant que la version de l'autre côté et la date ne sont pas sur la page, que l'autre côté n'a pas été exécuté, et que la perte n'est pas imprimée à côté du gain.
