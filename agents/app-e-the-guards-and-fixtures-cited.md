# The guards and fixtures cited, by chapter

Source: Appendix E. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

A guard is a file of the library's test tree that holds assertions. A chapter that says "this is proved" names the guards that prove it, in the front matter of its source, and the build reads each one: it finds the file in the library at the commit the book runs at, and counts the assertions in it. A guard that is not there fails the build.

This appendix is that reading, by chapter. Nothing in it is typed. It is regenerated at every build, so the figures are always the ones the last build read.

Two things to keep in mind. A figure is the number of assertion calls the file holds, counted in its text; it is not a run. Most of these guards are not run by the book, because they write files, open ports or spawn processes. The few I ran myself are named in the chapters that rely on them, with the date. And the only fixtures the book cites are the ones the guards and the blocks read: the course folder of the library's education program, and the data folders its guards name. The blocks of the book are themselves the other fixtures: each one runs inside the library at the commit named under every chapter's title.

The chapters cite 114 distinct guards, holding 3359 assertions between them, read from the test tree at commit 93d7a39bd on 2026-10-09 03:28 UTC+01:00. A guard cited by two chapters is counted once in this total.

### 1 · Change arrives faster than trust

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `service_registry_narrated` | 93 | `base/test/system/service_registry_narrated.ring` |
| `safeworld_narrated` | 76 | `base/test/agentic/safeworld_narrated.ring` |
| `governance_crossing_narrated` | 31 | `base/test/system/governance_crossing_narrated.ring` |

### 2 · The software crafter

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `agentfile_narrated` | 88 | `base/test/agentic/agentfile_narrated.ring` |
| `service_registry_narrated` | 93 | `base/test/system/service_registry_narrated.ring` |
| `graphrule_object_narrated` | 34 | `base/test/graph/graphrule_object_narrated.ring` |
| `semantic_resolver_narrated` | 83 | `base/test/natural/semantic_resolver_narrated.ring` |
| `00_orgchart_narrated` | 10 | `base/test/orgchart/00_orgchart_narrated.ring` |

### 3 · The method, from first principles

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `modality_narrated` | 45 | `base/test/natural/modality_narrated.ring` |
| `wisecoding_narrated` | 13 | `base/test/conversation/wisecoding_narrated.ring` |
| `wisecoding_rich_narrated` | 52 | `base/test/conversation/wisecoding_rich_narrated.ring` |

### 4 · The platform in one picture

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `00_stzapp_narrated` | 3 | `base/test/app/00_stzapp_narrated.ring` |
| `06_stzsuperapp_narrated` | 21 | `base/test/app/06_stzsuperapp_narrated.ring` |
| `full_scope_model_narrated` | 62 | `base/test/system/full_scope_model_narrated.ring` |
| `01_platform_narrated` | 31 | `base/test/platform/01_platform_narrated.ring` |
| `threat_model_narrated` | 11 | `base/test/security/threat_model_narrated.ring` |

### 5 · Law: the code adheres to the way a person thinks, and the court judges it whoever wrote it

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `coderule_narrated` | 77 | `base/test/meta/coderule_narrated.ring` |
| `testoor_promises_narrated` | 46 | `base/test/testoor/testoor_promises_narrated.ring` |
| `05_containsemptystrings` | 5 | `base/test/list/05_containsemptystrings.ring` |
| `466_keeping_the_history_of_updates_of_a_softanza_objec` | 2 | `base/test/string/466_keeping_the_history_of_updates_of_a_softanza_objec.ring` |

### 6 · The mental model, and the metaphors

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `00_yielder_narrated` | 8 | `base/test/yielder/00_yielder_narrated.ring` |
| `597_walker_basics` | 6 | `base/test/list/597_walker_basics.ring` |
| `611_checkw` | 1 | `base/test/list/611_checkw.ring` |
| `621_perform` | 2 | `base/test/list/621_perform.ring` |
| `483_w_and_wf_forms_in_conditional_code` | 2 | `base/test/list/483_w_and_wf_forms_in_conditional_code.ring` |
| `495_walking_until_and_until_before` | 4 | `base/test/list/495_walking_until_and_until_before.ring` |

