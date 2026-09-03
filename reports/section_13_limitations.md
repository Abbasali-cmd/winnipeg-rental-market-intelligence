## 13. Limitations

### 13.1 Cross-Sectional Design

The primary analysis is cross-sectional, using rental-market and household-income measures associated with Winnipeg census tracts. The analysis therefore identifies geographic associations at a point in time rather than estimating changes over time or causal effects.

The regression coefficients should not be interpreted as causal effects of rental supply or income on rental prices or affordability.

### 13.2 Incomplete CMHC Coverage

CMHC observations are not available for every census tract for every rental-market measure.

Income is available for 185 of 187 tracts, while total average rent is available for 77 and total vacancy for 57.

The most complete four-variable analysis contains only 36 census tracts. For this reason, the project does not use the complete-case subset as its universal analytical dataset.

Instead, each analysis uses the observations available for the variables required for that specific question.

### 13.3 Suppression and Reliability

CMHC source data contain suppression and reliability indicators. Suppressed (`**`) and unavailable (`--`) values are retained as missing rather than converted to zero.

This approach prevents the analysis from incorrectly treating unavailable rental-market observations as evidence of zero units, zero rent, or zero vacancy.

### 13.4 Rental Market Survey Coverage

The CMHC Rental Market Survey does not represent every form of rental housing. Its survey universe has specific inclusion criteria, and social or affordable housing outside the survey frame may not be represented.

Consequently, the rental-unit counts and market statistics should be understood as measures of the CMHC survey universe rather than the complete Winnipeg rental-housing stock.

### 13.5 Market-Level Affordability Indicator

The rent-to-income indicator combines census-tract average market rent with census-tract median household income.

It does not observe the income and rent of the same household and therefore cannot be interpreted as an individual household's rent burden or shelter-cost-to-income ratio.

The indicator is intended for relative geographic comparison.

### 13.6 Geographic Aggregation

The project operates primarily at the census-tract level. Census tracts contain multiple households and housing units, so relationships observed across tracts cannot automatically be applied to individual households.

This is an important ecological-inference limitation.

### 13.7 Small Analytical Samples

Several analyses use relatively small samples because of incomplete CMHC coverage.

For example, the rental-price regression uses 59 census tracts, while the vacancy analysis uses 57 for total vacancy.

Statistical estimates from these subsets should therefore be interpreted with appropriate caution.

### 13.8 Influential Observations

Influence diagnostics identified observations that could materially affect some model estimates.

Rather than removing observations solely because they were influential, the project retains plausible observations and evaluates their influence through sensitivity analysis.

This approach preserves potentially meaningful market variation while making the robustness of the statistical conclusions explicit.

### 13.9 Rural and Small-Centre Benchmark

The Manitoba rural/small-centre benchmark uses a small number of CSD observations with usable CMHC values.

The benchmark also operates at a different geographic scale from the Winnipeg census-tract analysis.

It is therefore intended as descriptive context rather than formal statistical inference about urban versus rural rental markets.

### 13.10 Future Improvements

Future versions of the project could strengthen the analysis by incorporating additional years of rental-market observations, longitudinal methods, neighbourhood characteristics, building characteristics, and more detailed measures of household housing costs.

Additional geographic and socioeconomic variables could also support more comprehensive multivariable modelling while reducing the risk of omitted-variable bias.