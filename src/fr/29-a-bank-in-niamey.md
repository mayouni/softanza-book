---
id: a-bank-in-niamey
part: 6
number: 29
title: Une banque à Niamey
spine: false
narrations: [stzOrgChartDoc-BankUseCase.md, stz-rules-as-graph-rules-narration.md]
site: [forged, customers]
guards: [orgrule_narrated, 14_bceao_governance, 15_multiple_validators, 13_segregation_of_duties, rulereport_narrated, 36_import_from_stzorg]
stage:
  built: "l'organigramme comme un texte qu'une personne peut éditer ; les validateurs du régulateur régional et de la séparation des tâches ; les sept régimes comme un seul mécanisme ; une règle écrite comme une donnée ; un rapport avec un verdict"
  designed: "le contenu qui ferait différer les six autres régimes du premier ; un fichier de règles qui juge, et pas seulement qui se charge"
  absent: "le produit livré tournant sur la bibliothèque ; un mot des gens de la banque ; la lecture, par un auditeur, d'un constat produit par la bibliothèque"
status: draft
rulings: ["12.19", "12.29", "12.30"]
research: research/ch29.md
---

Dans ce chapitre, je prends une banque de Niamey, sous la banque centrale de l'union monétaire ouest-africaine, et je dis d'abord où est la leçon : dans la bibliothèque, et non dans le produit que la banque fait tourner. J'écris l'organigramme d'une petite banque comme un texte et je le juge selon la règle régionale et selon la séparation des tâches. J'imprime ce que chacun des sept régimes contient, j'ajoute une règle propre à la banque comme une donnée, et je lis le rapport unique avec son verdict. Je dis les quatre choses que j'ai refusées, la première étant de cacher la structure dans une base de données. Le principe tient en une phrase : l'organigramme dit ce qui est, la règle dit ce qui doit être, et le verdict nomme la règle et le lieu.

## 1. Le concept, tel que le terrain le tient

Une banque est jugée sur sa structure autant que sur ses chiffres. Un régulateur demande qui rend compte à qui : si la fonction d'audit est indépendante des dirigeants qu'elle audite, s'il y a un conseil, si une fonction de risque existe. Il demande si la personne qui exécute un paiement est celle qui l'approuve. Le terrain répond par des documents : un organigramme dessiné dans une diapositive, une politique écrite dans un traitement de texte, un audit qui compare les deux une fois par an.

Le terrain a aussi une famille d'outils appelés plateformes de gouvernance, de risque et de conformité, qui tiennent des registres de risques et de contrôles et suivent les constats jusqu'à leur clôture. Ils enregistrent qu'un contrôle existe et à qui il appartient. Ils ne lisent en général pas la structure de l'organisation pour vous dire qu'elle est fausse. C'est une connaissance générale, pas une étude du dossier.

## 2. Le premier principe

**Une organisation peut être jugée par son propre organigramme, selon les règles d'un régulateur, par un programme qui lit l'organigramme comme une donnée : l'organigramme dit ce qui est, la règle dit ce qui doit être, et le verdict nomme la règle et le lieu.**

## 3. La forme Softanza

Une banque commerciale de Niamey, sous les règles de la banque centrale de l'union monétaire ouest-africaine, fait tourner un produit d'évaluation des organisations que j'ai construit. Il est installé sur le réseau interne de la banque, sous licence, et le guide d'installation que j'ai remis à la banque est le document qui atteste la référence. Le produit lui-même est une application Python : un petit serveur web avec une base de données. Je le dis d'abord, parce que la leçon que je vais vous montrer est dans la bibliothèque, et non à l'intérieur de ce produit.

La leçon est qu'un organigramme est une donnée qu'un programme peut juger. Elle commence par un texte qu'une personne peut éditer, sans programmer : des postes, leurs titres, leurs départements, et à qui chacun rend compte. Voici l'organigramme d'une petite banque. Que dit de lui la règle du régulateur régional ? Lancez-le :