### 7 · The writing style, and the seven goals

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `coderule_narrated` | 77 | `base/test/meta/coderule_narrated.ring` |
| `602_l_function` | 6 | `base/test/list/602_l_function.ring` |
| `59_use_of_the_l_small_function` | 8 | `base/test/list/59_use_of_the_l_small_function.ring` |
| `527_identifying_lists_inside_a_string` | 32 | `base/test/string/527_identifying_lists_inside_a_string.ring` |
| `48_replacebymany` | 1 | `base/test/string/48_replacebymany.ring` |
| `483_w_and_wf_forms_in_conditional_code` | 2 | `base/test/list/483_w_and_wf_forms_in_conditional_code.ring` |
| `28_numberofoccurrenceofcharleftside` | 8 | `base/test/string/28_numberofoccurrenceofcharleftside.ring` |
| `646_content` | 1 | `base/test/string/646_content.ring` |
| `972_narration_viz-finding_a_recurring_substring` | 7 | `base/test/string/972_narration_viz-finding_a_recurring_substring.ring` |
| `testoor_promises_narrated` | 46 | `base/test/testoor/testoor_promises_narrated.ring` |

### 8 · Functions as linguistic expressions, and scope

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `00_regex_narrated` | 28 | `base/test/regex/00_regex_narrated.ring` |
| `972_narration_viz-finding_a_recurring_substring` | 7 | `base/test/string/972_narration_viz-finding_a_recurring_substring.ring` |
| `full_scope_model_narrated` | 62 | `base/test/system/full_scope_model_narrated.ring` |
| `system_scope_model_narrated` | 62 | `base/test/system/system_scope_model_narrated.ring` |
| `delivery_narrated` | 34 | `base/test/system/delivery_narrated.ring` |

### 9 · Patterns of thought: the Softanzuter, Reaxis and the engines

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `00_overflow_narrated` | 17 | `base/test/reactivestream/00_overflow_narrated.ring` |
| `60_reaxis_on_reactor_narrated` | 9 | `base/test/reactive/60_reaxis_on_reactor_narrated.ring` |
| `piagent_narrated` | 14 | `base/test/agentic/piagent_narrated.ring` |
| `00_grid_narrated` | 24 | `base/test/grid/00_grid_narrated.ring` |
| `test_timeline_regression` | 20 | `base/test/timeline/test_timeline_regression.ring` |
| `01_deeplist_narrated` | 16 | `base/test/list/01_deeplist_narrated.ring` |

### 10 · Programming becomes refinement

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `refinablecode_narrated` | 17 | `base/test/refine/refinablecode_narrated.ring` |
| `refine_deepening_narrated` | 24 | `base/test/refine/refine_deepening_narrated.ring` |
| `gate_deepening_narrated` | 19 | `base/test/refine/gate_deepening_narrated.ring` |

### 11 · Law: a language is declared and closed, and whatever speaks it, person or model, is judged by it

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `multilingual_pack_narrated` | 45 | `base/test/natural/multilingual_pack_narrated.ring` |
| `semantic_resolver_narrated` | 83 | `base/test/natural/semantic_resolver_narrated.ring` |
| `literate_templates_narrated` | 10 | `base/test/natural/literate_templates_narrated.ring` |
| `question_narrated` | 21 | `base/test/natural/question_narrated.ring` |
| `structuredoutput_narrated` | 73 | `base/test/neural/structuredoutput_narrated.ring` |
| `schema_grammar_narrated` | 28 | `base/test/neural/schema_grammar_narrated.ring` |
| `constrained_decoding_narrated` | 50 | `base/test/neural/constrained_decoding_narrated.ring` |

### 12 · A language, declared

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `structuredoutput_narrated` | 73 | `base/test/neural/structuredoutput_narrated.ring` |
| `schema_grammar_narrated` | 28 | `base/test/neural/schema_grammar_narrated.ring` |
| `constrained_decoding_narrated` | 50 | `base/test/neural/constrained_decoding_narrated.ring` |
| `483_w_and_wf_forms_in_conditional_code` | 2 | `base/test/list/483_w_and_wf_forms_in_conditional_code.ring` |
| `calc_column_engine_narrated` | 14 | `base/test/table/calc_column_engine_narrated.ring` |

