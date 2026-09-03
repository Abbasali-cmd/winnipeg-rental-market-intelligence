# Data Dictionary

## Winnipeg Census-Tract Rental Market Analytical Dataset

File: `data/processed/winnipeg_ct_rental_market_analytical.csv`

| Variable | Description | Unit / Interpretation |
|---|---|---|
| `ct_id` | Winnipeg census tract identifier | Census tract code |
| `geo` | Census tract geography label | Geographic identifier |
| `units_total` | Total rental units in CMHC universe | Units |
| `units_bachelor` | Bachelor rental units | Units |
| `units_1br` | One-bedroom rental units | Units |
| `units_2br` | Two-bedroom rental units | Units |
| `units_3br_plus` | Three-bedroom-plus rental units | Units |
| `share_bachelor` | Bachelor share of rental supply | Proportion |
| `share_1br` | One-bedroom share of rental supply | Proportion |
| `share_2br` | Two-bedroom share of rental supply | Proportion |
| `share_3br_plus` | Three-bedroom-plus share of rental supply | Proportion |
| `rent_bachelor` | Average bachelor rent | Monthly dollars |
| `rent_1br` | Average one-bedroom rent | Monthly dollars |
| `rent_2br` | Average two-bedroom rent | Monthly dollars |
| `rent_3br_plus` | Average three-bedroom-plus rent | Monthly dollars |
| `rent_total` | Total average rent across reported rental units | Monthly dollars |
| `vacancy_bachelor` | Bachelor vacancy rate | Percent |
| `vacancy_1br` | One-bedroom vacancy rate | Percent |
| `vacancy_2br` | Two-bedroom vacancy rate | Percent |
| `vacancy_3br_plus` | Three-bedroom-plus vacancy rate | Percent |
| `vacancy_total` | Total vacancy rate | Percent |
| `median_household_income_2020` | Median household total income for 2020 | 2020 constant dollars |
| `annual_rent_total` | Annualized total average rent | `rent_total × 12` |
| `rent_income_pct` | Annualized rent-to-median-household-income indicator | Percent |
| `affordability_tier` | Relative quartile classification of rent-income indicator | Lower / Moderate / Higher / Highest |

## Important Interpretation Notes

### Rental Supply

Rental-unit counts represent the CMHC Rental Market Survey universe and should not be interpreted as the complete housing stock.

### Rent

Average rents are monthly rental-market measures. Suppressed or unavailable observations remain missing.

### Vacancy

Vacancy rates are reported as percentages. Missing or suppressed observations are not converted to zero.

### Household Income

The income variable represents median household total income for 2020 from the 2021 Census, expressed in 2020 constant dollars.

### Rent-to-Income Indicator

The project calculates:

**Annualized total average rent / median household income × 100**

This is an ecological market-level indicator. It is **not** an individual household rent-burden measure.

### Reliability and Suppression

CMHC reliability information is retained in the source processing workflow. Suppressed (`**`) and unavailable (`--`) observations are treated as missing rather than zero.
