---
id: your-users-keep-their-medium
part: 5
number: 25
title: Vos utilisateurs gardent leur médium
spine: false
narrations: [stz-service-virtualization-code-first-subscribe-later.md, stznatural-narration.md, stzApp-building-your-first-app-narration.md]
site: [zui]
guards: [sms_port_narrated, wisecoding_rich_narrated, sound_convergence_narrated, sound_listener_narrated, sound_semantics_narrated, payments_webhooks_narrated]
stage:
  built: "la conversation gouvernée avec sa question comme donnée ; le port SMS et son bac à sable, avec la facture par segment dans deux alphabets ; un vérificateur du corps d'un message entrant ; cinq valeurs sémantiques rendues en couleur, en earcon et en phrase ; une voix qui parle, et qui entend une grammaire fermée ; un ensemble fermé de phrases qu'une entreprise accepte de dire ; un message de trois champs entre identités d'une même plateforme"
  designed: "le service du socle commun pour la messagerie ; des surfaces conversationnelles pour une application de messagerie, le SMS, l'USSD et la voix, avec une matrice de satisfaisabilité comme tribunal ; des gabarits comme grammaire"
  absent: "une application de messagerie, l'USSD ou une ligne téléphonique, sous quelque forme que ce soit ; une projection conversationnelle d'un monde ; un canal, une session, un gabarit, le consentement ; la question dans une autre langue que l'anglais ; une voix pour le haoussa, le zarma ou le fulfulde ; les vingt-deux verbes comme liste que la bibliothèque détient ; une réponse contenant un espace"
status: draft
rulings: ["12.15", "12.23", "12.24", "12.25", "12.26", "12.27"]
research: research/ch25.md
---

Dans ce chapitre, je prends une phrase de la constitution de l'interface, un nouveau médium ajoute des rendus, jamais des verbes, et je l'exécute sur le médium que je peux mesurer. Une question devient une ligne de texte, part sur un bac à sable SMS, et est facturée par segment dans deux alphabets. Je montre ce que la bibliothèque livre, la question comme donnée et le tribunal, et ce que vous écrivez, le rendu et le lecteur. Je rapporte les refus du dossier comme ceux du dossier : une conversation qui n'a pas besoin de modèle, et une voix qui entend des commandes et non de la dictée. Et j'imprime la limite entière : pas d'application de messagerie, pas d'USSD, pas de ligne téléphonique, et une réponse contenant un espace, que la conversation ne peut pas encore prendre.

## 1. Le concept, tel que le terrain le tient

Le commerce conversationnel, ou omnicanal : une entreprise rejoint ses clients dans les canaux qu'ils utilisent déjà, et un moteur de dialogue se tient derrière. Ce sont les pratiques, tirées de la connaissance générale et non d'une étude du dossier. Chaque date et chaque règle de fournisseur est à relire avant l'impression, comme l'étude du dossier le dit dans son propre "Not measured". Cette étude est une longue étude, par un lecteur extérieur, des racines du projet, et sa section 12.25 est celle qui traite de la messagerie.

Les cadres de dialogue possèdent le modèle de dialogue. Le concepteur écrit des intentions et des flux dans la notation du cadre, et le cadre comprend le texte libre avec des modèles entraînés et livre des connecteurs vers les canaux.

La plateforme d'entreprise d'une application de messagerie : les messages arrivent par un webhook, et l'entreprise peut répondre librement à l'intérieur d'une fenêtre de service que le client a ouverte. En dehors, seulement des gabarits approuvés, par un compte d'entreprise vérifié.

Les passerelles des opérateurs : SMS et USSD. Le SMS est facturé par segment, et je le mesure moi-même plus bas. L'USSD est une session de courts écrans avec un délai d'expiration, par la passerelle d'un opérateur, pays par pays, sur n'importe quel téléphone sans données. Aucun fichier de l'instantané ne dit quoi que ce soit de l'USSD.

Et la parole de plateforme, dans le plan propre de la bibliothèque : Windows a une interface de parole, macOS en a une autre, et chaque navigateur moderne en a une troisième.

Ce qu'ils ont en commun, c'est que le dialogue est écrit une fois par canal ou une fois par cadre, et que le canal est un connecteur, un détail de déploiement. Le chapitre retourne cette image. Le monde est déclaré une fois, et le médium en est un rendu.

