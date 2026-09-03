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