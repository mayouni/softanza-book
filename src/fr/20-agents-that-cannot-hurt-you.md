---
id: agents-that-cannot-hurt-you
part: 4
number: 20
title: Des agents qui ne peuvent pas vous nuire
spine: false
narrations: [stz-agents-that-cannot-hurt-you-narration.md, stz-service-virtualization-code-first-subscribe-later.md]
site: [agentic, security]
guards: [safeworld_narrated, agentfile_narrated, agentloop_engine_narrated, containment_drill_narrated, virtual_system_twin_narrated]
stage:
  built: "la réversibilité comme contrat déclaré et comme barrière d'enregistrement ; la posture confrontée à la réversibilité, à la porte et au chargement ; l'atelier, le plan, le rejet du relecteur, l'acteur validant sous une portée ; l'exercice de confinement ; les emplacements bornés et la file du moteur (la boîte de réception bornée n'est testée qu'en Zig, non exécutée pour le livre)"
  designed: "le côté de l'agent dans la négociation autour d'un plan ; la salle d'examen ; les branches comme esprits parallèles ; les jumeaux pour les bases de données, les interfaces et les réseaux"
  absent: "un plan sans exécutant qui soit refusé ; un classement des risques d'un plan ; le code déjà en cours d'exécution dans le processus, qui est hors de portée ; le Droit à un humain comme contrôle machine"
status: draft
rulings: ["12.18", "12.19", "12.22", "12.23", "12.29"]
research: research/ch20.md
---

Dans ce chapitre, je prends la moitié de l'action de ce que le chapitre 17 a dit de l'esprit entier : ce qui se passe quand la proposition rencontre le monde. Je montre quatre étapes en code : l'agent d'IA propose, l'atelier répète, le tribunal juge, et seul un acteur gouverné valide. Viennent ensuite les cas où une étape ne tient pas. Je dis ce que j'ai refusé : les agents sûrs, un contrôle de permission comme frontière, un second atelier pour les machines, une barrière facultative. Et je dis où cela s'arrête : un plan sans aucun exécutant est permis, et la boucle vérifie qu'une déclaration de couverture existe, non qu'elle est vraie. Le principe est celui de la doctrine : ne construisez pas des agents sûrs ; construisez un monde sûr, et lâchez-y des agents ordinaires.

## 1. Le concept, tel que le terrain le tient

Sur le terrain, la sûreté est une propriété de l'agent d'IA. Le document de doctrine de la bibliothèque énumère ce que le terrain offre : l'alignement, les garde-fous, les invites de confirmation, une case à cocher qui dit qu'un humain est dans la boucle. Les agents à outils, et les agents autonomes qui en descendent, laissent les appels d'outils du modèle toucher la réalité immédiatement, avec une invite de confirmation. Les agents d'usage de l'ordinateur tournent dans une machine virtuelle en bac à sable, qui contient un processus et qui, dans les mots de la doctrine, ne distingue pas un déplacement de fichier d'un brassage d'octets aléatoires.

Le meilleur conseil du terrain, que, selon la narration, tout guide sérieux de 2026 donne (elle paraphrase une feuille de route), est de séparer la planification de l'exécution et de placer entre les deux une approbation humaine. C'est un bon conseil, et c'est un conseil : un patron que vous implémentez, et que vous pouvez oublier. Les listes de menaces du terrain, dont la liste de risques de l'OWASP pour les applications agentiques, sont des lentilles, et le dossier s'en sert ainsi.

Donc la posture du terrain, en une ligne, est que l'agent est un modèle d'IA dans une boucle, et que la sûreté est de la vigilance autour de lui. C'est de la connaissance générale, et non une étude du dossier, sauf là où je nomme le document. Le chapitre 17 l'a dit de l'esprit entier. Ce chapitre prend la moitié de l'action : ce qui se passe quand la proposition rencontre le monde.

## 2. Le premier principe

**Ne construisez pas des agents sûrs. Construisez un monde sûr, et lâchez-y des agents ordinaires.**

La phrase est dans le document de doctrine de la bibliothèque : « We will not build safe agents. We will build a safe world, and let ordinary agents loose inside it. » Le document en donne la moitié structurelle en une phrase de plus. Le seul artefact qui quitte jamais son monde est un plan de mise à jour, et les plans sont exécutés par quelqu'un d'autre. Le document ne porte ni date ni ligne d'auteur dans son en-tête, et git l'enregistre pour la première fois dans un commit du 9 juillet 2026. Le chapitre tient la phrase pour celle du document, datée par ce premier commit, et ne donne pas de date d'écriture.

## 3. La forme Softanza

