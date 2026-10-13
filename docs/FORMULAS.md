# Physics formula implementation register

The eight-book phase contains one handoff book and seven calculation books with 38 registered formula IDs. The source expressions, inputs, source locations, owner aliases, evidence rows and boundaries are preserved in `data/physics_formula_register.json`. Method/example checks in a workbook do not approve site-specific values.

## Source-to-function mapping

| Group | IDs | C implementation priority | Owner/boundary |
|---|---|---|---|
| Equipment/rack | F-PWR-001-006 | E4/E5 BoR and AC boundaries | Team C |
| Electrical/UPS | F-ELE-001-007 | E4/E5 capacity/loss checks | Team C; topology evidence needed |
| PUE/facility | F-FAC-001-004 | E5 matched energy/factor method | Team C |
| Profile/energy | F-ENE-001-005 | Starter implements general weighted profile | Team C |
| Heat/capacity | F-THM-001-006 | C supplies IT-room heat; B owns cooling adequacy | Joint boundary |
| Air transport | F-AIR-001-004 | Interface reference, not core C cooling selection | Team B |
| Liquid/COP/water | F-LIQ-001-006 | Interface reference and overhead coupling | Team B |

## Every registered formula

| ID | Source expression | Source location | Applicability/limitation |
|---|---|---|---|
| F-PWR-001 | P_server=n_server × p_server_AC | NVIDIA · Why the gap exists | One server figure includes GPUs/CPU/PSU; never add their TDP again. |
| F-PWR-002 | P_other=P_network+P_storage | PUE · Executive summary, IT boundary | List all other IT classes; this worked example has only two. |
| F-PWR-003 | P_IT=P_server+P_other | PUE · §3.1 measurement boundary | A sum of selected operating values is a scenario estimate, not measured annual PUE denominator. |
| F-PWR-004 | P_rack=n_rack × p_server,max+p_network,max,in_rack | HAND · §13.7/13.8 | Other rack devices and simultaneous power basis must be explicit. |
| F-PWR-005 | P_noncoincident_bound=n_server × p_server,max+p_network,max+p_storage,max | NVIDIA · Why the gap exists | Not observed coincident peak; source warns peaks may differ in time. |
| F-PWR-006 | Margin=P_rack_limit−P_rack_peak | PACK · §5 Rack/PDU fields | A positive result does not validate wiring, derating or redundancy. |
| F-ELE-001 | P_in=P_out/η_UPS | SCHUPS · Definition | Never take efficiency from another load/mode; do not add UPS loss again through PUE. |
| F-ELE-002 | P_loss=P_in−P_out | SCHUPS · Definition | Heat location depends on physical placement; not all goes to IT room. |
| F-ELE-003 | S=P_active/PF | SCH3 · Power table | PF belongs to same circuit/load; distortion and unbalanced phase design require separate check. |
| F-ELE-004 | I=1000 P_kW/(sqrt(3) U_LL PF) | SCH3 · Balanced three-phase table | Only balanced three-phase steady-state; code/thermal/short-circuit checks separate. |
| F-ELE-005 | Margin_kW=P_rated−P_out | PACK · §5 UPS field dictionary | Not a safety factor or code compliance assessment. |
| F-ELE-006 | Margin_kVA=S_rated−S_demand | SCH3 · Power table | Both kW and kVA margins must be examined. |
| F-ELE-007 | P_surviving=P_installed−P_largest | UPTIME · Tier classification discussion | Distribution path, UPS mode, shared failure and Tier status require separate topology evaluation. |
| F-FAC-001 | PUE=E_fac/E_IT | PUE · Executive summary; §§3.1–3.2 | Annual measured category requires meter locations, scope and non-electric energy treatment. |
| F-FAC-002 | P_fac,plan=P_IT×PUE_plan | PUE · PUE definition (derived scenario inversion) | An annual energy-based PUE is not automatically a design-peak multiplier. |
| F-FAC-003 | P_overhead=P_fac,plan−P_IT | PUE · §3.1 facility/IT boundary | Includes UPS/cooling/lighting inside chosen boundary; do not add separately. |
| F-FAC-004 | E_overhead=E_fac−E_IT | PUE · §3.1 energy boundary | Difference requires E_fac >= E_IT; if not, meter boundary/data issue. |
| F-ENE-001 | E_1=P_mean,1×Δt | NIST · Watt-hour to joule unit entry | Do not use instantaneous peak as interval mean. |
| F-ENE-002 | E_day=Σ_i P_mean,i×Δt_i | NIST · Watt-hour conversion; derived integration | Only a complete day if time coverage is 24 h without gaps. |
| F-ENE-003 | P_avg=E_day/(4×Δt) | NIST · Watt-hour conversion; derived inversion | If intervals differ, divide by sum of actual durations. |
| F-ENE-004 | E_year,scenario=E_day×D | NIST · Energy = power × time, derived scenario | Project assumption only; cannot be described as measured annual consumption. |
| F-ENE-005 | H_covered=4×Δt | NIST · Time units; derived sum | Continuous 24-h day requires no overlaps or gaps as well as numeric total. |
| F-THM-001 | Q_IT≈P_IT_room | DOE24 · Cooling / electrical heat link | Heat leaves via air/liquid/export paths; location and transients matter. |
| F-THM-002 | Q_air=Q_IT×(1−f_liquid)+Q_other | ASHDC · Chapter 20 hybrid cooling | f_liquid must be measured/engineered, not a universal percentage. |
| F-THM-003 | Q_liquid=Q_IT×f_liquid | ASHDC · Chapter 20 CDU/loop discussion | Assumes other room heat is air-side and no uncounted exports. |
| F-THM-004 | Q_required=Q_air+Q_liquid | ASH20 · §2.2 loads and heat balance | Not PUE×IT power; non-IT outdoor plant losses do not all heat IT room. |
| F-THM-005 | Q_surviving=Q_installed−Q_largest | UPTIME · Tier redundancy discussion | Individual ratings must hold at design temperatures and flow; paths shared failure matter. |
| F-THM-006 | u=Q_required/Q_surviving | HAND · §13.9 | If surviving=0, result blocked, never claim zero utilization. |
| F-AIR-001 | m_dot=Q_s/(c_p ΔT) | ASH20 · Chapter 13 §2.2 Eq. (1), inverted | Property basis must match dry/moist air convention and actual state. |
| F-AIR-002 | V_dot=m_dot/ρ_air | ASH25 · Chapter 18, standard/actual air density | Do not use sea-level density for elevated/hot site uncritically. |
| F-AIR-003 | Q_total=m_dot×Δh | ASH20 · Chapter 13 §2.2 Eq. (4) | If humidity changes, Q_total can differ from sensible; enthalpy must share kg basis. |
| F-AIR-004 | Q_latent=Q_total−Q_s | ASH25 · Chapter 18 sensible and latent equations | A negative result indicates mismatched properties or state/boundary; flag. |
| F-LIQ-001 | m_dot=Q_loop/(c_p ΔT_liq) | ASH20 · Chapter 13 §2.2 Eq. (7), inverted | No pump/head sizing or two-phase refrigerant; use mixture properties. |
| F-LIQ-002 | V_dot=1000 m_dot/ρ_liq | ASH20 · Chapter 13 §2.2 Eq. (8) | Flow is circulated water, not consumed water. |
| F-LIQ-003 | Q_selected=m_selected×c_p×ΔT | ASH20 · Chapter 13 §2.2 Eq. (7) | Matched fluid, temperatures, branch routing and real flow measurement are required. |
| F-LIQ-004 | P_cool=Q_cooling/COP | ASHCOP · Cooling system energy COP entry | COP must include correct equipment/fan/pump boundary, not a fixed site value. |
| F-LIQ-005 | Q_reject=Q_cooling+P_cool | ASHDC · Chapter 20 loop/heat-exchanger boundary, derived energy balance | Conditional: electrical losses may be rejected elsewhere; define equipment boundary. |
| F-LIQ-006 | WUE=W_site/E_IT | DOEW · WUE displayed equation | Not a water demand prediction from thermal load; site meter and scope required. |

