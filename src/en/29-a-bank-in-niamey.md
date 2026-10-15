---
id: a-bank-in-niamey
part: 6
number: 29
title: A bank in Niamey
spine: false
narrations: [stzOrgChartDoc-BankUseCase.md, stz-rules-as-graph-rules-narration.md]
site: [forged, customers]
guards: [orgrule_narrated, 14_bceao_governance, 15_multiple_validators, 13_segregation_of_duties, rulereport_narrated, 36_import_from_stzorg]
stage:
  built: "the organisation chart as a text a person can edit; the validators of the regional regulator and of segregation of duties; the seven regimes as one mechanism; a rule written as data; one report with one verdict"
  designed: "the content that would make the other six regimes differ from the first; a rule file that judges, and not only loads"
  absent: "the delivered product running on the library; a word from the bank's own people; an auditor's reading of a finding the library produced"
status: draft
rulings: ["12.19", "12.29", "12.30"]
research: research/ch29.md
---

In this chapter I take a bank in Niamey, under the central bank of the West African monetary union, and I say first where the lesson is: in the library, and not inside the product the bank runs. I write the chart of a small bank as a text and judge it under the regional rule and under segregation of duties. I print what each of the seven regimes holds, add a rule of the bank's own as data, and read the one report with its verdict. I say the four things I refused, the first of them to hide the structure in a database. The principle is one sentence: the chart says what is, the rule says what must be, and the verdict names the rule and the place.

## 1. The concept, as the field holds it

A bank is judged on its structure as much as on its numbers. A regulator asks who reports to whom: whether the audit function is independent of the executives it audits, whether there is a board, whether a risk function exists. It asks whether the person who operates a payment is the one who approves it. The field answers with documents: an organisation chart drawn in a slide, a policy written in a word processor, an audit that compares the two once a year.

The field also has a family of tools called governance, risk and compliance platforms, which keep registers of risks and controls and track findings through to closure. They record that a control exists and who owns it. They usually do not read the structure of the organisation and tell you that it is wrong. That is general knowledge, not a study of the record.

## 2. The first principle

**An organisation can be judged by its own chart, under a regulator's rules, by a program that reads the chart as data: the chart says what is, the rule says what must be, and the verdict names the rule and the place.**

## 3. The Softanza form

A commercial bank in Niamey, under the rules of the central bank of the West African monetary union, runs an organisation-assessment product I built. It is installed on the bank's own internal network, under licence, and the installation guide I delivered to the bank is the document that attests the reference. The product itself is a Python application: a small web server with a database. I say that first, because the lesson I am going to show you is in the library, and not inside that product.

The lesson is that an organisation chart is data a program can judge. It begins with a text that a person can edit, with no programming: positions, their titles, their departments, and who each one reports to. This is the chart of a small bank. What does the regional regulator's rule say of it? Run it:

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

The regulator's rule reads the chart and refuses it! Audit reports to the chief executive, and the verdict says so in its own words, `BCEAO-002: Audit reports to non-board position`, with a rule code an auditor can look up. A chart is judged by more than one court at a time, each finding carries its own code, and the compliance report says compliant or not. What does a second court say, the segregation of duties, which holds that operations must not report to treasury? I add treasury and operations, operations under treasury, and run both courts:

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

Two validators fail, each with its own code, and the compliance report says `non-compliant`.

The library names seven regimes, by class name: the regional one, Basel III, SOX, PCI DSS, ISO 27001, GDPR and HIPAA. They share one mechanism. How many rules does each hold? I print it, rather than write a sentence that says "Basel III is validated":

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

Six regimes carry four rules, and one carries five! Four rules every base carries: nobody reports to themselves, no reporting cycle, no orphan position, and a span of control. SOX adds one of its own: no position holds both the approver and the executor role. It is also called the separation of duties, but it is a different rule from the second court above. The library's comment says it plainly: the regime classes differ by name today, and only one adds a rule of its own. The four are the rule base's; the validator that refused the chart in the first block holds three rules of its own, coded BCEAO-001 to BCEAO-003, and the two are not the same thing. I will come back to what that means.