### 13 · Natural, and executable: two directions, one discipline

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `nnl_narrated` | 87 | `base/test/natural/nnl_narrated.ring` |
| `multilingual_pack_narrated` | 45 | `base/test/natural/multilingual_pack_narrated.ring` |
| `semantic_resolver_narrated` | 83 | `base/test/natural/semantic_resolver_narrated.ring` |
| `question_narrated` | 21 | `base/test/natural/question_narrated.ring` |
| `literate_templates_narrated` | 10 | `base/test/natural/literate_templates_narrated.ring` |
| `truthchain_narrated` | 12 | `base/test/natural/truthchain_narrated.ring` |
| `interrogative_narrated` | 11 | `base/test/natural/interrogative_narrated.ring` |

### 14 · Knowledge programming

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `knowledge_integration_narrated` | 19 | `base/test/natural/knowledge_integration_narrated.ring` |
| `provenance_survives_save_narrated` | 23 | `base/test/security/provenance_survives_save_narrated.ring` |
| `program_narrated` | 21 | `base/test/education/program_narrated.ring` |

### 15 · Pattern languages

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `00_regex_narrated` | 28 | `base/test/regex/00_regex_narrated.ring` |
| `00_numbrex_narrated` | 15 | `base/test/numbrex/00_numbrex_narrated.ring` |
| `tablex_narrated` | 95 | `base/test/regex/tablex_narrated.ring` |
| `00_matrex_narrated` | 8 | `base/test/matrex/00_matrex_narrated.ring` |
| `00_graphex_narrated` | 27 | `base/test/graphex/00_graphex_narrated.ring` |

### 16 · Seven languages, one door

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `51_extercode_narrated` | 11 | `base/test/extercode/51_extercode_narrated.ring` |
| `governance_narrated` | 19 | `base/test/governance/governance_narrated.ring` |
| `virtual_environment_twin_narrated` | 38 | `base/test/system/virtual_environment_twin_narrated.ring` |
| `pycodegraph_narrated` | 48 | `base/test/meta/pycodegraph_narrated.ring` |
| `jscodegraph_narrated` | 13 | `base/test/meta/jscodegraph_narrated.ring` |

### 17 · Law: programmatic by default, the model last, admission over generation

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `dlm_narrated` | 16 | `base/test/learning/dlm_narrated.ring` |
| `wisecoding_narrated` | 13 | `base/test/conversation/wisecoding_narrated.ring` |
| `knowledge_integration_narrated` | 19 | `base/test/natural/knowledge_integration_narrated.ring` |
| `agentgraph_narrated` | 11 | `base/test/agentic/agentgraph_narrated.ring` |
| `piagent_narrated` | 14 | `base/test/agentic/piagent_narrated.ring` |
| `ownagentstack_narrated` | 10 | `base/test/agentic/ownagentstack_narrated.ring` |

### 18 · The five registers, and conversations that ask

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `wisecoding_narrated` | 13 | `base/test/conversation/wisecoding_narrated.ring` |
| `wisecoding_rich_narrated` | 52 | `base/test/conversation/wisecoding_rich_narrated.ring` |
| `ownagentstack_narrated` | 10 | `base/test/agentic/ownagentstack_narrated.ring` |
| `tutor_gaps_narrated` | 29 | `base/test/education/tutor_gaps_narrated.ring` |

### 19 · The domain language model

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `dlm_narrated` | 16 | `base/test/learning/dlm_narrated.ring` |
| `structuredoutput_narrated` | 73 | `base/test/neural/structuredoutput_narrated.ring` |
| `schema_grammar_narrated` | 28 | `base/test/neural/schema_grammar_narrated.ring` |
| `knowledge_integration_narrated` | 19 | `base/test/natural/knowledge_integration_narrated.ring` |
| `constrained_decoding_narrated` | 50 | `base/test/neural/constrained_decoding_narrated.ring` |

