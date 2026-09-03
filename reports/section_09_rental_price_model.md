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