## 2. Le premier principe

**Un nouveau médium ajoute des rendus, jamais des verbes.**

C'est une phrase de la constitution de l'interface, imprimée sur le site : « La grammaire est fermée : un nouveau médium ajoute des rendus, jamais des verbes. » Le dossier ne dit rien sur la question de savoir si la formulation est de moi. Je la cite comme celle de la constitution. Je ne la raconte pas comme ma phrase. Les vingt-deux verbes dont elle parle sont ceux de la constitution, en six familles. L'annexe C les imprime tels que je les ai lus dans le fichier propre de la constitution le 9 octobre 2026. Le dépôt n'est pas nommé, puisqu'il n'est pas encore public.

La même phrase, construite, pour une famille de valeurs et non pour les vingt-deux verbes : la valeur est partagée, et la façon dont elle est rendue est propre à chaque médium. C'est une décision de Central, l'entité de coordination du domaine de projets, sur ma délégation, du 30 septembre 2026. Il prouve que le principe n'est pas seulement un slogan. C'est la forme de trois faces qui fonctionnent : couleur, earcon, phrase.

Pour le plancher du dialogue, la phrase propre du code : plancher déterministe, aucun modèle nécessaire. La loi du chapitre 17, appliquée à un médium.

## 3. La forme Softanza

La bibliothèque livre la question comme donnée : une force, un sujet, une relation, des options et une raison. Elle livre les verbes, demander, répondre, refuser et conclure, et le tribunal. Un médium est un rendu de la donnée et un lecteur de la réponse, tous deux écrits par l'artisan du logiciel en quelques lignes. Rien dans la bibliothèque ne rend une question vers un téléphone. Ce qu'elle livre est une ligne en anglais, `AskIn`, qui est déjà un menu textuel : "(1) cheese (2) olives". Je le dis en ces termes.

Deux petites fonctions à moi font tout le médium : l'une qui rend la question en une ligne de texte, et l'autre qui lit la réponse. La lecture compte, et je montre pourquoi dans le troisième bloc. Que coûte une question, en lettres latines et en arabe ? Exécutez-le :

```haro
aEn = QuestionAfter("couscous", "brik")
aAr = QuestionAfter("كسكس", "بريك")
? ToText(aEn)
#--> Which dish for order3? (every order needs 'dish') 1) couscous 2) brik. Reply with the number.
? StzSmsSegments(ToText(aEn))[:segments]
#--> 1
? StzSmsSegments(ToText(aAr))[:encoding]
#--> ucs2
? StzSmsSegments(ToText(aAr))[:segments]
#--> 2
oBill = new stzSmsSandbox()
oBill.Send("+22790112233", ToText(aEn))
oBill.Send("+22790112233", ToText(aAr))
? oBill.TotalSegments()
#--> 3

func ToText(aQ)
	cOut = "Which " + aQ[:relation] + " for " + aQ[:subject] + "? (" + aQ[:why] + ")"
	for i = 1 to len(aQ[:options])
		cOut += " " + i + ") " + aQ[:options][i]
	next
	return cOut + ". Reply with the number."

func ReadReply(cText)
	for c in cText
		if NOT isdigit(c)
			return cText
		ok
	next
	return 0 + cText

func QuestionAfter(cA, cB)
	oW = new stzKnowledgeGraph("stall")
	oW.Know("order1", "order").Know("order2", "order").Know("order3", "order")
	oW.AddConversationQ("c").SetGoal(StzGoalQ().RequireEach("order", "dish"))
	oW.AskIn("c")
	oW.ReplyIn("c", cA)
	oW.AskIn("c")
	oW.ReplyIn("c", cB)
	return oW.AskInXT("c")
```

La question est une donnée, donc n'importe quel médium la rend. Et la loi propre du médium, ici que le SMS est facturé par segment et que l'alphabet décide, est un test et non une surprise. Le texte anglais fait 93 caractères selon mon décompte, et le bloc imprime un segment. Le même cadre avec deux noms de plats en arabe fait 89 unités selon mon décompte (les deux noms sont plus courts de quatre lettres). Le bloc imprime `ucs2` et deux segments, parce que l'encodage change. Quatre lettres de moins, et un segment de plus ! Le numéro de téléphone est inventé, et seul l'indicatif du pays, qui est celui du Niger, est réel.

