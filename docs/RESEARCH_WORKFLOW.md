# From research books to reviewed implementation

## Existing source families
Hardware CSVs provide products and field audits. Rule CSVs provide canonical/legacy IDs, applicability, sources and gaps. Physics workbooks provide methods, inputs, examples and boundaries. Experiment files provide historical S1/S2 scenarios/replays. Literature PDFs provide rationale and measured methods, not complete hardware compatibility or site facts.

## Method for each new formula or decision
1. State exact question and applicable workload/configuration/boundary.
2. Search primary sources: OEM datasheet/engineering guide; official MLCommons result/log; standards body; paper full text or official author/institution copy.
3. Read conditions and equations, not just abstract or search snippet.
4. Record source URL, title, date/version, page/section, field/quantity, unit, retrieval date and content hash.
5. Classify sourced measurement/rating, derived formula, calibrated proxy, scenario assumption or unavailable value.
6. Write a specification with input/output units, preconditions, source and excluded cases.
7. Independently calculate one example; identify missing/zero/nonfinite input behavior.
8. Implement as a named pure function; link stable formula ID and rule consumers.
9. Peer review applicability and evidence separately from code; activate only after tests.
10. Record protocol changes with previous/new method and reason. Re-run affected examples and benchmark regressions.

## Search log template
Question; database/site; exact query; search date; candidate result; selected/rejected reason; source version; extracted fact/formula; location; licensing/public sharing boundary; reviewer; status. Use Google Scholar/academic databases for discovery and primary full text for extraction. Hardware claims use manufacturer documents where possible. Do not label a preprint peer-reviewed simply because downloaded into Literature.

## Existing literature roles
Dayarathna: hierarchical model choice and limits. Fan: aggregate demand vs provisioned rating. Latif and Vercellino: workload-conditioned power measurement/calibration and temporal profiles. MLPerf: exact benchmark comparability and metrics. Moore/Pahlavan: placement/thermal interactions. Govindan: stored-energy/topology context. LEGUP: upgrade-design context. Carbon Explorer: operational/embodied carbon distinction. Masanet/IEA: broad demand context, not server-sizing coefficients. References register classification needs current source validation for publication dates/version and review status.

## Using workbooks
Keep separate physics subject books as research references; normalize their formula/evidence IDs into data/physics_formula_register.json. Do not merge every book into one undocumented data table. Resolve owner/phase aliases in the register. Workbook examples are synthetic/method examples, not measured site inputs. Match formula row, variables, evidence and checks together before implementation.

## How to decide evidence is sufficient
A claim needs the exact applicable source, units and conditions. Existence of a URL or a 'Verified' cell is insufficient. Missing whole-server operational power blocks corresponding operational energy claims; rated GPU TDP supports only its stated boundary. A regional tariff from an old scenario is historical until refreshed for the planned date/class. Missing quote means incomplete monetary estimate, never a made-up low-confidence price.
