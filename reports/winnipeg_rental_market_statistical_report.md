# Winnipeg Rental Market Intelligence

## Statistical and Business Analysis Report

**Geographic scope:** Winnipeg census tracts  
**Primary market data:** CMHC Rental Market Survey  
**Income data:** Statistics Canada 2021 Census  
**Analytical period:** 2023 rental-market observations with 2021 Census income context

---

## Executive Summary

Winnipeg's rental market varies substantially across census tracts in terms of rental supply, average rents, vacancy, and the relationship between rental costs and local household income.

This project integrates Canada Mortgage and Housing Corporation (CMHC) Rental Market Survey data with 2021 Census household-income data from Statistics Canada to examine these patterns at the census-tract level.

The integrated analytical dataset contains **187 Winnipeg census tracts and 25 analytical variables**. Because CMHC reporting coverage varies across rental-market measures, individual analyses use the observations available for the relevant variables rather than restricting the entire project to a single complete-case sample.

### Key Findings

1. **Rental prices are positively associated with household income.** Among 77 census tracts with usable total-rent and income observations, the Pearson correlation was **r = 0.577** and the Spearman correlation was **rho = 0.498**. Higher-income areas therefore tend to have higher average rents.

2. **Higher-income areas tend to have lower relative rental-cost indicators.** The annualized total-rent-to-median-household-income indicator had a median value of **19.3%** across 77 observations and was negatively associated with household income (**Spearman rho = -0.506**). This indicates that higher-income areas generally have higher rents but rental costs represent a smaller share of median household income.

3. **Rental supply is concentrated geographically.** Among 135 census tracts with usable supply data, median rental supply was **223 units per tract**, with a maximum of **954 units**. Approximately **91%** of observed rental units were 1- or 2-bedroom units.

4. **Vacancy is low in most observed census tracts but varies considerably.** Among 57 tracts with usable total vacancy data, median vacancy was **0.7%**, while the maximum observed value was **26.0%**. The 26% observation was retained because it is a legitimate reported value and was assessed through sensitivity analysis rather than arbitrarily removed.

5. **The multivariable rent model explains substantial cross-tract variation.** A model using log-transformed rental supply and median household income explained approximately **68% of the variation in total average rent** across 59 census tracts (**R2 = 0.678; adjusted R2 = 0.666**). Mean absolute error was approximately **$138** and RMSE was approximately **$166**.

6. **The model relationships are observational.** Larger rental inventories and higher median household income are positively associated with total average rent after accounting for the other predictor. These coefficients should not be interpreted as causal effects.

7. **Winnipeg rents are higher than the selected rural/small-centre benchmark.** The Winnipeg census-tract median total average rent was **$1,124**, compared with **$848** among 10 Manitoba rural/small-centre CSDs with usable observations. The rural/small-centre median was approximately **24.6% lower**.

### Business Interpretation

The analysis suggests that Winnipeg's rental market should not be evaluated using rent alone. Rental prices, rental supply, vacancy, and local income provide different perspectives on market conditions.

In particular, the results show why a high-rent area is not necessarily the least affordable area when rental costs are evaluated relative to local median household income. Conversely, lower-rent areas can have higher relative rental-cost indicators when local household incomes are substantially lower.

For analysts and decision-makers, this supports monitoring rental-market conditions using multiple indicators rather than relying on a single citywide average.

### Important Caveat

The rent-to-income measure is an **ecological market indicator**, not a household-level affordability or rent-burden measure. It combines area-level average market rent with area-level median household income and should therefore be interpreted as a geographic comparison rather than evidence about individual households.

---

## 6. Rental Prices and Income

### 6.1 Objective

This analysis examines whether census tracts with higher median household income also tend to have higher average rental prices.

The analysis focuses on total average monthly rent and median household total income for 2020. Because both measures are aggregated at the census-tract level, the results describe geographic associations rather than individual household behaviour.

### 6.2 Sample

There are **77 Winnipeg census tracts** with non-missing observations for both total average rent and median household income.

The remaining census tracts are not treated as zero-rent observations. CMHC suppression and availability codes are retained as missing during data preparation.

### 6.3 Correlation Results

The Pearson correlation between total average rent and median household income is **r = 0.577**, indicating a moderately strong positive linear association.