Maintenant toute la conversation, répétée sur le bac à sable SMS avant qu'aucun compte existe. Une conversation est une boucle des verbes de la bibliothèque : le médium porte chaque question vers l'extérieur et chaque réponse vers l'intérieur. Les assertions sont la facture et le refus. Que compte le bac à sable, et que dit le tribunal à "7" ? Rien dans la boucle n'est un modèle :

```haro
oKB = new stzKnowledgeGraph("stall")
oKB.Know("order1", "order").Know("order2", "order").Know("order3", "order")
oKB.AddConversationQ("c").SetGoal(StzGoalQ().RequireEach("order", "dish"))
oSms = new stzSmsSandbox()
for cIn in [ "couscous", "brik", "7", "2" ]
	oSms.Send("+22790112233", ToText(oKB.AskInXT("c")))
	oKB.ReplyIn("c", ReadReply(cIn))
next
? oKB.ConversationQ("c").GoalState()
#--> fulfilled
? oSms.NumberOfMessages()
#--> 4
? oSms.TotalSegments()
#--> 4
? oKB.ConversationQ("c").Checkpoints()[1][:why]
#--> no option (7) was offered -- 2 option(s) on the table
? @@(oKB.Query([ "order3", "dish", "?o" ]))
#--> [ "brik" ]
```

Quatre messages, quatre segments, et la raison du tribunal mot pour mot : `no option (7) was offered -- 2 option(s) on the table`. Le refus de "7" est celui de la bibliothèque, comme au chapitre 18 ; la différence est qu'il est arrivé d'un téléphone.

**Le lecteur du médium est le travail du médium.** Un SMS entrant est une chaîne. La bibliothèque sépare les nombres, qui sont des indices d'options, des chaînes, qui sont des valeurs, et elle ne devine pas. Son propre commentaire : un indice ne peut jamais être pris pour une valeur littérale. Donc le lecteur du médium doit décider lequel c'est. Sans option sur la table, que devient le texte "2" ? Regardez :

```haro
oKT = new stzKnowledgeGraph("trap")
oKT.Know("order1", "order")
oKT.AddConversationQ("c").SetGoal(StzGoalQ().RequireEach("order", "dish"))
oKT.AskIn("c")
? @@(oKT.ReplyIn("c", "2")[:admitted])
#--> [ "2" ]
```

Un plat nommé 2 ! Dans le bloc d'avant, mon `ReadReply` a transformé le texte "2" en nombre 2, et l'option a été choisie. C'est la phrase la plus tranchante sur le pont : un médium ajoute des rendus, et il ajoute aussi une lecture. La lecture est l'endroit où vit la culture d'un utilisateur, les chiffres, les mots, un "OUI" local. Je tiens cela pour une vue, non pour un résultat.

**Une panne n'est pas un rejet.** Le médium refuse dans ses propres termes. Un numéro mal formé, sans `+`, n'est pas un numéro E.164 : corrigez la donnée. Une panne est autre chose : réessayez. Que répond le bac à sable à chacun ?

```haro
oPh = new stzSmsSandbox()
? oPh.Send("0612345678", "ready")[:status]
#--> rejected
oPh.FailNextQ()
? oPh.Send("+22790112233", "ready")[:status]
#--> refused
? oPh.NumberOfMessages()
#--> 0
? oPh.Send("+22790112233", "ready")[:status]
#--> sent
? oPh.NumberOfMessages()
#--> 1
```

`rejected` pour le numéro, `refused` pour la panne, et rien de compté. La reprise est `sent`, et le compte est de un.

**Un message entrant n'est cru qu'après vérification de sa signature.** Le chemin d'entrée est le motif que le volet des paiements a construit, et le vérificateur est générique, sur le corps. Aucun format d'en-tête ou de corps d'un fournisseur n'est modélisé, et le JSON est inventé. Les heures sont passées en paramètre, donc aucune horloge n'est lue. Que nomme le vérificateur quand un caractère du corps a changé depuis la signature ?