Quatre étapes, dans la forme que l'étude du dossier leur donne : l'agent d'IA propose, l'atelier répète, le tribunal juge, et seul un acteur gouverné valide. Je montrerai chacune en code, puis les cas où une étape ne tient pas.

**Cet agent peut-il exister ?** Avant qu'un agent ne fasse un seul tick, la gouvernance pose la question, et elle la pose quand la réponse est gratuite. Un agent qui ne déclare aucune couverture, une phrase disant ce qu'il couvre, est refusé. Un agent qui ne déclare aucune classe de réversibilité est refusé aussi : réversible, compensable ou irréversible. Les deux refus sont dans les phrases du moteur lui-même, et la porte de l'ancien langage hôte les répète. Que dit-elle à un agent qui ne déclare aucune couverture, et à un agent qui ne déclare aucune classe de réversibilité ? Exécutez-le :

```haro
oGov = new stzGovernance("shop")
oGov {
	DeclareReversibility("restocker", :Compensable)
	? ReversibilityOf("restocker")
	#--> compensable
	? MayRegister("mystery", "", "reversible")
	#--> 0
	? Why()
	#--> AGENTLOOP-R4: agent 'mystery' declares no coverage statement. Registration refuses it. Say what this agent covers, in one sentence, before the loop will run it. Law 18: nothing schedules what nobody has stated the reach of.
	? MayRegister("mystery", "reorders stock", "")
	#--> 0
	? Why()
	#--> AGENTLOOP-R5: agent 'mystery' declares no reversibility class. Registration refuses it. Declare one of: reversible | compensable | irreversible. Law 18: an agent whose reversal nobody stated cannot be scheduled by something that cannot undo it.
	? MayRegister("mystery", "reorders stock", :Compensable)
	#--> 1
}
```

Le premier refus se termine sur sa loi : rien ne planifie ce dont personne n'a énoncé la portée. Le numéro qu'il porte appartient à la liste des lois propre à la bibliothèque, que ce livre n'imprime pas. Avec les deux déclarées, le troisième appel répond `1`.

La réversibilité est le sixième contrat de la gouvernance, à côté du risque, de l'autorité, de la validation, de la mise hors service et de la filiation. Elle est orthogonale au risque : un acte de faible risque qui ne peut pas être défait mérite plus de cérémonie qu'un acte de grand risque qui peut l'être.

**Plus un acte est difficile à défaire, plus le code qui l'accomplit doit être digne de confiance.** Quelles postures peuvent accomplir quelles classes d'acte ? Voici la table entière, imprimée par une boucle propre au livre :

```haro
aPostures = [ "trusted", "external", "sandboxed" ]
aClasses = [ "reversible", "compensable", "irreversible" ]
for cP in aPostures
	cRow = cP + ":"
	for cC in aClasses
		if StzPostureReversibilityRefusal(cP, cC) = ""
			cRow += " yes"
		else
			cRow += " no"
		ok
	next
	? cRow
next
#--> trusted: yes yes yes
#--> external: yes yes no
#--> sandboxed: yes no no
? StzPostureReversibilityRefusal("sandboxed", "irreversible")
#--> a 'sandboxed' posture does not cover 'irreversible' work -- the harder an act is to undo, the more trusted the code performing it must be (reversibility x posture, ruling 3.2)
```

Lisez les lignes de haut en bas : le code de confiance peut accomplir les trois classes d'acte, le code externe les deux premières, le code en bac à sable seulement la réversible. La dernière ligne demande le refus et imprime sa phrase.

**L'agent s'exécute, croit avoir agi, et le disque ne bouge pas.** Un agent d'IA est un fichier et quelques fonctions. Sa fonction écrit une liste de prix. On lui donne un atelier, et la fonction atteint l'atelier comme un objet ambiant pendant un cycle, sans changement dans sa signature. La compétence vérifie son propre travail et le fait est appris. Après un cycle, le vrai fichier existe-t-il ? Interrogez le disque, puis l'atelier :

```haro
StzAllowAgentFunction("ScribblePrices", "trusted")
cFx = StzReplace(WorkingDirectory(), "\", "/") + "/_fixture"
StzDirCreatePath(cFx)
$cPrices = cFx + "/prices.csv"
cPia = "pia: 2
name: scribbler
kind: pi
coverage: writes a price list and records that it did
reversibility: compensable
schedule:
  timer: 20
skills:
  - name: scribble
    when: always
    does: ring:ScribblePrices
    verify: fact prices were written
    posture: trusted
"
oAg = StzAgentDeclarationQ(cPia).ToAgent()
oAg {
	GiveWorkbench()
	? Cycle()
	#--> 1
	? MemoryQ().Fact("prices", "were", "written")
	#--> 1
	? StzFileExists($cPrices)
	#--> 0
	? WorkbenchQ().Exists($cPrices)
	#--> 1
	? WorkbenchQ().ContentOf($cPrices)
	#--> espresso,2.40
	#--> flat-white,3.10
}

func ScribblePrices(poMemory)
	StzActiveWorkbenchQ().WriteFile($cPrices, "espresso,2.40" + char(10) + "flat-white,3.10")
	poMemory.Learn("prices", "were", "written")
```