The Spearman rank correlation is **rho = 0.498**, also indicating a positive monotonic association.

Both relationships are statistically significant.

The two correlation measures provide complementary evidence. Pearson correlation assesses linear association, while Spearman correlation assesses whether higher values of one variable generally correspond to higher values of the other without requiring the relationship to be strictly linear.

### 6.4 Interpretation

The results indicate that higher-income Winnipeg census tracts tend to have higher average rental prices.

This does not mean that household income causes rents to be higher. Census tracts differ in many characteristics that are not captured by this bivariate analysis, including housing composition, neighbourhood characteristics, and rental-market structure.

The finding is therefore best interpreted as a **cross-sectional geographic association**.

### 6.5 Analytical Implication

A citywide rental-price statistic can conceal important geographic differences. The positive rent-income relationship demonstrates why rental-market analysis benefits from considering local economic context alongside rental prices.

The next section extends this analysis by examining rental costs relative to median household income using a market-level affordability indicator.

---

## 7. Market Affordability Indicator

### 7.1 Indicator Definition

To place rental prices in the context of local household income, the project calculates an annualized rent-to-median-household-income indicator:

**Annualized total average rent / median household income × 100**

For example, a value of 20% means that annualized average market rent is equivalent to 20% of the area's median household income.

This measure is intended for **geographic market comparison**, not as a measure of an individual household's actual rent burden.

### 7.2 Distribution

The indicator can be calculated for **77 Winnipeg census tracts** with both total average rent and median household income available.

Across these observations:

- Mean indicator: **19.95%**
- Median indicator: **19.32%**
- First quartile: **16.39%**
- Third quartile: **22.67%**
- Minimum: **12.44%**
- Maximum: **32.33%**

The distribution demonstrates meaningful geographic variation in the relationship between market rents and local household incomes.

### 7.3 Relative Affordability Tiers

For descriptive dashboard purposes, census tracts are divided into four groups using the observed quartiles of the indicator:

- **Lower relative burden**
- **Moderate relative burden**
- **Higher relative burden**
- **Highest relative burden**

These categories are relative to the Winnipeg census-tract distribution. They are **not formal affordability thresholds** and should not be interpreted as policy-defined affordability classifications.

### 7.4 Relationship with Household Income

The Spearman rank correlation between the affordability indicator and median household income is **rho = -0.506**, based on 77 census tracts.

This indicates that higher-income census tracts generally have lower annualized rent-to-median-household-income indicators.

Combined with the positive rent-income correlation from Section 6, the result produces an important market pattern: **higher-income areas tend to have higher rents, but rental costs represent a smaller proportion of median household income in those areas**.

### 7.5 Interpretation

The result suggests that examining rental prices alone can produce an incomplete picture of geographic affordability. A tract may have relatively high rents while still having a comparatively low rent-to-income indicator because household incomes are also higher.

Conversely, a tract with lower nominal rents can have a higher relative indicator if local household incomes are substantially lower.

This distinction is particularly important when comparing neighbourhoods with different socioeconomic profiles.

### 7.6 Limitation

The indicator combines an area-level average rental price with an area-level median household income. It does not observe the income or rent paid by the same household.

It therefore should **not** be described as the percentage of income that households actually spend on rent, nor as a household-level shelter-cost-to-income ratio.

The measure is best described as an **annualized market rent-to-median-household-income indicator**.

---

## 8. Rental Supply and Market Affordability

### 8.1 Objective

This analysis examines whether rental-market inventory is associated with the annualized rent-to-median-household-income indicator after accounting for local household income.

The analysis is designed to distinguish the relationship between rental supply and relative rental costs from the separate relationship between income and the affordability indicator.

### 8.2 Analytical Sample

The multivariable analysis uses **59 census tracts** with complete observations for total rental supply, total average rent, and median household income.

The smaller sample reflects the limited availability of tract-level CMHC rent observations. It is used for the regression analysis only and is not treated as representative of all 187 Winnipeg census tracts.

### 8.3 Descriptive Relationships

Rental supply has a positive association with the rent-to-income indicator.

For the 59 complete observations:

- Pearson correlation between rental supply and the indicator: **r = 0.658**
- Spearman correlation: **rho = 0.639**