```haro
oSig = new stzRequestSigner("inbound")
oSig.AddKey("provider", "a-shared-secret")
cBody = '{"from":"+22790112233","text":"2"}'
cSig = oSig.SignBody("provider", cBody)
? oSig.VerifyWebhook(cBody, cSig, 1000, 5000)
#--> provider
? "[" + oSig.VerifyWebhook('{"from":"+22790112233","text":"1"}', cSig, 2000, 5000) + "]"
#--> []
? oSig.Why()
#--> signature mismatch (tampered body, or a secret this receiver does not hold)
```

Le premier corps a donné `provider`. Le corps modifié a donné `[]`, et la raison est `signature mismatch (tampered body, or a secret this receiver does not hold)`. Un caractère a changé, et aucun fournisseur n'a été nommé ! Un corps rejoué à l'intérieur de la fenêtre a donné "replay detected" dans ma sonde.

**Une valeur, plusieurs rendus.** La forme du pont, construite pour les cinq valeurs sémantiques de la constitution de l'interface. La couleur, l'earcon et la phrase rendent une valeur. `muted` est le silence dans le son et un traitement dans la couleur. Une valeur que la loi ne connaît pas est refusée :

```haro
? @@(StzSemanticValues())
#--> [ "danger", "warning", "info", "success", "muted" ]
oE = new stzEarcons()
? oE.WouldFireAt("Catastrophe", 1)
#--> 0
? StzColorToNumber("danger.muted") != StzColorToNumber("success.muted")
#--> 1
```

**La voix : dite, entendue, signifiée.** Texte vers son, son vers texte, texte vers sens. Le médium appelé voix rend et lit avec une grammaire fermée, et le sens est ma déclaration. Ce bloc a besoin d'une voix française et d'un module de reconnaissance français. Cette machine parle deux langues et en entend une, et une machine sans elles donnerait une autre réponse, donc la sortie montrée est celle enregistrée sur cette machine. Pas de micro, pas de fichier, pas de réseau : le module de reconnaissance est celui qui tourne dans le processus. Que fait-il d'une phrase qu'on lui a apprise, et d'une phrase qu'on ne lui a pas apprise ?

```haro
oV = StzVoiceQ()
oV.UseLanguage("fr-FR")
oL = new stzListener()
oL.AcceptMeanings([ [ "disque plein", :Danger ], [ "sauvegarde terminee", :Success ] ])
oL.HearSound( oV.ToSoundOf("disque plein") )
? oL.MeaningHeard()
#--> danger
oL.HearSound( oV.ToSoundOf("je voudrais un cafe au lait") )
? oL.WasNoMatch()
#--> 1
? oL.AcceptMeanings([ [ "tout brule", :Catastrophe ] ])
#--> 0
```

La phrase apprise a donné `danger`, la phrase non apprise n'a donné aucune correspondance (`1`), et `Catastrophe` a été refusée (`0`). La raison du refus dit que `catastrophe` n'est pas l'une des cinq valeurs sémantiques. Je n'imprime pas la confiance du module de reconnaissance, qui varie selon la machine.

**Le monde déclare ses verbes et sa portée, et son code ne nomme aucun médium.** Un monde contient des écrans déclarés par intention, cinq des vingt-deux verbes, et une liste de ce qu'il atteint. Rien ne refuse `:whatsapp` quand il est déclaré :

```haro
oApp = new stzApp("stall")
oApp.AddThingQ(:Dish) { Has([ :name, :price ]) }
oApp.AddScreenQ(:Menu) { ToDiscover(:Dish)  Shows([ :name, :price ]) }
oApp.AddScreenQ(:Basket) { ToSelect(:Dish)  Acts(:Confirm, :Order) }
oApp.AddReaches([ :web, :whatsapp ])
oApp.Explain()
#--> WORLD stall   lives in: memory (not persisted)
#      BEING
#        dish (name, price)
#      MET FROM WITHOUT
#        screen menu: discover dish shows name, price
#        screen basket: select dish
#        reaches web, whatsapp
```

`Acts(...)` est stocké et non narré. Et la scène en exécution : que dit la plateforme quand on lui demande de générer la surface que le monde a déclarée ? Ce bloc crée un répertoire vide dans le répertoire de travail :

```haro
oPlat = StzPlatformQ("stall-platform")
oPlat.SetWorld(oApp)
try
	oPlat.Generate(:whatsapp)
catch
	? cCatchError
done
#--> stzPlatform.Generate: unknown reach surface 'whatsapp' (web/desktop/mobile).
```