### 20 · Agents that cannot hurt you

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `safeworld_narrated` | 76 | `base/test/agentic/safeworld_narrated.ring` |
| `agentfile_narrated` | 88 | `base/test/agentic/agentfile_narrated.ring` |
| `agentloop_engine_narrated` | 54 | `base/test/agentic/agentloop_engine_narrated.ring` |
| `containment_drill_narrated` | 27 | `base/test/security/containment_drill_narrated.ring` |
| `virtual_system_twin_narrated` | 48 | `base/test/system/virtual_system_twin_narrated.ring` |

### 21 · The court: promises, perception, security and performance

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `testoor_promises_narrated` | 46 | `base/test/testoor/testoor_promises_narrated.ring` |
| `threat_model_narrated` | 11 | `base/test/security/threat_model_narrated.ring` |
| `security_ledger_narrated` | 35 | `base/test/system/security_ledger_narrated.ring` |
| `secretstore_narrated` | 26 | `base/test/system/secretstore_narrated.ring` |
| `secret_narrated` | 53 | `base/test/system/secret_narrated.ring` |
| `stopwatch_narrated` | 35 | `base/test/perf/stopwatch_narrated.ring` |
| `tracing_tail_narrated` | 26 | `base/test/perf/tracing_tail_narrated.ring` |
| `governed_loop_narrated` | 31 | `base/test/perf/governed_loop_narrated.ring` |
| `security_sentinel_narrated` | 33 | `base/test/system/security_sentinel_narrated.ring` |

### 22 · Compared, honestly

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `numeric_exactness_narrated` | 39 | `base/test/number/numeric_exactness_narrated.ring` |
| `numeric_no_loss_narrated` | 31 | `base/test/number/numeric_no_loss_narrated.ring` |
| `semantic_resolver_narrated` | 83 | `base/test/natural/semantic_resolver_narrated.ring` |
| `engine_is_optimised_narrated` | 7 | `base/test/number/engine_is_optimised_narrated.ring` |

### 23 · A world, a constellation, a platform, and the architect

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `06_stzsuperapp_narrated` | 21 | `base/test/app/06_stzsuperapp_narrated.ring` |
| `01_platform_narrated` | 31 | `base/test/platform/01_platform_narrated.ring` |
| `full_scope_model_narrated` | 62 | `base/test/system/full_scope_model_narrated.ring` |
| `04_stzapp_pursue_narrated` | 11 | `base/test/app/04_stzapp_pursue_narrated.ring` |
| `05_stzapp_live_narrated` | 11 | `base/test/app/05_stzapp_live_narrated.ring` |

### 24 · Rehearse, then commit

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `service_registry_narrated` | 93 | `base/test/system/service_registry_narrated.ring` |
| `service_delivery_narrated` | 60 | `base/test/system/service_delivery_narrated.ring` |
| `virtual_system_twin_narrated` | 48 | `base/test/system/virtual_system_twin_narrated.ring` |
| `virtual_environment_twin_narrated` | 38 | `base/test/system/virtual_environment_twin_narrated.ring` |
| `emulator_narrated` | 39 | `base/test/system/emulator_narrated.ring` |
| `deployment_narrated` | 63 | `base/test/system/deployment_narrated.ring` |
| `full_scope_model_narrated` | 62 | `base/test/system/full_scope_model_narrated.ring` |

### 25 · Your users keep their medium

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `sms_port_narrated` | 53 | `base/test/system/sms_port_narrated.ring` |
| `wisecoding_rich_narrated` | 52 | `base/test/conversation/wisecoding_rich_narrated.ring` |
| `sound_convergence_narrated` | 26 | `base/test/sound/sound_convergence_narrated.ring` |
| `sound_listener_narrated` | 21 | `base/test/sound/sound_listener_narrated.ring` |
| `sound_semantics_narrated` | 41 | `base/test/sound/sound_semantics_narrated.ring` |
| `payments_webhooks_narrated` | 51 | `base/test/system/payments_webhooks_narrated.ring` |

