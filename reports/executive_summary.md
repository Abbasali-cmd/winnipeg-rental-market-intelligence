# Executive Summary

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