`unknown reach surface 'whatsapp' (web/desktop/mobile)` : la plateforme l'a refusée ! Elle nomme les trois surfaces qu'elle a, et le même refus répond à `:ussd`.

**Ce qu'on peut dire à un client est un ensemble fermé.** Le tribunal de ce qui est dit a aujourd'hui un mécanisme : une énumération fermée compilée en grammaire. Les chapitres 11 et 19 l'utilisent pour un langage et pour la sortie d'un modèle. Ici elle contient les réponses qu'une entreprise accepte d'envoyer. Ce n'est pas une unité de gabarit de messagerie, et il n'y en a aucune. Que dit le tribunal d'une phrase que l'entreprise n'a jamais approuvée ? Deux choses à imprimer avec elle : le message dit "the model answered" quel que soit le locuteur, et l'énumération est insensible à la casse :

```haro
oSay = StzOutputSchemaQ([ [ :field = "reply", :type = :oneof, :choices = [ "Your order is received.", "Your order is ready.", "We are closed tonight." ] ] ])
? oSay.ParseOutput('{"reply": "Your order is ready."}')[:ok]
#--> 1
aNo = oSay.ParseOutput('{"reply": "Your order is free, tonight only."}')
? aNo[:ok]
#--> 0
? oSay.CiteFindings(aNo[:findings])
#--> [oneof @ reply] field 'reply' is a closed enumeration (your order is received. | your order is ready. | we are closed tonight.) and the model answered 'Your order is free, tonight only.'.
```

La phrase approuvée est passée (`1`), la phrase inventée a été refusée (`0`), et la raison du tribunal commence par `[oneof @ reply] field 'reply' is a closed enumeration`.

### Le médium du restaurant

Le chapitre 1 dit que le propriétaire du restaurant a fait sa première démonstration sur une application de messagerie. Le dossier ne soutient pas cette phrase telle qu'elle est, et je la signale à l'auteur. Le chapitre 2 donne déjà son outil comme un tableur. Son propre rapport du 4 juillet 2026 donne comme outil actuel un tableur. Il demande une page web ouverte par un code QR ou par un bouton d'un réseau social. Rien de lourd à télécharger. La ligne sur diverses applications, dont une application de messagerie, est l'étiquette d'une option du formulaire de cadrage, et ce n'est pas ce qu'il a coché. "Simple comme une application de messagerie" est simulé dans le projet, comme le chapitre 28 l'a déjà constaté.

Le restaurant est donc la première forme de la phrase de ce chapitre, et non un exemple du médium de messagerie. Le client garde son médium : un lien qui s'ouvre dans le navigateur qu'il a déjà. Le médium de messagerie, comme thèse, n'est pas construit. Je raconte cette histoire et ne fais aucune déclaration sur l'usage d'une application de messagerie par le propriétaire, puisque le dossier n'en contient aucune. Le chapitre 1 garde sa propre formulation de cette démonstration, et ce que le dossier montre plus exactement est ce que dit cette section.

Voilà la forme, construite et exécutée ; viennent ensuite ce que j'ai décidé et ce que j'ai refusé.

## 4. La décision, et ce que j'ai refusé

Les refus ci-dessous, après le premier, sont ceux du dossier : des décisions d'une session, écrites dans les en-têtes des fichiers de son de la bibliothèque et dans son plan de la voix. Je les rapporte comme tels, et ce ne sont pas des décisions de moi.

**La messagerie, la question.** Le rapport de l'étude sur ma demande : les conversations ont lieu de façon programmatique par défaut, ou avec une configuration minimale, sans obliger les utilisateurs à changer leurs cultures d'usage. La section de l'étude est intitulée « tranché » et non « tranché par l'auteur », et ses propositions pour les surfaces conversationnelles sont celles d'une session. Le dossier ne contient aucune décision de ma part qui les adopte. Je dis *proposé*, pas *décidé*.

**Une conversation n'a pas besoin de modèle.** Le plancher est déterministe. Un modèle peut améliorer la fluidité derrière la même surface.

**La voix n'est pas un paradigme.** Le plan du dossier dit hors de portée jusqu'à demande écrite : toute la gestion du dialogue, les mots d'éveil, l'analyse d'intentions et l'interruption par l'utilisateur.

