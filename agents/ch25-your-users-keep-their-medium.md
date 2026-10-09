# Your users keep their medium

Source: Chapter 25. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the governed conversation with its question as data; the SMS port and its sandbox, with the bill per segment in two alphabets; a verifier for the body of an inbound message; five semantic values rendered as colour, earcon and phrase; a voice that speaks, and hears a closed grammar; a closed set of sentences a business agrees to say; a message of three fields between identities of one platform; designed: the commons service of messaging; conversational surfaces for a messaging app, SMS, USSD and voice, with a satisfiability matrix as a court; templates as a grammar; the twenty-two verbs as a list the library holds; absent: a messaging app, USSD or a telephone line, in any form; a conversational projection of a world; a channel, a session, a template, consent; the question in a language other than English; a voice for Hausa, Zarma or Fulfulde; a reply with a space in it

Run: 11 of 11 blocks kept their promise, on 2026-10-09 02:57 UTC+01:00.

## 1. The concept, as the field holds it

Conversational commerce, or omnichannel: a business reaches its customers in the channels they already use, and a dialogue engine sits behind them. These are the practices, from general knowledge and not from a study of the record. Every date and every provider rule is to be re-read before print, as the study of the record says in its own "Not measured".

The dialogue frameworks own the dialogue model. The designer writes intents and flows in the framework's notation, and the framework understands free text with trained models and ships connectors to channels.

The business platform of a messaging app: messages arrive by a webhook, and the business may answer freely inside a service window that the customer opened, and outside it only with approved templates, through a verified business account.

The operators' gateways: SMS and USSD. SMS is billed per segment, and I measure this myself below. USSD is a session of short screens with a timeout, through an operator's gateway, country by country, on any phone without data. No file of the snapshot says anything about USSD.

And platform speech, in the library's own plan: Windows has one speech interface, macOS has another, and every modern browser has a third.

What they share is that the dialogue is written once per channel or once per framework, and the channel is a connector, a deployment detail. The chapter turns that picture around. The world is declared once, and the medium is a rendering of it.

## 2. The first principle

**A new medium adds renderings, never verbs.**

It is a sentence of the interface constitution, printed on the site: the grammar is closed, a new medium adds renderings and never verbs. The record is silent on whether the wording is mine. I quote it as the constitution's. [AUTHOR: Is the bridge sentence yours, to be told in the first person, or do I only quote it as the constitution's? And may the chapter list the twenty-two verbs while that repository is not public yet?]

The same sentence, built, for one family of values and not for the twenty-two verbs: the value is shared, and how it is rendered is each medium's own. It is a ruling by Central on my delegation, of 30 September 2026. It proves that the principle is not only a slogan. It is the shape of three working faces: colour, earcon, phrase.

For the floor of the dialogue, the code's own sentence: deterministic floor, no model needed. Chapter 17's law, applied to a medium.

## 3. The Softanza form

The library ships the question as data: a force, a subject, a relation, options and a reason. It ships the verbs, ask, reply, refuse and conclude, and the court. A medium is a rendering of the data and a reader of the reply, both written by the crafter in a few lines. Nothing in the library renders a question to a phone. What it ships is an English line, `AskIn`, which is already a text menu: "(1) cheese (2) olives". I say that in those words.

Two small functions of my own are the whole of the medium: one that renders the question to a line of text, and one that reads the reply. The reading matters, and I show why in the third block:

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

> run: kept

The question is data, so any medium renders it. And the medium's own law, here that SMS is billed per segment and the alphabet decides, is a test and not a surprise. The English text is 93 characters and one segment. The same frame with two Arabic dish names is 89 units, in two segments, because the encoding changes. The telephone number is invented, and only the country code, which is Niger's, is real.

Now the whole conversation, rehearsed over the SMS sandbox before any account exists. A conversation is a loop of the library's verbs: the medium carries each question out and each reply in. The assertions are the bill and the refusal. The refusal of "7" is the library's own, as in chapter 18; the difference is that it arrives from a phone, and the sandbox counted four messages and four segments. Nothing in the loop is a model:

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

> run: kept

**The reader of the medium is the medium's job.** An inbound SMS is a string. The library separates numbers, which are option indices, from strings, which are values, and it does not guess. Its own comment: an index can never be mistaken for a literal value. So the medium's reader must decide which it is. With no options on the table, the text "2" is admitted as a dish named 2:

```haro
oKT = new stzKnowledgeGraph("trap")
oKT.Know("order1", "order")
oKT.AddConversationQ("c").SetGoal(StzGoalQ().RequireEach("order", "dish"))
oKT.AskIn("c")
? @@(oKT.ReplyIn("c", "2")[:admitted])
#--> [ "2" ]
```

> run: kept

In the block before, my `ReadReply` turned the text "2" into the number 2, and the option was picked. This is the sharpest sentence about the bridge: a medium adds renderings, and it adds a reading too. The reading is where a user's culture lives, the digits, the words, a local "OUI".

**An outage is not a rejection.** The medium refuses in its own terms. A malformed number, with no `+`, is not an E.164 number, and it is rejected: fix the data. An outage is refused: retry:

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

> run: kept

**An inbound message is believed only after its signature is verified.** The way in is the pattern the payments plane built, and the verifier is generic, over the body. No provider's header or body format is modelled, and the JSON is invented. Times are passed in, so no clock is read:

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

> run: kept

A replayed body inside the window gave "replay detected" in my probe.

**One value, many renderings.** The bridge's shape, built for the five semantic values of the interface constitution. Colour, earcon and phrase render one value. `muted` is silence in sound and a treatment in colour. A value the law does not know is refused:

```haro
? @@(StzSemanticValues())
#--> [ "danger", "warning", "info", "success", "muted" ]
oE = new stzEarcons()
? oE.WouldFireAt("Catastrophe", 1)
#--> 0
? StzColorToNumber("danger.muted") != StzColorToNumber("success.muted")
#--> 1
```

> run: kept

**The voice: spoken, heard, meant.** Text to sound, sound to text, text to meaning. The medium called voice renders and reads with a closed grammar, and the meaning is my declaration. This block needs a French voice and a French recogniser. This machine speaks two languages and hears one, and a machine without them would give another answer, so the output shown is the one recorded on this machine. No microphone, no file, no network: the recogniser is the in-process one:

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

> run: kept

The refusal's reason says that `catastrophe` is not one of the five semantic values. I do not print the recogniser's confidence, which varies by machine.

**The world declares its verbs and its reach, and its code names no medium.** A world holds screens declared by intent, five of the twenty-two verbs, and a list of what it reaches. Nothing refuses `:whatsapp` when it is declared:

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

> run: kept

`Acts(...)` is stored and not narrated. And the stage as a run: the platform refuses a surface it cannot generate, and the refusal names the three surfaces it has. This block creates an empty folder in the working directory:

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

> run: kept

The same refusal answers `:ussd`.

**What may be said to a customer is a closed set.** The court of what is said has a mechanism today: a closed enumeration compiled to a grammar, which chapters 11 and 19 use for a language and for a model's output. Here it holds the replies that a business is willing to send. It is not a messaging-template unit, and there is none. Two things to print with it: the message says "the model answered" whoever the speaker is, and the enumeration is case-folded:

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

> run: kept

### The restaurant's medium

Chapter 1 says that the owner of the restaurant made his first demonstration over a messaging app, and chapter 2 said, in its first draft, that a messaging app was among his tools. The record does not support either sentence as it stands, and I correct chapter 2 and flag chapter 1, which is your text. His own report of 4 July 2026 gives his current tool as a spreadsheet, and asks for a web page opened by a QR code or by a button for a social network, with nothing to download. The line about various apps, a messaging app among them, is the label of an option in the scoping form, and it is not what he ticked. "Simple like a messaging app" is simulated in the project, as chapter 28 already found.

