# FRENCH — how the French edition is written

The French is a translation of the English page, page for page, in the same voice (first person, the author's) and with the
same structure. The vocabulary below is the site's own French (`stzsite/data/glossary.json`, `content/fr/`), so the book and
the site say the same thing. Written 2026-10-09, Phase 6.

## What is translated and what is not

**Translated:** every sentence of prose; the title; the values of `stage:` in the front matter (built, designed, absent);
the headings; the cells of a table; the text of every `[AUTHOR: ...]` marker; list items.

**Never changed, byte for byte:**
- every code fence, whatever its tag, including the comments inside it and the strings it prints: the code is Haro and its
  promises are the run's. A French page runs the same blocks;
- the front matter keys and the values of `id`, `part`, `number`, `spine`, `narrations`, `site`, `guards`, `rulings`,
  `research`, `appendix`, `generated`, `law`, `figures`, `status`;
- the names of the library: classes, methods, functions, files, guards, narrations, commits (`stzKnowledgeGraph`, `Prove`, `book.json`);
- backtick spans (`` `like this` ``): they are code or names. Do not translate them;
- numbers, dates (written in French: 9 octobre 2026) and quotations of the library's own messages, which are in English
  and stay in English, in quotation marks;
- the proper names: Softanza, Haro, Reaxis, Softanzuter, Regexuter, AYOUNI.

## The shape

Keep the headings and their numbers. The nine fixed headings of a chapter, in French:

| # | English | French |
|---|---|---|
| 1 | The concept, as the field holds it | Le concept, tel que le terrain le tient |
| 2 | The first principle | Le premier principe |
| 3 | The Softanza form | La forme Softanza |
| 4 | The decision, and what I refused | La décision, et ce que j'ai refusé |
| 5 | The court | Le tribunal |
| 6 | The field, and where it leads | Le terrain, et où il mène |
| 7 | The limit | La limite |
| 8 | Six doors | Six portes |
| 9 | Exercise | Exercice |

The six doors keep their order: le programmeur, l'analyste, le concepteur, le décideur, le formateur, l'agent. The line that
opens each is bold: `**Le programmeur.** ...`. A heading that is not one of these (a `###`, or the unnumbered heading of a law chapter)
is translated freely.

Keep the same number of paragraphs, list items, table rows and [AUTHOR] markers. A bold sentence stays bold, an italic one italic.

## Voice and typography

- "I" is « je ». The reader is « vous ». The tone is the English one: plain, short sentences, no inflation, the loss printed beside the win.
- French quotation marks « ainsi », with a normal space inside. A non-breaking space before `:`, `;`, `?`, `!` is not needed:
  write the plain character, the reader's typography does the rest.
- Numbers of four digits or more are written with a space: 2 786. Decimals with a comma in prose (0,10), never inside a code span.
- Say « artisan du logiciel », never « fabricant » or « créateur ». Never write the word « substrat ».
- The former language is « l'ancien langage hôte »; its runtime is « le runtime de l'ancien langage hôte » (version 1.27).
- Haro, the language the book writes in, is « Haro ». A block is « un bloc », a promise « une promesse », a verdict « un verdict ».

## The words

| English | French | Note |
|---|---|---|
| court | tribunal | the site's word; "the court judges" = « le tribunal juge » |
| guard | garde | « une garde » (feminine); "narrated guard" = « garde narrée » |
| door (of foreign runtimes) | porte | and the six doors of a chapter: « six portes » |
| twin | jumeau | « le jumeau des fichiers » |
| world | monde | « un monde »; constellation stays « constellation » |
| bond | lien | between two worlds |
| commons | socle commun | |
| platform | plateforme | |
| engine | moteur | |
| layer | couche | core, base, max = noyau, base, max |
| refinement | raffinement | |
| promise | promesse | the `#-->` line |
| narration | narration | the author's article |
| declare | déclarer | « une déclaration » |
| crafter | artisan du logiciel | |
| stage words | mots d'étape | built = construit, designed = conçu, absent = absent |
| spine | colonne | « la colonne » (the nine chapters) |
| decision (box) | décision | |
| limit | limite | |
| field (the practice) | terrain | « ce que le terrain fait mieux » |
| gate | barrière | the registration gate, the production gate; never « porte » |
| commit, the governed act | valider, validation | « un acteur validant », « seul un acteur gouverné valide » |
| commit, in git | commit, commité | « à ce commit », « le commit imprimé »; never « validation » for the git object |
| rehearse | répéter | « répétition » |
| proposal, propose | proposition, proposer | |
| candidate | candidat | |
| admission | admission | « l'expression est libre, l'admission est gouvernée » |
| checkpoint | point de contrôle | |
| plan | plan | |
| posture | posture | |
| reversibility | réversibilité | reversible, compensable, irreversible = réversible, compensable, irréversible |
| lineage | filiation | |
| authority | autorité | and permission = permission |
| risk tier | niveau de risque | |
| gap (of a goal) | écart | |
| goal | but | |
| registry | registre | of services; and the register of innovations = le registre des innovations |
| sandbox | bac à sable | |
| fake | faux | « un faux » |
| double (test) | double | |
| live (posture) | réel | « le service réel » |
| lexicon | lexique | |
| pack (of a language) | paquet | « un paquet de langue » |
| facet | facette | and face (of Haro) = face |
| the interface constitution | la constitution de l'interface | never its product name |
| unperceived | non perçu | « un état, pas un échec » |
| wise coding | wise coding | the site's own use |
| the former host language | l'ancien langage hôte | |
| oracle | oracle | |
| the model (language model) | le modèle | |
| agent | agent | |
| AI model (where the bare word is ambiguous, VOICE-05) | modèle d'IA | « modèle de langage » stays for "language model" |
| AI agent (same) | agent d'IA | a person's agent stays « agent » / « mandataire » by context |
| actor | acteur | |
| plane (security, performance, sound, payments, agentic, system) | volet | « le volet de sécurité »; never « plan », which is the artefact a machine proposes |
| estate (the author's body of projects) | domaine de projets | « le domaine de projets », every time; « domaine » alone means a field of knowledge |
| workbench | atelier | « l'atelier répète la proposition »; the field's "language workbench" is « l'atelier de langages », and a merchant's workshop « la boutique » or « l'atelier du commerçant », said in full |
| floor (of the platform's picture) | étage | ch4's storeys; a *floor* as a minimum level ("a floor of trust") is « un plancher »: the French keeps apart what the English runs together |
| the next line (chapter 33) | la ligne suivante | the title of chapter 33, « La ligne suivante : une solution sur son propre moteur »; the part title is « Ce qui vient »; never « due » (VOICE-04) |
| ledger | registre | « le registre de sécurité », « le registre des décisions »; the same word as registry, the context tells them apart |
| window of service etc. | — | not in the book |

When a term is not here, take the site's French (`content/fr`), or the plainest French word, and keep it the same on every page you write.

## Appendices

Appendices E, F and G carry a generated part that the build writes; translate only the lead text of the source file. The build
writes the generated part in French itself.
Appendix D (the glossary) keeps one entry per English entry, with the French word in bold, in the order of the English entries.