**Des commandes, pas de la transcription : un refus mesuré.** La barrière a été fixée avant les chiffres : la dictée libre est livrée à quatre-vingts pour cent d'exactitude et 0,60 de confiance moyenne. L'exécution a donné 66,7 pour cent et 0,600, ce qui a échoué. La grammaire fermée a donné cent pour cent et 0,898, ce qui a réussi. Cette face n'a donc pas de `Transcribe()`, et n'en aura jamais tant qu'un meilleur module de reconnaissance n'existera pas.

**Refuser, ne jamais substituer.** Parler français à un opérateur qui a demandé l'anglais est pire que de ne rien dire.

**Pas de sens inféré.** L'auteur déclare toujours le sens. Une sixième valeur serait un amendement constitutionnel portant les habits d'une bibliothèque.

**Un puits prouve ce que vous auriez envoyé.** La limite honnête du port SMS : le filtrage des opérateurs de téléphonie, les règles d'identifiant d'expéditeur, les particularités d'alphabet par pays, et les accusés de réception asynchrones. Rien de cela n'est modélisé ici.

**L'écran acquitte, et le son n'est pas l'acquittement.**

La section suivante nomme les gardes qui se tiennent derrière ces exécutions.

## 5. Le tribunal

`sms_port_narrated` prouve la loi des segments, avec ses frontières à 160 et 161, 306 et 307, la falaise des émojis de 100 à 102 unités, 71 lettres arabes faisant deux segments, et les neuf caractères d'extension. Elle prouve l'E.164, le puits et sa facture, la panne contre le rejet, et le refus en production. Je l'ai exécutée une fois, et 53 assertions sur 53 ont passé. `wisecoding_rich_narrated` est celle du chapitre 18 : le cadre, les options numérotées, le refus d'un nombre que personne n'a offert, les points de contrôle avec une durée de vie. `payments_webhooks_narrated` prouve qu'une signature entrante est vérifiée avant d'être crue : non signée, falsifiée, rejouée. `sound_semantics_narrated` prouve que les cinq valeurs sont celles de la loi, que quatre sonnent et que `muted` est silencieuse, et qu'une valeur inventée est refusée. `sound_listener_narrated` prouve la grammaire fermée, que l'absence de correspondance est un résultat, et que la confiance est un appel séparé ; je l'ai exécutée une fois, et 21 ont passé. `sound_convergence_narrated` prouve que la boucle se ferme pour les quatre états, que la langue est négociée par direction, qu'une sixième valeur est refusée à la déclaration, et que la phrase d'un inconnu ne donne aucun sens.

Une réserve pour la ligne du tribunal. Les gardes du son ont besoin de la bibliothèque sonore du moteur, et pour la boucle, d'une voix et d'un module de reconnaissance. Sur une machine sans eux, les gardes de voix impriment "skipped" et passent. Un succès là ne prouve rien sur la parole. Les gardes pour le SMS et pour la conversation n'ont pas cette dépendance.

## 6. Le terrain, et où il mène

Le décompte propre du dossier, dans l'étude du 12.25 : des unités constitutives de la messagerie, dix-huit en tout, ce qui manque. La phrase de l'étude dit que le mot désignant une application de messagerie n'apparaît dans aucun fichier de code ni aucun document de conception de la bibliothèque, et l'USSD dans aucun. Je l'ai remesurée à ce commit et confirmée. Il n'y a aucun résultat dans le code ni dans la conception de base, core ou max. Les correspondances dans le reste de l'instantané sont des fichiers de données de listes de mots et de test, et l'USSD n'en a aucune en texte.

Les cadres sont en tête pour la compréhension et pour les connecteurs. Le chapitre 18 énonce le côté de Softanza à partir du code : la conversation demande un champ à la fois, sur un graphe que l'utilisateur doit d'abord avoir déclaré. Elle ne comprend pas une réponse ouverte.

Le terrain est en tête pour la couverture des canaux et pour la vérité de la livraison, les accusés de réception et les gabarits approuvés par le fournisseur. Le port SMS le dit lui-même : un puits prouve ce que vous auriez envoyé, pas qu'un opérateur l'accepterait, et l'adaptateur réel dépend de l'infrastructure. Aucun client réel de SMS n'est livré.

Le plan de la voix : une déclaration est portable, et une voix ne l'est pas. La voix d'un navigateur n'a pas de tampon, donc la boucle ne se ferme que sur le niveau natif. Cette machine peut parler anglais et ne peut pas l'entendre.