Rental supply is also positively associated with total average rent in this complete-case sample, while its bivariate relationship with median household income is weak and negative.

### 8.4 Multivariable Model

An ordinary least squares regression was estimated with the annualized rent-to-median-household-income indicator as the dependent variable and total rental supply plus median household income as explanatory variables.

The model explained approximately **50% of the cross-tract variation** in the indicator:

- R-squared: **0.499**
- Adjusted R-squared: **0.481**
- Number of observations: **59**

The estimated rental-supply coefficient was **0.0084** and statistically significant (**p < 0.001**). The median-income coefficient was **-0.0000517** and was also statistically significant in the primary specification (**p = 0.009**).

The positive supply coefficient indicates that, conditional on median household income, census tracts with larger rental inventories tend to have higher values of the rent-to-income indicator.

The negative income coefficient indicates that, conditional on rental supply, higher-income census tracts tend to have lower values of the indicator.

These are conditional statistical associations and should not be interpreted as causal effects.

### 8.5 Model Diagnostics

Diagnostic testing did not identify substantial evidence of non-normal residuals or heteroskedasticity in the primary specification.

The Shapiro-Wilk test produced **W = 0.977, p = 0.321**, while the Breusch-Pagan test produced **p = 0.301**.

The Durbin-Watson statistic was approximately **1.63**.

Variance inflation factors for the two explanatory variables were approximately **1.03**, indicating very little evidence of multicollinearity between rental supply and median household income.

### 8.6 Influence and Sensitivity Analysis

Four observations exceeded the project's Cook's-distance screening threshold of **4/n**. These observations were retained in the primary model because their underlying values appeared plausible rather than being obvious data errors.

As a sensitivity check, all four observations were excluded simultaneously. The resulting model produced an R-squared of **0.501**, compared with **0.499** in the primary model.

The rental-supply coefficient changed from **0.0084** to approximately **0.0087**, while remaining statistically significant.

The income coefficient remained negative but was no longer statistically significant after excluding the influential observations (**p = 0.102**).

This suggests that the positive association between rental supply and the rent-to-income indicator is more robust than the income coefficient in this particular complete-case sample.

### 8.7 Interpretation

The analysis does not support the claim that increasing rental supply causes affordability to improve or worsen. Instead, it shows that rental-market inventory is statistically associated with the observed rent-to-income indicator after accounting for local median household income.

The result should also be interpreted in light of the substantial missingness in tract-level CMHC rent and vacancy data. The 59-tract regression sample represents the subset of Winnipeg census tracts for which all required variables were reported.

---

## 9. Rental Price Model

### 9.1 Objective

The rental-price model examines which tract-level characteristics are associated with differences in total average monthly rent.

The model uses median household income and the logarithm of total rental supply as explanatory variables. The log transformation reduces the influence of very large rental inventories and provides a more appropriate functional form for the highly right-skewed supply variable.

### 9.2 Model Specification

The estimated ordinary least squares model is:

**Total average rent = -702.91 + 168.75 × log(rental supply + 1) + 0.0112 × median household income + error**

The model is estimated using **59 census tracts** with complete observations for total rent, rental supply, and median household income.

### 9.3 Model Fit

The model explains approximately **68% of the cross-tract variation in total average rent**:

- R-squared: **0.678**
- Adjusted R-squared: **0.666**
- F-statistic: **58.87**
- Model p-value: **1.71 × 10^-14**

Out-of-sample prediction is not claimed because the analysis is primarily explanatory and uses a relatively small cross-sectional sample.

Within the observed sample, mean absolute error was approximately **$138**, while root mean squared error was approximately **$166**.

### 9.4 Coefficient Interpretation

The coefficient on log rental supply was **168.75** and statistically significant.

Because supply is log-transformed, this coefficient should not be interpreted as an additional $168.75 of rent for every additional rental unit. Instead, the result indicates that census tracts with larger rental-market inventories tend to have higher average rents after accounting for median household income.

Median household income had a coefficient of approximately **0.0112** and was statistically significant.

Holding logged rental supply constant, a **$10,000 difference in median household income corresponds to approximately a $112 difference in predicted monthly total average rent**.

Both coefficients represent conditional associations rather than causal effects.