Le fichier vit dans le jumeau. L'agent croit avoir agi, et le disque n'a pas bougé !

Deux lignes décident qui peut agir. `posture: trusted` est dans le fichier, parce qu'une clause `ring:` doit porter une posture. `StzAllowAgentFunction` est une ligne du code de la plateforme, et non du fichier de l'agent, et elle décide quelles fonctions un fichier peut appeler.

**Le seul export est un plan, et il se narre lui-même.** Le tick n'exporte vers la réalité qu'un plan, et rien d'autre. Le plan dit ce qu'il ferait avant que quoi que ce soit ne soit tenté. Un modèle de langage désigné comme son exécutant est refusé avant toute tentative : `actor 'eager-llm' cannot commit -- it lacks the 'effectful' capability (required by operation 1)`. Un acteur nommé sous une portée qui ne couvre pas le chemin ne valide rien : le disque n'a toujours pas bougé. Le même acteur sous une portée qui couvre le chemin valide une fois, et la piste d'audit se lit `[ [ 1, "committed", "write_file", "shop-committer" ] ]`. Qui peut valider, et quand le disque bouge-t-il enfin ? Dans ce bloc, la réalité change ici, et seulement ici :

```haro
oPlan = oAg.GenerateUpdatePlan()
? StzReplace(oPlan.Narration(), cFx, "<fixture>")
#--> Update plan (1 of 1 operations to commit):
#-->   * 1. write 29 bytes to '<fixture>/prices.csv'
oPlan.SetExecutor(LLMActor("eager-llm"))
? oPlan.MayCommit()[2]
#--> actor 'eager-llm' cannot commit -- it lacks the 'effectful' capability (required by operation 1)
oScope = new stzCommitScope()
oScope.AllowUnder("/somewhere/else")
oPlan2 = oAg.GenerateUpdatePlan()
oPlan2.SetExecutor(PIActor("shop-committer"))
oPlan2.SetScope(oScope)
oPlan2.Execute()
? StzFileExists($cPrices)
#--> 0
oScope3 = new stzCommitScope()
oScope3.AllowUnder(cFx)
oPlan3 = oAg.GenerateUpdatePlan()
oPlan3.SetExecutor(PIActor("shop-committer"))
oPlan3.SetScope(oScope3)
oPlan3.Execute()
? StzFileExists($cPrices)
#--> 1
? @@(oPlan3.AuditTrail())
#--> [ [ 1, "committed", "write_file", "shop-committer" ] ]
StzDirDeleteAll(cFx)
```

J'ai remplacé le chemin absolu dans la narration pour que la sortie soit stable. Un plan inclut le chemin du fichier qu'il écrirait.

**Le tribunal au chargement.** La table ci-dessus est-elle appliquée quand le fichier est chargé, avant le premier tick ? Prenez le même fichier, rendez l'agent irréversible, et mettez son code en bac à sable :

```haro
cIrrev = StzReplace(StzReplace(cPia, "reversibility: compensable", "reversibility: irreversible"), "posture: trusted", "posture: sandboxed")
oD = StzAgentDeclarationQ(cIrrev)
? oD.IsValid()
#--> 0
? oD.CiteFindings()
#--> [pia-posture-reversibility @ skills.scribble.posture] a 'sandboxed' posture does not cover 'irreversible' work -- the harder an act is to undo, the more trusted the code performing it must be (reversibility x posture, ruling 3.2)
```

Le tribunal répond par la phrase même de la table : `a 'sandboxed' posture does not cover 'irreversible' work`. La même règle, au chargement : le fichier est refusé avant son premier tick !

**Une proposition qui tourne mal.** Un rangement qui supprime chaque fichier d'un répertoire, mené ici à la main à travers le jumeau comme le ferait un agent, propose trente suppressions. Le plan liste trente opérations et en signale trente comme des risques. Un modèle de langage qui demande à valider est refusé. Et quand il appelle `Execute()` malgré tout, combien de fichiers reste-t-il ? Comptez-les :