Ce que le terrain a en dictée dans le nuage et en modules de reconnaissance entraînés pour beaucoup de langues, le dossier a choisi de ne pas le livrer. La dictée libre a atteint 66,7 pour cent sur l'audio synthétique propre du volet lui-même.

Ce que le dossier affirme à la place : le dialogue est un rendu d'un monde déclaré jugé par un tribunal, déterministe par défaut. Le médium est un port avec un bac à sable, donc la conversation et sa facture sont répétées avant qu'aucun compte existe.

Le terrain est en tête sur certains points, et la limite vient ensuite, imprimée entière.

## 7. La limite

L'étude (12.25) contient deux erreurs que les exécutions de ce chapitre corrigent. La première : elle dit que la parole vers texte manque. À ce commit elle existe, par décision, pour les commandes et non pour la dictée. La seconde : elle dit qu'aucun message n'existe. Il existe un message de trois champs, entre identités d'une même plateforme, et je le montre :

```haro
oDb = new stzDatabase(":memory:")
oCom = StzPlatformQ("neighbourhood")
oCom.OpenCommonsOn(oDb)
oCom.PostMessage("customer", "kitchen", "one brik, no egg")
? @@(oCom.Inbox("kitchen"))
#--> [ [ "customer", "one brik, no egg" ] ]
```

C'est un expéditeur, un destinataire, un corps et une heure dans une table SQL. Il n'a ni médium, ni statut, ni parties. C'est le message que l'étude a trouvé absent, dans sa plus petite forme.

Ce qui est construit : la conversation gouvernée ; le port SMS et son bac à sable ; un vérificateur de signature de corps avec protection contre le rejeu, câblé à aucun fournisseur de messagerie ; la couche sémantique de cinq valeurs rendues en couleur, en earcon et en phrase. Construits aussi : la voix ; un message minimal dans le socle commun ; un ensemble fermé de phrases avec un refus ; et les intentions et portées déclarées du monde.

Ce qui est conçu : `Provides(:Messaging)` comme service du socle commun de la constellation. Un seul fichier de conception le dit, en deux lignes : un schéma qui range la messagerie parmi les communs, et une esquisse qui écrit `Provides(:Messaging)`. Le mot `Provides` n'est dans aucun fichier de code du répertoire de l'application. Le runtime du socle commun comme pendant opérationnel des fournitures et partages déclarés. Les surfaces conversationnelles pour une application de messagerie, le SMS, l'USSD, la voix et le chat web, la matrice de satisfaisabilité comme tribunal, les gabarits comme grammaire, un canal dans le profil de plateforme : ce sont les propositions B46 à B50 de l'étude. Elles sont celles d'une session, et non la conception de la bibliothèque. Une analyse parlée et un transport parlé : des démonstrations et des compositions, et non une unité.

Ce qui est absent :

- Des ports pour une application de messagerie, Telegram, l'USSD, et l'appel téléphonique : zéro résultat. Une session USSD n'a aucune forme dans la bibliothèque.
- Une projection conversationnelle d'un monde. La seule projection est `Generate`, qui connaît trois surfaces et en refuse une quatrième. Aucun shell ne rend une question ou un flux.
- Les unités de messagerie : canal, session avec une fenêtre ou un délai, gabarit, consentement. Aucune unité de consentement n'existe pour la messagerie. Le mot *consentement* apparaît dans l'instantané pour la frontière du microphone, dans des commentaires, et dans deux documents de conception en d'autres sens.
- Les vingt-deux verbes comme liste de la bibliothèque. `stzApp` en tient cinq comme cinq méthodes d'intention d'écran, et l'assistant derrière elles ne contrôle pas le mot qu'on lui donne. Les dix-sept autres sont dans la constitution et non dans la bibliothèque. La phrase-pont est appliquée à la main aujourd'hui.
- La question dans une autre langue que l'anglais. `AskIn` est en anglais, et le tuteur montre le motif en quatre langues. Dans une exécution de recherche à ce commit, `NaturallyIn` demandé pour le zarma a levé l'opaque "Unsupported object type!" et non "no pack for this language" ; aucun bloc de ce livre n'enregistre cet appel.
- Une voix pour les langues que les conceptions de produit nomment, le zarma, le haoussa et le fulfulde. Aucune ici ; la bibliothèque refuserait.
- **Une réponse contenant un espace, venant d'un téléphone.** Dans une exécution de recherche à ce commit, j'ai exécuté `ReplyIn("c", "grand couscous")` et il a levé une erreur, avec une variable non initialisée. Avec un trait d'union il a été admis. Aucun bloc de ce livre n'enregistre l'un ou l'autre résultat, comme le chapitre 18 le dit de la même faute. C'est la limite connue du chapitre 18, et elle est décisive ici, parce que les gens tapent des espaces dans un SMS. La conversation ci-dessus ne fonctionne que parce que les réponses sont des chiffres et des plats d'un seul mot.
- Des adaptateurs réels pour le SMS, pour une application de messagerie et pour une ligne téléphonique ; des accusés de réception de livraison ; des règles d'identifiant d'expéditeur.
- Rien dans le dossier ne tourne sur un vrai téléphone comme conversation.