A bank's own rule is data too. Take the rule that internal audit reports to the board. It is an object declared by calls. It names the department it governs, the line it requires and the sentence it prints, and it is added to a regime's rule base. Which rule broke, and where? The report says:

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

The report says `UNSOUND` and names the rule and the place: `ERROR audit-reports-to-board @ audit -- internal audit must report to the board`.

Then the verdict follows the chart. Two edits to two reporting lines, audit now to the board and operations to the chief executive. What do the courts that said no say now? Run it:

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

They say `compliant`, and the report says `SOUND`. That is the move the narration of a virtual bank tells, from a non-compliant structure to a governed one. The narration's own code does not run at the pinned commit; the calls above do. The report is one gate over the rule bases it is given. And here is the limit of it, as a block. A court reads what the chart declares and no more. The regional rule compares the department of a position's superior only when that department is declared, so I expect the finding on audit to vanish when the chief executive's department is left blank. What does it say when it is? Run it:

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

It says `1`: an audit function that reports to the chief executive passes! Declare the department, and the finding appears. The same block shows the banking validator answering `pass`: the library's own comment says it passes every time, a placeholder for rules not written yet.

My earlier book, *Refinement-Oriented Programming*, tells the discipline of governing change through the story of a bank facing a regulator's letter. This chapter does not retell it. It tells what the library carries.

## 4. The decision, and what I refused

**I refused to hide the structure in a database.** In the delivered product, an organisation chart is rows in two tables. In the library, it is a text that a person can read and edit, and it imports into the object the court judges. A rule applied to a database row is a query; a rule applied to a text is something a person can read before it runs.

**I refused to claim more than the library holds.** The word "validator" can be read for two different things. The regional regulator has a validator of three rules, and a rule base of four universal ones. Basel III has the rule base only, and so do the others. I printed the count, and the block above shows it.

**I refused to carry a regulator's text in a code I cannot source.** The codes BCEAO-001 to BCEAO-003 are the library's own. The record ties them to no article of the central bank's text. They are the library's own rules, named after the regulator's regime; the record does not name a text they are drawn from.

**I refused to tell what I do not know.** What the bank's own people declare, operate or say is not in the record. The installation guide is my document to the bank: installation steps, a licence file, a support contact. The Forged page keeps no figure and no person of a client. The record is silent on who at the bank declares the chart, the questionnaire or the rules. It is silent on how long the product has been installed, and on how many people use it. I will invent none of it, and the chapter does not fill the gap. On "built with Softanza", the record shows a Python application, a small web server with a database, that calls nothing of the library. The library's validators are separate from it, and they are what this chapter runs. Chapter 1 says that building the platform shaped Softanza; this chapter says what the record shows.

Six guards stand behind the blocks.

## 5. The court

`orgrule_narrated` proves SOX, GDPR and HIPAA as rule bases over the chart's graph, with the four universal rules and the separation of duties that SOX adds, and the chart joining the one report. The block above prints the seven counts. `14_bceao_governance` proves two of the three rules of the regional validator. `15_multiple_validators` proves the combined verdict, and `13_segregation_of_duties` the second court. `rulereport_narrated` proves the one report over findings from code, AI agents and security. `36_import_from_stzorg` proves the text form of the chart.

## 6. The field, and where it leads

The field leads in coverage. A governance and compliance platform usually holds a register of regulations, controls and findings, with workflows, owners and deadlines. That is general knowledge, not a study of the record. The library holds one structural check of a regional regulator, one of segregation of duties, and a mechanism. For GDPR, HIPAA and the others, it holds the mechanism and the four universal rules, and nothing that is specific to them.

The field leads in actual use: such a platform is often one that a bank's auditors already know, and that a regulator has already seen. That is general knowledge, not a study of the record.