### 26 · The environment

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `gui_stzui_narrated` | 58 | `base/test/gui/gui_stzui_narrated.ring` |
| `gui_profile_narrated` | 35 | `base/test/gui/gui_profile_narrated.ring` |
| `gui_tier_agreement_narrated` | 24 | `base/test/gui/gui_tier_agreement_narrated.ring` |
| `gui_accessibility_narrated` | 37 | `base/test/gui/gui_accessibility_narrated.ring` |
| `05_stzapp_live_narrated` | 11 | `base/test/app/05_stzapp_live_narrated.ring` |
| `emulator_narrated` | 39 | `base/test/system/emulator_narrated.ring` |

### 27 · The engine beneath: three layers, one engine, Haro

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `engine_is_optimised_narrated` | 7 | `base/test/number/engine_is_optimised_narrated.ring` |
| `engine_senses_narrated` | 36 | `base/test/perf/engine_senses_narrated.ring` |
| `wasm_narrated` | 23 | `base/test/system/wasm_narrated.ring` |
| `threat_model_narrated` | 11 | `base/test/security/threat_model_narrated.ring` |

### 28 · A restaurant in Lyon

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `06_stzsuperapp_narrated` | 21 | `base/test/app/06_stzsuperapp_narrated.ring` |
| `service_delivery_narrated` | 60 | `base/test/system/service_delivery_narrated.ring` |
| `payments_port_narrated` | 49 | `base/test/system/payments_port_narrated.ring` |
| `judgment_narrated` | 41 | `base/test/perf/judgment_narrated.ring` |
| `graphrule_object_narrated` | 34 | `base/test/graph/graphrule_object_narrated.ring` |

### 29 · A bank in Niamey

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `orgrule_narrated` | 22 | `base/test/graph/orgrule_narrated.ring` |
| `14_bceao_governance` | 1 | `base/test/orgchart/14_bceao_governance.ring` |
| `15_multiple_validators` | 1 | `base/test/orgchart/15_multiple_validators.ring` |
| `13_segregation_of_duties` | 1 | `base/test/orgchart/13_segregation_of_duties.ring` |
| `rulereport_narrated` | 23 | `base/test/graph/rulereport_narrated.ring` |
| `36_import_from_stzorg` | 3 | `base/test/orgchart/36_import_from_stzorg.ring` |

### 30 · An organisation in the field

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `graphruleset_narrated` | 25 | `base/test/graph/graphruleset_narrated.ring` |
| `gg_rule_governance` | 29 | `base/test/graph/gg_rule_governance.ring` |
| `wisecoding_narrated` | 13 | `base/test/conversation/wisecoding_narrated.ring` |
| `governance_narrated` | 19 | `base/test/governance/governance_narrated.ring` |
| `governance_lineage_narrated` | 37 | `base/test/governance/governance_lineage_narrated.ring` |
| `01_platform_narrated` | 31 | `base/test/platform/01_platform_narrated.ring` |

### 31 · What the projects did not prove

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `service_registry_narrated` | 93 | `base/test/system/service_registry_narrated.ring` |
| `full_scope_model_narrated` | 62 | `base/test/system/full_scope_model_narrated.ring` |
| `payments_live_adapter_narrated` | 125 | `base/test/system/payments_live_adapter_narrated.ring` |
| `sound_mu5_narrated` | 20 | `base/test/sound/sound_mu5_narrated.ring` |
| `deployment_narrated` | 63 | `base/test/system/deployment_narrated.ring` |
| `orgrule_narrated` | 22 | `base/test/graph/orgrule_narrated.ring` |
| `governance_narrated` | 19 | `base/test/governance/governance_narrated.ring` |

### 32 · Many minds on one body of work

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `coderule_narrated` | 77 | `base/test/meta/coderule_narrated.ring` |
| `codegraph_narrated` | 28 | `base/test/meta/codegraph_narrated.ring` |
| `coderule_project_narrated` | 13 | `base/test/meta/coderule_project_narrated.ring` |

### 33 · The one line still owed

| Guard | Assertions | Where in the library's test tree |
|---|---|---|
| `full_scope_model_narrated` | 62 | `base/test/system/full_scope_model_narrated.ring` |
| `virtual_system_twin_narrated` | 48 | `base/test/system/virtual_system_twin_narrated.ring` |
| `service_delivery_narrated` | 60 | `base/test/system/service_delivery_narrated.ring` |
