# SQL Analysis Documentation

## Winnipeg Rental Market Intelligence

The project uses SQLite to store the integrated census-tract analytical dataset and create reusable analytical views for dashboard reporting.

## Database

Primary table:

`ct_rental_market`

The table contains the integrated Winnipeg census-tract rental-market dataset.

## Analytical Views

### `vw_dashboard`

Tract-level dashboard view containing:

- Census tract identifier
- Rental supply
- Bedroom composition
- Average rents
- Vacancy rates
- Median household income
- Annualized rent
- Rent-to-income indicator
- Relative affordability tier

The view contains 187 census tracts.

### `vw_dashboard_kpis`

Provides aggregate dashboard metrics such as average rental supply, rent, vacancy, and income.

### `vw_dashboard_kpis_median`

Provides median-based dashboard metrics used where the median is more representative of the cross-tract distribution.

## Example Analytical Queries

### Rental supply distribution

```sql
SELECT
    COUNT(*) AS tracts,
    AVG(units_total) AS mean_units,
    MIN(units_total) AS min_units,
    MAX(units_total) AS max_units
FROM ct_rental_market
WHERE units_total IS NOT NULL;
```

### Rental prices by bedroom type

```sql
SELECT
    AVG(rent_1br) AS avg_1br_rent,
    AVG(rent_2br) AS avg_2br_rent
FROM ct_rental_market
WHERE rent_1br IS NOT NULL
   OR rent_2br IS NOT NULL;
```

### Highest observed vacancy

```sql
SELECT
    ct_id,
    vacancy_total,
    rent_total,
    median_household_income_2020
FROM ct_rental_market
WHERE vacancy_total IS NOT NULL
ORDER BY vacancy_total DESC
LIMIT 10;
```

### Rent-to-income indicator

```sql
SELECT
    ct_id,
    rent_total,
    median_household_income_2020,
    rent_total * 12.0
        / median_household_income_2020 * 100 AS rent_income_pct
FROM ct_rental_market
WHERE rent_total IS NOT NULL
  AND median_household_income_2020 IS NOT NULL;
```

## SQL Design Principles

- Preserve missing values rather than converting them to zero.
- Keep the integrated tract-level table as the analytical source of truth.
- Use views for reusable dashboard calculations.
- Keep transformations transparent and reproducible.
- Report sample sizes for analyses affected by missing CMHC observations.