```haro
cChart = '
orgchart "bank"

positions
    board
        title: Board of Directors
        level: executive
        department: board
        reportsTo:

    ceo
        title: Chief Executive
        level: executive
        department: executive
        reportsTo: board

    risk
        title: Chief Risk Officer
        level: management
        department: risk
        reportsTo: board

    audit
        title: Internal Audit
        level: management
        department: audit
        reportsTo: ceo
'
oOrg = new stzOrgChart("bank")
oOrg.ImportStzOrg(cChart)
? oOrg.NodeCount()
#--> 4
? @@( oOrg.ValidateXT(:BCEAO)[:issues] )
#--> [ "BCEAO-002: Audit reports to non-board position" ]
? oOrg.IsValidXT(:BCEAO)
#--> 0
```

La règle du régulateur lit l'organigramme et le refuse ! L'audit rend compte au directeur général, et le verdict le dit dans ses propres mots, `BCEAO-002: Audit reports to non-board position`, avec un code de règle qu'un auditeur peut retrouver. Un organigramme est jugé par plus d'un tribunal à la fois, chaque constat porte son propre code, et le rapport de conformité dit conforme ou non. Que dit un second tribunal, la séparation des tâches, qui veut que les opérations ne rendent pas compte à la trésorerie ? J'ajoute la trésorerie et les opérations, les opérations sous la trésorerie, et je lance les deux tribunaux :

```haro
oOrg.AddManagementPositionXT("treasury", "Treasury")
oOrg.SetPositionDepartment("treasury", "treasury")
oOrg.AddManagementPositionXT("ops", "Operations")
oOrg.SetPositionDepartment("ops", "operations")
oOrg.ReportsTo("treasury", "ceo")
oOrg.ReportsTo("ops", "treasury")
aV = oOrg.ValidateXT([ :BCEAO, :SOD ])
? aV[:validatorsFailed]
#--> 2
? aV[:results][1][:issues][1]
#--> BCEAO-002: Audit reports to non-board position
? aV[:results][2][:issues][1]
#--> SOD-001: Operations reports through Treasury
? oOrg.ComplianceReport()[:overallStatus]
#--> non-compliant
```

Deux validateurs échouent, chacun avec son propre code, et le rapport de conformité dit `non-compliant`.

La bibliothèque nomme sept régimes, par le nom de leurs classes : le régional, Bâle III, SOX, PCI DSS, ISO 27001, le RGPD et HIPAA. Ils partagent un seul mécanisme. Combien de règles chacun contient-il ? Je l'imprime, plutôt que d'écrire une phrase qui dit « Bâle III est validé » :

```haro
aBases = [ new stzBCEAORuleBase(), new stzBaselIIIRuleBase(), new stzSOXRuleBase(), new stzPCIDSSRuleBase(),
           new stzISO27001RuleBase(), new stzGDPRRuleBase(), new stzHIPAARuleBase() ]
for oBase in aBases
	? oBase.Name() + " : " + oBase.NumberOfRules()
next
#--> BCEAO : 4
#--> Basel III : 4
#--> SOX : 5
#--> PCI-DSS : 4
#--> ISO 27001 : 4
#--> GDPR : 4
#--> HIPAA : 4
```

Six régimes portent quatre règles, et un en porte cinq ! Quatre règles que chaque base porte : personne ne rend compte à soi-même, aucun cycle de rattachement, aucun poste orphelin, et une étendue de contrôle. SOX en ajoute une qui lui est propre : aucun poste ne tient à la fois le rôle d'approbateur et celui d'exécutant. Elle est appelée aussi séparation des tâches, mais c'est une règle différente du second tribunal ci-dessus. Le commentaire de la bibliothèque le dit sans détour : les classes de régimes ne diffèrent aujourd'hui que par le nom, et une seule ajoute une règle qui lui est propre. Les quatre sont celles de la base de règles ; le validateur qui a refusé l'organigramme dans le premier bloc tient trois règles qui lui sont propres, codées BCEAO-001 à BCEAO-003, et les deux ne sont pas la même chose. Je reviendrai sur ce que cela veut dire.

La règle propre d'une banque est aussi une donnée. Prenez la règle selon laquelle l'audit interne rend compte au conseil. C'est un objet déclaré par des appels. Elle nomme le département qu'elle gouverne, la ligne qu'elle exige et la phrase qu'elle imprime, et elle s'ajoute à la base de règles d'un régime. Quelle règle a été rompue, et où ? Le rapport le dit :