So the restaurant is the first form of the sentence of this chapter, and not an example of the messaging medium. The customer keeps their medium: a link that opens in the browser they already have. The messaging medium, as a thesis, is unbuilt. [AUTHOR: Which restaurant story should the chapter tell: the link as the first form of "the customer keeps their medium", with the messaging medium as an unbuilt thesis, or a statement from you about the owner's use of a messaging app, which the record does not hold? Chapter 1 carries the sentence I have flagged.]

## 4. The decision, and what I refused

**Messaging, the question.** The study's report of my ask: conversations happen programmatically by default, or through minimal configuration, without obliging the users to change their usability cultures. The study's section is titled "ruled" and not "ruled by the author", and its proposals for the conversational surfaces are a session's. The record holds no ruling of mine that adopts them. I say *proposed*, not *decided*.

**A conversation needs no model.** The floor is deterministic. A model can upgrade the fluency behind the same surface.

**Voice is not a paradigm.** The plan of record says out until asked in writing: all of dialogue management, wake words, intent parsing and barge-in.

**Commands, not transcription: a measured refusal.** The gate was set before the numbers: free dictation ships at eighty per cent exact and 0.60 mean confidence. The run gave 66.7 per cent and 0.600, which failed. The closed grammar gave a hundred per cent and 0.898, which passed. So this face has no `Transcribe()`, and never will until a better recogniser exists.

**Refuse, never substitute.** Speaking French to an operator who asked for English is worse than saying nothing.

**No inferred meaning.** The author still declares the meaning. A sixth value would be a constitutional amendment wearing a library's clothes.

**A sink proves what you would have sent.** The SMS port's honest limit: carrier filtering, sender-ID rules, per-country alphabet quirks, and asynchronous delivery receipts, none of which is modelled here.

**The screen acknowledges, and the sound is not the acknowledgement.**

## 5. The court

`sms_port_narrated` proves the segment law, with its boundaries at 160 and 161, 306 and 307, the emoji cliff at 100 to 102 units, 71 Arabic letters making two segments, and the nine extension characters; E.164; the sink and its bill; the outage against the rejection; and the refusal in production. I ran it once, and 53 of 53 assertions passed. `wisecoding_rich_narrated` is chapter 18's: the frame, the numbered options, the refusal of a number nobody offered, the checkpoints with a lifetime. `payments_webhooks_narrated` proves that an inbound signature is verified before it is believed: unsigned, forged, replayed. `sound_semantics_narrated` proves that the five values are the law's, that four sound and `muted` is silent, and that an invented value is refused. `sound_listener_narrated` proves the closed grammar, that no match is a result, and that the confidence is a separate call; I ran it once, and 21 passed. `sound_convergence_narrated` proves that the loop closes for the four states, that the language is negotiated per direction, that a sixth value is refused at declaration, and that a stranger's phrase gives no meaning.

A caveat for the court line. The sound guards need the engine's sound library, and for the loop, a voice and a recogniser. On a machine without them the voice guards print "skipped" and pass. A pass there proves nothing about speech. The guards for SMS and for the conversation have no such dependency.

## 6. The field, and where it leads

The record's own count, in the study of 12.25: of the constituent units of messaging, eighteen in all, what is missing. Its sentence that the word for a messaging app appears in no code file and no design document of the library, and USSD in none, I re-measured at this commit and confirmed. The only hits are word-list data files.

The frameworks lead in understanding and in connectors. Chapter 18 states Softanza's side from the code: the conversation asks one slot at a time, over a graph the user must first have declared, and it does not understand an open reply.

The field leads in channel coverage and in delivery truth, receipts and provider-approved templates. The SMS port says it itself: a sink proves what you would have sent, not that a carrier would accept it, and the live adapter is infrastructure-gated. No live client for SMS ships.

The voice plan: a declaration is portable, and a voice is not. A browser's voice has no buffer, so the loop closes on the native tier only. This machine can speak English and cannot hear it.

What the field has in cloud dictation and in trained recognisers for many languages, the record chose not to ship. Free dictation reached 66.7 per cent on the plane's own clean synthetic audio.

What the record claims instead: the dialogue is a rendering of a declared world judged by a court, deterministic by default. The medium is a port with a sandbox, so the conversation and its bill are rehearsed before an account exists.

## 7. The limit

The study (12.25) has two errors that this chapter's runs correct. The first: it says speech to text is missing. At this commit it exists, by decision, for commands and not for dictation. The second: it says no message exists. There is a message of three fields, between identities of one platform, and I show it:

```haro
oDb = new stzDatabase(":memory:")
oCom = StzPlatformQ("neighbourhood")
oCom.OpenCommonsOn(oDb)
oCom.PostMessage("customer", "kitchen", "one brik, no egg")
? @@(oCom.Inbox("kitchen"))
#--> [ [ "customer", "one brik, no egg" ] ]
```

> run: kept

It is a sender, a recipient, a body and a time in a SQL table. It has no medium, no status and no parts. It is the message the study found absent, in its smallest form.

What is built: the governed conversation; the SMS port and its sandbox; a body-signature verifier with replay protection, wired to no messaging provider; the semantic layer of five values rendered as colour, earcon and phrase; the voice; a minimal message in the commons; a closed set of sentences with a refusal; and the world's declared intents and reaches.

What is designed: `Provides(:Messaging)` as a commons service of the constellation. The design says so in two places, and the word `Provides` is in no code file of the application folder. The commons runtime as the operational counterpart of the declared provides and shares. Conversational surfaces for a messaging app, SMS, USSD, voice and web chat, the satisfiability matrix as a court, templates as a grammar, a channel in the platform profile: these are the study's five proposals, a session's, and not the library's design. A spoken analysis and a spoken transport: demos and compositions, and not a unit.

What is absent:

- Ports for a messaging app, Telegram, USSD, and the telephone call: zero hits. A USSD session has no shape in the library.
- A conversational projection of a world. The only projection is `Generate`, which knows three surfaces and refuses a fourth. No shell renders a question or a flow.
- The messaging units: channel, session with a window or a timeout, template, consent. The word *consent* appears in the snapshot only as the microphone's boundary, in comments.
- The twenty-two verbs as a library list. `stzApp` holds five of them as screen intents, unchecked, since any word is accepted. The other seventeen are in the constitution and not in the library. The bridge sentence is applied by hand today.
- The question in a language other than English. `AskIn` is English, and the tutor shows the pattern in four languages. `NaturallyIn` asked for Zarma raises the opaque "Unsupported object type!" and not "no pack for this language".
- A voice for the languages that the product designs name, Zarma, Hausa and Fulfulde. None here; the library would refuse.
- **A reply with a space in it, from a phone.** I ran `ReplyIn("c", "grand couscous")` and it raised, with an uninitialised variable. With a hyphen it is admitted. This is chapter 18's known limit, and it is decisive here, because people type spaces in a text message. The conversation above works only because the replies are digits and one-word dishes.
- Live adapters for SMS, for a messaging app and for a telephone line; delivery receipts; sender-ID rules.
- Nothing in the record runs on a real phone as a conversation.

[AUTHOR: May the chapter present `On(:whatsapp)`, `On(:ussd)`, `On(:voice)` and the satisfiability matrix as what you mean to build, with the limit beside them, or only as what a study proposed?]

## 8. Six doors

**The programmer.** The question comes back as data. You write the rendering and the reader for your medium in ten lines, and every reply goes through the same door whatever carried it.

**The analyst.** The goal is the schema of the conversation. The transcript says which message produced which fact. The sandbox counts the bill before a provider exists.

**The designer.** Your user keeps the phone they have: a text line with numbers, or a spoken phrase. The constitution's verbs are the grammar you render, and a verb the medium cannot render should be a red cell, and not a silent omission. That is designed and not built, since the matrix does not exist.

**The decision-maker.** A conversation by SMS can be priced in a test: two Arabic dish names moved a 93-character question from one segment to two. The question to ask a vendor, what refuses a sentence your business did not approve, has an answer here: a closed set.

**The educator.** The tutor already says the missing step as a question in four languages, in templates that carry no code. A learner on a plain phone is a case the record names and does not yet serve.

**The agent.** You may propose a reply, and only a sentence of the closed set passes. An invented one is refused with its reason. And you cannot give a meaning to a phrase: the author declares it.

## 9. Exercise

Take a question your own world asks. The one-relation world of chapter 18's exercise will do. Before you run anything, write under each line the output you expect:

1. the number of segments of your rendering of the question, with names in the Latin alphabet;
2. its segments if one option is a word in Arabic script;
3. what happens when the customer's reply is a digit that was not offered;
4. what happens when the reply is "yes please".

```haro exercise
? StzSmsSegments(YourRendering)[:segments]
#--> your prediction
? StzSmsSegments(YourRenderingWithOneArabicWord)[:segments]
#--> your prediction
```

> run: exercise

Run it, with the sandbox and never a real send, so that the exercise touches nothing. The fourth prediction raises today, and that is the lesson. If a promise breaks, do not change it: explain the output first.