Where I think this stands apart is that the chart is the data and the court is a rule over it. A chart is a text, a rule is data, a finding names the rule and the position, and the report is one verdict. The library's own comparison table for this feature is all wins, undated, with cost figures that cite nothing, and I will not print it.

Now the limit, in the stage words.

## 7. The limit

What is built: the organisation chart as a model and as text; the validators of the regional regulator and of segregation of duties; the seven regimes as one mechanism with the SOX exemplar. Built too: a rule written as data, and the one report with its verdict.

Four things are designed, or built in part.

- The content of the six regimes other than the regional one. Five of them hold the same four universal rules and nothing else; SOX adds a fifth.
- A rule file that judges. The library can load a file of rules in a `when` and `then` text, and the one in its test data loads two rules. The loader reads a rule's name, type, severity, function, params and message, and no `when` or `then` line. Such a rule loads and judges nothing. The format is admitted, and the rule is not enforced.
- A validator reads declared properties. It finds the board by the word "board" in a position title, and it compares departments only where they are declared: the limit block of section 3 blanks the chief executive's and the finding on audit disappears.
- The succession validator flags every filled position, by the library's own comment a known defect. The reorganisation simulation raises when it is asked to change a reporting line, also a known defect. The article that tells the simulation names a method that exists nowhere in the library.

Four things are absent.

- The delivered product running on the library. It is a Python application; a search of its code found no regional or Basel check and no call to the library.
- A word from the bank. The record is silent.
- A perceived verdict. No document says that an auditor or a supervisor read a finding that the library produced.
- A delivery date. The delivered files carry file-system times, and those are not a delivery date.

The web layer of the product was born in its own repository: its first commit is dated 4 February 2026, and the interface constitution's text was first committed on 8 February. The constitution's own evidence fields say that five of its rules were harvested from a banking-supervision product. The record does not say that product is the bank's installation. I will not say that it is.

Six doors follow, one for each reader.

## 8. Six doors

**The programmer.** The chart is a text, the rule is data, the court is a call. A finding names the rule and the position.

**The analyst.** You change a reporting line in the object, or in the text and import again, and you re-run: the verdict follows the chart.

**The designer.** The report is one verdict over the rule bases it is given: sound or unsound, with each finding where it was found.

**The decision-maker.** Ask which of the regulations the library holds, and ask for the count. Seven regimes, one with a validator beside its rule base and one that adds a rule; the rest carry the universal four.

**The educator.** The narration of a virtual bank tells the move from a non-compliant structure to a governed one, and the book shows the move with calls that run.

**The agent.** You may read a chart and a report. A rule you add is data a person can read, and the court judges the chart with it.

## 9. Exercise

Draw the chart of an organisation you know as a text of positions, titles, departments and reporting lines. Before you run anything, write what you expect the regional rule, then segregation of duties, to say of it. Then write a rule of your own as data, one that governs one department, and say what the report will print.

Run it. Then leave one department blank and say which finding disappears, and why that is dangerous.

I left this one in your hands, on purpose. Take the limit block of section 3 and change one line: the import takes the chart whole, with the chief executive's department declared.

```haro exercise
oOrg2 = new stzOrgChart("bank")
oOrg2.ImportStzOrg(cChart)
? oOrg2.IsValidXT(:BCEAO)
? oOrg2.ValidateXT(:Banking)[:status]
oOrg2.SetPositionDepartment("ceo", "executive")
? oOrg2.IsValidXT(:BCEAO)
```

Run it and put the three answers side by side. The regional court has already refused this chart, in section 3; now read what the second validator says of it, and why it is not the same as what the court said. Section 3 and section 4 say why. I do not give you the answer here. When you have it, you will know why a validator that answers `pass` has not judged the chart.

The next chapter leaves the bank for an organisation in the field, and its principle is one sentence: the AI agent proposes, and a person decides.