```haro
oRule = new stzGraphRule("audit-reports-to-board")
oRule.SetDomainQ("orgchart")
oRule.WhenQ("department", "equals", "audit")
oRule.ThenQ("reportsTo", "equals", "board")
oRule.ThenViolationQ("internal audit must report to the board")
oBasel = new stzBaselIIIRuleBase()
oBasel.AddRule(oRule)
oRep = new stzRuleReport("bank")
oRep.Ingest(oOrg.CheckCompliance(oBasel))
oRep.Report()
#--> Rule report 'bank': 1 finding(s), 1 error(s), 0 warning(s) -> UNSOUND (errors present)
#      [orgchart] 1 finding(s)
#        ERROR audit-reports-to-board @ audit -- internal audit must report to the board
```

Le rapport dit `UNSOUND` et nomme la règle et le lieu : `ERROR audit-reports-to-board @ audit -- internal audit must report to the board`.

Puis le verdict suit l'organigramme. Deux modifications de deux lignes de rattachement, l'audit rend désormais compte au conseil et les opérations au directeur général. Que disent maintenant les tribunaux qui disaient non ? Lancez-le :

```haro
oOrg.ReportsTo("audit", "board")
oOrg.ReportsTo("ops", "ceo")
? oOrg.IsValidXT([ :BCEAO, :SOD ])
#--> 1
? oOrg.ComplianceReport()[:overallStatus]
#--> compliant
oRep = new stzRuleReport("bank")
oRep.Ingest(oOrg.CheckCompliance(oBasel))
oRep.Report()
#--> Rule report 'bank': 0 finding(s), 0 error(s), 0 warning(s) -> SOUND
? oRep.IsSound()
#--> 1
```

Ils disent `compliant`, et le rapport dit `SOUND`. C'est le mouvement que raconte la narration d'une banque virtuelle, d'une structure non conforme à une structure gouvernée. Le code propre de la narration ne s'exécute pas au commit épinglé ; les appels ci-dessus, si. Le rapport est une seule barrière sur les bases de règles qu'on lui donne. Et voici la limite de ce mouvement, sous forme de bloc. Un tribunal lit ce que l'organigramme déclare, et rien de plus. La règle régionale ne compare le département du supérieur d'un poste que lorsque ce département est déclaré, donc je m'attends à ce que le constat sur l'audit disparaisse quand le département du directeur général est laissé vide. Que dit-il quand il l'est ? Lancez-le :

```haro
oOrg2 = new stzOrgChart("bank")
oOrg2.ImportStzOrg( substr(cChart, "department: executive", "department:") )
? oOrg2.IsValidXT(:BCEAO)
#--> 1
? oOrg2.ValidateXT(:Banking)[:status]
#--> pass
oOrg2.SetPositionDepartment("ceo", "executive")
? oOrg2.IsValidXT(:BCEAO)
#--> 0
```

Il dit `1` : une fonction d'audit qui rend compte au directeur général passe ! Déclarez le département, et le constat apparaît. Le même bloc montre le validateur bancaire qui répond `pass` : le commentaire de la bibliothèque dit qu'il passe à chaque fois, un emplacement réservé pour des règles pas encore écrites.

Mon livre précédent, *Refinement-Oriented Programming*, raconte la discipline qui gouverne le changement à travers l'histoire d'une banque face à la lettre d'un régulateur. Ce chapitre ne la raconte pas de nouveau. Il dit ce que la bibliothèque porte.

## 4. La décision, et ce que j'ai refusé

**J'ai refusé de cacher la structure dans une base de données.** Dans le produit livré, un organigramme est des lignes dans deux tables. Dans la bibliothèque, c'est un texte qu'une personne peut lire et éditer, et il s'importe dans l'objet que le tribunal juge. Une règle appliquée à la ligne d'une base est une requête ; une règle appliquée à un texte est quelque chose qu'une personne peut lire avant qu'elle ne s'exécute.

**J'ai refusé de prétendre plus que ce que la bibliothèque contient.** Le mot « validateur » peut se lire pour deux choses différentes. Le régulateur régional a un validateur de trois règles, et une base de règles de quatre règles universelles. Bâle III n'a que la base de règles, et les autres aussi. J'ai imprimé le compte, et le bloc ci-dessus le montre.