### 9.5 Multicollinearity

Variance inflation factors were approximately **1.01** for both explanatory variables.

This provides little evidence of problematic multicollinearity between logged rental supply and median household income.

The large condition number reported by the regression software is primarily attributable to differences in variable scale, particularly the dollar-valued income variable, rather than strong correlation between the predictors.

### 9.6 Model Diagnostics

The residual diagnostics did not indicate substantial departures from normality.

The Jarque-Bera test produced **p = 0.609**, with residual skewness of approximately **0.031** and kurtosis of approximately **2.37**.

The Durbin-Watson statistic was approximately **1.68**.

These diagnostics provide reasonable support for the primary OLS specification, while the cross-sectional geographic structure means that the results should still be interpreted cautiously.

### 9.7 Influence Analysis

Using a Cook's-distance screening threshold of **4/n**, one observation was identified as influential: census tract **0110.06**.

The observation was retained in the primary model because its rent, rental supply, and income values appeared plausible rather than representing an obvious data error.

A sensitivity model excluding this observation produced:

- R-squared: **0.699**, compared with 0.678 in the primary model
- Logged supply coefficient: **169.61**, compared with 168.75
- Income coefficient: **0.0120**, compared with 0.0112

The supply coefficient changed by approximately **0.5%**, while the income coefficient changed by approximately **7.2%**.

Both explanatory variables remained statistically significant in the sensitivity model.

The results therefore suggest that the primary model's substantive conclusions are not dependent on the single influential observation.

### 9.8 Interpretation

The model provides evidence that rental supply and local household income are both associated with cross-tract differences in average rental prices.

The relatively high R-squared indicates that these two variables capture a substantial portion of the observed geographic variation, but it should not be interpreted as proof that they determine rental prices.

Other factors—including neighbourhood characteristics, building age, housing quality, location, and broader market conditions—may also contribute to differences in rental prices and are not included in this model.

---

## 10. Vacancy and Market Pressure

### 10.1 Objective

Vacancy provides a complementary view of rental-market conditions. While rent measures the price of available rental housing, vacancy indicates the proportion of surveyed rental units that were unoccupied and available within the CMHC Rental Market Survey universe.

This section examines the distribution of vacancy across Winnipeg census tracts and its association with rental prices and local household income.

### 10.2 Vacancy Distribution

Total vacancy is available for **57 of the 187 Winnipeg census tracts** in the integrated dataset.

Among these observations:

- Mean vacancy: **1.82%**
- Median vacancy: **0.70%**
- First quartile: **0.40%**
- Third quartile: **1.80%**
- Maximum vacancy: **26.0%**

The distribution is therefore highly concentrated at relatively low vacancy rates, with a small number of tracts reporting substantially higher values.

### 10.3 Highest Observed Vacancy

The highest reported total vacancy rate is **26.0%** in census tract **0538.00**.

This observation corresponds to 96 rental units in the CMHC supply data, a total average rent of $1,097, and median household income of $90,000.

The observation is retained in the primary analysis because it is a reported market value rather than an identified data-entry error.

### 10.4 Vacancy and Rental Prices

Among **54 census tracts** with complete total vacancy, total rent, and income observations, the Spearman correlation between vacancy and total average rent is **rho = -0.328 (p = 0.015)**.

This indicates that higher-rent tracts tend to have lower observed vacancy rates within the available sample.

The relationship should be interpreted as an association rather than evidence that higher rents cause lower vacancy.

### 10.5 Vacancy and Household Income

Among the **57 tracts** with usable total vacancy and income data, the Spearman correlation between vacancy and median household income is **rho = -0.371 (p = 0.0045)**.

Higher-income census tracts therefore tend to have lower observed vacancy rates in the available data.

This relationship remains present when the 26% vacancy observation in CT 0538.00 is excluded: the Spearman correlation becomes approximately **rho = -0.415 (p = 0.0015)**.

### 10.6 Sensitivity Analysis

The 26% observation is potentially influential because it is substantially larger than the rest of the observed vacancy distribution.

Rather than removing it from the primary dataset, the analysis evaluates its influence through sensitivity testing.

For the vacancy-income relationship, excluding CT 0538.00 changes the Spearman correlation from **-0.371 to -0.415**, while statistical significance remains strong.

