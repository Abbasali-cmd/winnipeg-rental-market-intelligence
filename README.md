# Winnipeg Rental Market Intelligence

## Statistical Analysis of Rental Supply, Prices, Vacancy, and Affordability

An end-to-end data analytics and statistical analysis project examining Winnipeg's rental market at the census-tract level.

The project integrates **CMHC Rental Market Survey** data with **Statistics Canada 2021 Census** household-income data and combines Python, SQL, statistical modelling, data visualization, and business interpretation.

---

## Executive Summary

This project examines:

- Rental supply and bedroom composition
- Geographic variation in average rents
- Rental vacancy and market pressure
- Rental costs relative to local household income
- Relationships between rental supply, income, rent, and vacancy
- Winnipeg versus selected Manitoba rural/small-centre markets

The analytical dataset contains **187 Winnipeg census tracts**.

### Key Findings

- Median observed total average rent: **$1,124/month**
- Median observed vacancy rate: **0.7%**
- Median rental supply: **223 units per census tract**
- Approximately **91%** of observed rental units are one- or two-bedroom units
- Rent and median household income: **Spearman ρ = 0.498**
- Rental supply and the affordability indicator: **Spearman ρ = 0.639**
- Rent-to-income indicator and income: **Spearman ρ = -0.506**
- Rental-price model: **R² = 0.678**
- Rental-price model prediction error: **MAE ≈ $138/month**
- Selected Manitoba rural/small-centre median rent: **$848/month**

## Research Question

> How do rental prices, vacancy rates, housing supply, and neighbourhood characteristics vary across Winnipeg, and what factors are associated with rental-market pressure and affordability?

The analysis is observational and cross-sectional. Statistical relationships are interpreted as associations rather than causal effects.

## Project Deliverables

### Statistical Report

**[Statistical Analysis Report](reports/winnipeg_rental_market_statistical_report.md)**

The main written deliverable covering methodology, descriptive analysis, correlations, regression models, diagnostics, sensitivity analysis, business interpretation, and limitations.

### Reproducible Analysis

**[Analysis Notebook](notebooks/01_winnipeg_rental_market_analysis.ipynb)**

A self-contained Python notebook designed to execute from the processed analytical dataset.

### Dashboard

The dashboard is organized into six analytical views:

1. Market Overview
2. Rental Supply & Composition
3. Rental Prices & Affordability
4. Vacancy & Market Pressure
5. Rent Model & Statistical Evidence
6. Manitoba Benchmarking

### Dashboard Views

| View | Focus |
|---|---|
| Market Overview | Winnipeg rental-market KPIs |
| Rental Supply & Composition | Unit supply and bedroom composition |
| Rental Prices & Affordability | Rent levels and income relationships |
| Vacancy & Market Pressure | Vacancy and market-pressure indicators |
| Rent Model & Statistical Evidence | Regression results and diagnostics |
| Manitoba Benchmarking | Winnipeg versus selected rural/small-centre markets |

### SQL

**[SQL Documentation](sql/README.md)**

Documents the SQLite analytical database, dashboard views, and example analytical queries.

### Data Dictionary

**[Data Dictionary](docs/data_dictionary.md)**

Defines the analytical variables, units, interpretation, and important data-quality conventions.

## Data Sources

### Canada Mortgage and Housing Corporation

CMHC Rental Market Survey data provide rental supply, average rent, vacancy, and rental-market measures.

### Statistics Canada

2021 Census data provide median household total income for 2020 at the census-tract level.

### Manitoba Benchmark

Additional CMHC rural/small-centre data are used for descriptive comparison with selected Manitoba CSD observations.

## Methodology

The project workflow includes:

1. Source-data acquisition
2. Data cleaning and standardization
3. Suppression and missing-value handling
4. Integration of CMHC and Statistics Canada data
5. Exploratory and descriptive analysis
6. Correlation analysis
7. OLS regression modelling
8. Model diagnostics
9. Influence and sensitivity analysis
10. SQL analytical views
11. Dashboard development
12. Business interpretation

### Statistical Methods

- Descriptive statistics
- Pearson correlation
- Spearman rank correlation
- Ordinary least squares regression
- Log-transformed rental supply
- Shapiro-Wilk normality testing
- Breusch-Pagan heteroskedasticity testing
- Variance inflation factors
- Cook's distance
- Sensitivity analysis

## Data Quality

CMHC suppression and availability indicators are preserved during processing.

Values such as `**` and `--` are treated as missing rather than zero.

Analytical sample sizes vary by question because CMHC coverage differs across rental-market measures.

| Measure | Available observations |
|---|---:|
| Median household income | 185 |
| Rental supply | 135 |
| Total average rent | 77 |
| Total vacancy | 57 |
| Rent + vacancy + income | 54 |
| Supply + rent + vacancy + income | 36 |

The project deliberately avoids forcing all analyses onto the smallest complete-case sample.

## Limitations

- Cross-sectional rather than longitudinal design
- Incomplete tract-level CMHC coverage
- CMHC survey-universe limitations
- Suppressed observations
- Ecological rather than household-level affordability measurement
- Geographic aggregation
- Small samples for some statistical analyses
- Potential omitted variables
- Rural/small-centre benchmark uses different geographic units

The project does not establish causal effects.

## Repository Structure

```text
winnipeg_rental_market_intelligence/
├── data/
│   ├── raw/
│   │   ├── cmhc/
│   │   └── statcan/
│   └── processed/
│       ├── dashboard/
│       └── statcan/
├── dashboard/
├── docs/
│   └── data_dictionary.md
├── notebooks/
│   └── 01_winnipeg_rental_market_analysis.ipynb
├── reports/
│   ├── README.md
│   ├── executive_summary.md
│   └── winnipeg_rental_market_statistical_report.md
├── sql/
│   └── README.md
├── src/
├── .gitignore
├── README.md
└── requirements.txt
```
## Technical Skills

**Python:** pandas · NumPy · SciPy · statsmodels · Matplotlib

**SQL:** SQLite · Analytical Queries · Database Views

**Statistics:** Descriptive Statistics · Pearson Correlation · Spearman Correlation · OLS Regression · Model Diagnostics · Sensitivity Analysis

**Data Engineering:** Data Cleaning · Data Integration · Missing-Value Handling · Geographic Data Preparation

**Visualization:** Matplotlib · Seaborn · SVG · Dashboard Design

**Data Sources:** CMHC · Statistics Canada