## Corrections before coding

F-ENE-003 and F-ENE-005 use `4 × Δt` for their specific four-bin equal-width example. General profiles use sum(duration_i); do not carry four-bin assumptions into arbitrary-length production profiles. The implemented average is sum(P_i × h_i)/sum(h_i).

F-FAC-001 defines matched facility/IT energy PUE. The starter conditionally inverts this relation for a supplied scenario factor to estimate facility energy; it does not measure annual PUE or design-peak power. Record method/boundary explicitly. F-FAC-002 power multiplication requires a factor applicable at that load/time; annual PUE alone does not establish it.

F-PWR-004 uses the source symbol n_rack for a count multiplying server power; normalize the variable name to servers_in_rack after checking Variables sheet. Do not interpret it as total number of racks. Preserve the source expression alongside the corrected implementation notation.

Do not use whole-facility PUE-scaled load as IT-room cooling heat. Do not add inclusive server AC power plus GPU TDP. Cooling and UPS losses are included once only. Air/liquid fractions, COP, fluid properties, PF, efficiency and redundancy topology require evidence.

## Cost/carbon methods

Flat electricity scenario: facility_energy_kwh × tariff_pkr_per_kwh. Operational carbon scenario: facility_energy_kwh × matched factor_kgCO2e_per_kWh. These are explicit starter arithmetic methods supported by the architecture/data-findings intent; they are not assigned invented Physics IDs. Full time-of-use tariffs and lifecycle carbon require expanded contracts. Missing PUE/factors produce null.