For the vacancy-rent relationship, excluding the observation changes the Spearman correlation from **-0.328 to approximately -0.314**, with the relationship remaining statistically significant.

These results indicate that the broad negative associations are not dependent on the single highest-vacancy observation.

### 10.7 Interpretation

The observed vacancy pattern suggests that Winnipeg's rental-market conditions differ across census tracts. Most observed tracts have relatively low vacancy, while a small number have substantially higher vacancy.

The negative associations with rent and income suggest that higher-rent and higher-income areas generally have lower observed vacancy in the available sample.

However, vacancy coverage is limited to 57 of 187 tracts. The analysis therefore describes the reported CMHC observations rather than estimating vacancy for all Winnipeg census tracts.

### 10.8 Analytical Limitation

The vacancy results should not be interpreted as a complete measure of rental-market pressure across Winnipeg. CMHC survey coverage, suppression, and the structure of the Rental Market Survey universe limit the geographic coverage of the measure.

Missing vacancy observations are retained as missing throughout the analysis rather than being interpreted as zero vacancy.

---

## 11. Manitoba Benchmark

### 11.1 Objective

To provide geographic context for the Winnipeg results, the project compares selected Winnipeg census-tract rental-market statistics with a secondary benchmark consisting of Manitoba rural and small-centre census subdivision (CSD) observations.

The rural/small-centre benchmark is descriptive and is not intended to represent all rental housing outside Winnipeg.

### 11.2 Rental Prices

The median total average rent among Winnipeg census tracts with usable observations is **$1,124 per month**.

The corresponding median among the selected Manitoba rural/small-centre CSD observations is **$848 per month**.

The rural/small-centre benchmark is therefore approximately **24.6% lower** than the Winnipeg census-tract median.

This difference provides a useful descriptive indication of the rental-price gap between Winnipeg and the selected smaller Manitoba markets.

### 11.3 Vacancy

The median observed total vacancy rate is **0.70%** among Winnipeg census tracts with usable vacancy data.

The corresponding median among the selected Manitoba rural/small-centre CSD observations is **0.85%**.

The rural/small-centre benchmark is therefore approximately **0.15 percentage points higher** than the Winnipeg census-tract median.

The difference should not be interpreted as statistically significant because this benchmarking exercise is descriptive and the available sample sizes are small.

### 11.4 Sample Coverage

The Winnipeg rent comparison is based on **77 census tracts**, while the rural/small-centre rent comparison is based on only **10 CSD observations** with usable total-rent values.

For vacancy, the comparison uses **57 Winnipeg census tracts** and **8 rural/small-centre CSD observations**.

These differences in sample size substantially limit the strength of any generalization from the benchmark.

### 11.5 Geographic Comparability

The Winnipeg analysis is conducted at the census-tract level within a large urban rental market, while the rural/small-centre benchmark uses census subdivisions representing smaller markets.

The two geographic systems therefore should not be treated as perfectly equivalent analytical units.

The benchmark is used to provide context rather than to establish a causal or population-level estimate of the difference between urban and rural rental markets.

### 11.6 Interpretation

The benchmark indicates that observed rental prices are materially lower in the selected Manitoba rural/small-centre markets than in Winnipeg.

At the same time, the observed vacancy medians are relatively close, with the rural/small-centre benchmark slightly higher.

Taken together, these descriptive results reinforce the importance of considering both rental prices and vacancy when comparing rental-market conditions across geographic contexts.

### 11.7 Limitation

The rural/small-centre benchmark is based only on observations with usable CMHC values and should not be interpreted as a complete estimate of Manitoba's non-Winnipeg rental market.

The benchmark also uses different geographic scales and survey contexts from the Winnipeg census-tract analysis. It is therefore best presented as a **descriptive comparison**, not as formal statistical inference.

---

## 12. Business Interpretation

### 12.1 Why a Multi-Indicator View Matters

The analysis demonstrates that Winnipeg's rental market cannot be adequately described using a single rental-price statistic.

Rental prices, rental supply, vacancy, and household income capture different dimensions of the market. Examining them together provides a more informative view of geographic differences in rental-market conditions.

### 12.2 Rental Price and Local Economic Context