```haro
cDir = StzReplace(WorkingDirectory(), "\", "/") + "/_course"
StzDirCreatePath(cDir)
for i = 1 to 30
	StzFileWrite(cDir + "/lesson" + i + ".txt", "lesson " + i)
next
oBench = new stzVirtualFileSystem()
oBench.SetActor("tidy-bot")
for i = 1 to 30
	oBench.MirrorFile(cDir + "/lesson" + i + ".txt")
	oBench.DeleteFile(cDir + "/lesson" + i + ".txt")
next
oBig = oBench.GenerateUpdatePlan()
? oBig.NumberOfOperations()
#--> 30
? len(oBig.Risks())
#--> 30
oBig.SetExecutor(LLMActor("helper-llm"))
? oBig.MayCommit()[2]
#--> actor 'helper-llm' cannot commit -- it lacks the 'effectful' capability (required by operation 1)
oBig.Execute()
nLeft = 0
for i = 1 to 30
	nLeft += StzFileExists(cDir + "/lesson" + i + ".txt")
next
? nLeft
#--> 30
```

Trente ! Le modèle d'IA a demandé, a été refusé, a appelé `Execute()` malgré tout, et rien n'a changé sur le disque.

Le site montre cela avec un cours plus grand, dans sa démonstration d'éducation du 30 septembre 2026, que je n'ai pas exécutée pour ce livre, et il imprime un compte de six cent dix. Ce chiffre est celui du site, cité avec sa source et sa date. J'imprime trente, parce que trente est ce que ce bloc exécute.

**Une personne peut discuter avec un plan.** Le plan est un médium. Un relecteur rejette une étape, avec une raison. Que font les vingt-neuf autres étapes, et que reste-t-il sur le disque ? Le bloc imprime les comptes, non le nom du fichier :

```haro
oRev = oBench.GenerateUpdatePlan()
oRev.RejectOperation(2, "reviewer: keep lesson 2")
oRev.SetExecutor(PIActor("oncall"))
oScopeC = new stzCommitScope()
oScopeC.AllowUnder(cDir)
oRev.SetScope(oScopeC)
aRes = oRev.Execute()
? aRes[1][2]
#--> 29
? aRes[2][2]
#--> 1
nLeft = 0
for i = 1 to 30
	nLeft += StzFileExists(cDir + "/lesson" + i + ".txt")
next
? nLeft
#--> 1
StzDirDeleteAll(cDir)
```

Un acteur nommé sous une portée valide les vingt-neuf autres (`29`) ; une est sautée (`1`) ; et un fichier reste sur le disque (`1`), celui de l'étape que le relecteur a protégée.

**Une règle, deux couches, les mêmes mots.** Le refus que le chapitre 17 a montré au graphe, et que le fichier a montré plus haut, est aussi appliqué dans la boucle de ticks propre au moteur, à l'enregistrement. Il l'est dans la phrase de la règle du graphe, no-llm-effectful. Un modèle d'IA qui a la capacité de produire des effets est refusé. Un modèle qui ne l'a pas s'enregistre comme tout autre emplacement, un emplacement étant la place que prend un agent dans la boucle :

```haro
StzResetEngineAgentLoop()
nL = stzenginezutercreate("summarizer")
? stzengineagentloopregister(nL, 1, 1, 0, 1, 0, 10, "summarises tickets")
#--> -6
? stzengineagentlooplastrefusal()
#--> AGENTLOOP-R6: agent 'summarizer' (slot 0) breaks the rule no-llm-effectful -- llm actor holds 'effectful' -- an LLM proposes, only a pi-gate commits. Registration refuses it. Drop the effectful capability, or register it as a pi-gated composition rather than an llm actor.
nL2 = stzenginezutercreate("proposer")
? stzengineagentloopregister(nL2, 1, 1, 0, 0, 0, 10, "proposes summaries")
#--> 0
StzResetEngineAgentLoop()
```