**J'ai refusé de porter le texte d'un régulateur dans un code dont je ne peux pas citer la source.** Les codes BCEAO-001 à BCEAO-003 sont ceux de la bibliothèque. Le dossier ne les rattache à aucun article du texte de la banque centrale. Ce sont les propres règles de la bibliothèque, nommées d'après le régime du régulateur ; le dossier ne nomme aucun texte dont elles seraient tirées.

**J'ai refusé de dire ce que je ne sais pas.** Ce que les gens de la banque déclarent, exploitent ou disent n'est pas dans le dossier. Le guide d'installation est mon document à la banque : des étapes d'installation, un fichier de licence, un contact de support. La page Forged ne garde aucun chiffre ni aucune personne d'un client. Le dossier est muet sur qui, à la banque, déclare l'organigramme, le questionnaire ou les règles. Il est muet sur depuis combien de temps le produit est installé, et sur combien de personnes l'utilisent. Je n'en inventerai rien, et le chapitre ne comble pas le vide. Sur « construit avec Softanza », le dossier montre une application Python, un petit serveur web avec une base de données, qui n'appelle rien de la bibliothèque. Les validateurs de la bibliothèque en sont séparés, et ce sont eux que ce chapitre exécute. Le chapitre 1 dit que la construction de la plateforme a façonné Softanza ; ce chapitre dit ce que le dossier montre.

Six gardes se tiennent derrière les blocs.

## 5. Le tribunal

`orgrule_narrated` prouve SOX, le RGPD et HIPAA comme bases de règles sur le graphe de l'organigramme, avec les quatre règles universelles et la séparation des tâches que SOX ajoute, et l'organigramme qui rejoint le rapport unique. Le bloc ci-dessus imprime les sept comptes. `14_bceao_governance` prouve deux des trois règles du validateur régional. `15_multiple_validators` prouve le verdict combiné, et `13_segregation_of_duties` le second tribunal. `rulereport_narrated` prouve le rapport unique sur les constats du code, des agents d'IA et de la sécurité. `36_import_from_stzorg` prouve la forme texte de l'organigramme.

## 6. Le terrain, et où il mène

Le terrain mène en couverture. Une plateforme de gouvernance et de conformité tient en général un registre de réglementations, de contrôles et de constats, avec des flux de travail, des responsables et des échéances. C'est une connaissance générale, pas une étude du dossier. La bibliothèque tient un contrôle structurel d'un régulateur régional, un de séparation des tâches, et un mécanisme. Pour le RGPD, HIPAA et les autres, elle tient le mécanisme et les quatre règles universelles, et rien qui leur soit propre.

Le terrain mène en usage réel : une telle plateforme est souvent une que les auditeurs d'une banque connaissent déjà, et qu'un régulateur a déjà vue. C'est une connaissance générale, pas une étude du dossier.

Là où je pense que ceci se distingue, c'est que l'organigramme est la donnée et que le tribunal est une règle sur elle. Un organigramme est un texte, une règle est une donnée, un constat nomme la règle et le poste, et le rapport est un seul verdict. Le tableau de comparaison propre de la bibliothèque pour cette fonction n'est que victoires, sans dates, avec des chiffres de coût qui ne citent rien, et je ne l'imprimerai pas.

Voici la limite, dans les mots d'étape.

## 7. La limite

Ce qui est construit : l'organigramme comme modèle et comme texte ; les validateurs du régulateur régional et de la séparation des tâches ; les sept régimes comme un seul mécanisme avec l'exemple SOX. Construit aussi : une règle écrite comme une donnée, et le rapport unique avec son verdict.

Quatre choses sont conçues, ou construites en partie.

- Le contenu des six régimes autres que le régional. Cinq d'entre eux tiennent les mêmes quatre règles universelles et rien d'autre ; SOX en ajoute une cinquième.
- Un fichier de règles qui juge. La bibliothèque peut charger un fichier de règles dans un texte `when` et `then`, et celui de ses données de test charge deux règles. Le chargeur lit le nom, le type, la gravité, la fonction, les paramètres et le message d'une règle, et aucune ligne `when` ni `then`. Une telle règle se charge et ne juge rien. Le format est admis, et la règle n'est pas appliquée.
- Un validateur lit des propriétés déclarées. Il trouve le conseil par le mot « board » dans le titre d'un poste, et il ne compare les départements que là où ils sont déclarés : le bloc de la limite de la section 3 vide celui du directeur général et le constat sur l'audit disparaît.
- Le validateur de succession signale chaque poste pourvu, ce qui est, selon le commentaire de la bibliothèque elle-même, un défaut connu. La simulation de réorganisation lève une erreur quand on lui demande de changer une ligne de rattachement, également un défaut connu. L'article qui raconte la simulation nomme une méthode qui n'existe nulle part dans la bibliothèque.