Higher-income census tracts tend to have higher average rents. The positive rent-income relationship indicates that nominal rent comparisons should be interpreted alongside local economic conditions.

A high-rent area is therefore not automatically the least affordable area when rental costs are considered relative to local median household income.

### 12.3 Relative Rental-Cost Pressure

The market affordability indicator provides a second perspective on rental costs.

The negative relationship between the indicator and household income shows that areas with higher household incomes generally have lower relative rental-cost indicators, despite tending to have higher nominal rents.

This suggests that decision-makers interested in rental-market pressure should monitor both the level of rent and the economic context in which those rents occur.

### 12.4 Rental Supply

Rental supply is geographically concentrated. The median observed rental inventory is 223 units per census tract, while the largest observed tract contains 954 units.

Approximately 91% of observed rental units are either one- or two-bedroom units.

This composition suggests that the one- and two-bedroom segments are particularly important when evaluating the structure of Winnipeg's purpose-built rental-market inventory.

### 12.5 Vacancy and Market Conditions

Most observed census tracts have relatively low vacancy, although the distribution includes substantial geographic variation.

The negative associations between vacancy and both rent and household income suggest that vacancy should be monitored alongside price and income rather than interpreted independently.

The limited geographic coverage of tract-level vacancy data means that these findings should be treated as evidence about the observed CMHC sample rather than the entire Winnipeg market.

### 12.6 Potential Analytical Uses

The integrated dataset and dashboard could support several recurring analytical tasks:

- Identifying census tracts with relatively high rental costs.
- Comparing rental prices with local household-income conditions.
- Monitoring the geographic concentration and bedroom composition of rental supply.
- Identifying areas with unusually high or low observed vacancy.
- Benchmarking Winnipeg rental prices against selected smaller Manitoba markets.
- Prioritizing locations for deeper investigation using additional neighbourhood or housing-market data.

### 12.7 What the Analysis Does Not Establish

The results do not establish that rental supply causes rents to increase or decrease, that household income causes rents or vacancy to change, or that a particular neighbourhood is objectively affordable or unaffordable for individual households.

The analysis is observational and cross-sectional. The statistical relationships should therefore be interpreted as associations that can motivate further investigation rather than as causal estimates.

### 12.8 Decision-Making Implication

The strongest practical conclusion is that rental-market monitoring benefits from an integrated framework.

A useful market-monitoring system should combine **price, supply, vacancy, and local income context**, while explicitly reporting data coverage and uncertainty.

The project's dashboard is designed around this principle by presenting the four dimensions separately and then connecting them through statistical analysis.

---

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

---

## 14. Conclusion

This project provides an integrated statistical view of Winnipeg's rental market using census-tract-level rental supply, average rent, vacancy, and household-income data.

The analysis finds substantial geographic variation across Winnipeg. Higher-income census tracts tend to have higher average rents, while also tending to have lower annualized rent-to-median-household-income indicators. Rental supply is concentrated in particular census tracts, with one- and two-bedroom units accounting for approximately 91% of observed rental inventory.

Vacancy is relatively low in most observed census tracts but varies substantially across the available sample. The observed relationships between vacancy, rent, and household income remain broadly similar after sensitivity analysis of the highest-vacancy observation.

The rental-price regression provides additional evidence that both rental-market inventory and local household income are associated with cross-tract differences in average rent. The model explains approximately 68% of observed variation in total average rent, with similar conclusions after sensitivity analysis.

The Manitoba benchmark provides additional context: the selected rural/small-centre markets have a lower median observed rent than Winnipeg, although the comparison is based on substantially smaller samples and different geographic units.

The project's central analytical contribution is therefore not a single ranking or prediction. It is an integrated framework for examining rental-market conditions through multiple dimensions while explicitly accounting for missing data, suppression, geographic aggregation, and statistical uncertainty.

Future work could extend the project longitudinally by incorporating multiple years of CMHC observations, adding neighbourhood and building characteristics, and developing models that better account for spatial structure and changes over time.

Overall, the project demonstrates an end-to-end analytical workflow combining **data integration, data quality assessment, SQL, descriptive statistics, correlation analysis, regression modelling, diagnostics, sensitivity analysis, visualization, and business interpretation**.

---