Le moteur a refusé le résumeur, dans les mots de la règle du graphe ! Les arguments après le premier, qui est l'agent lui-même, sont, dans l'ordre où la garde les donne : le genre (1 est un modèle d'IA), la classe de réversibilité, le déclencheur et la capacité. Ce qui reste est la priorité, l'intervalle en millisecondes et la phrase de couverture. Ce sont les noms de bas niveau du moteur, et je les montre pour que vous voyiez le refus venir du moteur, dans les mêmes mots.

**Un agent de l'effectif propre du domaine de projets, répété.** Jusqu'au 22 août 2026, un agent de l'effectif propre du domaine de projets, celui qui fait tourner le registre, déplaçait directement un vrai fichier de journal, sur un tick. Il n'avait ni plan, ni portée, ni acteur validant.

Un registre, ici, est un relevé de ce qui s'est passé, tenu dans l'ordre où cela s'est passé. Cet agent fait tourner le registre propre du domaine de projets. Le chapitre 21 a le registre de sécurité, que le tribunal écrit et jamais la chose qu'il juge, une chaîne de hachage où une ligne modifiée est nommée. Le chapitre 23 a le registre de traversées de la constellation, avec les durées. Le mot a un autre sens ailleurs : l'une des cinq formes que peut prendre une réponse, ou le registre des innovations de l'annexe A.

La doctrine avait été écrite avant d'être vraie, et le dossier l'a attrapé le jour même. Depuis, la fonction qui écrit pour cet agent a un chemin de répétition. Dans le tick d'un agent qui tient un atelier, elle écrit dans le jumeau. Hors d'un tel tick, dans l'état de migration que le domaine de projets vivant fait encore tourner, c'est toujours l'écriture directe. La déclaration ci-dessous est la mienne, écrite pour ce livre ; ce n'est pas le fichier d'effectif vivant, que je n'ai pas exécuté. Avec un atelier, l'agent déplace le fichier dans le jumeau. Deux compétences se déclenchent et vérifient ; le vrai fichier de journal est là où il était ; aucune archive n'existe ; le tick a exporté un plan. Et seul l'acteur validant, sous une portée, déplace le fichier :

```haro
cEstate = StzReplace(WorkingDirectory(), "\", "/") + "/_estate"
StzDirCreatePath(cEstate + "/dashboard")
StzDirCreatePath(cEstate + "/journal")
SetEnvVar("STZ_SOFTANZA_ROOT", cEstate)
StzFileWrite(cEstate + "/journal/2000-01-scar.md", "an old journal entry" + char(10))
StzFileWrite(cEstate + "/dashboard/SESSION-LOG.md", "# SESSION-LOG" + char(10) + char(10) + "2000-01-15 09:00 | someone | long ago" + char(10))
StzAllowAgentFunction("RollRelocateMonths", "trusted")
StzAllowAgentFunction("RollWritePointer", "trusted")
cRoll = "pia: 2
name: ledger-roll
kind: pi
coverage: moves journal months before the current one into archive and leaves a pointer
reversibility: reversible
schedule:
  event: roll
governance:
  authority: delegated
  risks:
    relocate-evidence: 2
  grants:
    - relocate-evidence
skills:
  - name: relocate
    when: always
    does: ring:RollRelocateMonths
    verify: fact archive holds month
    effect: relocate-evidence
    posture: trusted
  - name: pointer
    when: fact archive holds month
    does: ring:RollWritePointer
    verify: fact ledger holds pointer
    effect: relocate-evidence
    posture: trusted
"
oRoll = StzAgentDeclarationQ(cRoll).ToAgent()
oRoll.GiveWorkbench()
? oRoll.Cycle()
#--> 2
? StzFileExists(cEstate + "/journal/2000-01-scar.md")
#--> 1
? StzFileExists(cEstate + "/journal/archive/2000-01-scar.md")
#--> 0
oRP = oRoll.GenerateUpdatePlan()
? oRP.NumberOfOperations()
#--> 7
? len(oRP.Risks()) >= 1
#--> 1
oRP.SetExecutor(PIActor("roll-committer"))
oScopeR = new stzCommitScope()
oScopeR.AllowUnder(cEstate)
oRP.SetScope(oScopeR)
oRP.Execute()
? StzFileExists(cEstate + "/journal/2000-01-scar.md")
#--> 0
? StzFileExists(cEstate + "/journal/archive/2000-01-scar.md")
#--> 1
StzDirDeleteAll(cEstate)
```

Le compte de sept opérations est ce que cette exécution mesure. La garde de la bibliothèque ne promet qu'au moins cinq.

Les blocs ont montré ce que fait le monde ; la section 4 dit ce que j'ai refusé de construire à la place.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé les agents sûrs.** La raison de la doctrine est que la sûreté du terrain essaie de rendre digne de confiance un acteur fondamentalement imprévisible. Je tiens cette raison pour une vue, non pour un résultat. L'image de la doctrine est que demander si l'agent d'IA pourrait s'échapper, c'est comme demander si un moteur d'échecs pourrait déplacer une pièce sur un échiquier physique. Elle dit que la surface d'outils de l'agent ne contient aucune opération qui touche le disque, une base de données ou le réseau. C'est l'affirmation de la doctrine, et la section 6 en donne les limites.

**J'ai refusé un contrôle de permission comme frontière.** Ce n'est pas un contrôle que l'agent ne pourrait pas contourner. Les pouvoirs sont séparés : la créativité sans l'autorité, l'autorité sans la créativité.

**J'ai refusé un second atelier pour les machines.** Le bac à sable est le même atelier que le programmeur humain utilise déjà. Le cadre a été conçu pour des programmeurs humains, et tout ce qui est conçu pour en libérer un est exactement ce qu'il faut pour en contenir un artificiel.

**J'ai refusé de laisser la barrière facultative.** La décision du 22 août 2026 dit que la barrière d'enregistrement est la doctrine, et que l'adhésion volontaire est un état de migration, non le dessin. Le dossier est honnête sur la découverte derrière la décision : là où la doctrine des agents qui ne peuvent pas vous nuire s'imposait ce jour-là, il n'y avait rien. Le monde sûr existait, et le répertoire agentique n'en mentionnait rien. La décision l'a refermé le jour même.

**J'ai refusé un bouchon.** Demander un agent d'IA réservé lève une erreur. L'architecture dit que c'est la loi qui travaille, et non un défaut.

**J'ai refusé d'abandonner en silence.** Dans le moteur, un envoi vers une boîte de réception pleine est refusé avec un code et compté. C'est testé dans le code Zig du moteur, par un test que je n'ai pas exécuté, et aucun bloc ici ni aucune garde narrée ne le montre. Quand la file d'exécution est pleine, les visites suivantes sont abandonnées et comptées. La boucle dit aussi ce qu'elle ne peut pas voir : l'intérieur d'un rappel, l'horloge, et si une déclaration de couverture est vraie.

**J'ai refusé de laisser une machine être le dernier recours.** La constitution de l'interface du domaine de projets a un droit, le sixième sur six : le Droit à un humain. Partout où une machine sert, une personne est joignable, clairement, et sans pénalité. Il est appliqué par un jugement, celui d'une personne, et non par une garde qui s'exécute ; la bibliothèque ne le mentionne pas. La constitution le tient pour le bout humain de la boucle : c'est la règle 102 de la constitution (annexe C).

La section 5 nomme les gardes qui prouvent ce que les blocs ont montré.

## 5. Le tribunal

`safeworld_narrated` a sept scènes : la réversibilité comme sixième contrat ; la barrière d'enregistrement dans les phrases du moteur ; la table de la posture face à la réversibilité ; le tribunal du fichier au chargement. Trois autres suivent : ce que le fichier déclare, qui atterrit dans la gouvernance de l'agent ; l'atelier, du disque qui n'a pas bougé jusqu'à la piste d'audit ; et l'agent de l'effectif répété puis validé. `agentfile_narrated` prouve qu'un agent est un fichier jugé au chargement, avec un refus par barrière, et qu'un répertoire est un déploiement. `agentloop_engine_narrated` prouve que la boucle du moteur énonce sa couverture à l'exécution, que l'enregistrement est une barrière, qu'une règle donne les mêmes mots dans deux couches, et qu'une file trop pleine abandonne des visites et les compte. `containment_drill_narrated` prouve un exercice contre une vraie cible en boucle locale : un enquêteur modèle propose le confinement et ne valide rien ; un humain valide, et le confinement tient quand on le vérifie de l'extérieur. Dans mon exécution du 8 octobre 2026, l'exercice a lu 443 ms pour détecter et 61 ms pour contenir, sur cette machine. Les données du livre ne contiennent pas cette exécution. Le site imprime d'autres nombres tirés de sa propre exécution, et le modèle de menace d'autres encore tirés de la sienne. Les trois diffèrent parce que l'exercice mesure une horloge. La limite de l'exercice est une seule forme d'attaque, en boucle locale, sur une seule machine, lancée à la demande. `virtual_system_twin_narrated` prouve le jumeau : une répétition ne touche rien de réel ; le plan se narre et signale ses risques ; une portée refuse ; un relecteur rejette une étape ; les instantanés reviennent en arrière.

La garde `roster_narrated` n'est pas dans l'en-tête, parce qu'elle ne peut pas s'exécuter depuis un instantané de la bibliothèque : elle charge les fichiers d'effectif du domaine de projets depuis un dépôt voisin. La répétition de l'agent de l'effectif est prouvée par `safeworld_narrated`, dont la septième scène est le dernier bloc ci-dessus.

La section 6 se tourne vers le terrain, et vers où il mène.

## 6. Le terrain, et où il mène

La table propre du dossier est honnête, et j'en porte les lignes en prose.

Le terrain mène en connecteurs : messagerie, disques et gestionnaires de tickets, magasins de vecteurs hébergés, interfaces en flux. Ils sont atteignables depuis Softanza et non pavés.

Le terrain mène en recherche sur des corpus ouverts. Softanza gagne sur un domaine sélectionné et perd sur le web ouvert.

Le terrain mène en raisonnement de frontière. Cette pile orchestre les plus grands modèles à chaque appel.

Le terrain mène en écosystème et en recrutement. Il y a un marché du travail pour cette pile, et aucun pour celle-ci.

Quand choisir laquelle, d'après la narration : la pile courante, quand la tâche est un travail de langage ouvert sur une matière que vous ne pouvez pas sélectionner. Ses exemples sont résumer des documents arbitraires, des produits conversationnels, de la recherche sur le web ouvert. La couche Softanza, quand les actions ont des conséquences et que quelqu'un finira par demander pourquoi elle a fait cela. Parmi ces cas, dans les mots de la narration : le travail réglementé ou audité, tout ce qui tourne sans surveillance, et tout ce qui doit continuer à fonctionner hors ligne à coût marginal nul. Les deux ne s'excluent pas, et un modèle d'IA peut siéger dans un système Softanza comme proposeur.

Le jumeau est un modèle de la réalité, non la réalité. Le cadre demande de la fidélité et de l'honnêteté, et le plan se revalide contre la réalité avant d'être validé. Une fois le vrai fichier supprimé dans le dos du jumeau, la vérification dit que la cible est absente dans la réalité. Je l'ai vue avertir, et je n'ai pas testé si elle bloque la validation.

Et la plus grande perte honnête. Le modèle de menace met *le code déjà en cours d'exécution dans le processus* hors de portée : il peut faire tout ce que le processus peut faire, effacer le registre ou lire un secret. L'atelier contient ce qui est écrit à travers l'atelier. Une fonction qui ne demande pas l'atelier n'est pas confinée. Les lectures sont libres : l'en-tête de l'atelier lui-même dit que les lectures sont de la perception et restent libres, et que seules les écritures sont confinées au jumeau. L'architecture dit que l'évasion n'est pas un défaut à fermer en le supprimant. Elle la réduit par une posture déclarée, et par du code, non le fichier, qui décide quelles fonctions un agent peut appeler. Je n'ai pas exécuté de fonction de confiance qui contourne l'atelier : j'ai lu cette limite dans l'architecture, dans le modèle de menace et dans l'en-tête de l'atelier.

## 7. La limite

Ce qui est construit : la réversibilité comme contrat déclaré, et la barrière d'enregistrement, dans la porte de l'ancien langage hôte et dans le moteur ; la posture confrontée à la réversibilité à la porte et au chargement. L'atelier est construit, avec un plan qui se narre, signale, valide, accepte un rejet et tient une piste d'audit ; l'agent de l'effectif répété puis validé l'est aussi, et l'exercice aussi. Les structures bornées du moteur sont construites : 64 emplacements d'agent, une boîte de réception de 8 messages (testée en Zig seulement, non exécutée pour ce livre) et une file d'exécution de 256.

Ce qui est conçu : le côté de l'agent dans la négociation, où le plan parvient à l'agent mais où la conversation sur le plan ne le fait pas encore. L'architecture le dit, et le modèle de menace le répète. J'ai cherché dans le code de la bibliothèque et n'ai trouvé aucune révision d'un plan. La salle d'examen, qui certifierait un agent pour une portée de validation comme on certifie un conducteur pour une catégorie de permis : elle apparaît dans des documents et dans aucun code. Les branches comme esprits parallèles : les instantanés et le retour en arrière sont construits, et je n'ai trouvé aucun appel de branche. Les jumeaux pour les bases de données, les interfaces et les réseaux : le cadre les nomme. Le jumeau des fichiers est construit, et le jumeau de l'environnement du processus aussi, avec ses variables, son répertoire de travail et son lancement mis en file (chapitre 24). Les trois autres ne le sont pas.

Chaque point ci-dessous est un écart, trouvé en exécutant et en lisant.

- **Un exécutant non défini et une portée non définie ne sont pas gardés.** Un plan sans exécutant répond qu'aucun exécutant n'est défini, qu'un humain au clavier n'est pas gardé, et `Execute()` est permis. Le refus du bloc ci-dessus s'applique à un modèle d'IA désigné comme exécutant. De même, le contrôle de portée ne s'exécute que lorsqu'une portée est définie : un plan avec un exécutant et sans portée est validé sans aucun contrôle des chemins qu'il touche. Donc « seul un acteur gouverné valide » est exact quand un exécutant et une portée sont définis, et une personne au clavier peut valider un plan qui n'en nomme aucun.
- **Un plan signale ; il ne classe pas.** La narration dit qu'un plan classe ses propres risques. Le code renvoie un signal par étape destructrice, dans l'ordre des opérations, avec une étiquette comme DESTRUCTIVE. Il n'y a pas de score ni d'ordre de gravité. Le chapitre dit « signale ».
- **La barrière est facultative chez l'hôte.** Un programme qui héberge la bibliothèque doit déclarer qu'il emploie la boucle du moteur ; tant que le dernier de ces programmes dans l'arbre propre de la bibliothèque n'a pas déclaré, le défaut reste inactif, et un programme neuf fait tourner l'ancienne boucle de tick de l'ancien langage hôte.
- **La boucle vérifie qu'une déclaration de couverture existe, non qu'elle est vraie.**
- **Les limites de l'exercice :** une forme d'attaque, en boucle locale, sur une seule machine.

Six portes suivent, le même chapitre vu de six endroits.

## 8. Six portes

**Le programmeur.** Votre agent est un fichier et quelques fonctions. Il s'exécute et croit avoir agi, et le disque ne bouge pas. Vous lisez le plan, vous choisissez l'acteur validant et la portée, et le tribunal vous dit en une phrase quelle règle vous a refusé.

**L'analyste.** Chaque proposition est un plan narré d'opérations avec les étapes destructrices signalées, et une ligne d'audit pour chaque validation. Vous pouvez lire ce que l'agent voulait faire, étape par étape, sans l'exécuter. Les signaux sont par genre, non notés.

**Le concepteur.** Le plan est l'unique artefact qui passe de l'agent à la personne, et une personne peut rejeter une étape. Le Droit à un humain dit qu'une personne est joignable partout où une machine sert, et le droit est tenu par un jugement.

**Le décideur.** Vous déclarez ce que chaque agent couvre et à quel point il est réversible avant qu'il puisse exister, et vous décidez la portée et l'acteur qui valide. Un modèle d'IA est structurellement incapable de valider, même trompé ; le modèle de menace suppose qu'il le sera. La partie la plus difficile est celle que le dessin vous laisse : quelles fonctions le code permet à un agent d'appeler.

**Le formateur.** L'agent d'un apprenant qui range un répertoire de cours en supprimant tout est une leçon sur ce qu'est un plan. Elle voit ce qu'il aurait fait, et les fichiers sont toujours là.

**L'agent.** Vous pouvez répéter sans limite, à l'intérieur du jumeau. Votre seul export est un plan, et on peut discuter avec vous à son sujet. Vous ne pouvez pas valider. Aujourd'hui la discussion est à sens unique : vous ne recevez pas encore l'objection du relecteur pour réviser.

## 9. Exercice

Choisissez un répertoire de dix fichiers que vous pouvez perdre. Écrivez un fichier d'agent pour un travail de rangement sur lui : ce qu'il couvre, à quel point il est réversible, une compétence. Avant d'exécuter quoi que ce soit, écrivez sous chaque ligne la promesse que vous attendez : combien de fichiers existent sur le disque après un cycle, combien d'opérations le plan contient, et combien d'entre elles le plan signale comme des risques. Puis écrivez ce qui arrive quand vous désignez un modèle de langage comme exécutant.

```haro exercise
cDirMine = StzReplace(WorkingDirectory(), "\", "/") + "/_mine"
StzDirCreatePath(cDirMine)
for i = 1 to 10
	StzFileWrite(cDirMine + "/file" + i + ".txt", "file " + i)
next
oMine = new stzVirtualFileSystem()
oMine.SetActor("my-tidy-bot")
# your tidy-up proposal here, with the promise you expect under each line
StzDirDeleteAll(cDirMine)
```

Exécutez-le. Puis donnez le plan à un acteur validant sous une portée qui ne couvre pas le répertoire, et écrivez la promesse de nouveau. Si une promesse se rompt, ne changez pas la promesse : expliquez d'abord la sortie. Un bon apprenant est surpris une fois. Le plan signale ses étapes destructrices et ne les classe pas, et un plan sans aucun exécutant est permis.

Je vous laisse celui-ci, exprès. Prenez le bloc qui a validé la liste de prix. Les six lignes qui ont construit `oScope3` et validé sous elle deviennent ces trois-ci, et les lignes qui les suivent restent :

```haro exercise
oPlan3 = oAg.GenerateUpdatePlan()
oPlan3.SetExecutor(PIActor("shop-committer"))
oPlan3.Execute()
```

Exécutez-le, et demandez au disque ce que le plan a fait, puis demandez-le à la piste d'audit. Je ne vous dis pas ce que vous trouverez. La page dit pourquoi à la section 7, dans le premier point de sa liste d'écarts ; lisez-le après avoir regardé, non avant. Quand vous saurez dire pourquoi « seul un acteur gouverné valide » tient pour ce plan ou ne tient pas, vous saurez de quoi cette phrase dépend.

Le chapitre 21 porte sur le tribunal lui-même, sous quatre de ses formes : promesses, perception, sécurité et performance. Son principe est qu'une affirmation ne vaut que ce que vaut le tribunal qui peut la refuser, et que là où aucun tribunal ne voit, le dossier le dit.