Quatre choses sont absentes.

- Le produit livré tournant sur la bibliothèque. C'est une application Python ; une recherche dans son code n'a trouvé aucun contrôle régional ou de Bâle et aucun appel à la bibliothèque.
- Un mot de la banque. Le dossier est muet.
- Un verdict perçu. Aucun document ne dit qu'un auditeur ou un superviseur ait lu un constat que la bibliothèque a produit.
- Une date de livraison. Les fichiers livrés portent des horodatages du système de fichiers, et ce ne sont pas une date de livraison.

La couche web du produit est née dans son propre dépôt : son premier commit est daté du 4 février 2026, et le texte de la constitution de l'interface a été commité pour la première fois le 8 février. Les champs de preuve de la constitution disent que cinq de ses règles ont été récoltées sur un produit de supervision bancaire. Le dossier ne dit pas que ce produit soit l'installation de la banque. Je ne dirai pas qu'il l'est.

Six portes suivent, une pour chaque lecteur.

## 8. Six portes

**Le programmeur.** L'organigramme est un texte, la règle est une donnée, le tribunal est un appel. Un constat nomme la règle et le poste.

**L'analyste.** Vous changez une ligne de rattachement dans l'objet, ou dans le texte puis vous l'importez de nouveau, et vous relancez : le verdict suit l'organigramme.

**Le concepteur.** Le rapport est un seul verdict sur les bases de règles qu'on lui donne : sain ou non sain, avec chaque constat là où il a été trouvé.

**Le décideur.** Demandez quelles réglementations la bibliothèque contient, et demandez le compte. Sept régimes, un avec un validateur à côté de sa base de règles et un qui ajoute une règle ; les autres portent les quatre universelles.

**Le formateur.** La narration d'une banque virtuelle raconte le passage d'une structure non conforme à une structure gouvernée, et le livre montre ce passage avec des appels qui s'exécutent.

**L'agent.** Vous pouvez lire un organigramme et un rapport. Une règle que vous ajoutez est une donnée qu'une personne peut lire, et le tribunal juge l'organigramme avec elle.

## 9. Exercice

Dessinez l'organigramme d'une organisation que vous connaissez comme un texte de postes, de titres, de départements et de lignes de rattachement. Avant de lancer quoi que ce soit, écrivez ce que vous attendez que la règle régionale, puis la séparation des tâches, en disent. Puis écrivez une règle à vous comme une donnée, qui gouverne un département, et dites ce que le rapport imprimera.

Lancez-la. Puis laissez un département vide et dites quel constat disparaît, et pourquoi c'est dangereux.

Je vous laisse celui-ci, exprès. Prenez le bloc de la limite de la section 3 et changez une ligne : l'import prend l'organigramme entier, avec le département du directeur général déclaré.

```haro exercise
oOrg2 = new stzOrgChart("bank")
oOrg2.ImportStzOrg(cChart)
? oOrg2.IsValidXT(:BCEAO)
? oOrg2.ValidateXT(:Banking)[:status]
oOrg2.SetPositionDepartment("ceo", "executive")
? oOrg2.IsValidXT(:BCEAO)
```

Lancez-le et mettez les trois réponses côte à côte. Le tribunal régional a déjà refusé cet organigramme, à la section 3 ; lisez maintenant ce que le second validateur en dit, et pourquoi ce n'est pas la même chose que ce que le tribunal a dit. Les sections 3 et 4 disent pourquoi. Je ne vous donne pas la réponse ici. Quand vous l'aurez, vous saurez pourquoi un validateur qui répond `pass` n'a pas jugé l'organigramme.

Le chapitre suivant quitte la banque pour une organisation sur le terrain, et son principe tient en une phrase : l'agent d'IA propose, et une personne décide.