`On(:whatsapp)`, `On(:ussd)`, `On(:voice)` et la matrice de satisfaisabilité sont ce qu'une étude a proposé, et je ne les présente pas comme ce que je compte construire. Je n'ai trouvé dans le dossier aucune décision de ma part de les construire, et la limite est la liste ci-dessus, où aucun d'eux n'existe.

Voilà la limite, imprimée entière ; les six portes suivent.

## 8. Six portes

**Le programmeur.** La question revient comme donnée. Vous écrivez le rendu et le lecteur de votre médium en une douzaine de lignes, et chaque réponse passe par la même porte quel que soit ce qui l'a portée.

**L'analyste.** Le but est le schéma de la conversation. La transcription dit quel message a produit quel fait. Le bac à sable compte la facture avant qu'un fournisseur existe.

**Le concepteur.** Votre utilisateur garde le téléphone qu'il a : une ligne de texte avec des numéros, ou une phrase parlée. Les verbes de la constitution sont la grammaire que vous rendez, et un verbe que le médium ne peut pas rendre devrait être une cellule rouge, et non une omission silencieuse. Je tiens cela pour une vue, non pour un résultat. C'est conçu et non construit, puisque la matrice n'existe pas.

**Le décideur.** Une conversation par SMS peut être chiffrée dans un test : deux noms de plats en arabe ont fait passer une question de 93 caractères d'un segment à deux. La question à poser à un fournisseur, qu'est-ce qui refuse une phrase que votre entreprise n'a pas approuvée, a ici une réponse : un ensemble fermé.

**Le formateur.** Le tuteur dit déjà l'étape manquante comme une question en quatre langues, dans des gabarits qui ne portent aucun code. Le dossier ne nomme pas d'apprenant sur un téléphone simple, et rien n'en sert un pour l'instant : il n'y a ni USSD ni application de messagerie.

**L'agent.** Vous pouvez proposer une réponse, et seule une phrase de l'ensemble fermé passe. Une phrase inventée est refusée avec sa raison. Et vous ne pouvez pas donner un sens à une phrase : l'auteur le déclare.

## 9. Exercice

Prenez une question que votre propre monde pose. Le monde à une relation de l'exercice du chapitre 18 fera l'affaire. Avant d'exécuter quoi que ce soit, écrivez sous chaque ligne la sortie que vous attendez :

1. le nombre de segments de votre rendu de la question, avec des noms en alphabet latin ;
2. ses segments si une option est un mot en écriture arabe ;
3. ce qui se passe quand la réponse du client est un chiffre qui n'a pas été offert ;
4. ce qui se passe quand la réponse est "yes please".

```haro exercise
? StzSmsSegments(YourRendering)[:segments]
#--> your prediction
? StzSmsSegments(YourRenderingWithOneArabicWord)[:segments]
#--> your prediction
```

Exécutez-le, avec le bac à sable et jamais un vrai envoi, pour que l'exercice ne touche à rien. La quatrième prédiction a levé une erreur dans mon exécution de recherche, et c'est la leçon. Si une promesse casse, ne la changez pas : expliquez d'abord la sortie.

Le chapitre suivant est l'environnement. Il déclare l'interface une fois, et chaque shell en est une projection ; une projection, comme un médium, peut ajouter des rendus, jamais des verbes.
