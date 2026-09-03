# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from pathlib import Path
from IPython.display import display
import os

print("Current working directory:")
print(os.getcwd())

print("\nFiles/folders here:")
print(os.listdir())

# %%
from pathlib import Path
import shutil

# CMHC files are already in the project
source_dir = Path("/Users/abbas90/winnipeg_rental_market_intelligence/data/raw/cmhc")

# Project location
project_dir = Path("/Users/abbas90/winnipeg_rental_market_intelligence")
cmhc_dir = project_dir / "data" / "raw" / "cmhc"

# Create project folder
cmhc_dir.mkdir(parents=True, exist_ok=True)

# List CMHC files
print("CMHC files:")
for file in sorted(cmhc_dir.iterdir()):
    if file.is_file():
        print(" -", file.name)

# %%
from pathlib import Path
import pandas as pd

cmhc_dir = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/data/raw/cmhc"
)

excel_files = sorted(
    [f for f in cmhc_dir.iterdir()
     if f.suffix.lower() in [".xlsx", ".xls"]]
)

print(f"CMHC files found: {len(excel_files)}\n")

for file in excel_files:
    print("=" * 80)
    print(file.name)

    try:
        xl = pd.ExcelFile(file)
        print("Sheets:", xl.sheet_names)
    except Exception as e:
        print("Could not read workbook:", e)

# %%
import pandas as pd
from pathlib import Path

cmhc_dir = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/data/raw/cmhc"
)

core_files = [
    "urban-rental-market-survey-data-number-units-2023-en.xlsx",
    "urban-rental-market-survey-data-vacancy-rates-2023-en.xlsx",
    "urban-rental-market-survey-data-average-rents-urban-centres-2023-en.xlsx"
]

for filename in core_files:
    filepath = cmhc_dir / filename

    print("\n" + "=" * 100)
    print(filename)
    print("=" * 100)

    for sheet in ["CSD", "Neighbourhood", "CT"]:

        df = pd.read_excel(
            filepath,
            sheet_name=sheet,
            header=None
        )

        print(f"\n--- {sheet} ---")
        print("Shape:", df.shape)

        # Display first 8 rows so we can see the actual structure
        display(df.head(8))

# %%
import pandas as pd
from pathlib import Path

cmhc_dir = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/data/raw/cmhc"
)

units_file = cmhc_dir / "urban-rental-market-survey-data-number-units-2023-en.xlsx"

units_raw = pd.read_excel(
    units_file,
    sheet_name="Neighbourhood",
    header=3
)

# Find Winnipeg observations
winnipeg_units = units_raw[
    units_raw["Centre"].astype(str).str.strip().eq("Winnipeg")
].copy()

print("Winnipeg rows:", len(winnipeg_units))
print()

print("Dwelling types:")
print(winnipeg_units["Dwelling Type"].value_counts(dropna=False))
print()

print("Zones:")
print(winnipeg_units["Zone"].dropna().unique())

# %%
print("Neighbourhood examples:")
display(
    winnipeg_units[
        ["Zone", "Neighbourhood", "Dwelling Type"]
    ].head(40)
)

# %%
print("Rows where Neighbourhood = Total:")
display(
    winnipeg_units[
        winnipeg_units["Neighbourhood"].astype(str).str.strip().eq("Total")
    ].head(30)
)

# %%
winnipeg_neighbourhood = winnipeg_units[
    (winnipeg_units["Centre"].astype(str).str.strip() == "Winnipeg") &
    (winnipeg_units["Zone"].astype(str).str.strip() != "Total") &
    (winnipeg_units["Neighbourhood"].astype(str).str.strip() != "Total")
].copy()

print("Rows remaining:", len(winnipeg_neighbourhood))
print("Unique neighbourhoods:", winnipeg_neighbourhood["Neighbourhood"].nunique())
print("Unique zones:", winnipeg_neighbourhood["Zone"].nunique())
print()

display(
    winnipeg_neighbourhood[
        ["Zone", "Neighbourhood", "Dwelling Type"]
    ].head(20)
)

# %%
winnipeg_apt = winnipeg_neighbourhood[
    winnipeg_neighbourhood["Dwelling Type"].astype(str).str.strip() == "Apt & Other"
].copy()

print("Rows:", len(winnipeg_apt))
print("Unique neighbourhoods:", winnipeg_apt["Neighbourhood"].nunique())
print("Unique zones:", winnipeg_apt["Zone"].nunique())

display(
    winnipeg_apt[
        ["Zone", "Neighbourhood", "Bachelor", "1 Bedroom",
         "2 Bedroom", "3 Bedroom +", "Total"]
    ].head(15)
)

# %%
[name for name in globals() if not name.startswith("_")]

# %%
from pathlib import Path
import pandas as pd

cmhc_dir = Path("/Users/abbas90/winnipeg_rental_market_intelligence/data/raw/cmhc")

vacancy_file = cmhc_dir / "urban-rental-market-survey-data-vacancy-rates-2023-en.xlsx"

print(vacancy_file.exists())

# %%
vacancy_raw = pd.read_excel(
    vacancy_file,
    sheet_name="Neighbourhood",
    header=None
)

print(vacancy_raw.shape)
display(vacancy_raw.head(8))

# %%
vacancy = pd.read_excel(
    vacancy_file,
    sheet_name="Neighbourhood",
    header=3
)

winnipeg_vacancy = vacancy[
    (vacancy["Centre"].astype(str).str.strip() == "Winnipeg") &
    (vacancy["Zone"].astype(str).str.strip() != "Total") &
    (vacancy["Neighbourhood"].astype(str).str.strip() != "Total") &
    (vacancy["Dwelling\nType"].astype(str).str.strip() == "Apt & Other")
].copy()

print("Rows:", len(winnipeg_vacancy))
print("Unique neighbourhoods:", winnipeg_vacancy["Neighbourhood"].nunique())
print("Unique zones:", winnipeg_vacancy["Zone"].nunique())

display(winnipeg_vacancy.head(15))

# %%
rent_file = cmhc_dir / "urban-rental-market-survey-data-average-rents-urban-centres-2023-en.xlsx"

print(rent_file.exists())

# %%
rent = pd.read_excel(
    rent_file,
    sheet_name="Neighbourhood",
    header=3
)

print(rent.shape)
print(rent.columns.tolist())

# %%
winnipeg_rent = rent[
    (rent["Centre"].astype(str).str.strip() == "Winnipeg") &
    (rent["Zone"].astype(str).str.strip() != "Total") &
    (rent["Neighbourhood"].astype(str).str.strip() != "Total") &
    (rent["Dwelling\nType"].astype(str).str.strip() == "Apt & Other")
].copy()

print("Rows:", len(winnipeg_rent))
print("Unique neighbourhoods:", winnipeg_rent["Neighbourhood"].nunique())
print("Unique zones:", winnipeg_rent["Zone"].nunique())

display(winnipeg_rent.head(15))

# %%
print("UNITS")
print(winnipeg_apt.columns.tolist())

print("\nVACANCY")
print(winnipeg_vacancy.columns.tolist())

print("\nRENT")
print(winnipeg_rent.columns.tolist())

# %%
# Standardize column names in the three CMHC datasets

# Units
winnipeg_apt = winnipeg_apt.rename(columns={
    "Dwelling Type": "dwelling_type"
})

# Vacancy
winnipeg_vacancy = winnipeg_vacancy.rename(columns={
    "Dwelling\nType": "dwelling_type",
    "1\nBedroom": "1 Bedroom",
    "2\nBedroom": "2 Bedroom",
    "3 Bedroom\n+": "3 Bedroom +"
})

# Rent
winnipeg_rent = winnipeg_rent.rename(columns={
    "Dwelling\nType": "dwelling_type",
    "1\nBedroom": "1 Bedroom",
    "2\nBedroom": "2 Bedroom",
    "3 Bedroom\n+": "3 Bedroom +"
})

print("Units:")
print(winnipeg_apt.columns.tolist())

print("\nVacancy:")
print(winnipeg_vacancy.columns.tolist())

print("\nRent:")
print(winnipeg_rent.columns.tolist())

# %%
# Standardize UNITS
winnipeg_apt = winnipeg_apt.rename(columns={
    "Province": "province",
    "Centre": "centre",
    "Zone": "zone",
    "Neighbourhood": "neighbourhood",
    "Bachelor": "units_bachelor",
    "1 Bedroom": "units_1br",
    "2 Bedroom": "units_2br",
    "3 Bedroom +": "units_3br_plus",
    "Total": "units_total"
})

# Standardize VACANCY
winnipeg_vacancy = winnipeg_vacancy.rename(columns={
    "Province": "province",
    "Centre": "centre",
    "Zone": "zone",
    "Neighbourhood": "neighbourhood",
    "Bachelor": "vacancy_bachelor",
    "Unnamed: 6": "vacancy_bachelor_reliability",
    "1 Bedroom": "vacancy_1br",
    "Unnamed: 8": "vacancy_1br_reliability",
    "2 Bedroom": "vacancy_2br",
    "Unnamed: 10": "vacancy_2br_reliability",
    "3 Bedroom +": "vacancy_3br_plus",
    "Unnamed: 12": "vacancy_3br_plus_reliability",
    "Total": "vacancy_total",
    "Unnamed: 14": "vacancy_total_reliability"
})

# Standardize RENT
winnipeg_rent = winnipeg_rent.rename(columns={
    "Province": "province",
    "Centre": "centre",
    "Zone": "zone",
    "Neighbourhood": "neighbourhood",
    "Bachelor": "rent_bachelor",
    "Unnamed: 6": "rent_bachelor_reliability",
    "Unnamed: 8": "rent_1br_reliability",
    "1 Bedroom": "rent_1br",
    "Unnamed: 10": "rent_2br_reliability",
    "2 Bedroom": "rent_2br",
    "Unnamed: 12": "rent_3br_plus_reliability",
    "3 Bedroom +": "rent_3br_plus",
    "Unnamed: 14": "rent_total_reliability",
    "Total": "rent_total"
})

# %%
print("UNITS:")
print(winnipeg_apt.columns.tolist())

print("\nVACANCY:")
print(winnipeg_vacancy.columns.tolist())

print("\nRENT:")

print(winnipeg_rent.columns.tolist())

# %%
import numpy as np
import re

def clean_rent(series):
    """
    Convert CMHC rent values such as '$909' to numeric.
    Suppressed/unavailable values such as '**' and '--' become NaN.
    """
    return pd.to_numeric(
        series.astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
        .replace({
            "**": np.nan,
            "--": np.nan,
            "n/a": np.nan,
            "": np.nan,
            "nan": np.nan
        }),
        errors="coerce"
    )


def clean_percent(series):
    """
    Convert CMHC percentage values such as '3.6%' to numeric.
    Result is percentage points: 3.6, not 0.036.
    Suppressed/unavailable values become NaN.
    """
    return pd.to_numeric(
        series.astype(str)
        .str.replace("%", "", regex=False)
        .str.strip()
        .replace({
            "**": np.nan,
            "--": np.nan,
            "n/a": np.nan,
            "": np.nan,
            "nan": np.nan
        }),
        errors="coerce"
    )


def clean_units(series):
    """
    Convert CMHC unit counts to numeric.
    Suppressed/unavailable values become NaN.
    """
    return pd.to_numeric(
        series.astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
        .replace({
            "**": np.nan,
            "--": np.nan,
            "n/a": np.nan,
            "": np.nan,
            "nan": np.nan
        }),
        errors="coerce"
    )


# %%
unit_cols = [
    "units_bachelor",
    "units_1br",
    "units_2br",
    "units_3br_plus",
    "units_total"
]

for col in unit_cols:
    winnipeg_apt[col] = clean_units(winnipeg_apt[col])

# %%
vacancy_cols = [
    "vacancy_bachelor",
    "vacancy_1br",
    "vacancy_2br",
    "vacancy_3br_plus",
    "vacancy_total"
]

for col in vacancy_cols:
    winnipeg_vacancy[col] = clean_percent(winnipeg_vacancy[col])

# %%
rent_cols = [
    "rent_bachelor",
    "rent_1br",
    "rent_2br",
    "rent_3br_plus",
    "rent_total"
]

for col in rent_cols:
    winnipeg_rent[col] = clean_rent(winnipeg_rent[col])

# %%
print("Vacancy missing/suppressed:")
print(winnipeg_vacancy[vacancy_cols].isna().sum())

print("\nRent missing/suppressed:")
print(winnipeg_rent[rent_cols].isna().sum())

print("\nUnits missing/suppressed:")
print(winnipeg_apt[unit_cols].isna().sum())

# %%
display(
    winnipeg_vacancy[
        ["neighbourhood", "vacancy_total", "vacancy_total_reliability"]
    ].head(15)
)

display(
    winnipeg_rent[
        ["neighbourhood", "rent_total", "rent_total_reliability"]
    ].head(15)
)

# %%
unit_names = set(winnipeg_apt["neighbourhood"])
vacancy_names = set(winnipeg_vacancy["neighbourhood"])
rent_names = set(winnipeg_rent["neighbourhood"])

print("Units only:")
print(sorted(unit_names - vacancy_names))
print(sorted(unit_names - rent_names))

print("\nVacancy only:")
print(sorted(vacancy_names - unit_names))
print(sorted(vacancy_names - rent_names))

print("\nRent only:")
print(sorted(rent_names - unit_names))
print(sorted(rent_names - vacancy_names))

# %%
key_cols = ["province", "centre", "zone", "neighbourhood", "dwelling_type"]

print("Units duplicate keys:",
      winnipeg_apt.duplicated(key_cols).sum())

print("Vacancy duplicate keys:",
      winnipeg_vacancy.duplicated(key_cols).sum())

print("Rent duplicate keys:",
      winnipeg_rent.duplicated(key_cols).sum())

# %%
# Columns to retain from each dataset
unit_keep = key_cols + [
    "units_bachelor",
    "units_1br",
    "units_2br",
    "units_3br_plus",
    "units_total"
]

vacancy_keep = key_cols + [
    "vacancy_bachelor",
    "vacancy_bachelor_reliability",
    "vacancy_1br",
    "vacancy_1br_reliability",
    "vacancy_2br",
    "vacancy_2br_reliability",
    "vacancy_3br_plus",
    "vacancy_3br_plus_reliability",
    "vacancy_total",
    "vacancy_total_reliability"
]

rent_keep = key_cols + [
    "rent_bachelor",
    "rent_bachelor_reliability",
    "rent_1br",
    "rent_1br_reliability",
    "rent_2br",
    "rent_2br_reliability",
    "rent_3br_plus",
    "rent_3br_plus_reliability",
    "rent_total",
    "rent_total_reliability"
]

units_master = winnipeg_apt[unit_keep].copy()
vacancy_master = winnipeg_vacancy[vacancy_keep].copy()
rent_master = winnipeg_rent[rent_keep].copy()

cmhc_master = (
    units_master
    .merge(
        vacancy_master,
        on=key_cols,
        how="left",
        validate="one_to_one"
    )
    .merge(
        rent_master,
        on=key_cols,
        how="left",
        validate="one_to_one"
    )
)

print("Master shape:", cmhc_master.shape)
print("Unique neighbourhoods:", cmhc_master["neighbourhood"].nunique())

# %%
display(
    cmhc_master[
        [
            "zone",
            "neighbourhood",
            "units_total",
            "vacancy_total",
            "vacancy_total_reliability",
            "rent_total",
            "rent_total_reliability"
        ]
    ]
)

# %%
print("Rows:", len(cmhc_master))
print("Duplicate keys:", cmhc_master.duplicated(key_cols).sum())
print("Missing total vacancy:", cmhc_master["vacancy_total"].isna().sum())
print("Missing total rent:", cmhc_master["rent_total"].isna().sum())
print("Missing total units:", cmhc_master["units_total"].isna().sum())


# %%
cmhc_raw_master = cmhc_master.copy()

print("CMHC raw master:", cmhc_raw_master.shape)

# %%
cmhc_master["vacancy_total_pct"] = cmhc_master["vacancy_total"]

cmhc_master["vacancy_total_prop"] = (
    cmhc_master["vacancy_total"] / 100
)

# %%
cmhc_master["share_1br"] = (
    cmhc_master["units_1br"] /
    cmhc_master["units_total"]
)

cmhc_master["share_2br"] = (
    cmhc_master["units_2br"] /
    cmhc_master["units_total"]
)

cmhc_master["share_3br_plus"] = (
    cmhc_master["units_3br_plus"] /
    cmhc_master["units_total"]
)

# %%
cmhc_master["calculated_unit_sum"] = (
    cmhc_master["units_bachelor"] +
    cmhc_master["units_1br"] +
    cmhc_master["units_2br"] +
    cmhc_master["units_3br_plus"]
)

cmhc_master["unit_total_difference"] = (
    cmhc_master["units_total"] -
    cmhc_master["calculated_unit_sum"]
)

display(
    cmhc_master[
        [
            "neighbourhood",
            "units_total",
            "calculated_unit_sum",
            "unit_total_difference"
        ]
    ]
)

# %%
# Remove temporary validation/derived columns from the raw analytical copy
cmhc_raw_master = cmhc_raw_master.drop(
    columns=[
        "calculated_unit_sum",
        "unit_total_difference"
    ],
    errors="ignore"
)

print(cmhc_raw_master.shape)

# %%
cmhc_analysis = cmhc_master.copy()

# Keep vacancy in percentage points as the canonical measure.
# Create the proportion only for modelling convenience.
cmhc_analysis["vacancy_total_prop"] = (
    cmhc_analysis["vacancy_total"] / 100
)

print("Analysis dataset:", cmhc_analysis.shape)

# %%
display(
    cmhc_analysis[
        [
            "zone",
            "neighbourhood",
            "units_total",
            "share_1br",
            "share_2br",
            "share_3br_plus",
            "vacancy_total",
            "vacancy_total_prop",
            "rent_total"
        ]
    ]
)

# %%
cmhc_master["share_bachelor"] = (
    cmhc_master["units_bachelor"] /
    cmhc_master["units_total"]
)

cmhc_master["total_bedroom_share"] = (
    cmhc_master["share_bachelor"] +
    cmhc_master["share_1br"] +
    cmhc_master["share_2br"] +
    cmhc_master["share_3br_plus"]
)

cmhc_master["share_sum_difference"] = (
    cmhc_master["total_bedroom_share"] - 1
)

display(
    cmhc_master[
        [
            "neighbourhood",
            "share_bachelor",
            "share_1br",
            "share_2br",
            "share_3br_plus",
            "total_bedroom_share",
            "share_sum_difference"
        ]
    ]
)

# %%
cmhc_master["units_total_thousands"] = (
    cmhc_master["units_total"] / 1000
)

# %%
cmhc_master[
    [
        "units_total",
        "rent_total",
        "vacancy_total",
        "share_bachelor",
        "share_1br",
        "share_2br",
        "share_3br_plus"
    ]
].describe().T

# %%
winnipeg_ct_units = units_raw[
    units_raw["Province"].astype(str).str.strip().eq("Man.") &
    units_raw["Centre"].astype(str).str.strip().eq("Winnipeg")
].copy()

print("Rows:", len(winnipeg_ct_units))
print("Columns:", winnipeg_ct_units.columns.tolist())

display(winnipeg_ct_units.head(15))

# %%
ct_units = pd.read_excel(
    units_file,
    sheet_name="CT",
    header=3
)

print("Shape:", ct_units.shape)
print("Columns:", ct_units.columns.tolist())
display(ct_units.head(10))

# %%

print(ct_units.columns.tolist())

# %%
winnipeg_ct_units = ct_units[
    ct_units["Centre"].astype(str).str.strip() == "Winnipeg"
].copy()

print("Winnipeg CT rows:", len(winnipeg_ct_units))
print(
    "Unique Census Tracts:",
    winnipeg_ct_units["Census\nTract"].nunique()
)

print("\nDwelling types:")
print(winnipeg_ct_units["Dwelling\nType"].value_counts())

display(
    winnipeg_ct_units[
        [
            "Province",
            "Centre",
            "Census\nTract",
            "Dwelling\nType",
            "Bachelor",
            "1\nBedroom",
            "2\nBedroom",
            "3 Bedroom\n+",
            "Total"
        ]
    ].head(15)
)

# %%
winnipeg_ct_apt = winnipeg_ct_units[
    winnipeg_ct_units["Dwelling\nType"].astype(str).str.strip() == "Apt & Other"
].copy()

winnipeg_ct_apt = winnipeg_ct_apt.rename(columns={
    "Province": "province",
    "Centre": "centre",
    "Census\nTract": "census_tract",
    "Dwelling\nType": "dwelling_type",
    "Bachelor": "units_bachelor",
    "1\nBedroom": "units_1br",
    "2\nBedroom": "units_2br",
    "3 Bedroom\n+": "units_3br_plus",
    "Total": "units_total"
})

print("Rows:", len(winnipeg_ct_apt))
print("Unique Census Tracts:", winnipeg_ct_apt["census_tract"].nunique())
print(winnipeg_ct_apt.columns.tolist())

# %%
display(
    winnipeg_ct_apt[
        ["census_tract", "units_bachelor",
         "units_1br", "units_2br",
         "units_3br_plus", "units_total"]
    ].head(20)
)

# %%
print(winnipeg_ct_apt["census_tract"].dtype)
print(winnipeg_ct_apt["census_tract"].tail(10).tolist())

# %%
winnipeg_ct_apt = winnipeg_ct_apt[
    winnipeg_ct_apt["census_tract"].astype(str).str.strip() != "Total"
].copy()

print("Rows:", len(winnipeg_ct_apt))
print("Unique Census Tracts:", winnipeg_ct_apt["census_tract"].nunique())
print("Aggregate rows remaining:",
      (winnipeg_ct_apt["census_tract"] == "Total").sum())

# %%
print(winnipeg_ct_apt["census_tract"].head(10).tolist())
print(winnipeg_ct_apt["census_tract"].tail(10).tolist())

print("\nData type:")
print(winnipeg_ct_apt["census_tract"].dtype)

# %%
ct_unit_cols = [
    "units_bachelor",
    "units_1br",
    "units_2br",
    "units_3br_plus",
    "units_total"
]

for col in ct_unit_cols:
    winnipeg_ct_apt[col] = clean_units(winnipeg_ct_apt[col])

print(
    winnipeg_ct_apt[ct_unit_cols]
    .isna()
    .sum()
)

# %%
missing_ct_units = winnipeg_ct_apt[
    winnipeg_ct_apt["units_total"].isna()
].copy()

print("Census tracts with missing unit data:", len(missing_ct_units))

print(
    missing_ct_units[
        ["census_tract", "dwelling_type"]
    ].to_string(index=False)
)

# %%
print(
    winnipeg_ct_apt[
        ["units_bachelor", "units_1br", "units_2br",
         "units_3br_plus", "units_total"]
    ].describe()
)

# %%
# Basic integrity checks for Winnipeg CT rental supply

print("Rows:", len(winnipeg_ct_apt))
print("Unique CTs:", winnipeg_ct_apt["census_tract"].nunique())

print("\nDwelling types:")
print(winnipeg_ct_apt["dwelling_type"].value_counts())

print("\nMissing total units:", winnipeg_ct_apt["units_total"].isna().sum())

print("\nDuplicate CTs:")
print(winnipeg_ct_apt["census_tract"].duplicated().sum())

print("\nUnit reconciliation:")
ct_sum = (
    winnipeg_ct_apt[
        ["units_bachelor", "units_1br", "units_2br", "units_3br_plus"]
    ]
    .sum(axis=1, min_count=4)
)

print(
    "Rows where bedroom sum != total:",
    (
        ct_sum.notna()
        & (ct_sum != winnipeg_ct_apt["units_total"])
    ).sum()
)

# %%
print(
    winnipeg_ct_apt[
        ["census_tract", "units_total",
         "units_bachelor", "units_1br",
         "units_2br", "units_3br_plus"]
    ]
    .sort_values("units_total", ascending=False)
    .head(15)
    .to_string(index=False)
)

# %%
ct_rental_supply = winnipeg_ct_apt.copy()

# Rental-market supply shares
ct_rental_supply["share_bachelor"] = (
    ct_rental_supply["units_bachelor"]
    / ct_rental_supply["units_total"]
)

ct_rental_supply["share_1br"] = (
    ct_rental_supply["units_1br"]
    / ct_rental_supply["units_total"]
)

ct_rental_supply["share_2br"] = (
    ct_rental_supply["units_2br"]
    / ct_rental_supply["units_total"]
)

ct_rental_supply["share_3br_plus"] = (
    ct_rental_supply["units_3br_plus"]
    / ct_rental_supply["units_total"]
)

# Useful for skewed distributions / modelling
ct_rental_supply["log_units_total"] = np.log1p(
    ct_rental_supply["units_total"]
)

print(ct_rental_supply.shape)
print(
    ct_rental_supply[
        [
            "census_tract",
            "units_total",
            "share_bachelor",
            "share_1br",
            "share_2br",
            "share_3br_plus",
            "log_units_total"
        ]
    ].head()
)

# %%
ct_rental_supply = ct_rental_supply.reset_index(drop=True)

print(ct_rental_supply.shape)
print(ct_rental_supply.head())

# %%
from pathlib import Path

statcan_dir = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/data/raw/statcan"
)

statcan_dir.mkdir(parents=True, exist_ok=True)

print("Created:", statcan_dir)
print("Exists:", statcan_dir.exists())

# %%
import os

print("Current working directory:")
print(os.getcwd())

print("\nFiles/folders here:")
print(os.listdir())

# %%
from pathlib import Path

project_dir = Path("/Users/abbas90/winnipeg_rental_market_intelligence")
statcan_dir = project_dir / "data" / "raw" / "statcan"

print("Project:", project_dir)
print("Project exists:", project_dir.exists())

print("\nStatCan folder:", statcan_dir)
print("StatCan folder exists:", statcan_dir.exists())

print("\nFiles in StatCan folder:")
if statcan_dir.exists():
    files = list(statcan_dir.iterdir())
    if files:
        for f in files:
            print(f.name)
    else:
        print("(empty)")

# %%
from pathlib import Path

search_root = Path("/home/jupyter/R/x86_64-pc-linux-gnu-library")

matches = []

for pattern in ["98100058*", "*0058*"]:
    matches.extend(search_root.rglob(pattern))

matches = sorted(set(matches))

print("Matching files:")
for f in matches:
    print(f)

# %%
import shutil
from pathlib import Path

destination_file = Path(
    "data/raw/statcan/98100058.csv"
)

print("StatCan CSV already exists:")
print(destination_file)
print(
    "Size:",
    f"{destination_file.stat().st_size / 1_000_000:.1f} MB"
)

print("Copied successfully:")
print(destination_file)
print(
    "Size:",
    f"{destination_file.stat().st_size / 1_000_000:.1f} MB"
)

# %%
print("Statistics Canada files:")

for f in statcan_dir.iterdir():
    print(
        f.name,
        f"{f.stat().st_size / 1_000_000:.1f} MB"
    )

# %%
import pandas as pd
from pathlib import Path

statcan_file = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "data/raw/statcan/98100058.csv"
)

income_raw = pd.read_csv(statcan_file)

print("Shape:", income_raw.shape)

print("\nColumns:")
print(income_raw.columns.tolist())

print("\nFirst 5 rows:")
print(income_raw.head().to_string())

# %%
# Find all records whose geography contains Winnipeg
winnipeg_geo = income_raw[
    income_raw["GEO"].str.contains("Winnipeg", case=False, na=False)
].copy()

print("Rows containing Winnipeg:", len(winnipeg_geo))

print("\nUnique Winnipeg-related geographies:")
for geo in winnipeg_geo["GEO"].drop_duplicates():
    print(geo)

# %%
print("Number of unique GEO values:", income_raw["GEO"].nunique())

print("\nFirst 100 GEO values:")
print(
    income_raw["GEO"]
    .drop_duplicates()
    .head(100)
    .to_string(index=False)
)

# %%
winnipeg_income = income_raw[
    income_raw["GEO"].str.contains(
        r"- Winnipeg$",
        case=False,
        na=False
    )
].copy()

print("Rows:", len(winnipeg_income))
print(
    "Unique GEO values:",
    winnipeg_income["GEO"].nunique()
)

print("\nFirst 20:")
print(
    winnipeg_income["GEO"]
    .drop_duplicates()
    .head(20)
    .to_string(index=False)
)

# %%
winnipeg_geo = income_raw[
    income_raw["GEO"].astype(str).str.contains(
        "Winnipeg",
        case=False,
        na=False
    )
].copy()

print("Rows containing Winnipeg:", len(winnipeg_geo))

print("\nFirst 30 Winnipeg-related GEO values:")
print(
    winnipeg_geo["GEO"]
    .drop_duplicates()
    .head(30)
    .to_string(index=False)
)

# %%
geo_series = income_raw["GEO"].astype(str)

print("Examples containing 'Win' anywhere:")
print(
    geo_series[
        geo_series.str.lower().str.find("win") >= 0
    ]
    .drop_duplicates()
    .head(50)
    .to_string(index=False)
)

# %%
print("Examples containing 'Man' anywhere:")
print(
    geo_series[
        geo_series.str.lower().str.find("man") >= 0
    ]
    .drop_duplicates()
    .head(50)
    .to_string(index=False)
)

# %%
print(
    income_raw["GEO"]
    .drop_duplicates()
    .tail(100)
    .to_string(index=False)
)

# %%
print("Unique DGUID values:", income_raw["DGUID"].nunique())

print("\nFirst 50 DGUID values:")
print(
    income_raw["DGUID"]
    .drop_duplicates()
    .head(50)
    .to_string(index=False)
)

# %%
print("Unique Coordinate values:", income_raw["Coordinate"].nunique())

print(
    income_raw[
        ["GEO", "DGUID", "Coordinate"]
    ]
    .drop_duplicates()
    .head(100)
    .to_string(index=False)
)

# %%
cma_rows = income_raw[
    income_raw["DGUID"].astype(str).str.match(
        r"^2021S0503\d+$",
        na=False
    )
].copy()

print("CMA-level rows:", len(cma_rows))

print("\nCMA geographies:")
print(
    cma_rows[
        ["GEO", "DGUID"]
    ]
    .drop_duplicates()
    .to_string(index=False)
)

# %%
# Check what geographic levels are actually represented
geo_counts = income_raw["DGUID"].astype(str).str.extract(
    r"^(2021S050[37])"
)[0].value_counts(dropna=False)

print(geo_counts)

# %%
# Check the range of CT-level geographies by CMA
ct_rows = income_raw[
    income_raw["DGUID"].astype(str).str.startswith("2021S0507")
].copy()

print("CT rows:", len(ct_rows))
print("Unique CT geographies:", ct_rows["GEO"].nunique())
print("Unique CT DGUIDs:", ct_rows["DGUID"].nunique())

print("\nFirst 20 CT geographies:")
print(ct_rows[["GEO", "DGUID"]].drop_duplicates().head(20).to_string(index=False))

# %%
# Extract the CMA name from the CT geography label
ct_geo = (
    ct_rows[["GEO", "DGUID"]]
    .drop_duplicates()
    .copy()
)

ct_geo["cma_name"] = ct_geo["GEO"].str.extract(
    r" - (.+)$"
)[0]

print("Number of CMAs represented:", ct_geo["cma_name"].nunique())

print("\nCMAs represented:")
print(
    sorted(ct_geo["cma_name"].dropna().unique())
)

# %%
from pathlib import Path

# Find all 98100058 files on the filesystem
matches = list(Path("/home/jupyter").rglob("98100058*"))

for p in matches:
    print(p)

# %%
metadata_file = Path(
    "data/raw/statcan/98100058_MetaData.csv"
)

metadata = pd.read_csv(metadata_file)

print("Shape:", metadata.shape)
print("Columns:")
print(metadata.columns.tolist())

print("\nFirst 20 rows:")
print(metadata.head(20).to_string(index=False))

# %%
print(metadata.columns.tolist())

# Show the first few values of the first column
print("\nFirst column values:")
print(metadata.iloc[:15, 0].tolist())

# %%
# Find rows where ANY cell contains "Winnipeg"
mask = metadata.astype(str).apply(
    lambda row: row.str.contains("Winnipeg", case=False, na=False).any(),
    axis=1
)

print("Rows containing Winnipeg:", mask.sum())

# Show only the first 20 matching rows
print(metadata.loc[mask].head(20).to_string(index=False))

# %%
# Search the first column of the metadata file for Winnipeg
first_col = metadata.iloc[:, 0].astype(str)

winnipeg_rows = metadata[
    first_col.str.contains("Winnipeg", case=False, na=False)
]

print("Rows containing Winnipeg:", len(winnipeg_rows))

print(
    winnipeg_rows.head(30).to_string(index=False)
)

# %%
# Geography member rows appear after a "Dimension ID" section.
# Extract rows whose first-column value looks like a geography name.

geo_candidates = metadata[
    metadata.iloc[:, 0].astype(str).str.contains(
        r"\(CMA\)|\bCSD\b| - ",
        regex=True,
        na=False
    )
]

print("Candidate geography rows:", len(geo_candidates))

print(
    geo_candidates.iloc[:, 0]
    .drop_duplicates()
    .head(100)
    .to_string(index=False)
)

# %%
# Search the actual income dataset for Winnipeg
wpg_mask = income_raw.astype(str).apply(
    lambda col: col.str.contains("Winnipeg", case=False, na=False)
).any(axis=1)

print("Rows containing Winnipeg:", wpg_mask.sum())

wpg_income = income_raw.loc[wpg_mask].copy()

print(
    wpg_income[["GEO", "DGUID"]]
    .drop_duplicates()
    .head(20)
    .to_string(index=False)
)

# %%
from pathlib import Path
import pandas as pd

# File locations
project_dir = Path("/Users/abbas90/winnipeg_rental_market_intelligence")
statcan_dir = project_dir / "data" / "raw" / "statcan"

statcan_file = statcan_dir / "98100058.csv"
metadata_file = Path(
    "data/raw/statcan/98100058_MetaData.csv"
)

# Load the metadata
metadata = pd.read_csv(
    metadata_file,
    low_memory=False
)

print("Metadata loaded:", metadata.shape)

# %%
# Find Winnipeg anywhere in the metadata
wpg_meta = metadata[
    metadata.astype(str).apply(
        lambda col: col.str.contains(
            "Winnipeg",
            case=False,
            na=False
        )
    ).any(axis=1)
].copy()

print("Winnipeg metadata rows:", len(wpg_meta))

print(
    wpg_meta.iloc[:20, :6]
    .to_string(index=False)
)

# %%
# Extract Winnipeg geography metadata rows
wpg_meta = metadata[
    metadata.astype(str).apply(
        lambda col: col.str.contains(
            "Winnipeg",
            case=False,
            na=False
        )
    ).any(axis=1)
].copy()

# Display the metadata columns so we can identify the member-ID field
print(wpg_meta.columns.tolist())

print("\nWinnipeg geography rows:")
print(wpg_meta.iloc[:10, :].to_string(index=False))

# %%
# Find the column containing the Winnipeg CT classification/member codes
for col in wpg_meta.columns:
    matches = wpg_meta[col].astype(str).str.contains(
        r"6020001\.00|6020002\.00",
        regex=True,
        na=False
    )
    if matches.any():
        print("Matching column:", col)
        print(wpg_meta.loc[matches, [col]].head(10).to_string(index=False))

# %%
# Extract Winnipeg CT records using the CANSIM Id column
wpg_ct_meta = metadata[
    metadata["CANSIM Id"]
    .astype(str)
    .str.match(r"^\[602\d+\.\d+\]$", na=False)
].copy()

print("Winnipeg CT metadata rows:", len(wpg_ct_meta))

print(
    wpg_ct_meta[["CANSIM Id"]]
    .head(20)
    .to_string(index=False)
)

# %%
# Create clean Winnipeg CT IDs from Statistics Canada metadata
wpg_ct_meta["ct_id"] = (
    wpg_ct_meta["CANSIM Id"]
    .astype(str)
    .str.extract(r"\[602(\d+\.\d+)\]")[0]
)

# Check the StatsCan CT list
print("StatsCan CTs:", wpg_ct_meta["ct_id"].nunique())
print("First 10:", wpg_ct_meta["ct_id"].head(10).tolist())
print("Last 10:", wpg_ct_meta["ct_id"].tail(10).tolist())

# %%
from pathlib import Path
import pandas as pd
import numpy as np

project_dir = Path("/Users/abbas90/winnipeg_rental_market_intelligence")
cmhc_dir = project_dir / "data" / "raw" / "cmhc"

units_file = cmhc_dir / "urban-rental-market-survey-data-number-units-2023-en.xlsx"

# Read the CT sheet
ct_units = pd.read_excel(
    units_file,
    sheet_name="CT",
    header=3
)

# Standardize column names
ct_units.columns = (
    ct_units.columns
    .astype(str)
    .str.replace("\n", "_", regex=False)
    .str.strip()
)

print(ct_units.columns.tolist())

# %%
# Keep Winnipeg apartment & other rental records
winnipeg_ct_supply = ct_units[
    (ct_units["Centre"] == "Winnipeg") &
    (ct_units["Dwelling_Type"] == "Apt & Other") &
    (ct_units["Census_Tract"].astype(str) != "Total")
].copy()

# Standardize CT ID
winnipeg_ct_supply["ct_id"] = (
    winnipeg_ct_supply["Census_Tract"]
    .astype(str)
    .str.strip()
)

print("CMHC Winnipeg CTs:", winnipeg_ct_supply["ct_id"].nunique())
print("Rows:", len(winnipeg_ct_supply))

# %%
statcan_cts = set(wpg_ct_meta["ct_id"].dropna())
cmhc_cts = set(winnipeg_ct_supply["ct_id"].dropna())

print("StatsCan CTs:", len(statcan_cts))
print("CMHC CTs:", len(cmhc_cts))

print("\nStatsCan CTs missing from CMHC:")
print(sorted(statcan_cts - cmhc_cts))

print("\nCMHC CTs missing from StatsCan:")
print(sorted(cmhc_cts - statcan_cts))

print("\nOverlap:", len(statcan_cts & cmhc_cts))

# %%
# Reload the existing StatsCan data after the kernel restart
income_raw = pd.read_csv(
    statcan_file,
    low_memory=False
)

print("Shape:", income_raw.shape)

for col in [
    "Household size (7)",
    "Household type including census family structure  (11)",
    "Household income statistics (6):Median household total income (2020) (2020 constant dollars)[3]"
]:
    print("\n", col)
    print(income_raw[col].drop_duplicates().tolist())

# %%
import requests

url = "https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/98100058/en"

response = requests.get(url, timeout=60)

print("Status:", response.status_code)
print("Content type:", response.headers.get("content-type"))
print("Response length:", len(response.content))
print(response.text[:500])

# %%
import requests
from pathlib import Path
import zipfile

zip_url = "https://www150.statcan.gc.ca/n1/tbl/csv/98100058-eng.zip"

zip_path = statcan_dir / "98100058-eng.zip"

response = requests.get(zip_url, timeout=120)
response.raise_for_status()

zip_path.write_bytes(response.content)

print("Downloaded:", zip_path)
print("Size (MB):", round(zip_path.stat().st_size / 1_000_000, 2))

with zipfile.ZipFile(zip_path) as z:
    print("\nFiles in ZIP:")
    for name in z.namelist():
        print(name)

# %%
import zipfile
from pathlib import Path

statcan_extract_dir = statcan_dir / "98100058_full"

with zipfile.ZipFile(zip_path) as z:
    z.extractall(statcan_extract_dir)

print("Extracted to:", statcan_extract_dir)
print("\nFiles:")
for p in statcan_extract_dir.iterdir():
    print(p.name, round(p.stat().st_size / 1_000_000, 2), "MB")

# %%
full_statcan_file = statcan_extract_dir / "98100058.csv"

income_full = pd.read_csv(
    full_statcan_file,
    low_memory=False
)

print("Full table shape:", income_full.shape)
print("Columns:", income_full.columns.tolist())

print(
    "\nWinnipeg rows:",
    income_full["GEO"]
    .astype(str)
    .str.contains("Winnipeg", case=False, na=False)
    .sum()
)

# %%
# Keep Winnipeg census-tract observations
wpg_income = income_full[
    income_full["GEO"].astype(str).str.contains(
        r" - Winnipeg$",
        regex=True,
        na=False
    )
].copy()

print("Winnipeg CT rows:", len(wpg_income))
print("Unique geographies:", wpg_income["GEO"].nunique())

print(
    wpg_income[["GEO", "DGUID"]]
    .drop_duplicates()
    .head(10)
    .to_string(index=False)
)

# %%
income_col = (
    "Household income statistics (6):"
    "Median household total income (2020) (2020 constant dollars)[3]"
)

wpg_income_core = wpg_income[
    (wpg_income["Household size (7)"] ==
     "Total - Households by household size") &
    (wpg_income["Household type including census family structure  (11)"] ==
     "Total – Household type including census family structure")
].copy()

print("Rows:", len(wpg_income_core))
print("Unique CTs:", wpg_income_core["DGUID"].nunique())

print(
    wpg_income_core[
        ["GEO", "DGUID", income_col]
    ].head(15).to_string(index=False)
)

# %%
# Check whether exactly one income observation exists per CT
ct_counts = wpg_income_core["DGUID"].value_counts()

print("CTs with exactly 1 observation:", (ct_counts == 1).sum())
print("CTs with >1 observation:", (ct_counts > 1).sum())
print("CTs with 0 observations:", 187 - ct_counts.nunique())

print("\nMissing income values:", wpg_income_core[income_col].isna().sum())

# %%
# Create the clean CT-level income table
statcan_income = wpg_income_core[
    ["GEO", "DGUID", income_col]
].copy()

statcan_income = statcan_income.rename(columns={
    "GEO": "geo",
    "DGUID": "statcan_dguid",
    income_col: "median_household_income_2020"
})

# Create the same CT identifier used by CMHC
statcan_income["ct_id"] = (
    statcan_income["geo"]
    .str.extract(r"^(\d+\.\d+)")[0]
)

# Reorder columns
statcan_income = statcan_income[
    ["ct_id", "geo", "statcan_dguid", "median_household_income_2020"]
].sort_values("ct_id").reset_index(drop=True)

print(statcan_income.shape)
print(statcan_income.head(10).to_string(index=False))

# %%
print(
    statcan_income[
        statcan_income["median_household_income_2020"].isna()
    ].to_string(index=False)
)

# %%
processed_dir = project_dir / "data" / "processed" / "statcan"
processed_dir.mkdir(parents=True, exist_ok=True)

income_output = processed_dir / "winnipeg_ct_household_income_2021.csv"

statcan_income.to_csv(income_output, index=False)

print("Saved:", income_output)

# %%
rent_file = (
    cmhc_dir /
    "urban-rental-market-survey-data-average-rents-urban-centres-2023-en.xlsx"
)

ct_rent = pd.read_excel(
    rent_file,
    sheet_name="CT",
    header=3
)

ct_rent.columns = (
    ct_rent.columns
    .astype(str)
    .str.replace("\n", "_", regex=False)
    .str.strip()
)

print(ct_rent.columns.tolist())
print("Shape:", ct_rent.shape)

# %%
# Winnipeg + Apartment & Other + exclude aggregate Total
winnipeg_ct_rent = ct_rent[
    (ct_rent["Centre"] == "Winnipeg") &
    (ct_rent["Dwelling_Type"] == "Apt & Other") &
    (ct_rent["Census_Tract"].astype(str).str.strip() != "Total")
].copy()

winnipeg_ct_rent["ct_id"] = (
    winnipeg_ct_rent["Census_Tract"]
    .astype(str)
    .str.strip()
)

print("Rows:", len(winnipeg_ct_rent))
print("Unique CTs:", winnipeg_ct_rent["ct_id"].nunique())

print(
    winnipeg_ct_rent.head(10).to_string(index=False)
)

# %%
rent_map = {
    "Bachelor": ("rent_bachelor", "rent_bachelor_reliability"),
    "1 Bedroom": ("rent_1br", "rent_1br_reliability"),
    "2 Bedroom": ("rent_2br", "rent_2br_reliability"),
    "3 Bedroom_+": ("rent_3br_plus", "rent_3br_plus_reliability"),
    "Total": ("rent_total", "rent_total_reliability"),
}

rent_clean = winnipeg_ct_rent[
    ["ct_id"] +
    [col for pair in rent_map.values() for col in []]
].copy()

# Start with the CT identifier
rent_clean = winnipeg_ct_rent[["ct_id"]].copy()

for source_col, (value_col, reliability_col) in rent_map.items():
    rent_clean[value_col] = (
        winnipeg_ct_rent[source_col]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .replace({
            "**": np.nan,
            "--": np.nan,
            "nan": np.nan
        })
    )
    
    rent_clean[value_col] = pd.to_numeric(
        rent_clean[value_col],
        errors="coerce"
    )
    
    rent_clean[reliability_col] = (
        winnipeg_ct_rent[
            winnipeg_ct_rent.columns[
                winnipeg_ct_rent.columns.get_loc(source_col) + 1
            ]
        ]
        .astype(str)
        .replace("nan", np.nan)
    )

print(rent_clean.head(10).to_string(index=False))

# %%
for col in [
    "rent_bachelor",
    "rent_1br",
    "rent_2br",
    "rent_3br_plus",
    "rent_total"
]:
    print(
        f"{col}:",
        "usable =", rent_clean[col].notna().sum(),
        "| missing/suppressed =", rent_clean[col].isna().sum()
    )

# %%
print("Reliability codes by variable:")

for col in [
    "rent_bachelor_reliability",
    "rent_1br_reliability",
    "rent_2br_reliability",
    "rent_3br_plus_reliability",
    "rent_total_reliability"
]:
    print(f"\n{col}")
    print(rent_clean[col].value_counts(dropna=False).to_string())

# %%
# Inspect the beginning of the workbook for CMHC notes/definitions
xls = pd.ExcelFile(rent_file)

print(xls.sheet_names)

for sheet_name in xls.sheet_names:
    print("\n---", sheet_name, "---")
    preview = pd.read_excel(
        rent_file,
        sheet_name=sheet_name,
        header=None,
        nrows=12
    )
    print(preview.to_string(index=False, header=False))

# %%
vacancy_file = (
    cmhc_dir /
    "urban-rental-market-survey-data-vacancy-rates-2023-en.xlsx"
)

ct_vacancy = pd.read_excel(
    vacancy_file,
    sheet_name="CT",
    header=3
)

ct_vacancy.columns = (
    ct_vacancy.columns
    .astype(str)
    .str.replace("\n", "_", regex=False)
    .str.strip()
)

print(ct_vacancy.columns.tolist())
print("Shape:", ct_vacancy.shape)

# %%
winnipeg_ct_vacancy = ct_vacancy[
    (ct_vacancy["Centre"] == "Winnipeg") &
    (ct_vacancy["Dwelling_Type"] == "Apt & Other") &
    (ct_vacancy["Census_Tract"].astype(str).str.strip() != "Total")
].copy()

winnipeg_ct_vacancy["ct_id"] = (
    winnipeg_ct_vacancy["Census_Tract"]
    .astype(str)
    .str.strip()
)

print("Rows:", len(winnipeg_ct_vacancy))
print("Unique CTs:", winnipeg_ct_vacancy["ct_id"].nunique())

print(
    winnipeg_ct_vacancy.head(10).to_string(index=False)
)

# %%
import numpy as np
import pandas as pd

vacancy_clean = winnipeg_ct_vacancy.copy()

# Rename columns
vacancy_clean = vacancy_clean.rename(columns={
    "Bachelor": "vacancy_bachelor",
    "Unnamed: 5": "vacancy_bachelor_reliability",
    "1 Bedroom": "vacancy_1br",
    "Unnamed: 7": "vacancy_1br_reliability",
    "2 Bedroom": "vacancy_2br",
    "Unnamed: 9": "vacancy_2br_reliability",
    "3 Bedroom_+": "vacancy_3br_plus",
    "Unnamed: 11": "vacancy_3br_plus_reliability",
    "Total": "vacancy_total",
    "Unnamed: 13": "vacancy_total_reliability"
})

# Convert percentage strings to numeric percentages
vacancy_cols = [
    "vacancy_bachelor",
    "vacancy_1br",
    "vacancy_2br",
    "vacancy_3br_plus",
    "vacancy_total"
]

for col in vacancy_cols:
    vacancy_clean[col] = (
        vacancy_clean[col]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.strip()
        .replace({
            "**": np.nan,
            "--": np.nan,
            "nan": np.nan,
            "": np.nan
        })
    )
    vacancy_clean[col] = pd.to_numeric(
        vacancy_clean[col],
        errors="coerce"
    )

print(vacancy_clean[
    ["ct_id"] + vacancy_cols
].head(10).to_string(index=False))

# %%
print("Vacancy coverage:")
print(
    vacancy_clean[vacancy_cols]
    .notna()
    .sum()
    .to_string()
)

print("\nMissing/suppressed:")
print(
    vacancy_clean[vacancy_cols]
    .isna()
    .sum()
    .to_string()
)

# %%
print("Total vacancy summary:")
print(
    vacancy_clean["vacancy_total"]
    .describe()
    .to_string()
)

print("\nObserved total vacancy values:")
print(
    sorted(vacancy_clean["vacancy_total"].dropna().unique())
)

# %%
print("Total vacancy reliability:")
print(
    vacancy_clean["vacancy_total_reliability"]
    .value_counts(dropna=False)
    .sort_index()
)

# %%
import pandas as pd
import numpy as np
from pathlib import Path

# Project paths
project_root = Path("/Users/abbas90/winnipeg_rental_market_intelligence")
cmhc_dir = project_root / "data" / "raw" / "cmhc"

# Load CMHC CT rental-unit data
units_file = (
    cmhc_dir /
    "urban-rental-market-survey-data-number-units-2023-en.xlsx"
)

ct_units = pd.read_excel(
    units_file,
    sheet_name="CT",
    header=3
)

# Clean column names
ct_units.columns = (
    ct_units.columns
    .astype(str)
    .str.replace("\n", "_", regex=False)
    .str.strip()
)

print(ct_units.columns.tolist())
print("Shape:", ct_units.shape)

# %%
print(ct_units.columns.tolist())

# %%
winnipeg_ct_apt = ct_units[
    (ct_units["Centre"] == "Winnipeg") &
    (ct_units["Dwelling_Type"] == "Apt & Other") &
    (ct_units["Census_Tract"].astype(str).str.strip() != "Total")
].copy()

winnipeg_ct_apt["ct_id"] = (
    winnipeg_ct_apt["Census_Tract"]
    .astype(str)
    .str.strip()
)

# Rename unit columns using the actual workbook names
winnipeg_ct_apt = winnipeg_ct_apt.rename(columns={
    "Bachelor": "units_bachelor",
    "1_Bedroom": "units_1br",
    "2_Bedroom": "units_2br",
    "3 Bedroom_+": "units_3br_plus",
    "Total": "units_total"
})

unit_cols = [
    "units_bachelor",
    "units_1br",
    "units_2br",
    "units_3br_plus",
    "units_total"
]

# Convert to numeric
for col in unit_cols:
    winnipeg_ct_apt[col] = pd.to_numeric(
        winnipeg_ct_apt[col],
        errors="coerce"
    )

print("Rows:", len(winnipeg_ct_apt))
print("Unique CTs:", winnipeg_ct_apt["ct_id"].nunique())
print("Duplicate CTs:", winnipeg_ct_apt["ct_id"].duplicated().sum())

print(
    winnipeg_ct_apt[
        ["ct_id"] + unit_cols
    ].head(10).to_string(index=False)
)

# %%
ct_rental_supply = winnipeg_ct_apt[
    ["ct_id"] + unit_cols
].copy()

ct_rental_supply["share_bachelor"] = (
    ct_rental_supply["units_bachelor"]
    / ct_rental_supply["units_total"]
)

ct_rental_supply["share_1br"] = (
    ct_rental_supply["units_1br"]
    / ct_rental_supply["units_total"]
)

ct_rental_supply["share_2br"] = (
    ct_rental_supply["units_2br"]
    / ct_rental_supply["units_total"]
)

ct_rental_supply["share_3br_plus"] = (
    ct_rental_supply["units_3br_plus"]
    / ct_rental_supply["units_total"]
)

ct_rental_supply["log_units_total"] = np.log1p(
    ct_rental_supply["units_total"]
)

print("Shape:", ct_rental_supply.shape)
print("Unique CTs:", ct_rental_supply["ct_id"].nunique())
print("Duplicate CTs:", ct_rental_supply["ct_id"].duplicated().sum())

print("\nSample:")
print(
    ct_rental_supply.head(10).to_string(index=False)
)

# %%
rent_file = (
    cmhc_dir /
    "urban-rental-market-survey-data-average-rents-urban-centres-2023-en.xlsx"
)

ct_rents = pd.read_excel(
    rent_file,
    sheet_name="CT",
    header=3
)

ct_rents.columns = (
    ct_rents.columns
    .astype(str)
    .str.replace("\n", "_", regex=False)
    .str.strip()
)

print(ct_rents.columns.tolist())
print("Shape:", ct_rents.shape)

# %%
winnipeg_ct_rents = ct_rents[
    (ct_rents["Centre"] == "Winnipeg") &
    (ct_rents["Dwelling_Type"] == "Apt & Other") &
    (ct_rents["Census_Tract"].astype(str).str.strip() != "Total")
].copy()

winnipeg_ct_rents["ct_id"] = (
    winnipeg_ct_rents["Census_Tract"]
    .astype(str)
    .str.strip()
)

winnipeg_ct_rents = winnipeg_ct_rents.rename(columns={
    "Bachelor": "rent_bachelor",
    "Unnamed: 5": "rent_bachelor_reliability",
    "1 Bedroom": "rent_1br",
    "Unnamed: 7": "rent_1br_reliability",
    "2 Bedroom": "rent_2br",
    "Unnamed: 9": "rent_2br_reliability",
    "3 Bedroom_+": "rent_3br_plus",
    "Unnamed: 11": "rent_3br_plus_reliability",
    "Total": "rent_total",
    "Unnamed: 13": "rent_total_reliability"
})

rent_cols = [
    "rent_bachelor",
    "rent_1br",
    "rent_2br",
    "rent_3br_plus",
    "rent_total"
]

for col in rent_cols:
    winnipeg_ct_rents[col] = (
        winnipeg_ct_rents[col]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
        .replace({
            "**": np.nan,
            "--": np.nan,
            "nan": np.nan,
            "": np.nan
        })
    )

    winnipeg_ct_rents[col] = pd.to_numeric(
        winnipeg_ct_rents[col],
        errors="coerce"
    )

rent_clean = winnipeg_ct_rents[
    ["ct_id"] +
    rent_cols +
    [
        "rent_bachelor_reliability",
        "rent_1br_reliability",
        "rent_2br_reliability",
        "rent_3br_plus_reliability",
        "rent_total_reliability"
    ]
].copy()

print("Rows:", len(rent_clean))
print("Unique CTs:", rent_clean["ct_id"].nunique())
print("Duplicate CTs:", rent_clean["ct_id"].duplicated().sum())

print("\nCoverage:")
print(rent_clean[rent_cols].notna().sum().to_string())

# %%
vacancy_file = (
    cmhc_dir /
    "urban-rental-market-survey-data-vacancy-rates-2023-en.xlsx"
)

ct_vacancy = pd.read_excel(
    vacancy_file,
    sheet_name="CT",
    header=3
)

ct_vacancy.columns = (
    ct_vacancy.columns
    .astype(str)
    .str.replace("\n", "_", regex=False)
    .str.strip()
)

print(ct_vacancy.columns.tolist())
print("Shape:", ct_vacancy.shape)

# %%
winnipeg_ct_vacancy = ct_vacancy[
    (ct_vacancy["Centre"] == "Winnipeg") &
    (ct_vacancy["Dwelling_Type"] == "Apt & Other") &
    (ct_vacancy["Census_Tract"].astype(str).str.strip() != "Total")
].copy()

winnipeg_ct_vacancy["ct_id"] = (
    winnipeg_ct_vacancy["Census_Tract"]
    .astype(str)
    .str.strip()
)

winnipeg_ct_vacancy = winnipeg_ct_vacancy.rename(columns={
    "Bachelor": "vacancy_bachelor",
    "Unnamed: 5": "vacancy_bachelor_reliability",
    "1 Bedroom": "vacancy_1br",
    "Unnamed: 7": "vacancy_1br_reliability",
    "2 Bedroom": "vacancy_2br",
    "Unnamed: 9": "vacancy_2br_reliability",
    "3 Bedroom_+": "vacancy_3br_plus",
    "Unnamed: 11": "vacancy_3br_plus_reliability",
    "Total": "vacancy_total",
    "Unnamed: 13": "vacancy_total_reliability"
})

vacancy_cols = [
    "vacancy_bachelor",
    "vacancy_1br",
    "vacancy_2br",
    "vacancy_3br_plus",
    "vacancy_total"
]

for col in vacancy_cols:
    winnipeg_ct_vacancy[col] = (
        winnipeg_ct_vacancy[col]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.strip()
        .replace({
            "**": np.nan,
            "--": np.nan,
            "nan": np.nan,
            "": np.nan
        })
    )

    winnipeg_ct_vacancy[col] = pd.to_numeric(
        winnipeg_ct_vacancy[col],
        errors="coerce"
    )

vacancy_clean = winnipeg_ct_vacancy[
    ["ct_id"] +
    vacancy_cols +
    [
        "vacancy_bachelor_reliability",
        "vacancy_1br_reliability",
        "vacancy_2br_reliability",
        "vacancy_3br_plus_reliability",
        "vacancy_total_reliability"
    ]
].copy()

print("Rows:", len(vacancy_clean))
print("Unique CTs:", vacancy_clean["ct_id"].nunique())
print("Duplicate CTs:", vacancy_clean["ct_id"].duplicated().sum())

print("\nCoverage:")
print(vacancy_clean[vacancy_cols].notna().sum().to_string())

# %%
statcan_dir = (
    project_root /
    "data" /
    "raw" /
    "statcan"
)

income_file = statcan_dir / "98100058_full" / "98100058.csv"

print("File exists:", income_file.exists())
print("File:", income_file)

# %%
income_full = pd.read_csv(
    income_file,
    low_memory=False
)

print("Shape:", income_full.shape)

print("\nColumns:")
print(income_full.columns.tolist())

# %%
wpg_income = income_full[
    income_full["GEO"].astype(str).str.match(
        r"^\d+\.\d+ - Winnipeg$"
    )
].copy()

print("Winnipeg rows:", len(wpg_income))
print("Unique geographies:", wpg_income["GEO"].nunique())

print("\nSample geographies:")
print(
    wpg_income["GEO"]
    .drop_duplicates()
    .head(10)
    .to_string(index=False)
)

# %%
print("Household size values:")
print(
    wpg_income["Household size (7)"]
    .drop_duplicates()
    .tolist()
)

print("\nHousehold type values:")
print(
    wpg_income[
        "Household type including census family structure  (11)"
    ]
    .drop_duplicates()
    .tolist()
)

# %%
income_col = (
    "Household income statistics (6):"
    "Median household total income (2020) "
    "(2020 constant dollars)[3]"
)

household_size_total = "Total - Households by household size"

household_type_total = (
    "Total – Household type including census family structure"
)

wpg_income_core = wpg_income[
    (wpg_income["Household size (7)"] == household_size_total) &
    (
        wpg_income[
            "Household type including census family structure  (11)"
        ]
        == household_type_total
    )
].copy()

print("Rows:", len(wpg_income_core))
print("Unique geographies:", wpg_income_core["GEO"].nunique())

print(
    wpg_income_core[
        ["GEO", income_col]
    ]
    .head(10)
    .to_string(index=False)
)

# %%
statcan_income = wpg_income_core[
    ["GEO", "DGUID", income_col]
].copy()

statcan_income = statcan_income.rename(columns={
    "GEO": "geo",
    "DGUID": "statcan_dguid",
    income_col: "median_household_income_2020"
})

# Extract the CT identifier from "0001.00 - Winnipeg"
statcan_income["ct_id"] = (
    statcan_income["geo"]
    .str.extract(r"^(\d+\.\d+)")
)

statcan_income = statcan_income[
    [
        "ct_id",
        "geo",
        "statcan_dguid",
        "median_household_income_2020"
    ]
].copy()

print("Rows:", len(statcan_income))
print("Unique CTs:", statcan_income["ct_id"].nunique())
print("Duplicate CTs:", statcan_income["ct_id"].duplicated().sum())

print("\nMissing income:")
print(
    statcan_income[
        statcan_income["median_household_income_2020"].isna()
    ][["ct_id", "geo"]]
    .to_string(index=False)
)

# %%
# Recreate the Statistics Canada income layer
income_col = (
    "Household income statistics (6):"
    "Median household total income (2020) "
    "(2020 constant dollars)[3]"
)

household_size_total = "Total - Households by household size"

household_type_total = (
    "Total – Household type including census family structure"
)

wpg_income_core = wpg_income[
    (wpg_income["Household size (7)"] == household_size_total) &
    (
        wpg_income[
            "Household type including census family structure  (11)"
        ]
        == household_type_total
    )
].copy()

statscan_income = wpg_income_core[
    ["GEO", "DGUID", income_col]
].copy()

statscan_income = statscan_income.rename(columns={
    "GEO": "geo",
    "DGUID": "statcan_dguid",
    income_col: "median_household_income_2020"
})

statscan_income["ct_id"] = (
    statscan_income["geo"]
    .str.extract(r"^(\d+\.\d+)")
)

statscan_income = statscan_income[
    [
        "ct_id",
        "geo",
        "statcan_dguid",
        "median_household_income_2020"
    ]
].copy()

# Now merge all four layers
wpg_ct = ct_rental_supply.copy()

wpg_ct = wpg_ct.merge(
    vacancy_clean,
    on="ct_id",
    how="left",
    validate="one_to_one"
)

wpg_ct = wpg_ct.merge(
    rent_clean,
    on="ct_id",
    how="left",
    validate="one_to_one"
)

wpg_ct = wpg_ct.merge(
    statscan_income,
    on="ct_id",
    how="left",
    validate="one_to_one"
)

print("Shape:", wpg_ct.shape)
print("Unique CTs:", wpg_ct["ct_id"].nunique())
print("Duplicate CTs:", wpg_ct["ct_id"].duplicated().sum())

# %%
key_vars = [
    "ct_id",
    "units_total",
    "rent_total",
    "rent_1br",
    "rent_2br",
    "vacancy_total",
    "vacancy_1br",
    "vacancy_2br",
    "median_household_income_2020"
]

print(wpg_ct[key_vars].head(15).to_string(index=False))

print("\nMissing key variables:")
print(
    wpg_ct[key_vars]
    .isna()
    .sum()
    .to_string()
)

# %%
processed_dir = (
    project_root /
    "data" /
    "processed"
)

processed_dir.mkdir(
    parents=True,
    exist_ok=True
)

master_file = (
    processed_dir /
    "winnipeg_ct_rental_market_master_2023.csv"
)

wpg_ct.to_csv(
    master_file,
    index=False
)

print("Saved:", master_file)
print("Rows:", len(wpg_ct))
print("Columns:", len(wpg_ct.columns))
print("File exists:", master_file.exists())

# %%
quality_summary = pd.DataFrame({
    "variable": wpg_ct.columns,
    "non_missing": [
        wpg_ct[col].notna().sum()
        for col in wpg_ct.columns
    ],
    "missing": [
        wpg_ct[col].isna().sum()
        for col in wpg_ct.columns
    ],
    "missing_pct": [
        wpg_ct[col].isna().mean() * 100
        for col in wpg_ct.columns
    ]
})

print(
    quality_summary
    .sort_values("missing_pct", ascending=False)
    .to_string(index=False)
)

# %%
analysis_coverage = pd.DataFrame({
    "analysis": [
        "Income only",
        "Rental supply + income",
        "Total rent + income",
        "1BR rent + income",
        "2BR rent + income",
        "Total vacancy + income",
        "1BR vacancy + income",
        "2BR vacancy + income",
        "Rent + vacancy + income",
        "Supply + rent + vacancy + income"
    ],
    "required_variables": [
        ["median_household_income_2020"],
        ["units_total", "median_household_income_2020"],
        ["rent_total", "median_household_income_2020"],
        ["rent_1br", "median_household_income_2020"],
        ["rent_2br", "median_household_income_2020"],
        ["vacancy_total", "median_household_income_2020"],
        ["vacancy_1br", "median_household_income_2020"],
        ["vacancy_2br", "median_household_income_2020"],
        ["rent_total", "vacancy_total", "median_household_income_2020"],
        ["units_total", "rent_total", "vacancy_total",
         "median_household_income_2020"]
    ]
})

analysis_coverage["n_complete"] = analysis_coverage[
    "required_variables"
].apply(
    lambda cols: wpg_ct[cols].notna().all(axis=1).sum()
)

analysis_coverage["pct_of_187"] = (
    analysis_coverage["n_complete"] / len(wpg_ct) * 100
).round(1)

print(
    analysis_coverage[
        ["analysis", "n_complete", "pct_of_187"]
    ].to_string(index=False)
)

# %%
core_vars = [
    "units_total",
    "rent_total",
    "vacancy_total",
    "median_household_income_2020"
]

core_ct = wpg_ct[
    wpg_ct[core_vars].notna().all(axis=1)
].copy()

print("Core analytical CTs:", len(core_ct))
print("Percentage of Winnipeg CTs:", round(len(core_ct) / 187 * 100, 1))

print("\nCore CTs:")
print(
    core_ct[
        ["ct_id"] + core_vars
    ].head(20).to_string(index=False)
)

# %%
# Track 1: Rental supply + income
supply_df = wpg_ct[
    [
        "ct_id",
        "units_total",
        "units_bachelor",
        "units_1br",
        "units_2br",
        "units_3br_plus",
        "share_bachelor",
        "share_1br",
        "share_2br",
        "share_3br_plus",
        "median_household_income_2020"
    ]
].dropna(
    subset=["units_total", "median_household_income_2020"]
).copy()


# Track 2: Total rent + income
rent_df = wpg_ct[
    [
        "ct_id",
        "units_total",
        "rent_total",
        "rent_1br",
        "rent_2br",
        "median_household_income_2020"
    ]
].dropna(
    subset=["rent_total", "median_household_income_2020"]
).copy()


# Track 3: Vacancy + rent + income
vacancy_df = wpg_ct[
    [
        "ct_id",
        "units_total",
        "rent_total",
        "vacancy_total",
        "median_household_income_2020"
    ]
].dropna(
    subset=[
        "rent_total",
        "vacancy_total",
        "median_household_income_2020"
    ]
).copy()


print("Supply analysis:", len(supply_df), "CTs")
print("Rent analysis:", len(rent_df), "CTs")
print("Vacancy analysis:", len(vacancy_df), "CTs")

# %%
print("=== SUPPLY + INCOME ===")
print(
    supply_df[
        [
            "units_total",
            "share_1br",
            "share_2br",
            "median_household_income_2020"
        ]
    ].describe()
    .round(2)
    .to_string()
)

print("\n=== RENT + INCOME ===")
print(
    rent_df[
        [
            "rent_total",
            "rent_1br",
            "rent_2br",
            "median_household_income_2020"
        ]
    ].describe()
    .round(2)
    .to_string()
)

print("\n=== VACANCY + RENT + INCOME ===")
print(
    vacancy_df[
        [
            "rent_total",
            "vacancy_total",
            "median_household_income_2020"
        ]
    ].describe()
    .round(2)
    .to_string()
)

# %%
from scipy.stats import pearsonr, spearmanr

def correlation_report(df, x, y):
    data = df[[x, y]].dropna()

    pearson_r, pearson_p = pearsonr(data[x], data[y])
    spearman_r, spearman_p = spearmanr(data[x], data[y])

    return {
        "n": len(data),
        "pearson_r": pearson_r,
        "pearson_p": pearson_p,
        "spearman_rho": spearman_r,
        "spearman_p": spearman_p
    }


results = []

# Rent vs income
results.append({
    "relationship": "Total rent vs household income",
    **correlation_report(
        rent_df,
        "rent_total",
        "median_household_income_2020"
    )
})

# Supply vs income
results.append({
    "relationship": "Rental supply vs household income",
    **correlation_report(
        supply_df,
        "units_total",
        "median_household_income_2020"
    )
})

# Vacancy vs rent
results.append({
    "relationship": "Vacancy vs total rent",
    **correlation_report(
        vacancy_df,
        "vacancy_total",
        "rent_total"
    )
})

# Vacancy vs income
results.append({
    "relationship": "Vacancy vs household income",
    **correlation_report(
        vacancy_df,
        "vacancy_total",
        "median_household_income_2020"
    )
})

# Rent vs supply
results.append({
    "relationship": "Total rent vs rental supply",
    **correlation_report(
        vacancy_df,
        "rent_total",
        "units_total"
    )
})

correlation_results = pd.DataFrame(results)

print(
    correlation_results.round(4).to_string(index=False)
)

# %%
print(
    vacancy_df[
        vacancy_df["vacancy_total"] >= 7
    ][
        [
            "ct_id",
            "units_total",
            "rent_total",
            "vacancy_total",
            "median_household_income_2020"
        ]
    ]
    .sort_values("vacancy_total", ascending=False)
    .to_string(index=False)
)

# %%
# Full vacancy sample
vacancy_full = vacancy_df.copy()

# Remove the extreme vacancy observation
vacancy_no_extreme = vacancy_df[
    vacancy_df["vacancy_total"] < 26
].copy()

relationships = [
    ("Vacancy vs rent", "vacancy_total", "rent_total"),
    (
        "Vacancy vs income",
        "vacancy_total",
        "median_household_income_2020"
    )
]

sensitivity_results = []

for label, x, y in relationships:

    # Full sample
    full_data = vacancy_full[[x, y]].dropna()
    r_full, p_full = pearsonr(full_data[x], full_data[y])
    rho_full, sp_full = spearmanr(full_data[x], full_data[y])

    # Without extreme observation
    clean_data = vacancy_no_extreme[[x, y]].dropna()
    r_clean, p_clean = pearsonr(clean_data[x], clean_data[y])
    rho_clean, sp_clean = spearmanr(clean_data[x], clean_data[y])

    sensitivity_results.append({
        "relationship": label,
        "n_full": len(full_data),
        "pearson_full": r_full,
        "spearman_full": rho_full,
        "n_without_26pct": len(clean_data),
        "pearson_without_26pct": r_clean,
        "spearman_without_26pct": rho_clean
    })

sensitivity_results = pd.DataFrame(sensitivity_results)

print(
    sensitivity_results.round(4).to_string(index=False)
)

# %%
print(
    wpg_ct[
        wpg_ct["ct_id"] == "0538.00"
    ][
        [
            "ct_id",
            "units_bachelor",
            "units_1br",
            "units_2br",
            "units_3br_plus",
            "units_total",
            "rent_bachelor",
            "rent_1br",
            "rent_2br",
            "rent_3br_plus",
            "rent_total",
            "vacancy_bachelor",
            "vacancy_1br",
            "vacancy_2br",
            "vacancy_3br_plus",
            "vacancy_total",
            "median_household_income_2020"
        ]
    ].to_string(index=False)
)

# %%
affordability_df = wpg_ct[
    [
        "ct_id",
        "rent_total",
        "rent_1br",
        "rent_2br",
        "median_household_income_2020"
    ]
].copy()

# Annualized average rent as a share of median household income
affordability_df["total_rent_income_ratio"] = (
    affordability_df["rent_total"] * 12
    / affordability_df["median_household_income_2020"]
)

affordability_df["rent_1br_income_ratio"] = (
    affordability_df["rent_1br"] * 12
    / affordability_df["median_household_income_2020"]
)

affordability_df["rent_2br_income_ratio"] = (
    affordability_df["rent_2br"] * 12
    / affordability_df["median_household_income_2020"]
)

# Express as percentages
affordability_df["total_rent_income_pct"] = (
    affordability_df["total_rent_income_ratio"] * 100
)

affordability_df["rent_1br_income_pct"] = (
    affordability_df["rent_1br_income_ratio"] * 100
)

affordability_df["rent_2br_income_pct"] = (
    affordability_df["rent_2br_income_ratio"] * 100
)

print(
    affordability_df[
        [
            "ct_id",
            "rent_total",
            "median_household_income_2020",
            "total_rent_income_pct"
        ]
    ]
    .dropna()
    .head(15)
    .round(2)
    .to_string(index=False)
)

# %%
affordability_summary = affordability_df[
    [
        "total_rent_income_pct",
        "rent_1br_income_pct",
        "rent_2br_income_pct"
    ]
].describe().round(2)

print(
    affordability_summary.to_string()
)

# %%
affordability_ranked = affordability_df[
    [
        "ct_id",
        "rent_total",
        "median_household_income_2020",
        "total_rent_income_pct"
    ]
].dropna().sort_values(
    "total_rent_income_pct"
)

print("Lowest rent-to-income ratios:")
print(
    affordability_ranked.head(10)
    .round(2)
    .to_string(index=False)
)

print("\nHighest rent-to-income ratios:")
print(
    affordability_ranked.tail(10)
    .sort_values(
        "total_rent_income_pct",
        ascending=False
    )
    .round(2)
    .to_string(index=False)
)

# %%
from scipy.stats import pearsonr, spearmanr

affordability_analysis = affordability_df[
    [
        "ct_id",
        "rent_total",
        "median_household_income_2020",
        "total_rent_income_pct"
    ]
].dropna().copy()

pearson_r, pearson_p = pearsonr(
    affordability_analysis["total_rent_income_pct"],
    affordability_analysis["median_household_income_2020"]
)

spearman_rho, spearman_p = spearmanr(
    affordability_analysis["total_rent_income_pct"],
    affordability_analysis["median_household_income_2020"]
)

print("N:", len(affordability_analysis))
print(f"Pearson r:   {pearson_r:.4f}")
print(f"Pearson p:   {pearson_p:.4f}")
print(f"Spearman rho:{spearman_rho:.4f}")
print(f"Spearman p:  {spearman_p:.4f}")

# %%
rent_income_data = rent_df[
    ["rent_total", "median_household_income_2020"]
].dropna()

r_rent_income, p_rent_income = pearsonr(
    rent_income_data["rent_total"],
    rent_income_data["median_household_income_2020"]
)

rho_rent_income, sp_rent_income = spearmanr(
    rent_income_data["rent_total"],
    rent_income_data["median_household_income_2020"]
)

print("Rent vs income")
print(f"N:           {len(rent_income_data)}")
print(f"Pearson r:   {r_rent_income:.4f}")
print(f"Pearson p:   {p_rent_income:.4f}")
print(f"Spearman rho:{rho_rent_income:.4f}")
print(f"Spearman p:  {sp_rent_income:.4f}")

# %%
affordability_ranked = affordability_df[
    [
        "ct_id",
        "rent_total",
        "median_household_income_2020",
        "total_rent_income_pct"
    ]
].dropna().copy()

affordability_ranked = affordability_ranked.sort_values(
    "total_rent_income_pct",
    ascending=False
)

print("Highest rent-to-income indicators:")
display(
    affordability_ranked.head(10).round(2)
)

print("\nLowest rent-to-income indicators:")
display(
    affordability_ranked.tail(10)
    .sort_values("total_rent_income_pct")
    .round(2)
)

# %%
affordability_supply = wpg_ct[
    [
        "ct_id",
        "units_total",
        "share_1br",
        "share_2br",
        "rent_total",
        "median_household_income_2020"
    ]
].merge(
    affordability_df[
        [
            "ct_id",
            "total_rent_income_pct"
        ]
    ],
    on="ct_id",
    how="left",
    validate="one_to_one"
)

affordability_supply = affordability_supply.dropna(
    subset=[
        "units_total",
        "rent_total",
        "median_household_income_2020",
        "total_rent_income_pct"
    ]
).copy()

print("N:", len(affordability_supply))

display(
    affordability_supply[
        [
            "units_total",
            "rent_total",
            "median_household_income_2020",
            "total_rent_income_pct"
        ]
    ].describe().round(2)
)

# %%
from scipy.stats import pearsonr, spearmanr

variables = [
    ("units_total", "total_rent_income_pct"),
    ("units_total", "rent_total"),
    ("units_total", "median_household_income_2020")
]

for x, y in variables:
    temp = affordability_supply[[x, y]].dropna()

    r, p = pearsonr(temp[x], temp[y])
    rho, sp = spearmanr(temp[x], temp[y])

    print(f"\n{x} vs {y}")
    print(f"N:            {len(temp)}")
    print(f"Pearson r:    {r:.4f}")
    print(f"Pearson p:    {p:.4f}")
    print(f"Spearman rho: {rho:.4f}")
    print(f"Spearman p:   {sp:.4f}")

# %%
import statsmodels.api as sm

model_data = affordability_supply[
    [
        "rent_total",
        "units_total",
        "median_household_income_2020"
    ]
].dropna().copy()

X = model_data[
    [
        "units_total",
        "median_household_income_2020"
    ]
]

X = sm.add_constant(X)

y = model_data["rent_total"]

model = sm.OLS(y, X).fit()

print(model.summary())

# %%
import numpy as np

model_data["log_units_total"] = np.log1p(
    model_data["units_total"]
)

X_log = model_data[
    [
        "log_units_total",
        "median_household_income_2020"
    ]
]

X_log = sm.add_constant(X_log)

model_log = sm.OLS(y, X_log).fit()

print(model_log.summary())

# %%
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy.stats import shapiro

# Residuals and fitted values
residuals = model_log.resid
fitted = model_log.fittedvalues

# 1. VIF
X_vif = model_data[
    [
        "log_units_total",
        "median_household_income_2020"
    ]
].copy()

X_vif = sm.add_constant(X_vif)

vif_results = pd.DataFrame({
    "variable": X_vif.columns,
    "VIF": [
        variance_inflation_factor(X_vif.values, i)
        for i in range(X_vif.shape[1])
    ]
})

print("Variance Inflation Factors:")
display(vif_results.round(3))


# 2. Breusch-Pagan test for heteroskedasticity
bp_test = het_breuschpagan(
    residuals,
    model_log.model.exog
)

bp_labels = [
    "LM statistic",
    "LM p-value",
    "F statistic",
    "F p-value"
]

print("\nBreusch-Pagan test:")
for label, value in zip(bp_labels, bp_test):
    print(f"{label}: {value:.4f}")


# 3. Shapiro-Wilk test for residual normality
shapiro_stat, shapiro_p = shapiro(residuals)

print("\nShapiro-Wilk test:")
print(f"Statistic: {shapiro_stat:.4f}")
print(f"p-value:   {shapiro_p:.4f}")

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.scatter(fitted, residuals)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel("Fitted rent")
plt.ylabel("Residual")
plt.title("Residuals vs fitted values")

plt.show()

# %%
import statsmodels.api as sm
import matplotlib.pyplot as plt

sm.qqplot(
    residuals,
    line="45",
    fit=True
)

plt.title("Q-Q plot of regression residuals")
plt.show()

# %%
from statsmodels.stats.outliers_influence import OLSInfluence

influence = OLSInfluence(model_log)

influence_df = model_data[
    [
        "units_total",
        "rent_total",
        "median_household_income_2020",
        "log_units_total"
    ]
].copy()

influence_df["ct_id"] = affordability_supply.loc[
    model_data.index, "ct_id"
].values

influence_df["cooks_distance"] = influence.cooks_distance[0]
influence_df["leverage"] = influence.hat_matrix_diag
influence_df["studentized_residual"] = influence.resid_studentized_external

influence_df = influence_df.sort_values(
    "cooks_distance",
    ascending=False
)

display(
    influence_df.head(10).round(3)
)

# %%
print("Number of observations:", len(influence_df))

print(
    "Cook's distance threshold:",
    round(4 / len(influence_df), 4)
)

print(
    "Observations above threshold:",
    (
        influence_df["cooks_distance"]
        > 4 / len(influence_df)
    ).sum()
)

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

plt.stem(
    range(len(influence_df)),
    influence_df["cooks_distance"]
)

plt.axhline(
    4 / len(influence_df),
    linestyle="--"
)

plt.xlabel("Observation")
plt.ylabel("Cook's distance")
plt.title("Cook's distance for regression observations")

plt.show()

# %%
print(model_data.columns.tolist())
print(model_data.index.name)
print(model_data.index[:5])


# %%
model_data = (
    wpg_ct[
        [
            "ct_id",
            "rent_total",
            "units_total",
            "median_household_income_2020",
            "log_units_total"
        ]
    ]
    .dropna()
    .copy()
)

print(model_data.shape)
print(model_data["ct_id"].head())


# %%
def fit_rental_model(data):
    X = data[
        [
            "log_units_total",
            "median_household_income_2020"
        ]
    ]

    X = sm.add_constant(X)

    y = data["rent_total"]

    return sm.OLS(y, X).fit()


model_full = fit_rental_model(model_data)

model_no_0110 = fit_rental_model(
    model_data[
        model_data["ct_id"] != "0110.06"
    ]
)

model_no_0110_0021 = fit_rental_model(
    model_data[
        ~model_data["ct_id"].isin(
            ["0110.06", "0021.00"]
        )
    ]
)

# %%
comparison = pd.DataFrame({
    "Full sample": [
        model_full.rsquared,
        model_full.rsquared_adj,
        model_full.params["log_units_total"],
        model_full.params["median_household_income_2020"]
    ],

    "Exclude 0110.06": [
        model_no_0110.rsquared,
        model_no_0110.rsquared_adj,
        model_no_0110.params["log_units_total"],
        model_no_0110.params["median_household_income_2020"]
    ],

    "Exclude 0110.06 + 0021.00": [
        model_no_0110_0021.rsquared,
        model_no_0110_0021.rsquared_adj,
        model_no_0110_0021.params["log_units_total"],
        model_no_0110_0021.params["median_household_income_2020"]
    ]
}, index=[
    "R-squared",
    "Adjusted R-squared",
    "Log supply coefficient",
    "Income coefficient"
])

display(comparison.round(4))

# %%
final_results = pd.DataFrame({
    "Coefficient": model_full.params,
    "Std. Error": model_full.bse,
    "t-statistic": model_full.tvalues,
    "p-value": model_full.pvalues,
    "CI Lower": model_full.conf_int()[0],
    "CI Upper": model_full.conf_int()[1]
})

display(final_results.round(4))

# %%
affordability_analysis = (
    wpg_ct[
        [
            "ct_id",
            "rent_total",
            "units_total",
            "median_household_income_2020"
        ]
    ]
    .copy()
)

affordability_analysis["annual_rent"] = (
    affordability_analysis["rent_total"] * 12
)

affordability_analysis["rent_income_pct"] = (
    affordability_analysis["annual_rent"]
    / affordability_analysis["median_household_income_2020"]
    * 100
)

affordability_analysis = affordability_analysis.dropna(
    subset=[
        "rent_total",
        "median_household_income_2020",
        "rent_income_pct"
    ]
)

print("Observations:", len(affordability_analysis))

display(
    affordability_analysis[
        [
            "ct_id",
            "rent_total",
            "median_household_income_2020",
            "rent_income_pct"
        ]
    ].head(10)
)

# %%
q25 = affordability_analysis["rent_income_pct"].quantile(0.25)
q50 = affordability_analysis["rent_income_pct"].quantile(0.50)
q75 = affordability_analysis["rent_income_pct"].quantile(0.75)

def affordability_tier(x):
    if x <= q25:
        return "Lower relative burden"
    elif x <= q50:
        return "Moderate relative burden"
    elif x <= q75:
        return "Higher relative burden"
    else:
        return "Highest relative burden"

affordability_analysis["affordability_tier"] = (
    affordability_analysis["rent_income_pct"]
    .apply(affordability_tier)
)

print("Quartile thresholds:")
print(f"25th percentile: {q25:.2f}%")
print(f"50th percentile: {q50:.2f}%")
print(f"75th percentile: {q75:.2f}%")

print("\nTier counts:")
display(
    affordability_analysis["affordability_tier"]
    .value_counts()
    .sort_index()
)

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.hist(
    affordability_analysis["rent_income_pct"],
    bins=15
)

plt.axvline(q25, linestyle="--", label=f"25th percentile = {q25:.2f}%")
plt.axvline(q50, linestyle="--", label=f"Median = {q50:.2f}%")
plt.axvline(q75, linestyle="--", label=f"75th percentile = {q75:.2f}%")

plt.xlabel("Annualized rent-to-median-household-income (%)")
plt.ylabel("Number of census tracts")
plt.title(
    "Distribution of Winnipeg Rental-Market Affordability Indicator"
)

plt.legend()
plt.tight_layout()
plt.show()

# %%
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=affordability_analysis,
    x="median_household_income_2020",
    y="rent_total",
    hue="affordability_tier",
    s=80
)

sns.regplot(
    data=affordability_analysis,
    x="median_household_income_2020",
    y="rent_total",
    scatter=False,
    ci=95
)

plt.xlabel("Median household income (2020, $)")
plt.ylabel("Average monthly total rent ($)")
plt.title(
    "Winnipeg Rental Costs and Local Household Income"
)

plt.legend(
    title="Relative rent burden",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

plt.tight_layout()
plt.show()

# %%

affordability_analysis[
    [
        "affordability_tier",
        "median_household_income_2020",
        "rent_total",
        "rent_income_pct"
    ]
].groupby("affordability_tier").agg(
    n=("rent_income_pct", "count"),
    median_income=("median_household_income_2020", "median"),
    median_rent=("rent_total", "median"),
    median_ratio=("rent_income_pct", "median")
).round(2)


# %%
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=affordability_analysis,
    x="median_household_income_2020",
    y="rent_total",
    hue="affordability_tier",
    s=90
)

sns.regplot(
    data=affordability_analysis,
    x="median_household_income_2020",
    y="rent_total",
    scatter=False,
    ci=95,
    color="black"
)

plt.xlabel("Median household income (2020, $)")
plt.ylabel("Average monthly total rent ($)")
plt.title("Winnipeg Rental Costs Increase With Local Household Income")

plt.legend(
    title="Relative rent burden",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)
plt.title(
    "Winnipeg Rental Costs and Local Household Income"
)
plt.tight_layout()
plt.show()

# %%
supply_affordability = (
    affordability_analysis[
        [
            "ct_id",
            "rent_total",
            "median_household_income_2020",
            "rent_income_pct"
        ]
    ]
    .merge(
        wpg_ct[
            [
                "ct_id",
                "units_total"
            ]
        ],
        on="ct_id",
        how="left",
        validate="one_to_one"
    )
    .dropna(
        subset=[
            "rent_total",
            "median_household_income_2020",
            "rent_income_pct",
            "units_total"
        ]
    )
)

print("N =", len(supply_affordability))

print(
    supply_affordability[
        [
            "units_total",
            "rent_total",
            "median_household_income_2020",
            "rent_income_pct"
        ]
    ].corr(method="spearman").round(3)
)

# %%
plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=supply_affordability,
    x="units_total",
    y="rent_income_pct",
    s=90
)

sns.regplot(
    data=supply_affordability,
    x="units_total",
    y="rent_income_pct",
    scatter=False,
    ci=95,
    color="black"
)

plt.xlabel("Total rental units in CMHC universe")
plt.ylabel("Annualized rent-to-median-household-income (%)")
plt.title("Rental Supply and Relative Rent Burden Across Winnipeg Census Tracts")

plt.tight_layout()
plt.show()

# %%
import statsmodels.api as sm

model_data = supply_affordability[
    [
        "rent_income_pct",
        "units_total",
        "median_household_income_2020"
    ]
].dropna().copy()

X = model_data[
    [
        "units_total",
        "median_household_income_2020"
    ]
]

X = sm.add_constant(X)

y = model_data["rent_income_pct"]

affordability_model = sm.OLS(y, X).fit()

print(affordability_model.summary())

# %%
from statsmodels.stats.outliers_influence import variance_inflation_factor

X_vif = model_data[
    [
        "units_total",
        "median_household_income_2020"
    ]
].copy()

X_vif = sm.add_constant(X_vif)

vif_results = pd.DataFrame({
    "variable": X_vif.columns,
    "VIF": [
        variance_inflation_factor(X_vif.values, i)
        for i in range(X_vif.shape[1])
    ]
})

print(vif_results)

# %%
from scipy import stats
from statsmodels.stats.diagnostic import het_breuschpagan

# %%
residuals = affordability_model.resid
fitted = affordability_model.fittedvalues

print("Shapiro-Wilk test:")
print(stats.shapiro(residuals))

print("\nBreusch-Pagan test:")

bp_test = het_breuschpagan(
    residuals,
    affordability_model.model.exog
)

bp_labels = [
    "LM Statistic",
    "LM p-value",
    "F Statistic",
    "F p-value"
]

print(dict(zip(bp_labels, bp_test)))

# %%
import numpy as np

influence = affordability_model.get_influence()

cooks_d = influence.cooks_distance[0]
leverage = influence.hat_matrix_diag
studentized_resid = influence.resid_studentized_internal

influence_df = model_data.copy()

influence_df["cooks_distance"] = cooks_d
influence_df["leverage"] = leverage
influence_df["studentized_residual"] = studentized_resid

influence_df = influence_df.sort_values(
    "cooks_distance",
    ascending=False
)

threshold = 4 / len(model_data)

print("Number of observations:", len(model_data))
print("Cook's distance threshold:", round(threshold, 4))
print("\nTop 10 influential observations:")

print(
    influence_df[
        [
            "cooks_distance",
            "leverage",
            "studentized_residual"
        ]
    ].head(10).round(4)
)

print(
    "\nObservations above threshold:",
    (influence_df["cooks_distance"] > threshold).sum()
)

# %%
# Rebuild the model dataset while retaining the census tract ID
model_data = supply_affordability[
    [
        "ct_id",
        "rent_income_pct",
        "units_total",
        "median_household_income_2020"
    ]
].dropna().copy()

# Refit the same model
X = model_data[
    [
        "units_total",
        "median_household_income_2020"
    ]
]

X = sm.add_constant(X)

y = model_data["rent_income_pct"]

affordability_model = sm.OLS(y, X).fit()

# Recalculate influence diagnostics
influence = affordability_model.get_influence()

model_data["cooks_distance"] = influence.cooks_distance[0]
model_data["leverage"] = influence.hat_matrix_diag
model_data["studentized_residual"] = influence.resid_studentized_internal

threshold = 4 / len(model_data)

print(
    model_data[
        model_data["cooks_distance"] > threshold
    ][
        [
            "ct_id",
            "rent_income_pct",
            "units_total",
            "median_household_income_2020",
            "cooks_distance",
            "leverage",
            "studentized_residual"
        ]
    ].sort_values(
        "cooks_distance",
        ascending=False
    ).round(4)
)

# %%
# Identify influential CTs
influential_cts = model_data.loc[
    model_data["cooks_distance"] > threshold,
    "ct_id"
].tolist()

print("Influential CTs:", influential_cts)

# Function to fit the affordability model
def fit_affordability_model(df):
    X = df[
        [
            "units_total",
            "median_household_income_2020"
        ]
    ]
    X = sm.add_constant(X)

    y = df["rent_income_pct"]

    return sm.OLS(y, X).fit()


# Full model
full_model = fit_affordability_model(model_data)

# Exclude all influential observations
sensitivity_data = model_data[
    ~model_data["ct_id"].isin(influential_cts)
].copy()

sensitivity_model = fit_affordability_model(sensitivity_data)

print("\nFULL MODEL")
print("N =", len(model_data))
print("R-squared =", round(full_model.rsquared, 4))
print("Supply coefficient =", round(full_model.params["units_total"], 6))
print("Income coefficient =", round(full_model.params["median_household_income_2020"], 8))

print("\nSENSITIVITY MODEL — excluding influential CTs")
print("N =", len(sensitivity_data))
print("R-squared =", round(sensitivity_model.rsquared, 4))
print("Supply coefficient =", round(sensitivity_model.params["units_total"], 6))
print("Income coefficient =", round(sensitivity_model.params["median_household_income_2020"], 8))

# %%
print(sensitivity_model.summary())

# %%
final_ct = wpg_ct[
    [
        "ct_id",
        "geo",
        "units_total",
        "units_bachelor",
        "units_1br",
        "units_2br",
        "units_3br_plus",
        "share_bachelor",
        "share_1br",
        "share_2br",
        "share_3br_plus",
        "rent_bachelor",
        "rent_1br",
        "rent_2br",
        "rent_3br_plus",
        "rent_total",
        "vacancy_bachelor",
        "vacancy_1br",
        "vacancy_2br",
        "vacancy_3br_plus",
        "vacancy_total",
        "median_household_income_2020"
    ]
].copy()

# Derived affordability indicators
final_ct["annual_rent_total"] = (
    final_ct["rent_total"] * 12
)

final_ct["rent_income_pct"] = (
    final_ct["annual_rent_total"]
    / final_ct["median_household_income_2020"]
    * 100
)

# Relative affordability tiers based on the observed distribution
q25 = final_ct["rent_income_pct"].quantile(0.25)
q50 = final_ct["rent_income_pct"].quantile(0.50)
q75 = final_ct["rent_income_pct"].quantile(0.75)

final_ct["affordability_tier"] = pd.cut(
    final_ct["rent_income_pct"],
    bins=[-np.inf, q25, q50, q75, np.inf],
    labels=[
        "Lower relative burden",
        "Moderate relative burden",
        "Higher relative burden",
        "Highest relative burden"
    ]
)

print("Shape:", final_ct.shape)
print("Unique CTs:", final_ct["ct_id"].nunique())
print("\nColumns:")
print(final_ct.columns.tolist())

# %%
print(final_ct.head())

print("\nMissing values:")
print(
    final_ct.isna()
    .sum()
    .sort_values(ascending=False)
)

print("\nAffordability tiers:")
print(
    final_ct["affordability_tier"]
    .value_counts(dropna=False)
)

# %%
from pathlib import Path

output_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/data/processed/"
    "winnipeg_ct_rental_market_analytical.csv"
)

final_ct.to_csv(output_path, index=False)

print("Saved to:")
print(output_path)

print("\nFile exists:", output_path.exists())
print("Rows:", len(final_ct))
print("Columns:", len(final_ct.columns))

# %%
final_check = pd.read_csv(output_path)

print("Shape:", final_check.shape)
print("Unique CTs:", final_check["ct_id"].nunique())
print("Duplicate CT IDs:", final_check["ct_id"].duplicated().sum())

print("\nAffordability observations:",
      final_check["rent_income_pct"].notna().sum())

print("\nRental supply observations:",
      final_check["units_total"].notna().sum())

print("\nIncome observations:",
      final_check["median_household_income_2020"].notna().sum())

# %%
dashboard_metrics = pd.DataFrame({
    "metric": [
        "Census tracts",
        "Rental supply observations",
        "Rent observations",
        "Vacancy observations",
        "Income observations",
        "Median total rent",
        "Median vacancy rate",
        "Median household income",
        "Median rent-to-income indicator"
    ],
    "value": [
        final_ct["ct_id"].nunique(),
        final_ct["units_total"].notna().sum(),
        final_ct["rent_total"].notna().sum(),
        final_ct["vacancy_total"].notna().sum(),
        final_ct["median_household_income_2020"].notna().sum(),
        final_ct["rent_total"].median(),
        final_ct["vacancy_total"].median(),
        final_ct["median_household_income_2020"].median(),
        final_ct["rent_income_pct"].median()
    ]
})

print(dashboard_metrics)

# %%
supply_ranking = (
    final_ct[
        [
            "ct_id",
            "geo",
            "units_total",
            "share_bachelor",
            "share_1br",
            "share_2br",
            "share_3br_plus"
        ]
    ]
    .dropna(subset=["units_total"])
    .sort_values("units_total", ascending=False)
    .head(15)
    .reset_index(drop=True)
)

print(supply_ranking)

# %%
rent_ranking = (
    final_ct[
        [
            "ct_id",
            "geo",
            "rent_total",
            "rent_1br",
            "rent_2br",
            "median_household_income_2020",
            "rent_income_pct"
        ]
    ]
    .dropna(subset=["rent_total"])
    .sort_values("rent_total", ascending=False)
    .reset_index(drop=True)
)

print("Highest rents:")
print(rent_ranking.head(10))

print("\nLowest rents:")
print(
    rent_ranking
    .sort_values("rent_total")
    .head(10)
)

# %%
affordability_ranking = (
    final_ct[
        [
            "ct_id",
            "geo",
            "rent_total",
            "median_household_income_2020",
            "rent_income_pct",
            "affordability_tier"
        ]
    ]
    .dropna(subset=["rent_income_pct"])
    .sort_values("rent_income_pct", ascending=False)
    .reset_index(drop=True)
)

print("Highest relative burden:")
print(affordability_ranking.head(10))

print("\nLowest relative burden:")
print(
    affordability_ranking
    .sort_values("rent_income_pct")
    .head(10)
)

# %%
import matplotlib.pyplot as plt

supply_plot = (
    final_ct[
        [
            "ct_id",
            "units_total"
        ]
    ]
    .dropna(subset=["units_total"])
    .sort_values("units_total", ascending=False)
    .head(15)
    .sort_values("units_total")
)

plt.figure(figsize=(10, 7))

plt.barh(
    supply_plot["ct_id"],
    supply_plot["units_total"]
)

plt.xlabel("Rental units in CMHC survey universe")
plt.ylabel("Census tract")
plt.title("Rental Supply Concentration Across Winnipeg Census Tracts")

plt.tight_layout()
plt.show()

# %%
rent_values = final_ct["rent_total"].dropna()

plt.figure(figsize=(10, 6))

plt.hist(
    rent_values,
    bins=12
)

plt.axvline(
    rent_values.median(),
    linestyle="--",
    label=f"Median = ${rent_values.median():,.0f}"
)

plt.xlabel("Average monthly total rent ($)")
plt.ylabel("Number of census tracts")
plt.title("Distribution of Average Monthly Rental Costs Across Winnipeg")
plt.legend()

plt.tight_layout()
plt.show()

# %%
tier_summary = (
    affordability_analysis
    .groupby("affordability_tier")
    .agg(
        n=("ct_id", "count"),
        median_income=("median_household_income_2020", "median"),
        median_rent=("rent_total", "median"),
        median_ratio=("rent_income_pct", "median")
    )
    .reset_index()
)

tier_summary

# %%
tier_order = [
    "Lower relative burden",
    "Moderate relative burden",
    "Higher relative burden",
    "Highest relative burden"
]

tier_plot = (
    tier_summary
    .set_index("affordability_tier")
    .reindex(tier_order)
    .reset_index()
)

plt.figure(figsize=(10, 6))

plt.bar(
    tier_plot["affordability_tier"],
    tier_plot["median_ratio"]
)

plt.ylabel("Median annualized rent-to-median-household-income (%)")
plt.xlabel("Relative burden tier")
plt.title("Relative Rental-Market Burden Across Winnipeg Census Tracts")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()

# %%
x = np.arange(len(tier_plot))
width = 0.35

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(
    x - width/2,
    tier_plot["median_income"],
    width,
    label="Median household income"
)

ax1.set_ylabel("Median household income ($)")
ax1.set_xticks(x)
ax1.set_xticklabels(tier_plot["affordability_tier"], rotation=20)

ax2 = ax1.twinx()

ax2.bar(
    x + width/2,
    tier_plot["median_rent"],
    width,
    label="Median monthly rent"
)

ax2.set_ylabel("Median monthly rent ($)")

plt.title("Income and Rent Across Relative Rental-Burden Tiers")

fig.tight_layout()
plt.show()

# %%
vacancy_analysis = (
    final_ct[
        [
            "ct_id",
            "vacancy_total",
            "rent_total",
            "units_total",
            "median_household_income_2020"
        ]
    ]
    .dropna(subset=["vacancy_total"])
    .copy()
)

print("N =", len(vacancy_analysis))

print(
    vacancy_analysis[
        [
            "vacancy_total",
            "rent_total",
            "units_total",
            "median_household_income_2020"
        ]
    ].describe().round(2)
)

# %%
vacancy_analysis[
    [
        "vacancy_total",
        "rent_total",
        "units_total",
        "median_household_income_2020"
    ]
].corr(method="spearman").round(3)

# %%
vacancy_no_extreme = vacancy_analysis[
    vacancy_analysis["vacancy_total"] < 26
].copy()

print("Full sample N =", len(vacancy_analysis))
print("Without 26% vacancy N =", len(vacancy_no_extreme))

print("\nFull sample:")
print(
    vacancy_analysis[
        [
            "vacancy_total",
            "rent_total",
            "median_household_income_2020"
        ]
    ].corr(method="spearman").round(3)
)

print("\nWithout 26% vacancy observation:")
print(
    vacancy_no_extreme[
        [
            "vacancy_total",
            "rent_total",
            "median_household_income_2020"
        ]
    ].corr(method="spearman").round(3)
)

# %%
vacancy_rent_plot = (
    vacancy_analysis[
        [
            "ct_id",
            "vacancy_total",
            "rent_total"
        ]
    ]
    .dropna()
    .copy()
)

plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=vacancy_rent_plot,
    x="rent_total",
    y="vacancy_total",
    s=90
)

sns.regplot(
    data=vacancy_rent_plot,
    x="rent_total",
    y="vacancy_total",
    scatter=False,
    ci=95,
    color="black"
)

plt.xlabel("Average monthly total rent ($)")
plt.ylabel("Total vacancy rate (%)")
plt.title("Rental Costs and Vacancy Across Winnipeg Census Tracts")

plt.tight_layout()
plt.show()

# %%
import sqlite3

print("SQLite version:", sqlite3.sqlite_version)

# %%
import sqlite3
from pathlib import Path

project_root = Path("/Users/abbas90/winnipeg_rental_market_intelligence")

db_path = project_root / "data" / "winnipeg_rental_market.db"

conn = sqlite3.connect(db_path)

print("Database created at:")
print(db_path)

print("\nSQLite version:")
print(sqlite3.sqlite_version)

# %%
import pandas as pd

csv_path = (
    project_root
    / "data"
    / "processed"
    / "winnipeg_ct_rental_market_analytical.csv"
)

df_sql = pd.read_csv(csv_path)

print("Rows:", len(df_sql))
print("Columns:", len(df_sql.columns))

df_sql.head()

# %%
# Replace any existing version of the table
df_sql.to_sql(
    "ct_rental_market",
    conn,
    if_exists="replace",
    index=False
)

print("Table created: ct_rental_market")

# %%
query = """
SELECT
    COUNT(*) AS n_rows,
    COUNT(DISTINCT ct_id) AS unique_cts
FROM ct_rental_market;
"""

pd.read_sql_query(query, conn)

# %%
query = """
SELECT
    ct_id,
    geo,
    units_total,
    units_1br,
    units_2br,
    units_3br_plus
FROM ct_rental_market
WHERE units_total IS NOT NULL
ORDER BY units_total DESC
LIMIT 10;
"""

top_supply_sql = pd.read_sql_query(query, conn)

top_supply_sql

# %%
query = """
SELECT
    ct_id,
    geo,
    rent_total,
    median_household_income_2020,
    rent_income_pct,

    CASE
        WHEN rent_income_pct <= 16.39
            THEN 'Lower relative burden'
        WHEN rent_income_pct <= 19.32
            THEN 'Moderate relative burden'
        WHEN rent_income_pct <= 22.67
            THEN 'Higher relative burden'
        WHEN rent_income_pct > 22.67
            THEN 'Highest relative burden'
        ELSE NULL
    END AS burden_category

FROM ct_rental_market
WHERE rent_income_pct IS NOT NULL
ORDER BY rent_income_pct DESC;
"""

affordability_sql = pd.read_sql_query(query, conn)

affordability_sql.head(10)

# %%
query = """
SELECT
    CASE
        WHEN rent_income_pct <= 16.39
            THEN 'Lower relative burden'
        WHEN rent_income_pct <= 19.32
            THEN 'Moderate relative burden'
        WHEN rent_income_pct <= 22.67
            THEN 'Higher relative burden'
        WHEN rent_income_pct > 22.67
            THEN 'Highest relative burden'
    END AS burden_category,

    COUNT(*) AS census_tracts,
    ROUND(AVG(rent_total), 2) AS avg_monthly_rent,
    ROUND(AVG(median_household_income_2020), 2) AS avg_median_income,
    ROUND(AVG(rent_income_pct), 2) AS avg_rent_income_pct

FROM ct_rental_market
WHERE rent_income_pct IS NOT NULL

GROUP BY burden_category

ORDER BY
    CASE burden_category
        WHEN 'Lower relative burden' THEN 1
        WHEN 'Moderate relative burden' THEN 2
        WHEN 'Higher relative burden' THEN 3
        WHEN 'Highest relative burden' THEN 4
    END;
"""

burden_summary_sql = pd.read_sql_query(query, conn)

burden_summary_sql

# %%
query = """
SELECT
    COUNT(*) AS census_tracts,
    ROUND(AVG(units_total), 2) AS avg_rental_units,
    ROUND(AVG(vacancy_total), 2) AS avg_vacancy_rate,
    ROUND(AVG(rent_total), 2) AS avg_monthly_rent,
    ROUND(AVG(median_household_income_2020), 2) AS avg_median_income
FROM ct_rental_market
WHERE vacancy_total IS NOT NULL;
"""

vacancy_supply_summary = pd.read_sql_query(query, conn)

vacancy_supply_summary

# %%
query = """
DROP VIEW IF EXISTS vw_dashboard;

CREATE VIEW vw_dashboard AS
SELECT
    ct_id,
    geo,

    -- Rental supply
    units_total,
    units_bachelor,
    units_1br,
    units_2br,
    units_3br_plus,
    share_bachelor,
    share_1br,
    share_2br,
    share_3br_plus,

    -- Rental prices
    rent_bachelor,
    rent_1br,
    rent_2br,
    rent_3br_plus,
    rent_total,

    -- Vacancy
    vacancy_bachelor,
    vacancy_1br,
    vacancy_2br,
    vacancy_3br_plus,
    vacancy_total,

    -- Census income
    median_household_income_2020,

    -- Derived affordability measures
    annual_rent_total,
    rent_income_pct,

    CASE
        WHEN rent_income_pct <= 16.39
            THEN 'Lower relative burden'
        WHEN rent_income_pct <= 19.32
            THEN 'Moderate relative burden'
        WHEN rent_income_pct <= 22.67
            THEN 'Higher relative burden'
        WHEN rent_income_pct > 22.67
            THEN 'Highest relative burden'
        ELSE NULL
    END AS affordability_tier

FROM ct_rental_market;
"""

conn.executescript(query)
conn.commit()

print("View created: vw_dashboard")

# %%
query = """
SELECT
    COUNT(*) AS n_rows,
    COUNT(DISTINCT ct_id) AS unique_cts
FROM vw_dashboard;
"""

pd.read_sql_query(query, conn)

# %%
query = """
SELECT
    ct_id,
    units_total,
    rent_total,
    vacancy_total,
    median_household_income_2020,
    rent_income_pct,
    affordability_tier
FROM vw_dashboard
ORDER BY rent_income_pct DESC
LIMIT 10;
"""

pd.read_sql_query(query, conn)

# %%
q25_exact = final_ct["rent_income_pct"].quantile(0.25)
q50_exact = final_ct["rent_income_pct"].quantile(0.50)
q75_exact = final_ct["rent_income_pct"].quantile(0.75)

print(f"Q25 = {q25_exact:.10f}")
print(f"Q50 = {q50_exact:.10f}")
print(f"Q75 = {q75_exact:.10f}")

# %%
query = f"""
DROP VIEW IF EXISTS vw_dashboard;

CREATE VIEW vw_dashboard AS
SELECT
    ct_id,
    geo,

    -- Rental supply
    units_total,
    units_bachelor,
    units_1br,
    units_2br,
    units_3br_plus,
    share_bachelor,
    share_1br,
    share_2br,
    share_3br_plus,

    -- Rental prices
    rent_bachelor,
    rent_1br,
    rent_2br,
    rent_3br_plus,
    rent_total,

    -- Vacancy
    vacancy_bachelor,
    vacancy_1br,
    vacancy_2br,
    vacancy_3br_plus,
    vacancy_total,

    -- Census income
    median_household_income_2020,

    -- Derived affordability measures
    annual_rent_total,
    rent_income_pct,

    CASE
        WHEN rent_income_pct <= {q25_exact}
            THEN 'Lower relative burden'
        WHEN rent_income_pct <= {q50_exact}
            THEN 'Moderate relative burden'
        WHEN rent_income_pct <= {q75_exact}
            THEN 'Higher relative burden'
        WHEN rent_income_pct > {q75_exact}
            THEN 'Highest relative burden'
        ELSE NULL
    END AS affordability_tier

FROM ct_rental_market;
"""

conn.executescript(query)
conn.commit()

print("Dashboard view rebuilt with exact quartile thresholds.")

# %%
query = """
SELECT
    affordability_tier,
    COUNT(*) AS census_tracts,
    ROUND(AVG(rent_total), 2) AS avg_monthly_rent,
    ROUND(AVG(median_household_income_2020), 2) AS avg_median_income,
    ROUND(AVG(rent_income_pct), 2) AS avg_rent_income_pct
FROM vw_dashboard
WHERE rent_income_pct IS NOT NULL
GROUP BY affordability_tier
ORDER BY
    CASE affordability_tier
        WHEN 'Lower relative burden' THEN 1
        WHEN 'Moderate relative burden' THEN 2
        WHEN 'Higher relative burden' THEN 3
        WHEN 'Highest relative burden' THEN 4
    END;
"""

pd.read_sql_query(query, conn)

# %%
query = """
DROP VIEW IF EXISTS vw_dashboard_kpis;

CREATE VIEW vw_dashboard_kpis AS
SELECT
    COUNT(*) AS census_tracts,

    COUNT(units_total) AS rental_supply_observations,

    COUNT(rent_total) AS rent_observations,

    COUNT(vacancy_total) AS vacancy_observations,

    COUNT(median_household_income_2020) AS income_observations,

    ROUND(AVG(rent_total), 2) AS avg_total_rent,

    ROUND(AVG(vacancy_total), 2) AS avg_vacancy_rate,

    ROUND(AVG(median_household_income_2020), 2)
        AS avg_median_household_income,

    ROUND(AVG(rent_income_pct), 2)
        AS avg_rent_income_pct

FROM vw_dashboard;
"""

conn.executescript(query)
conn.commit()

print("KPI view created: vw_dashboard_kpis")

# %%
query = """
SELECT *
FROM vw_dashboard_kpis;
"""

pd.read_sql_query(query, conn)

# %%
query = """
DROP VIEW IF EXISTS vw_dashboard_kpis_median;

CREATE VIEW vw_dashboard_kpis_median AS

WITH
rent_values AS (
    SELECT rent_total
    FROM vw_dashboard
    WHERE rent_total IS NOT NULL
),
vacancy_values AS (
    SELECT vacancy_total
    FROM vw_dashboard
    WHERE vacancy_total IS NOT NULL
),
income_values AS (
    SELECT median_household_income_2020 AS income
    FROM vw_dashboard
    WHERE median_household_income_2020 IS NOT NULL
),
affordability_values AS (
    SELECT rent_income_pct
    FROM vw_dashboard
    WHERE rent_income_pct IS NOT NULL
),

rent_median AS (
    SELECT AVG(rent_total) AS median_rent
    FROM (
        SELECT
            rent_total,
            ROW_NUMBER() OVER (ORDER BY rent_total) AS rn,
            COUNT(*) OVER () AS n
        FROM rent_values
    )
    WHERE rn IN ((n + 1) / 2, (n + 2) / 2)
),

vacancy_median AS (
    SELECT AVG(vacancy_total) AS median_vacancy
    FROM (
        SELECT
            vacancy_total,
            ROW_NUMBER() OVER (ORDER BY vacancy_total) AS rn,
            COUNT(*) OVER () AS n
        FROM vacancy_values
    )
    WHERE rn IN ((n + 1) / 2, (n + 2) / 2)
),

income_median AS (
    SELECT AVG(income) AS median_income
    FROM (
        SELECT
            income,
            ROW_NUMBER() OVER (ORDER BY income) AS rn,
            COUNT(*) OVER () AS n
        FROM income_values
    )
    WHERE rn IN ((n + 1) / 2, (n + 2) / 2)
),

affordability_median AS (
    SELECT AVG(rent_income_pct) AS median_affordability
    FROM (
        SELECT
            rent_income_pct,
            ROW_NUMBER() OVER (ORDER BY rent_income_pct) AS rn,
            COUNT(*) OVER () AS n
        FROM affordability_values
    )
    WHERE rn IN ((n + 1) / 2, (n + 2) / 2)
)

SELECT
    (SELECT COUNT(*) FROM vw_dashboard) AS census_tracts,
    (SELECT COUNT(units_total) FROM vw_dashboard) AS rental_supply_observations,
    (SELECT COUNT(rent_total) FROM vw_dashboard) AS rent_observations,
    (SELECT COUNT(vacancy_total) FROM vw_dashboard) AS vacancy_observations,
    (SELECT COUNT(median_household_income_2020) FROM vw_dashboard) AS income_observations,

    ROUND((SELECT median_rent FROM rent_median), 2)
        AS median_total_rent,

    ROUND((SELECT median_vacancy FROM vacancy_median), 2)
        AS median_vacancy_rate,

    ROUND((SELECT median_income FROM income_median), 2)
        AS median_household_income,

    ROUND((SELECT median_affordability FROM affordability_median), 2)
        AS median_rent_income_pct;
"""

conn.executescript(query)
conn.commit()

print("Median KPI view created.")

# %%
query = """
SELECT *
FROM vw_dashboard_kpis_median;
"""

pd.read_sql_query(query, conn)

# %%
id="sql_median_debug3p"
query = """
SELECT
    median_total_rent,
    median_vacancy_rate,
    median_household_income,
    median_rent_income_pct
FROM vw_dashboard_kpis_median;
"""

median_kpi_check = pd.read_sql_query(query, conn)

print(median_kpi_check.to_string(index=False))
print("\nData types:")
print(median_kpi_check.dtypes)

# %%
dashboard_dir = (
    project_root
    / "data"
    / "processed"
    / "dashboard"
)

dashboard_dir.mkdir(parents=True, exist_ok=True)

# 1. Tract-level dashboard data
pd.read_sql_query(
    """
    SELECT *
    FROM vw_dashboard
    """,
    conn
).to_csv(
    dashboard_dir / "dashboard_tracts.csv",
    index=False
)

# 2. Affordability summary
pd.read_sql_query(
    """
    SELECT
        affordability_tier,
        COUNT(*) AS census_tracts,
        ROUND(AVG(rent_total), 2) AS avg_monthly_rent,
        ROUND(AVG(median_household_income_2020), 2)
            AS avg_median_income,
        ROUND(AVG(rent_income_pct), 2)
            AS avg_rent_income_pct
    FROM vw_dashboard
    WHERE rent_income_pct IS NOT NULL
    GROUP BY affordability_tier
    ORDER BY
        CASE affordability_tier
            WHEN 'Lower relative burden' THEN 1
            WHEN 'Moderate relative burden' THEN 2
            WHEN 'Higher relative burden' THEN 3
            WHEN 'Highest relative burden' THEN 4
        END;
    """,
    conn
).to_csv(
    dashboard_dir / "dashboard_affordability.csv",
    index=False
)

# 3. KPI cards
pd.read_sql_query(
    """
    SELECT *
    FROM vw_dashboard_kpis_median
    """,
    conn
).to_csv(
    dashboard_dir / "dashboard_kpis.csv",
    index=False
)

print("Dashboard exports created:")
print(dashboard_dir)

# %%
for file_name in [
    "dashboard_tracts.csv",
    "dashboard_affordability.csv",
    "dashboard_kpis.csv"
]:
    path = dashboard_dir / file_name
    check = pd.read_csv(path)

    print(
        f"{file_name}: "
        f"{check.shape[0]} rows × {check.shape[1]} columns"
    )

# %%


# %%
# Page 1 — dashboard data preparation

dashboard_tracts = pd.read_csv(
    dashboard_dir / "dashboard_tracts.csv"
)

dashboard_kpis = pd.read_csv(
    dashboard_dir / "dashboard_kpis.csv"
)

dashboard_affordability = pd.read_csv(
    dashboard_dir / "dashboard_affordability.csv"
)

print("Dashboard data loaded successfully.")
print("Tracts:", dashboard_tracts.shape)
print("KPIs:", dashboard_kpis.shape)
print("Affordability:", dashboard_affordability.shape)

# %%
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Prepare data
# -----------------------------

kpi = dashboard_kpis.iloc[0]

top_supply = (
    dashboard_tracts[
        ["ct_id", "units_total"]
    ]
    .dropna(subset=["units_total"])
    .sort_values("units_total", ascending=False)
    .head(15)
    .sort_values("units_total")
)

rent_data = (
    dashboard_tracts["rent_total"]
    .dropna()
)

median_rent = dashboard_tracts["rent_total"].median()


# -----------------------------
# Create dashboard canvas
# -----------------------------

fig = plt.figure(figsize=(16, 9))

fig.suptitle(
    "Winnipeg Rental Market Intelligence",
    fontsize=24,
    fontweight="bold",
    x=0.05,
    y=0.96,
    ha="left"
)

fig.text(
    0.05,
    0.915,
    "Census-tract analysis of rental supply, rents, vacancy and household income",
    fontsize=12,
    ha="left"
)

fig.text(
    0.05,
    0.885,
    "CMHC Rental Market Survey, 2023 + Statistics Canada Census 2021",
    fontsize=9,
    ha="left"
)


# -----------------------------
# KPI cards
# -----------------------------

kpis = [
    ("187", "Census tracts"),
    (f"${kpi['median_total_rent']:,.0f}", "Median monthly total rent"),
    (f"{kpi['median_vacancy_rate']:.1f}%", "Median vacancy rate"),
    (f"${kpi['median_household_income']:,.0f}", "Median household income")
]

card_x = [0.05, 0.285, 0.52, 0.755]

for x, (value, label) in zip(card_x, kpis):

    ax = fig.add_axes([x, 0.75, 0.19, 0.10])
    ax.axis("off")

    ax.text(
        0.02,
        0.65,
        value,
        fontsize=20,
        fontweight="bold"
    )

    ax.text(
        0.02,
        0.20,
        label,
        fontsize=9
    )


# -----------------------------
# Rental supply chart
# -----------------------------

ax1 = fig.add_axes([0.05, 0.37, 0.52, 0.30])

ax1.barh(
    top_supply["ct_id"],
    top_supply["units_total"]
)

ax1.set_title(
    "Rental Supply Is Concentrated Across a Small Number of Census Tracts",
    loc="left",
    fontsize=13,
    fontweight="bold"
)

ax1.set_xlabel("Rental units in CMHC survey universe")
ax1.set_ylabel("Census tract")


# -----------------------------
# Rent distribution
# -----------------------------

ax2 = fig.add_axes([0.63, 0.37, 0.32, 0.30])

ax2.hist(
    rent_data,
    bins=12
)

ax2.axvline(
    median_rent,
    linestyle="--",
    label=f"Median = ${median_rent:,.0f}"
)

ax2.set_title(
    "Monthly Total Rent Distribution",
    loc="left",
    fontsize=13,
    fontweight="bold"
)

ax2.set_xlabel("Average monthly total rent ($)")
ax2.set_ylabel("Census tracts")

ax2.legend()


# -----------------------------
# Key findings
# -----------------------------

fig.text(
    0.05,
    0.28,
    "KEY FINDINGS",
    fontsize=12,
    fontweight="bold"
)

findings = [
    "Higher-income tracts tend to have higher rents "
    "(Spearman ρ = 0.498, n = 77).",

    "Higher-income tracts tend to have lower relative "
    "rent-to-income indicators (Spearman ρ = −0.506, n = 77).",

    "Data coverage varies substantially: income is available "
    "for 185 tracts, rent for 77, and vacancy for 57."
]

y = 0.235

for finding in findings:

    fig.text(
        0.05,
        y,
        "• " + finding,
        fontsize=10,
        wrap=True
    )

    y -= 0.055


# -----------------------------
# Methodology note
# -----------------------------

fig.text(
    0.05,
    0.055,
    "Note: Rent-to-income is an annualized market-rent / median-household-income indicator, "
    "not a household-level affordability measure. Missing CMHC observations are retained as missing.",
    fontsize=8,
    style="italic"
)

plt.show()

# %%
import matplotlib.pyplot as plt

# -----------------------------
# Prepare data
# -----------------------------

kpi = dashboard_kpis.iloc[0]

top_supply = (
    dashboard_tracts[
        ["ct_id", "units_total"]
    ]
    .dropna(subset=["units_total"])
    .sort_values("units_total", ascending=False)
    .head(10)
    .sort_values("units_total")
)

rent_data = dashboard_tracts["rent_total"].dropna()
median_rent = dashboard_tracts["rent_total"].median()


# -----------------------------
# Dashboard canvas
# -----------------------------

fig = plt.figure(figsize=(16, 9))

fig.suptitle(
    "Winnipeg Rental Market Intelligence",
    fontsize=24,
    fontweight="bold",
    x=0.05,
    y=0.96,
    ha="left"
)

fig.text(
    0.05,
    0.915,
    "Census-tract analysis of rental supply, rents, vacancy and household income",
    fontsize=12,
    ha="left"
)

fig.text(
    0.05,
    0.885,
    "CMHC Rental Market Survey (2023) • Statistics Canada Census (2021)",
    fontsize=9,
    ha="left"
)


# -----------------------------
# KPI cards
# -----------------------------

kpis = [
    ("187", "Census tracts"),
    (f"${kpi['median_total_rent']:,.0f}", "Median monthly rent"),
    (f"{kpi['median_vacancy_rate']:.1f}%", "Median vacancy"),
    (f"${kpi['median_household_income']:,.0f}", "Median household income")
]

card_positions = [
    (0.05, 0.755),
    (0.285, 0.755),
    (0.52, 0.755),
    (0.755, 0.755)
]

for (value, label), (x, y) in zip(kpis, card_positions):

    ax = fig.add_axes([x, y, 0.19, 0.085])
    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(True)

    ax.text(
        0.05,
        0.62,
        value,
        fontsize=21,
        fontweight="bold",
        transform=ax.transAxes
    )

    ax.text(
        0.05,
        0.18,
        label,
        fontsize=9,
        transform=ax.transAxes
    )


# -----------------------------
# Rental supply chart
# -----------------------------

ax1 = fig.add_axes([0.05, 0.39, 0.52, 0.29])

ax1.barh(
    top_supply["ct_id"],
    top_supply["units_total"]
)

ax1.set_title(
    "Rental supply is concentrated across a small number of census tracts",
    loc="left",
    fontsize=13,
    fontweight="bold",
    pad=10
)

ax1.set_xlabel("Rental units in CMHC survey universe")
ax1.set_ylabel("Census tract")

ax1.grid(
    axis="x",
    linestyle=":",
    alpha=0.4
)

ax1.set_axisbelow(True)


# -----------------------------
# Rent distribution
# -----------------------------

ax2 = fig.add_axes([0.63, 0.39, 0.32, 0.29])

ax2.hist(
    rent_data,
    bins=12
)

ax2.axvline(
    median_rent,
    linestyle="--",
    linewidth=2,
    label=f"Median = ${median_rent:,.0f}"
)

ax2.set_title(
    "Observed monthly total-rent distribution",
    loc="left",
    fontsize=13,
    fontweight="bold",
    pad=10
)

ax2.set_xlabel("Average monthly total rent ($)")
ax2.set_ylabel("Census tracts")

ax2.grid(
    axis="y",
    linestyle=":",
    alpha=0.4
)

ax2.set_axisbelow(True)
ax2.legend(frameon=False)


# -----------------------------
# Key findings
# -----------------------------

fig.text(
    0.05,
    0.295,
    "KEY FINDINGS",
    fontsize=12,
    fontweight="bold"
)

findings = [
    "Higher-income tracts tend to have higher rents "
    "(Spearman ρ = 0.498; n = 77).",

    "Higher-income tracts tend to have lower relative "
    "rent-to-income indicators (Spearman ρ = −0.506; n = 77).",

    "Coverage varies substantially: income = 185/187 tracts, "
    "rent = 77/187, vacancy = 57/187."
]

y = 0.245

for finding in findings:

    fig.text(
        0.05,
        y,
        "• " + finding,
        fontsize=10
    )

    y -= 0.052


# -----------------------------
# Interpretation panel
# -----------------------------

fig.text(
    0.63,
    0.295,
    "HOW TO READ THIS DASHBOARD",
    fontsize=12,
    fontweight="bold"
)

fig.text(
    0.63,
    0.245,
    "Rental prices should be interpreted alongside local income.\n"
    "The highest rent does not necessarily represent the highest\n"
    "relative rental burden.",
    fontsize=10,
    linespacing=1.5
)


# -----------------------------
# Footer
# -----------------------------

fig.text(
    0.05,
    0.055,
    "Source: CMHC Rental Market Survey, 2023; Statistics Canada Census 2021.",
    fontsize=8
)

fig.text(
    0.05,
    0.032,
    "Note: Rent-to-income is an annualized market-rent / median-household-income indicator, "
    "not a household-level affordability measure. Missing CMHC observations remain missing.",
    fontsize=7.5,
    style="italic"
)

plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Prepare supply data
# -----------------------------

supply_data = (
    dashboard_tracts[
        [
            "ct_id",
            "units_total",
            "units_bachelor",
            "units_1br",
            "units_2br",
            "units_3br_plus",
            "share_bachelor",
            "share_1br",
            "share_2br",
            "share_3br_plus"
        ]
    ]
    .dropna(subset=["units_total"])
    .copy()
)

print("Rental-supply observations:", len(supply_data))
print("Unique census tracts:", supply_data["ct_id"].nunique())

print("\nSupply summary:")
print(
    supply_data[
        [
            "units_total",
            "units_bachelor",
            "units_1br",
            "units_2br",
            "units_3br_plus"
        ]
    ].describe().round(2)
)

# %%
# -----------------------------
# Page 2 — Rental Supply
# -----------------------------

# Top 15 tracts
top15 = (
    supply_data
    .sort_values("units_total", ascending=False)
    .head(15)
    .sort_values("units_total")
)

# Bedroom composition for tracts with complete bedroom data
composition = supply_data.dropna(
    subset=[
        "units_bachelor",
        "units_1br",
        "units_2br",
        "units_3br_plus"
    ]
).copy()

# Overall bedroom totals
bedroom_totals = {
    "Bachelor": composition["units_bachelor"].sum(),
    "1 Bedroom": composition["units_1br"].sum(),
    "2 Bedroom": composition["units_2br"].sum(),
    "3 Bedroom+": composition["units_3br_plus"].sum()
}

# Summary metrics
median_supply = supply_data["units_total"].median()
mean_supply = supply_data["units_total"].mean()
max_supply = supply_data["units_total"].max()


# -----------------------------
# Canvas
# -----------------------------

fig = plt.figure(figsize=(16, 9))

fig.suptitle(
    "Rental Supply & Market Structure",
    fontsize=24,
    fontweight="bold",
    x=0.05,
    y=0.96,
    ha="left"
)

fig.text(
    0.05,
    0.915,
    "Rental inventory and bedroom composition across Winnipeg census tracts",
    fontsize=12,
    ha="left"
)

fig.text(
    0.05,
    0.885,
    "CMHC Rental Market Survey, 2023 • Apt & Other rental segment",
    fontsize=9,
    ha="left"
)


# -----------------------------
# KPI cards
# -----------------------------

kpis = [
    (f"{len(supply_data)}", "Tracts with supply data"),
    (f"{median_supply:,.0f}", "Median rental units"),
    (f"{mean_supply:,.0f}", "Mean rental units"),
    (f"{max_supply:,.0f}", "Largest observed inventory")
]

card_x = [0.05, 0.285, 0.52, 0.755]

for x, (value, label) in zip(card_x, kpis):

    ax = fig.add_axes([x, 0.75, 0.19, 0.10])
    ax.axis("off")

    ax.text(
        0.02,
        0.62,
        value,
        fontsize=21,
        fontweight="bold"
    )

    ax.text(
        0.02,
        0.18,
        label,
        fontsize=9
    )


# -----------------------------
# Top 15 supply
# -----------------------------

ax1 = fig.add_axes([0.05, 0.39, 0.52, 0.29])

ax1.barh(
    top15["ct_id"],
    top15["units_total"]
)

ax1.set_title(
    "Rental inventory is concentrated in a limited number of census tracts",
    loc="left",
    fontsize=13,
    fontweight="bold",
    pad=10
)

ax1.set_xlabel("Rental units in CMHC survey universe")
ax1.set_ylabel("Census tract")

ax1.grid(
    axis="x",
    linestyle=":",
    alpha=0.4
)

ax1.set_axisbelow(True)


# -----------------------------
# Bedroom composition
# -----------------------------

ax2 = fig.add_axes([0.63, 0.39, 0.32, 0.29])

labels = list(bedroom_totals.keys())
values = list(bedroom_totals.values())

ax2.bar(
    labels,
    values
)

ax2.set_title(
    "Observed rental supply by bedroom type",
    loc="left",
    fontsize=13,
    fontweight="bold",
    pad=10
)

ax2.set_ylabel("Rental units")

ax2.grid(
    axis="y",
    linestyle=":",
    alpha=0.4
)

ax2.set_axisbelow(True)

ax2.tick_params(axis="x", rotation=20)


# -----------------------------
# Key findings
# -----------------------------

fig.text(
    0.05,
    0.285,
    "KEY FINDINGS",
    fontsize=12,
    fontweight="bold"
)

largest_ct = top15.iloc[-1]["ct_id"]
largest_units = top15.iloc[-1]["units_total"]

findings = [
    f"The largest observed rental inventory is in CT {largest_ct}, "
    f"with {largest_units:,.0f} units.",

    f"The median census tract contains approximately "
    f"{median_supply:,.0f} rental units in the CMHC survey universe.",

    "Rental supply varies substantially across census tracts, "
    "indicating an uneven spatial distribution of rental inventory."
]

y = 0.235

for finding in findings:

    fig.text(
        0.05,
        y,
        "• " + finding,
        fontsize=10
    )

    y -= 0.055


# -----------------------------
# Interpretation panel
# -----------------------------

fig.text(
    0.63,
    0.285,
    "HOW TO READ THIS PAGE",
    fontsize=12,
    fontweight="bold"
)

fig.text(
    0.63,
    0.235,
    "Rental supply is measured within the CMHC survey universe.\n"
    "It does not represent every rental dwelling in Winnipeg.\n\n"
    "Bedroom composition describes the observed rental inventory,\n"
    "not household demand or housing need.",
    fontsize=10,
    linespacing=1.5
)


# -----------------------------
# Footer
# -----------------------------

fig.text(
    0.05,
    0.055,
    "Source: CMHC Rental Market Survey, 2023.",
    fontsize=8
)

fig.text(
    0.05,
    0.032,
    "Note: Missing CMHC observations remain missing. Supply counts represent the survey universe, not total citywide rental stock.",
    fontsize=7.5,
    style="italic"
)

plt.show()

# %%
# -----------------------------
# Page 2 — Rental Supply
# -----------------------------

top15 = (
    supply_data
    .sort_values("units_total", ascending=False)
    .head(15)
    .sort_values("units_total")
)

composition = supply_data.dropna(
    subset=[
        "units_bachelor",
        "units_1br",
        "units_2br",
        "units_3br_plus"
    ]
).copy()

bedroom_totals = {
    "Bachelor": composition["units_bachelor"].sum(),
    "1 Bedroom": composition["units_1br"].sum(),
    "2 Bedroom": composition["units_2br"].sum(),
    "3 Bedroom+": composition["units_3br_plus"].sum()
}

median_supply = supply_data["units_total"].median()
mean_supply = supply_data["units_total"].mean()
max_supply = supply_data["units_total"].max()

fig = plt.figure(figsize=(16, 9))

fig.suptitle(
    "Rental Supply & Market Structure",
    fontsize=24,
    fontweight="bold",
    x=0.05,
    y=0.96,
    ha="left"
)

fig.text(
    0.05,
    0.915,
    "Rental inventory and bedroom composition across Winnipeg census tracts",
    fontsize=12,
    ha="left"
)

fig.text(
    0.05,
    0.885,
    "CMHC Rental Market Survey, 2023 • Apt & Other rental segment",
    fontsize=9,
    ha="left"
)

# KPI cards
kpis = [
    (f"{len(supply_data)}", "Tracts with supply data"),
    (f"{median_supply:,.0f}", "Median rental units"),
    (f"{mean_supply:,.0f}", "Mean rental units"),
    (f"{max_supply:,.0f}", "Largest observed inventory")
]

card_x = [0.05, 0.285, 0.52, 0.755]

for x, (value, label) in zip(card_x, kpis):
    ax = fig.add_axes([x, 0.75, 0.19, 0.10])
    ax.axis("off")

    ax.text(
        0.02,
        0.62,
        value,
        fontsize=21,
        fontweight="bold"
    )

    ax.text(
        0.02,
        0.18,
        label,
        fontsize=9
    )

# Top 15 supply
ax1 = fig.add_axes([0.05, 0.39, 0.52, 0.29])

ax1.barh(
    top15["ct_id"],
    top15["units_total"]
)

ax1.set_title(
    "Rental inventory is concentrated in a limited number of census tracts",
    loc="left",
    fontsize=13,
    fontweight="bold",
    pad=10
)

ax1.set_xlabel("Rental units in CMHC survey universe")
ax1.set_ylabel("Census tract")

ax1.grid(
    axis="x",
    linestyle=":",
    alpha=0.4
)

ax1.set_axisbelow(True)

# Bedroom composition
ax2 = fig.add_axes([0.63, 0.39, 0.32, 0.29])

labels = list(bedroom_totals.keys())
values = list(bedroom_totals.values())

ax2.bar(
    labels,
    values
)

ax2.set_title(
    "Observed rental supply by bedroom type",
    loc="left",
    fontsize=13,
    fontweight="bold",
    pad=10
)

ax2.set_ylabel("Rental units")

ax2.grid(
    axis="y",
    linestyle=":",
    alpha=0.4
)

ax2.set_axisbelow(True)

ax2.tick_params(axis="x", rotation=20)

# Key findings
fig.text(
    0.05,
    0.285,
    "KEY FINDINGS",
    fontsize=12,
    fontweight="bold"
)

largest_ct = top15.iloc[-1]["ct_id"]
largest_units = top15.iloc[-1]["units_total"]

findings = [
    f"The largest observed rental inventory is in CT {largest_ct}, "
    f"with {largest_units:,.0f} units.",

    f"The median census tract contains approximately "
    f"{median_supply:,.0f} rental units in the CMHC survey universe.",

    "Rental supply varies substantially across census tracts, "
    "indicating an uneven spatial distribution of rental inventory."
]

y = 0.235

for finding in findings:
    fig.text(
        0.05,
        y,
        "• " + finding,
        fontsize=10
    )
    y -= 0.055

# Interpretation
fig.text(
    0.63,
    0.285,
    "HOW TO READ THIS PAGE",
    fontsize=12,
    fontweight="bold"
)

fig.text(
    0.63,
    0.235,
    "Rental supply is measured within the CMHC survey universe.\n"
    "It does not represent every rental dwelling in Winnipeg.\n\n"
    "Bedroom composition describes the observed rental inventory,\n"
    "not household demand or housing need.",
    fontsize=10,
    linespacing=1.5
)

# Footer
fig.text(
    0.05,
    0.055,
    "Source: CMHC Rental Market Survey, 2023.",
    fontsize=8
)

fig.text(
    0.05,
    0.032,
    "Note: Missing CMHC observations remain missing. Supply counts represent the survey universe, not total citywide rental stock.",
    fontsize=7.5,
    style="italic"
)

plt.show()

# %%
bedroom_totals

# %%
bedroom_total = sum(bedroom_totals.values())

bedroom_shares = {
    bedroom: value / bedroom_total * 100
    for bedroom, value in bedroom_totals.items()
}

bedroom_shares

# %%
one_two_share = (
    bedroom_shares["1 Bedroom"]
    + bedroom_shares["2 Bedroom"]
)

one_two_share

# %%
sum(bedroom_shares.values())

# %%
max(bedroom_shares, key=bedroom_shares.get)

# %%
two_to_one_ratio = (
    bedroom_totals["2 Bedroom"]
    / bedroom_totals["1 Bedroom"]
)

two_to_one_ratio

# %%
supply_data[
    [
        "share_bachelor",
        "share_1br",
        "share_2br",
        "share_3br_plus"
    ]
].mean().mul(100).round(2)


# %%
supply_data.loc[
    supply_data["units_total"].idxmax(),
    ["ct_id", "units_total"]
]

# %%
top_15_share = (
    supply_data.nlargest(15, "units_total")["units_total"].sum()
    / supply_data["units_total"].sum()
    * 100
)

top_15_share

# %%
top_5_share = (
    supply_data.nlargest(5, "units_total")["units_total"].sum()
    / supply_data["units_total"].sum()
    * 100
)

top_5_share

# %%
supply_data.nlargest(
    5,
    "units_total"
)[["ct_id", "units_total"]]

# %%
supply_data["units_total"].median()

# %%
supply_data["units_total"].mean() / supply_data["units_total"].median()

# %%
bedroom_mix = {
    "Bachelor": bedroom_shares["Bachelor"],
    "1 Bedroom": bedroom_shares["1 Bedroom"],
    "2 Bedroom": bedroom_shares["2 Bedroom"],
    "3 Bedroom+": bedroom_shares["3 Bedroom+"]
}

plt.figure(figsize=(9, 6))
plt.bar(
    bedroom_mix.keys(),
    bedroom_mix.values()
)

plt.ylabel("Share of observed rental units (%)")
plt.title("Winnipeg Rental Supply by Bedroom Type")
plt.ylim(0, 50)

for i, value in enumerate(bedroom_mix.values()):
    plt.text(
        i,
        value + 1,
        f"{value:.1f}%",
        ha="center"
    )

plt.tight_layout()
plt.show()

# %%
supply_data["units_total"].quantile([0.25, 0.50, 0.75])

# %%
import matplotlib.pyplot as plt
import numpy as np

# Data
top_supply = (
    supply_data
    .nlargest(10, "units_total")
    .sort_values("units_total")
)

bedroom_labels = list(bedroom_shares.keys())
bedroom_values = list(bedroom_shares.values())

# Figure
fig = plt.figure(figsize=(16, 9))
fig.suptitle(
    "Winnipeg Rental Supply & Market Structure",
    fontsize=24,
    fontweight="bold",
    x=0.05,
    y=0.96,
    ha="left"
)

fig.text(
    0.05,
    0.915,
    "Rental inventory and bedroom composition across Winnipeg census tracts",
    fontsize=12,
    ha="left"
)

fig.text(
    0.05,
    0.885,
    "CMHC Rental Market Survey, 2023 | 135 census tracts with usable supply data",
    fontsize=9,
    ha="left"
)

# KPI cards
kpis = [
    ("Median supply / tract", f"{supply_data['units_total'].median():,.0f}"),
    ("Mean supply / tract", f"{supply_data['units_total'].mean():,.1f}"),
    ("Top 15 supply share", f"{top_15_share:.1f}%"),
    ("1–2 bedroom share", f"{one_two_share:.1f}%")
]

card_x = [0.05, 0.285, 0.52, 0.755]

for x, (label, value) in zip(card_x, kpis):
    fig.text(
        x,
        0.79,
        value,
        fontsize=23,
        fontweight="bold",
        ha="left"
    )
    fig.text(
        x,
        0.755,
        label,
        fontsize=10,
        ha="left"
    )

# Chart 1: Top 10 supply
ax1 = fig.add_axes([0.07, 0.16, 0.42, 0.48])

ax1.barh(
    top_supply["ct_id"].astype(str),
    top_supply["units_total"]
)

ax1.set_title(
    "Largest Rental-Supply Census Tracts",
    fontsize=14,
    fontweight="bold",
    loc="left"
)
ax1.set_xlabel("Rental units")
ax1.set_ylabel("Census tract")

# Chart 2: Bedroom mix
ax2 = fig.add_axes([0.57, 0.16, 0.36, 0.48])

bars = ax2.bar(
    bedroom_labels,
    bedroom_values
)

ax2.set_title(
    "Rental Supply by Bedroom Type",
    fontsize=14,
    fontweight="bold",
    loc="left"
)
ax2.set_ylabel("Share of observed units (%)")
ax2.set_ylim(0, 50)

for bar, value in zip(bars, bedroom_values):
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        value + 1,
        f"{value:.1f}%",
        ha="center",
        fontsize=10
    )

# Key findings
fig.text(
    0.05,
    0.075,
    "KEY FINDINGS",
    fontsize=11,
    fontweight="bold"
)

fig.text(
    0.05,
    0.045,
    "• Rental supply is concentrated: the top 15 tracts contain 31.9% of observed units.",
    fontsize=10
)

fig.text(
    0.52,
    0.045,
    "• 1- and 2-bedroom units account for 91.1% of observed rental inventory.",
    fontsize=10
)

plt.show()

# %%
rent_data = (
    dashboard_tracts[
        [
            "ct_id",
            "rent_total",
            "rent_1br",
            "rent_2br",
            "median_household_income_2020",
            "rent_income_pct",
            "affordability_tier"
        ]
    ]
    .copy()
)

print("Total-rent observations:", rent_data["rent_total"].notna().sum())
print("1-bedroom rent observations:", rent_data["rent_1br"].notna().sum())
print("2-bedroom rent observations:", rent_data["rent_2br"].notna().sum())
print("Affordability observations:", rent_data["rent_income_pct"].notna().sum())

print("\nRent summary:")
print(
    rent_data[
        ["rent_total", "rent_1br", "rent_2br"]
    ].describe().round(2)
)

# %%
rent_data["affordability_tier"].value_counts()

# %%
rent_data.groupby(
    "affordability_tier",
    observed=True
)[
    ["rent_total", "median_household_income_2020", "rent_income_pct"]
].mean().round(2)

# %%
tier_order = [
    "Lower relative burden",
    "Moderate relative burden",
    "Higher relative burden",
    "Highest relative burden"
]

tier_rent = (
    rent_data.groupby(
        "affordability_tier",
        observed=True
    )["rent_total"]
    .mean()
    .reindex(tier_order)
)

fig, ax = plt.subplots(figsize=(10, 5.5))

tier_rent.plot(
    kind="bar",
    ax=ax
)

ax.set_title(
    "Average Total Rent by Relative Affordability Tier",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("")
ax.set_ylabel("Average monthly rent ($)")
ax.tick_params(axis="x", rotation=0)

for i, value in enumerate(tier_rent):
    ax.text(
        i,
        value + 20,
        f"${value:,.0f}",
        ha="center",
        fontsize=10
    )

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# %%
fig, ax = plt.subplots(figsize=(9, 6))

ax.scatter(
    rent_data["median_household_income_2020"],
    rent_data["rent_total"],
    alpha=0.7
)

ax.set_title(
    "Total Rent vs. Median Household Income",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("Median household income (2020, $)")
ax.set_ylabel("Average monthly total rent ($)")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# %%
from scipy.stats import spearmanr

corr_data = rent_data.dropna(
    subset=["median_household_income_2020", "rent_total"]
)

rho, p_value = spearmanr(
    corr_data["median_household_income_2020"],
    corr_data["rent_total"]
)

print(f"Observations: {len(corr_data)}")
print(f"Spearman correlation: {rho:.3f}")
print(f"P-value: {p_value:.4g}")

# %%
plot_data = rent_data.dropna(
    subset=["median_household_income_2020", "rent_total"]
)

x = plot_data["median_household_income_2020"]
y = plot_data["rent_total"]

slope, intercept = np.polyfit(x, y, 1)

fig, ax = plt.subplots(figsize=(9, 6))

ax.scatter(
    x,
    y,
    alpha=0.7
)

x_line = np.linspace(x.min(), x.max(), 100)
y_line = intercept + slope * x_line

ax.plot(
    x_line,
    y_line,
    linewidth=2
)

ax.set_title(
    "Total Rent vs. Median Household Income",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("Median household income (2020, $)")
ax.set_ylabel("Average monthly total rent ($)")

ax.text(
    0.05,
    0.95,
    f"Spearman ρ = {rho:.3f}\np < 0.001",
    transform=ax.transAxes,
    verticalalignment="top",
    fontsize=11
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# %%
affordability_data = rent_data.dropna(
    subset=[
        "median_household_income_2020",
        "rent_income_pct"
    ]
)

rho_aff, p_aff = spearmanr(
    affordability_data["median_household_income_2020"],
    affordability_data["rent_income_pct"]
)

print(f"Observations: {len(affordability_data)}")
print(f"Spearman correlation: {rho_aff:.3f}")
print(f"P-value: {p_aff:.4g}")

# %%
fig, ax = plt.subplots(figsize=(9, 6))

ax.scatter(
    affordability_data["median_household_income_2020"],
    affordability_data["rent_income_pct"],
    alpha=0.7
)

x = affordability_data["median_household_income_2020"]
y = affordability_data["rent_income_pct"]

slope_aff, intercept_aff = np.polyfit(x, y, 1)

x_line = np.linspace(x.min(), x.max(), 100)
y_line = intercept_aff + slope_aff * x_line

ax.plot(
    x_line,
    y_line,
    linewidth=2
)

ax.set_title(
    "Relative Rent Burden vs. Median Household Income",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("Median household income (2020, $)")
ax.set_ylabel("Annualized rent-to-income indicator (%)")

ax.text(
    0.05,
    0.95,
    f"Spearman ρ = {rho_aff:.3f}\np < 0.001",
    transform=ax.transAxes,
    verticalalignment="top",
    fontsize=11
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# %%
print(
    f"Median rent-to-income indicator: "
    f"{rent_data['rent_income_pct'].median():.1f}%"
)

# %%
tier_order = [
    "Lower relative burden",
    "Moderate relative burden",
    "Higher relative burden",
    "Highest relative burden"
]

tier_rent = (
    rent_data.groupby(
        "affordability_tier",
        observed=True
    )["rent_total"]
    .mean()
    .reindex(tier_order)
)

fig = plt.figure(figsize=(16, 9))

# -------------------------
# KPI CARDS
# -------------------------

fig.text(
    0.08, 0.91,
    "RENTAL PRICES & AFFORDABILITY",
    fontsize=24,
    fontweight="bold"
)

fig.text(
    0.08, 0.875,
    "Winnipeg census-tract rental-market analysis",
    fontsize=12
)

kpis = [
    ("Median total rent", f"${rent_data['rent_total'].median():,.0f}"),
    ("Median 1-bedroom rent", f"${rent_data['rent_1br'].median():,.0f}"),
    ("Median 2-bedroom rent", f"${rent_data['rent_2br'].median():,.0f}"),
    ("Median rent-to-income", f"{rent_data['rent_income_pct'].median():.1f}%")
]

x_positions = [0.08, 0.30, 0.52, 0.74]

for (label, value), x_pos in zip(kpis, x_positions):
    fig.text(
        x_pos,
        0.81,
        value,
        fontsize=20,
        fontweight="bold"
    )
    fig.text(
        x_pos,
        0.785,
        label,
        fontsize=10
    )

# -------------------------
# CHART 1
# -------------------------

ax1 = fig.add_axes([0.08, 0.40, 0.39, 0.30])

tier_rent.plot(
    kind="bar",
    ax=ax1
)

ax1.set_title(
    "Average Total Rent by Relative Affordability Tier",
    fontsize=14,
    fontweight="bold"
)
ax1.set_xlabel("")
ax1.set_ylabel("Average monthly rent ($)")
ax1.tick_params(axis="x", rotation=0)

for i, value in enumerate(tier_rent):
    ax1.text(
        i,
        value + 20,
        f"${value:,.0f}",
        ha="center",
        fontsize=9
    )

ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# -------------------------
# CHART 2
# -------------------------

ax2 = fig.add_axes([0.55, 0.40, 0.39, 0.30])

x = affordability_data["median_household_income_2020"]
y = affordability_data["rent_income_pct"]

ax2.scatter(
    x,
    y,
    alpha=0.7
)

slope_aff, intercept_aff = np.polyfit(x, y, 1)

x_line = np.linspace(x.min(), x.max(), 100)
y_line = intercept_aff + slope_aff * x_line

ax2.plot(
    x_line,
    y_line,
    linewidth=2
)

ax2.set_title(
   "Rent-to-Income Indicator vs. Median Household Income",
    fontsize=14,
    fontweight="bold"
)
ax2.set_xlabel("Median household income (2020, $)")
ax2.set_ylabel("Annualized rent-to-income indicator (%)")

ax2.text(
    0.05,
    0.95,
    f"Spearman ρ = {rho_aff:.3f}\np < 0.001",
    transform=ax2.transAxes,
    verticalalignment="top",
    fontsize=10
)

ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# -------------------------
# INSIGHT PANEL
# -------------------------

fig.text(
    0.08,
    0.31,
    "KEY INSIGHT",
    fontsize=12,
    fontweight="bold"
)

fig.text(
    0.08,
    0.265,
    "Higher-income tracts tend to have higher rents,",
    fontsize=13
)

fig.text(
    0.08,
    0.235,
    "but rental costs represent a smaller share of median household income.",
    fontsize=13
)

fig.text(
    0.08,
    0.19,
    "Income vs. rent: Spearman ρ = 0.498 (n = 77)",
    fontsize=10
)

fig.text(
    0.08,
    0.165,
    "Income vs. rent-to-income indicator: Spearman ρ = −0.506 (n = 77)",
    fontsize=10
)

# -------------------------
# METHODOLOGY NOTE
# -------------------------

fig.text(
    0.08,
    0.08,
    "Methodology: Affordability is an annualized market-rent / median-household-income indicator",
    fontsize=9
)

fig.text(
    0.08,
    0.055,
    "at the census-tract level; it is not a household-level rent-burden measure. Missing CMHC observations remain missing.",
    fontsize=9
)

plt.show()

# %%
from scipy.stats import spearmanr

corr_data = rent_data.dropna(
    subset=["median_household_income_2020", "rent_total"]
)

rho, p_value = spearmanr(
    corr_data["median_household_income_2020"],
    corr_data["rent_total"]
)

print(f"Observations: {len(corr_data)}")
print(f"Spearman correlation: {rho:.3f}")
print(f"P-value: {p_value:.4g}")

# %%
vacancy_data = (
    dashboard_tracts[
        [
            "ct_id",
            "vacancy_total",
            "vacancy_1br",
            "vacancy_2br",
            "rent_total",
            "units_total",
            "median_household_income_2020"
        ]
    ]
    .copy()
)

print("Total vacancy observations:", vacancy_data["vacancy_total"].notna().sum())
print("1-bedroom vacancy observations:", vacancy_data["vacancy_1br"].notna().sum())
print("2-bedroom vacancy observations:", vacancy_data["vacancy_2br"].notna().sum())

print("\nVacancy summary:")
print(
    vacancy_data[
        ["vacancy_total", "vacancy_1br", "vacancy_2br"]
    ].describe().round(2)
)

# %%
top_vacancy = (
    vacancy_data
    .dropna(subset=["vacancy_total"])
    .sort_values("vacancy_total", ascending=False)
    [
        [
            "ct_id",
            "vacancy_total",
            "rent_total",
            "units_total",
            "median_household_income_2020"
        ]
    ]
    .head(10)
)

print(top_vacancy.to_string(index=False))

# %%
from scipy.stats import spearmanr

vac_rent = vacancy_data.dropna(
    subset=["vacancy_total", "rent_total"]
)

rho_vr, p_vr = spearmanr(
    vac_rent["rent_total"],
    vac_rent["vacancy_total"]
)

print(f"Observations: {len(vac_rent)}")
print(f"Spearman correlation: {rho_vr:.3f}")
print(f"P-value: {p_vr:.4g}")

# %%
vac_rent_sensitivity = vac_rent[
    vac_rent["ct_id"] != "0538.00"
].copy()

rho_vr_sens, p_vr_sens = spearmanr(
    vac_rent_sensitivity["rent_total"],
    vac_rent_sensitivity["vacancy_total"]
)

print(f"Observations: {len(vac_rent_sensitivity)}")
print(f"Spearman correlation: {rho_vr_sens:.3f}")
print(f"P-value: {p_vr_sens:.4g}")

# %%
print(vac_rent["ct_id"].head().to_list())
print(vac_rent["ct_id"].dtype)
print(
    vac_rent.loc[
        vac_rent["vacancy_total"] == 26,
        "ct_id"
    ].to_list()
)

# %%
vac_rent_sensitivity = vac_rent[
    vac_rent["ct_id"] != 538.0
].copy()

rho_vr_sens, p_vr_sens = spearmanr(
    vac_rent_sensitivity["rent_total"],
    vac_rent_sensitivity["vacancy_total"]
)

print(f"Observations: {len(vac_rent_sensitivity)}")
print(f"Spearman correlation: {rho_vr_sens:.3f}")
print(f"P-value: {p_vr_sens:.4g}")

# %%
vac_income = vacancy_data.dropna(
    subset=[
        "vacancy_total",
        "median_household_income_2020"
    ]
)

rho_vi, p_vi = spearmanr(
    vac_income["median_household_income_2020"],
    vac_income["vacancy_total"]
)

print(f"Observations: {len(vac_income)}")
print(f"Spearman correlation: {rho_vi:.3f}")
print(f"P-value: {p_vi:.4g}")

# %%
vac_income_sensitivity = vac_income[
    vac_income["ct_id"] != 538.0
].copy()

rho_vi_sens, p_vi_sens = spearmanr(
    vac_income_sensitivity["median_household_income_2020"],
    vac_income_sensitivity["vacancy_total"]
)

print(f"Observations: {len(vac_income_sensitivity)}")
print(f"Spearman correlation: {rho_vi_sens:.3f}")
print(f"P-value: {p_vi_sens:.4g}")


# %%
fig, ax = plt.subplots(figsize=(9, 6))

plot_data = vacancy_data.dropna(
    subset=["rent_total", "vacancy_total"]
)

ax.scatter(
    plot_data["rent_total"],
    plot_data["vacancy_total"],
    alpha=0.7
)

x = plot_data["rent_total"]
y = plot_data["vacancy_total"]

slope, intercept = np.polyfit(x, y, 1)

x_line = np.linspace(x.min(), x.max(), 100)
y_line = intercept + slope * x_line

ax.plot(
    x_line,
    y_line,
    linewidth=2
)

ax.set_title(
    "Vacancy Rate vs. Average Total Rent",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("Average monthly total rent ($)")
ax.set_ylabel("Vacancy rate (%)")

ax.text(
    0.05,
    0.95,
    f"Spearman ρ = {rho_vr:.3f}\np = 0.015",
    transform=ax.transAxes,
    verticalalignment="top",
    fontsize=11
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# %%
fig, ax = plt.subplots(figsize=(9, 6))

plot_data = vacancy_data.dropna(
    subset=[
        "median_household_income_2020",
        "vacancy_total"
    ]
)

ax.scatter(
    plot_data["median_household_income_2020"],
    plot_data["vacancy_total"],
    alpha=0.7
)

x = plot_data["median_household_income_2020"]
y = plot_data["vacancy_total"]

slope, intercept = np.polyfit(x, y, 1)

x_line = np.linspace(x.min(), x.max(), 100)
y_line = intercept + slope * x_line

ax.plot(
    x_line,
    y_line,
    linewidth=2
)

ax.set_title(
    "Vacancy Rate vs. Median Household Income",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("Median household income (2020, $)")
ax.set_ylabel("Vacancy rate (%)")

ax.text(
    0.05,
    0.95,
    f"Spearman ρ = {rho_vi:.3f}\np = 0.005",
    transform=ax.transAxes,
    verticalalignment="top",
    fontsize=11
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# %%
print(f"Median vacancy rate: {vacancy_data['vacancy_total'].median():.1f}%")
print(f"Mean vacancy rate: {vacancy_data['vacancy_total'].mean():.2f}%")
print(f"Highest vacancy rate: {vacancy_data['vacancy_total'].max():.1f}%")
print(f"Vacancy observations: {vacancy_data['vacancy_total'].notna().sum()}")

# %%
from IPython.display import display

# -----------------------------
# Page 4 dashboard
# -----------------------------

fig = plt.figure(figsize=(16, 9))

fig.suptitle(
    "VACANCY & MARKET PRESSURE",
    fontsize=22,
    fontweight="bold",
    x=0.05,
    ha="left",
    y=0.96
)

# -----------------------------
# KPI cards
# -----------------------------

kpis = [
    ("Median vacancy", "0.7%"),
    ("Mean vacancy", "1.82%"),
    ("Highest vacancy", "26.0%"),
    ("Observed tracts", "57")
]

x_positions = [0.05, 0.28, 0.51, 0.74]

for (label, value), x in zip(kpis, x_positions):

    fig.text(
        x,
        0.86,
        value,
        fontsize=24,
        fontweight="bold"
    )

    fig.text(
        x,
        0.825,
        label,
        fontsize=10
    )

# -----------------------------
# Chart 1: Vacancy vs rent
# -----------------------------

ax1 = fig.add_axes([0.07, 0.43, 0.40, 0.30])

plot_data = vacancy_data.dropna(
    subset=["rent_total", "vacancy_total"]
)

ax1.scatter(
    plot_data["rent_total"],
    plot_data["vacancy_total"],
    alpha=0.7
)

x = plot_data["rent_total"]
y = plot_data["vacancy_total"]

slope, intercept = np.polyfit(x, y, 1)

x_line = np.linspace(x.min(), x.max(), 100)
y_line = intercept + slope * x_line

ax1.plot(
    x_line,
    y_line,
    linewidth=2
)

ax1.set_title(
    "Vacancy Rate vs. Average Total Rent",
    fontsize=13,
    fontweight="bold"
)

ax1.set_xlabel("Average monthly total rent ($)")
ax1.set_ylabel("Vacancy rate (%)")

ax1.text(
    0.05,
    0.95,
    "Spearman ρ = −0.328\np = 0.015",
    transform=ax1.transAxes,
    verticalalignment="top",
    fontsize=10
)

ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# -----------------------------
# Chart 2: Vacancy vs income
# -----------------------------

ax2 = fig.add_axes([0.53, 0.43, 0.40, 0.30])

plot_data = vacancy_data.dropna(
    subset=[
        "median_household_income_2020",
        "vacancy_total"
    ]
)

ax2.scatter(
    plot_data["median_household_income_2020"],
    plot_data["vacancy_total"],
    alpha=0.7
)

x = plot_data["median_household_income_2020"]
y = plot_data["vacancy_total"]

slope, intercept = np.polyfit(x, y, 1)

x_line = np.linspace(x.min(), x.max(), 100)
y_line = intercept + slope * x_line

ax2.plot(
    x_line,
    y_line,
    linewidth=2
)

ax2.set_title(
    "Vacancy Rate vs. Median Household Income",
    fontsize=13,
    fontweight="bold"
)

ax2.set_xlabel("Median household income (2020, $)")
ax2.set_ylabel("Vacancy rate (%)")

ax2.text(
    0.05,
    0.95,
    "Spearman ρ = −0.371\np = 0.005",
    transform=ax2.transAxes,
    verticalalignment="top",
    fontsize=10
)

ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# -----------------------------
# Insight panel
# -----------------------------

fig.text(
    0.07,
    0.31,
    "KEY FINDINGS",
    fontsize=13,
    fontweight="bold"
)

fig.text(
    0.07,
    0.265,
    "• Higher-rent tracts tend to have lower vacancy rates.",
    fontsize=11
)

fig.text(
    0.07,
    0.225,
    "• Higher-income tracts also tend to have lower vacancy rates.",
    fontsize=11
)

fig.text(
    0.07,
    0.185,
    "• Both relationships remain statistically significant after excluding",
    fontsize=11
)

fig.text(
    0.085,
    0.15,
    "the 26% vacancy observation.",
    fontsize=11
)

fig.text(
    0.07,
    0.08,
    "METHOD: Vacancy analysis uses 2023 CMHC census-tract observations.",
    fontsize=9
)

fig.text(
    0.07,
    0.055,
    "Only 57 of 187 tracts report total vacancy; missing observations are retained as missing.",
    fontsize=9
)

fig.text(
    0.07,
    0.03,
    "Associations are descriptive and do not establish causality. CT 0538.00 (26% vacancy) is retained.",
    fontsize=9
)

plt.show()

# %%
print("RENT ↔ VACANCY")
print(f"Full sample:       ρ = {rho_vr:.3f}, p = {p_vr:.4f}, n = {len(vac_rent)}")
print(f"Excluding CT 0538: ρ = {rho_vr_sens:.3f}, p = {p_vr_sens:.4f}, n = {len(vac_rent_sensitivity)}")

print("\nINCOME ↔ VACANCY")
print(f"Full sample:       ρ = {rho_vi:.3f}, p = {p_vi:.4f}, n = {len(vac_income)}")
print(f"Excluding CT 0538: ρ = {rho_vi_sens:.3f}, p = {p_vi_sens:.4f}, n = {len(vac_income_sensitivity)}")

# %%
model_data = dashboard_tracts[
    [
        "ct_id",
        "rent_total",
        "units_total",
        "median_household_income_2020"
    ]
].dropna().copy()

model_data["log_units_total"] = np.log1p(
    model_data["units_total"]
)

print("Model observations:", len(model_data))
print("Unique census tracts:", model_data["ct_id"].nunique())

print("\nModel variables:")
print(
    model_data[
        [
            "rent_total",
            "units_total",
            "log_units_total",
            "median_household_income_2020"
        ]
    ].describe().round(2)
)

# %%
import statsmodels.api as sm

X = model_data[
    [
        "log_units_total",
        "median_household_income_2020"
    ]
]

X = sm.add_constant(X)

y = model_data["rent_total"]

rent_model = sm.OLS(y, X).fit()

print(rent_model.summary())

# %%
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_data = pd.DataFrame({
    "variable": X.columns,
    "VIF": [
        variance_inflation_factor(X.values, i)
        for i in range(X.shape[1])
    ]
})

print(vif_data.round(3))

# %%
from statsmodels.stats.outliers_influence import OLSInfluence

influence = OLSInfluence(rent_model)

model_data["cooks_distance"] = influence.cooks_distance[0]

threshold = 4 / len(model_data)

influential = (
    model_data[
        model_data["cooks_distance"] > threshold
    ]
    [
        [
            "ct_id",
            "rent_total",
            "units_total",
            "median_household_income_2020",
            "cooks_distance"
        ]
    ]
    .sort_values("cooks_distance", ascending=False)
)

print(f"Cook's distance threshold: {threshold:.4f}")
print(f"Influential observations: {len(influential)}")
print()
print(influential.to_string(index=False))

# %%
sensitivity_data = model_data[
    model_data["ct_id"] != 110.06
].copy()

X_sens = sensitivity_data[
    [
        "log_units_total",
        "median_household_income_2020"
    ]
]

X_sens = sm.add_constant(X_sens)

y_sens = sensitivity_data["rent_total"]

rent_model_sens = sm.OLS(
    y_sens,
    X_sens
).fit()

print(rent_model_sens.summary())

# %%
full_supply_coef = rent_model.params["log_units_total"]
sens_supply_coef = rent_model_sens.params["log_units_total"]

full_income_coef = rent_model.params["median_household_income_2020"]
sens_income_coef = rent_model_sens.params["median_household_income_2020"]

supply_change = (
    (sens_supply_coef - full_supply_coef)
    / full_supply_coef
    * 100
)

income_change = (
    (sens_income_coef - full_income_coef)
    / full_income_coef
    * 100
)

print(f"Supply coefficient: {full_supply_coef:.4f} → {sens_supply_coef:.4f}")
print(f"Supply coefficient change: {supply_change:.2f}%")

print()

print(f"Income coefficient: {full_income_coef:.6f} → {sens_income_coef:.6f}")
print(f"Income coefficient change: {income_change:.2f}%")

# %%
model_data["predicted_rent"] = rent_model.predict(
    sm.add_constant(
        model_data[
            [
                "log_units_total",
                "median_household_income_2020"
            ]
        ]
    )
)

fig, ax = plt.subplots(figsize=(9, 6))

ax.scatter(
    model_data["rent_total"],
    model_data["predicted_rent"],
    alpha=0.7
)

min_val = min(
    model_data["rent_total"].min(),
    model_data["predicted_rent"].min()
)

max_val = max(
    model_data["rent_total"].max(),
    model_data["predicted_rent"].max()
)

ax.plot(
    [min_val, max_val],
    [min_val, max_val],
    linewidth=2
)

ax.set_title(
    "Observed vs. Predicted Total Rent",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel("Observed average monthly rent ($)")
ax.set_ylabel("Predicted average monthly rent ($)")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.text(
    0.05,
    0.95,
    "OLS model: R² = 0.678\nn = 59",
    transform=ax.transAxes,
    verticalalignment="top",
    fontsize=11
)

plt.tight_layout()
plt.show()

# %%
from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(
    model_data["rent_total"],
    model_data["predicted_rent"]
)

rmse = np.sqrt(
    mean_squared_error(
        model_data["rent_total"],
        model_data["predicted_rent"]
    )
)

print(f"MAE: ${mae:.2f}")
print(f"RMSE: ${rmse:.2f}")
print(f"R-squared: {rent_model.rsquared:.3f}")
print(f"Adjusted R-squared: {rent_model.rsquared_adj:.3f}")

# %%
# -----------------------------
# Page 5 dashboard
# -----------------------------

fig = plt.figure(figsize=(16, 9))

fig.suptitle(
    "RENT MODEL & STATISTICAL EVIDENCE",
    fontsize=22,
    fontweight="bold",
    x=0.05,
    ha="left",
    y=0.96
)

# -----------------------------
# KPI cards
# -----------------------------

kpis = [
    ("R²", "0.678"),
    ("Adjusted R²", "0.666"),
    ("MAE", "$138"),
    ("RMSE", "$166")
]

x_positions = [0.05, 0.28, 0.51, 0.74]

for (label, value), x in zip(kpis, x_positions):

    fig.text(
        x,
        0.86,
        value,
        fontsize=24,
        fontweight="bold"
    )

    fig.text(
        x,
        0.825,
        label,
        fontsize=10
    )

# -----------------------------
# Observed vs predicted chart
# -----------------------------

ax = fig.add_axes([0.07, 0.40, 0.42, 0.32])

ax.scatter(
    model_data["rent_total"],
    model_data["predicted_rent"],
    alpha=0.7
)

min_val = min(
    model_data["rent_total"].min(),
    model_data["predicted_rent"].min()
)

max_val = max(
    model_data["rent_total"].max(),
    model_data["predicted_rent"].max()
)

ax.plot(
    [min_val, max_val],
    [min_val, max_val],
    linewidth=2
)

ax.set_title(
    "Observed vs. Predicted Total Rent",
    fontsize=13,
    fontweight="bold"
)

ax.set_xlabel("Observed average monthly rent ($)")
ax.set_ylabel("Predicted average monthly rent ($)")

ax.text(
    0.05,
    0.95,
    "R² = 0.678\nMAE = $138\nn = 59",
    transform=ax.transAxes,
    verticalalignment="top",
    fontsize=10
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# -----------------------------
# Coefficient summary
# -----------------------------

ax2 = fig.add_axes([0.55, 0.40, 0.37, 0.32])

ax2.axis("off")

ax2.text(
    0,
    0.95,
    "MODEL COEFFICIENTS",
    fontsize=13,
    fontweight="bold"
)

ax2.text(
    0,
    0.78,
    "Rental supply",
    fontsize=11,
    fontweight="bold"
)

ax2.text(
    0,
    0.70,
    "β = 168.75  |  p < 0.001",
    fontsize=11
)

ax2.text(
    0,
    0.58,
    "Median household income",
    fontsize=11,
    fontweight="bold"
)

ax2.text(
    0,
    0.50,
    "β = 0.0112  |  p < 0.001",
    fontsize=11
)

ax2.text(
    0,
    0.34,
    "Model:",
    fontsize=10,
    fontweight="bold"
)

ax2.text(
    0,
    0.27,
    "Total rent ~ log(rental supply) + household income",
    fontsize=10
)

# -----------------------------
# Key findings
# -----------------------------

fig.text(
    0.07,
    0.30,
    "KEY FINDINGS",
    fontsize=13,
    fontweight="bold"
)

fig.text(
    0.07,
    0.255,
    "• Rental supply and household income jointly explain 67.8% of rent variation.",
    fontsize=11
)

fig.text(
    0.07,
    0.215,
    "• Both predictors remain statistically significant in the multivariable model.",
    fontsize=11
)

fig.text(
    0.07,
    0.175,
    "• Removing the influential CT 0110.06 increases R² to 0.699;",
    fontsize=11
)

fig.text(
    0.085,
    0.14,
    "the supply coefficient changes by only 0.51%.",
    fontsize=11
)

# -----------------------------
# Methodology
# -----------------------------

fig.text(
    0.07,
    0.08,
    "METHOD: OLS regression using 59 Winnipeg census tracts with complete rent, supply and income data.",
    fontsize=9
)

fig.text(
    0.07,
    0.055,
    "Supply is log-transformed. CT 0110.06 exceeded the Cook's-distance threshold but is retained in the primary model.",
    fontsize=9
)

fig.text(
    0.07,
    0.03,
    "Coefficients describe conditional associations and should not be interpreted as causal effects.",
    fontsize=9
)

plt.show()

# %%
from pathlib import Path

cmhc_dir = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/data/raw/cmhc"
)

rural_files = sorted(
    [
        f.name
        for f in cmhc_dir.iterdir()
        if f.is_file()
        and "rural" in f.name.lower()
    ]
)

print("Rural CMHC files:")
for f in rural_files:
    print(f)

# %%
from pathlib import Path

search_roots = [
    cmhc_dir,
]

matches = []

for root in search_roots:
    if root.exists():
        for f in root.rglob("*"):
            if f.is_file() and any(
                term in f.name.lower()
                for term in ["rural", "small-centre", "small_centre"]
            ):
                matches.append(str(f))

print("Matching files:")
for f in sorted(set(matches)):
    print(f)

# %%
from pathlib import Path
import pandas as pd

units_path = Path(
    "data/raw/cmhc/rental-market-survey-number-units-universe-bedroom-type-census-subdivision-2025-en.xlsx"
)

print("Exists:", units_path.exists())
print("Path:", units_path)

rural_units_csd = pd.read_excel(
    units_path,
    sheet_name="Universe_CSD",
    header=0
)

print("Shape:", rural_units_csd.shape)
print("Columns:", rural_units_csd.columns.tolist())

# %%
# Reload with no header so we can inspect the workbook structure
rural_units_raw = pd.read_excel(
    units_path,
    sheet_name="Universe_CSD",
    header=None
)

print(rural_units_raw.iloc[:8, :].to_string(index=False, header=False))

# %%
rural_units_csd = pd.read_excel(
    units_path,
    sheet_name="Universe_CSD",
    header=3
)

# Standardize column names
rural_units_csd.columns = [
    "dwelling_type",
    "province",
    "csd",
    "units_studio",
    "units_1br",
    "units_2br",
    "units_3br_plus",
    "units_total"
]

# Keep Manitoba only
rural_units_mb = rural_units_csd[
    rural_units_csd["province"].eq("Manitoba")
].copy()

print("Manitoba rows:", len(rural_units_mb))
print("Unique CSDs:", rural_units_mb["csd"].nunique())

print("\nDwelling types:")
print(rural_units_mb["dwelling_type"].value_counts())

print("\nFirst Manitoba records:")
print(rural_units_mb.head(10).to_string(index=False))

# %%
rural_units_apartment = (
    rural_units_mb[
        rural_units_mb["dwelling_type"].eq("Apartment")
    ]
    .copy()
    .reset_index(drop=True)
)

print("Apartment CSDs:", len(rural_units_apartment))
print("Unique CSDs:", rural_units_apartment["csd"].nunique())

print("\nSummary:")
print(
    rural_units_apartment[
        ["units_studio", "units_1br", "units_2br",
         "units_3br_plus", "units_total"]
    ]
    .describe()
    .round(2)
)

print("\nLargest apartment rental markets:")
print(
    rural_units_apartment[
        ["csd", "units_total"]
    ]
    .sort_values("units_total", ascending=False)
    .head(10)
    .to_string(index=False)
)

# %%
rural_rent_csd = pd.read_excel(
    "data/raw/cmhc/rural-rental-market-survey-data-average-rent-census-subdivision-2025-en.xlsx",
    sheet_name="Avg Rent_CSD",
    header=3
)

rural_rent_csd.columns = [
    "dwelling_type",
    "province",
    "csd",
    "rent_studio",
    "rent_studio_reliability",
    "rent_1br",
    "rent_1br_reliability",
    "rent_2br",
    "rent_2br_reliability",
    "rent_3br_plus",
    "rent_3br_plus_reliability",
    "rent_total",
    "rent_total_reliability"
]

rural_rent_mb = rural_rent_csd[
    rural_rent_csd["province"].eq("Manitoba")
    & rural_rent_csd["dwelling_type"].eq("Apartment")
].copy()

print("Manitoba apartment CSDs:", len(rural_rent_mb))
print("\nColumns:")
print(rural_rent_mb.columns.tolist())

print("\nRent preview:")
print(
    rural_rent_mb[
        ["csd", "rent_studio", "rent_1br", "rent_2br",
         "rent_3br_plus", "rent_total"]
    ].head(10).to_string(index=False)
)

# %%
rent_cols = [
    "rent_studio",
    "rent_1br",
    "rent_2br",
    "rent_3br_plus",
    "rent_total"
]

for col in rent_cols:
    rural_rent_mb[col] = (
        rural_rent_mb[col]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .replace({"**": pd.NA, "--": pd.NA, "nan": pd.NA, "": pd.NA})
    )
    rural_rent_mb[col] = pd.to_numeric(
        rural_rent_mb[col],
        errors="coerce"
    )

print("Usable rent observations:")
print(rural_rent_mb[rent_cols].notna().sum())

print("\nTotal-rent summary:")
print(rural_rent_mb["rent_total"].describe().round(2))

print("\nApartment CSDs with usable total rent:")
print(
    rural_rent_mb.loc[
        rural_rent_mb["rent_total"].notna(),
        ["csd", "rent_total"]
    ]
    .sort_values("rent_total")
    .to_string(index=False)
)

# %%
rural_vacancy_csd = pd.read_excel(
    "data/raw/cmhc/rural-rental-market-survey-data-vacancy-rate-census-subdivision-2025-en.xlsx",
    sheet_name="Vacancy Rate_CSD",
    header=3
)

rural_vacancy_csd.columns = [
    "dwelling_type",
    "province",
    "csd",
    "vacancy_studio",
    "vacancy_studio_reliability",
    "vacancy_1br",
    "vacancy_1br_reliability",
    "vacancy_2br",
    "vacancy_2br_reliability",
    "vacancy_3br_plus",
    "vacancy_3br_plus_reliability",
    "vacancy_total",
    "vacancy_total_reliability"
]

rural_vacancy_mb = rural_vacancy_csd[
    rural_vacancy_csd["province"].eq("Manitoba")
    & rural_vacancy_csd["dwelling_type"].eq("Apartment")
].copy()

print("Manitoba apartment CSDs:", len(rural_vacancy_mb))

print("\nVacancy preview:")
print(
    rural_vacancy_mb[
        ["csd", "vacancy_studio", "vacancy_1br",
         "vacancy_2br", "vacancy_3br_plus", "vacancy_total"]
    ].head(10).to_string(index=False)
)

# %%
vacancy_cols = [
    "vacancy_studio",
    "vacancy_1br",
    "vacancy_2br",
    "vacancy_3br_plus",
    "vacancy_total"
]

for col in vacancy_cols:
    rural_vacancy_mb[col] = (
        rural_vacancy_mb[col]
        .astype(str)
        .str.replace("%", "", regex=False)
        .replace({
            "**": pd.NA,
            "--": pd.NA,
            "nan": pd.NA,
            "": pd.NA
        })
    )
    rural_vacancy_mb[col] = pd.to_numeric(
        rural_vacancy_mb[col],
        errors="coerce"
    )

print("Usable vacancy observations:")
print(rural_vacancy_mb[vacancy_cols].notna().sum())

print("\nTotal-vacancy summary:")
print(
    rural_vacancy_mb["vacancy_total"]
    .describe()
    .round(2)
)

print("\nCSDs with usable total vacancy:")
print(
    rural_vacancy_mb.loc[
        rural_vacancy_mb["vacancy_total"].notna(),
        ["csd", "vacancy_total"]
    ]
    .sort_values("vacancy_total")
    .to_string(index=False)
)

# %%
units_benchmark = rural_units_apartment[
    [
        "csd",
        "units_studio",
        "units_1br",
        "units_2br",
        "units_3br_plus",
        "units_total"
    ]
].copy()

rent_benchmark = rural_rent_mb[
    [
        "csd",
        "rent_studio",
        "rent_1br",
        "rent_2br",
        "rent_3br_plus",
        "rent_total"
    ]
].copy()

vacancy_benchmark = rural_vacancy_mb[
    [
        "csd",
        "vacancy_studio",
        "vacancy_1br",
        "vacancy_2br",
        "vacancy_3br_plus",
        "vacancy_total"
    ]
].copy()

rural_benchmark = (
    units_benchmark
    .merge(rent_benchmark, on="csd", how="left", validate="one_to_one")
    .merge(vacancy_benchmark, on="csd", how="left", validate="one_to_one")
)

print("Shape:", rural_benchmark.shape)
print("Unique CSDs:", rural_benchmark["csd"].nunique())

print("\nCoverage:")
print(
    rural_benchmark[
        ["units_total", "rent_total", "vacancy_total"]
    ].notna().sum()
)

print("\nMerged benchmark:")
print(
    rural_benchmark[
        ["csd", "units_total", "rent_total", "vacancy_total"]
    ]
    .sort_values("rent_total")
    .to_string(index=False)
)

# %%
from pathlib import Path
import pandas as pd

analytical_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "data/processed/winnipeg_ct_rental_market_analytical.csv"
)

dashboard_tracts = pd.read_csv(analytical_path)

print("Shape:", dashboard_tracts.shape)
print("Unique census tracts:", dashboard_tracts["ct_id"].nunique())

print("\nRent observations:")
print(
    dashboard_tracts["rent_total"].notna().sum()
)

print("\nMedian Winnipeg total rent:")
print(
    dashboard_tracts["rent_total"].median()
)

# %%
import pandas as pd

# Units
rural_units_csd = pd.read_excel(
    "data/raw/cmhc/rental-market-survey-number-units-universe-bedroom-type-census-subdivision-2025-en.xlsx",
    sheet_name="Universe_CSD",
    header=3
)

rural_units_csd.columns = [
    "dwelling_type", "province", "csd",
    "units_studio", "units_1br", "units_2br",
    "units_3br_plus", "units_total"
]

rural_units_apartment = rural_units_csd[
    (rural_units_csd["province"] == "Manitoba") &
    (rural_units_csd["dwelling_type"] == "Apartment")
].copy()

# Rent
rural_rent_csd = pd.read_excel(
    "data/raw/cmhc/rural-rental-market-survey-data-average-rent-census-subdivision-2025-en.xlsx",
    sheet_name="Avg Rent_CSD",
    header=3
)

rural_rent_csd.columns = [
    "dwelling_type", "province", "csd",
    "rent_studio", "rent_studio_reliability",
    "rent_1br", "rent_1br_reliability",
    "rent_2br", "rent_2br_reliability",
    "rent_3br_plus", "rent_3br_plus_reliability",
    "rent_total", "rent_total_reliability"
]

rural_rent_mb = rural_rent_csd[
    (rural_rent_csd["province"] == "Manitoba") &
    (rural_rent_csd["dwelling_type"] == "Apartment")
].copy()

for col in ["rent_studio", "rent_1br", "rent_2br",
            "rent_3br_plus", "rent_total"]:
    rural_rent_mb[col] = pd.to_numeric(
        rural_rent_mb[col]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .replace({"**": pd.NA, "--": pd.NA, "nan": pd.NA, "": pd.NA}),
        errors="coerce"
    )

# Vacancy
rural_vacancy_csd = pd.read_excel(
    "data/raw/cmhc/rural-rental-market-survey-data-vacancy-rate-census-subdivision-2025-en.xlsx",
    sheet_name="Vacancy Rate_CSD",
    header=3
)

rural_vacancy_csd.columns = [
    "dwelling_type", "province", "csd",
    "vacancy_studio", "vacancy_studio_reliability",
    "vacancy_1br", "vacancy_1br_reliability",
    "vacancy_2br", "vacancy_2br_reliability",
    "vacancy_3br_plus", "vacancy_3br_plus_reliability",
    "vacancy_total", "vacancy_total_reliability"
]

rural_vacancy_mb = rural_vacancy_csd[
    (rural_vacancy_csd["province"] == "Manitoba") &
    (rural_vacancy_csd["dwelling_type"] == "Apartment")
].copy()

for col in ["vacancy_studio", "vacancy_1br", "vacancy_2br",
            "vacancy_3br_plus", "vacancy_total"]:
    rural_vacancy_mb[col] = pd.to_numeric(
        rural_vacancy_mb[col]
        .astype(str)
        .str.replace("%", "", regex=False)
        .replace({"**": pd.NA, "--": pd.NA, "nan": pd.NA, "": pd.NA}),
        errors="coerce"
    )

# Merge
rural_benchmark = (
    rural_units_apartment[
        ["csd", "units_total"]
    ]
    .merge(
        rural_rent_mb[["csd", "rent_total"]],
        on="csd",
        how="left",
        validate="one_to_one"
    )
    .merge(
        rural_vacancy_mb[["csd", "vacancy_total"]],
        on="csd",
        how="left",
        validate="one_to_one"
    )
)

print("Rural benchmark shape:", rural_benchmark.shape)
print("Unique CSDs:", rural_benchmark["csd"].nunique())
print("Usable rent:", rural_benchmark["rent_total"].notna().sum())
print("Usable vacancy:", rural_benchmark["vacancy_total"].notna().sum())

# %%
import matplotlib.pyplot as plt

# Winnipeg tract-level rents
wpg_rent = (
    dashboard_tracts[["ct_id", "rent_total"]]
    .dropna(subset=["rent_total"])
    .copy()
)

# Rural/small-centre rents
rural_rent_plot = (
    rural_benchmark[["csd", "rent_total"]]
    .dropna(subset=["rent_total"])
    .sort_values("rent_total")
    .copy()
)

wpg_median = wpg_rent["rent_total"].median()
wpg_q1 = wpg_rent["rent_total"].quantile(0.25)
wpg_q3 = wpg_rent["rent_total"].quantile(0.75)
rural_median = rural_rent_plot["rent_total"].median()

fig, ax = plt.subplots(figsize=(11, 7))

ax.scatter(
    rural_rent_plot["rent_total"],
    rural_rent_plot["csd"],
    s=65
)

ax.axvline(
    wpg_median,
    linestyle="--",
    linewidth=2,
    label=f"Winnipeg median: ${wpg_median:,.0f}"
)

ax.axvspan(
    wpg_q1,
    wpg_q3,
    alpha=0.15,
    label=f"Winnipeg IQR: ${wpg_q1:,.0f}–${wpg_q3:,.0f}"
)

ax.set_title(
    "Total Average Rent: Winnipeg vs Manitoba Rural/Small-Centre Apartments",
    fontsize=14,
    pad=15
)

ax.set_xlabel("Monthly average rent ($)")
ax.set_ylabel("Manitoba rural/small-centre CSD")
ax.legend(loc="lower right")

ax.text(
    0.01,
    -0.13,
    "Source: CMHC Rental Market Survey. Winnipeg n=77 census tracts; "
    "rural/small-centre benchmark n=10 CSDs with usable total rent. "
    "Suppressed values treated as missing.",
    transform=ax.transAxes,
    fontsize=9,
    va="top"
)

plt.tight_layout()

svg_path = (
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "data/processed/dashboard/"
    "benchmark_winnipeg_vs_manitoba_rural_rent.svg"
)

plt.savefig(svg_path, format="svg", bbox_inches="tight")
plt.show()

print("Winnipeg median:", f"${wpg_median:,.0f}")
print("Winnipeg IQR:", f"${wpg_q1:,.0f}–${wpg_q3:,.0f}")
print("Rural/small-centre median:", f"${rural_median:,.0f}")
print("Rural/small-centre n:", len(rural_rent_plot))
print("SVG saved:", svg_path)

# %%
import matplotlib.pyplot as plt

# Winnipeg tract-level vacancy
wpg_vacancy = (
    dashboard_tracts[["ct_id", "vacancy_total"]]
    .dropna(subset=["vacancy_total"])
    .copy()
)

# Manitoba rural/small-centre apartment vacancy
rural_vacancy_plot = (
    rural_benchmark[["csd", "vacancy_total"]]
    .dropna(subset=["vacancy_total"])
    .sort_values("vacancy_total")
    .copy()
)

wpg_median = wpg_vacancy["vacancy_total"].median()
wpg_q1 = wpg_vacancy["vacancy_total"].quantile(0.25)
wpg_q3 = wpg_vacancy["vacancy_total"].quantile(0.75)

rural_median = rural_vacancy_plot["vacancy_total"].median()

fig, ax = plt.subplots(figsize=(11, 7))

ax.scatter(
    rural_vacancy_plot["vacancy_total"],
    rural_vacancy_plot["csd"],
    s=65
)

ax.axvline(
    wpg_median,
    linestyle="--",
    linewidth=2,
    label=f"Winnipeg median: {wpg_median:.1f}%"
)

ax.axvspan(
    wpg_q1,
    wpg_q3,
    alpha=0.15,
    label=f"Winnipeg IQR: {wpg_q1:.1f}%–{wpg_q3:.1f}%"
)

ax.set_title(
    "Total Vacancy Rate: Winnipeg vs Manitoba Rural/Small-Centre Apartments",
    fontsize=14,
    pad=15
)

ax.set_xlabel("Vacancy rate (%)")
ax.set_ylabel("Manitoba rural/small-centre CSD")
ax.legend(loc="lower right")

ax.text(
    0.01,
    -0.13,
    "Source: CMHC Rental Market Survey. Winnipeg n=57 census tracts; "
    "rural/small-centre benchmark n=8 CSDs with usable total vacancy. "
    "Suppressed values treated as missing.",
    transform=ax.transAxes,
    fontsize=9,
    va="top"
)

plt.tight_layout()

svg_path = (
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "data/processed/dashboard/"
    "benchmark_winnipeg_vs_manitoba_rural_vacancy.svg"
)

plt.savefig(svg_path, format="svg", bbox_inches="tight")
plt.show()

print("Winnipeg median:", f"{wpg_median:.1f}%")
print("Winnipeg IQR:", f"{wpg_q1:.1f}%–{wpg_q3:.1f}%")
print("Rural/small-centre median:", f"{rural_median:.1f}%")
print("Rural/small-centre n:", len(rural_vacancy_plot))
print("SVG saved:", svg_path)

# %%
benchmark_summary = pd.DataFrame({
    "Market": [
        "Winnipeg census tracts",
        "Manitoba rural/small-centre CSDs"
    ],
    "Rent_median": [
        dashboard_tracts["rent_total"].median(),
        rural_benchmark["rent_total"].median()
    ],
    "Rent_n": [
        dashboard_tracts["rent_total"].notna().sum(),
        rural_benchmark["rent_total"].notna().sum()
    ],
    "Vacancy_median": [
        dashboard_tracts["vacancy_total"].median(),
        rural_benchmark["vacancy_total"].median()
    ],
    "Vacancy_n": [
        dashboard_tracts["vacancy_total"].notna().sum(),
        rural_benchmark["vacancy_total"].notna().sum()
    ]
})

benchmark_summary["Rent_gap_vs_Winnipeg_pct"] = (
    (benchmark_summary["Rent_median"] / benchmark_summary.loc[0, "Rent_median"] - 1)
    * 100
)

benchmark_summary["Vacancy_gap_vs_Winnipeg_pp"] = (
    benchmark_summary["Vacancy_median"] - benchmark_summary.loc[0, "Vacancy_median"]
)

print(benchmark_summary.round(2).to_string(index=False))

# %%
import matplotlib.pyplot as plt
import numpy as np

# Benchmark values
wpg_rent_median = benchmark_summary.loc[0, "Rent_median"]
rural_rent_median = benchmark_summary.loc[1, "Rent_median"]

wpg_vacancy_median = benchmark_summary.loc[0, "Vacancy_median"]
rural_vacancy_median = benchmark_summary.loc[1, "Vacancy_median"]

rent_gap_pct = benchmark_summary.loc[1, "Rent_gap_vs_Winnipeg_pct"]
vacancy_gap_pp = benchmark_summary.loc[1, "Vacancy_gap_vs_Winnipeg_pp"]

fig = plt.figure(figsize=(14, 9))

fig.text(
    0.05, 0.94,
    "MANITOBA BENCHMARKING",
    fontsize=24,
    fontweight="bold"
)

fig.text(
    0.05, 0.895,
    "Winnipeg census tracts vs rural/small-centre apartment markets",
    fontsize=13
)

# KPI cards
kpis = [
    ("WINNIPEG MEDIAN RENT", f"${wpg_rent_median:,.0f}"),
    ("RURAL/SMALL-CENTRE MEDIAN", f"${rural_rent_median:,.0f}"),
    ("RENT DIFFERENCE", f"{rent_gap_pct:.1f}%"),
    ("VACANCY DIFFERENCE", f"+{vacancy_gap_pp:.2f} pp")
]

positions = [0.05, 0.28, 0.51, 0.74]

for (label, value), x in zip(kpis, positions):
    ax = fig.add_axes([x, 0.73, 0.19, 0.11])
    ax.axis("off")
    ax.text(0.02, 0.68, label, fontsize=9)
    ax.text(0.02, 0.15, value, fontsize=20, fontweight="bold")

# Rent comparison
ax1 = fig.add_axes([0.08, 0.38, 0.38, 0.25])

markets = ["Winnipeg", "Rural / small-centre"]
rent_values = [wpg_rent_median, rural_rent_median]

bars = ax1.bar(markets, rent_values)

ax1.set_title(
    "Median monthly total average rent",
    fontsize=12,
    pad=10
)

ax1.set_ylabel("Monthly rent ($)")
ax1.set_ylim(0, max(rent_values) * 1.25)

for bar, value in zip(bars, rent_values):
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        value + 25,
        f"${value:,.0f}",
        ha="center",
        fontsize=10
    )

# Vacancy comparison
ax2 = fig.add_axes([0.55, 0.38, 0.38, 0.25])

vacancy_values = [wpg_vacancy_median, rural_vacancy_median]

bars = ax2.bar(markets, vacancy_values)

ax2.set_title(
    "Median total vacancy rate",
    fontsize=12,
    pad=10
)

ax2.set_ylabel("Vacancy rate (%)")
ax2.set_ylim(0, max(vacancy_values) * 1.6)

for bar, value in zip(bars, vacancy_values):
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.04,
        f"{value:.2f}%",
        ha="center",
        fontsize=10
    )

# Findings
fig.text(
    0.08, 0.27,
    "KEY FINDINGS",
    fontsize=12,
    fontweight="bold"
)

findings = [
    f"• Rural/small-centre median rent is ${wpg_rent_median - rural_rent_median:,.0f} "
    f"lower than the Winnipeg tract median ({abs(rent_gap_pct):.1f}% lower).",
    
    f"• Median vacancy is similar in magnitude: {rural_vacancy_median:.2f}% "
    f"in rural/small-centre CSDs versus {wpg_vacancy_median:.2f}% in Winnipeg.",
    
    "• The rural benchmark covers only CSDs with usable CMHC observations, "
    "so missing and suppressed values are not treated as zero.",
    
    "• Geographic scale differs: Winnipeg observations are census tracts, "
    "while the rural benchmark uses census subdivisions."
]

for i, finding in enumerate(findings):
    fig.text(
        0.08,
        0.23 - i * 0.035,
        finding,
        fontsize=10
    )

# Methodology
fig.text(
    0.55, 0.27,
    "BENCHMARK DESIGN",
    fontsize=12,
    fontweight="bold"
)

method = (
    f"Winnipeg rent n={int(benchmark_summary.loc[0, 'Rent_n'])}; "
    f"rural/small-centre rent n={int(benchmark_summary.loc[1, 'Rent_n'])}.\n"
    f"Winnipeg vacancy n={int(benchmark_summary.loc[0, 'Vacancy_n'])}; "
    f"rural/small-centre vacancy n={int(benchmark_summary.loc[1, 'Vacancy_n'])}.\n"
    "CMHC Rental Market Survey observations; suppressed values retained as missing."
)

fig.text(
    0.55,
    0.22,
    method,
    fontsize=10,
    va="top"
)

fig.text(
    0.05,
    0.055,
    "Interpretation: descriptive benchmark only. Differences should not be interpreted as causal "
    "or as directly comparable household affordability measures.",
    fontsize=9
)

fig.text(
    0.05,
    0.025,
    "Source: CMHC Rental Market Survey, 2023 Winnipeg urban data and 2025 rural/small-centre data.",
    fontsize=8
)

svg_path = (
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "data/processed/dashboard/"
    "page6_manitoba_benchmarking.svg"
)

plt.savefig(svg_path, format="svg", bbox_inches="tight")
plt.show()

print("Page 6 SVG saved:", svg_path)

# %%
import pandas as pd
import os

analytical_path = (
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "data/processed/winnipeg_ct_rental_market_analytical.csv"
)

final_ct = pd.read_csv(analytical_path)

print("Analytical dataset")
print("-" * 50)
print(f"Rows: {len(final_ct):,}")
print(f"Columns: {len(final_ct.columns):,}")
print(f"Unique CTs: {final_ct['ct_id'].nunique():,}")
print(f"Duplicate CT IDs: {final_ct['ct_id'].duplicated().sum():,}")
print(f"File exists: {os.path.exists(analytical_path)}")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

folders = [
    "data/raw/cmhc",
    "data/raw/statcan",
    "data/processed/statcan",
    "data/processed/dashboard",
    "notebooks",
    "sql",
    "src",
    "reports",
    "dashboard",
    "docs"
]

for folder in folders:
    (project_root / folder).mkdir(parents=True, exist_ok=True)

print("GitHub project structure created:")
print()

for folder in folders:
    print(f"✓ {folder}/")

# %%
from pathlib import Path

project_root = Path("/Users/abbas90/winnipeg_rental_market_intelligence")

lines = [
    "# Winnipeg Rental Market Intelligence",
    "",
    "## Rental Prices, Vacancy, Supply, and Market Affordability Across Winnipeg",
    "",
    "### Overview",
    "",
    "This project analyzes Winnipeg's rental market at the census-tract level by integrating CMHC Rental Market Survey data with 2021 Census household-income data from Statistics Canada.",
    "",
    "The workflow demonstrates:",
    "",
    "- Data ingestion and cleaning",
    "- Multi-source data integration",
    "- SQL database construction",
    "- Statistical analysis",
    "- Regression modelling",
    "- Model diagnostics",
    "- Sensitivity analysis",
    "- Dashboard development",
    "- Business-oriented interpretation",
    "",
    "### Research Question",
    "",
    "**How do rental prices, vacancy rates, rental-housing supply, and local economic characteristics vary across Winnipeg, and what factors are associated with rental-market pressure and affordability?**",
    "",
    "### Data Sources",
    "",
    "#### CMHC Rental Market Survey",
    "",
    "- Rental housing supply by census tract",
    "- Average rent by bedroom type",
    "- Total average rent",
    "- Vacancy rates",
    "- Reliability indicators",
    "",
    "The primary Winnipeg analysis uses the **Apartment & Other** rental-market segment.",
    "",
    "#### Statistics Canada Census",
    "",
    "Table **98-10-0058-01** provides census-tract household income statistics.",
    "",
    "Primary income variable: **Median household total income (2020), 2020 constant dollars.**",
    "",
    "### Analytical Dataset",
    "",
    "- 187 Winnipeg census tracts",
    "- 25 analytical variables",
    "- 187 unique census-tract IDs",
    "- 0 duplicate IDs",
    "",
    "Different analyses use the observations available for the relevant variables because CMHC reporting coverage varies.",
    "",
    "### Statistical Methods",
    "",
    "- Descriptive statistics",
    "- Pearson correlation",
    "- Spearman correlation",
    "- Ordinary least squares regression",
    "- Residual diagnostics",
    "- Shapiro-Wilk test",
    "- Breusch-Pagan test",
    "- Variance inflation factors",
    "- Cook's distance",
    "- Sensitivity analysis",
    "",
    "### Key Findings",
    "",
    "#### Rental Prices and Income",
    "",
    "Across 77 census tracts with usable rent and income data:",
    "",
    "- Pearson r = **0.577**",
    "- Spearman rho = **0.498**",
    "",
    "Higher-income census tracts tend to have higher average rents.",
    "",
    "#### Market Affordability Indicator",
    "",
    "The project calculates:",
    "",
    "**Annualized average rent / median household income × 100**",
    "",
    "Across 77 observations:",
    "",
    "- Median = **19.3%**",
    "- Mean = **20.0%**",
    "- Minimum = **12.4%**",
    "- Maximum = **32.3%**",
    "",
    "The indicator is negatively associated with income:",
    "",
    "**Spearman rho = -0.506**",
    "",
    "This is an ecological market indicator, **not a household-level rent-burden measure**.",
    "",
    "#### Rental Supply",
    "",
    "Among 135 census tracts with usable supply data:",
    "",
    "- Median supply = **223 units**",
    "- Mean supply = **288 units**",
    "- Maximum = **954 units**",
    "",
    "Approximately 91% of observed rental units are 1- or 2-bedroom units.",
    "",
    "#### Vacancy",
    "",
    "Among 57 census tracts with usable total vacancy:",
    "",
    "- Median = **0.7%**",
    "- Mean = **1.82%**",
    "- Maximum = **26.0%**",
    "",
    "The 26% observation is retained and evaluated through sensitivity analysis.",
    "",
    "#### Multivariable Rent Model",
    "",
    "The final OLS model uses log-transformed rental supply and median household income to explain variation in total average rent.",
    "",
    "- **n = 59**",
    "- **R² = 0.678**",
    "- **Adjusted R² = 0.666**",
    "- **MAE = $138**",
    "- **RMSE = $166**",
    "",
    "The model is observational, so coefficients are interpreted as associations rather than causal effects.",
    "",
    "#### Manitoba Benchmark",
    "",
    "| Metric | Winnipeg | Rural / Small Centre |",
    "|---|---:|---:|",
    "| Median total rent | $1,124 | $848 |",
    "| Rent observations | 77 | 10 |",
    "| Median vacancy | 0.70% | 0.85% |",
    "| Vacancy observations | 57 | 8 |",
    "",
    "The rural/small-centre median rent is approximately **24.6% lower** than the Winnipeg tract median.",
    "",
    "This is a descriptive benchmark, not a causal or household-level affordability comparison.",
    "",
    "### Dashboard",
    "",
    "1. Market Overview",
    "2. Rental Supply & Composition",
    "3. Rental Prices & Affordability",
    "4. Vacancy & Market Pressure",
    "5. Rent Model & Statistical Evidence",
    "6. Manitoba Benchmarking",
    "",
    "### Data Quality",
    "",
    "CMHC suppression and reliability codes are preserved.",
    "",
    "Suppressed or unavailable observations are **not treated as zero**.",
    "",
    "Analyses report their usable sample sizes rather than forcing all variables into one complete-case dataset.",
    "",
    "### Limitations",
    "",
    "This is an observational cross-sectional analysis.",
    "",
    "The affordability indicator combines area-level average rent with area-level median household income. It does not measure individual household housing-cost burden.",
    "",
    "Geographic units also differ between the Winnipeg tract analysis and the rural/small-centre benchmark.",
    "",
    "### Repository Structure",
    "",
    "```text",
    "winnipeg_rental_market_intelligence/",
    "├── data/",
    "├── notebooks/",
    "├── sql/",
    "├── src/",
    "├── reports/",
    "├── dashboard/",
    "├── docs/",
    "└── README.md",
    "```",
    "",
    "### Tools",
    "",
    "Python • pandas • NumPy • matplotlib • statsmodels • SQLite • SQL • R • Power BI/Tableau • Git/GitHub",
    "",
    "### Author",
    "",
    "Statistics Honours student at the University of Manitoba with an Economics minor, focused on data analytics, statistical analysis, business intelligence, and applied machine learning."
]

readme_path = project_root / "README.md"
readme_path.write_text("\n".join(lines), encoding="utf-8")

print("README created successfully.")
print("Path:", readme_path)
print("Lines:", len(lines))
print("Characters:", len(readme_path.read_text(encoding="utf-8")))

# %%
from pathlib import Path

readme_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/README.md"
)

text = readme_path.read_text(encoding="utf-8")

print("README QA")
print("-" * 50)
print("Exists:", readme_path.exists())
print("Characters:", len(text))
print("Has title:", text.startswith("# Winnipeg Rental Market Intelligence"))
print("Has research question:", "### Research Question" in text)
print("Has key findings:", "### Key Findings" in text)
print("Has dashboard section:", "### Dashboard" in text)
print("Has limitations:", "### Limitations" in text)
print("Has repository structure:", "### Repository Structure" in text)

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

requirements = [
    "pandas",
    "numpy",
    "matplotlib",
    "scipy",
    "statsmodels",
    "openpyxl",
    "jupyter",
]

requirements_path = project_root / "requirements.txt"
requirements_path.write_text(
    "\n".join(requirements) + "\n",
    encoding="utf-8"
)

print("requirements.txt created:")
print(requirements_path)
print()
print(requirements_path.read_text(encoding="utf-8"))

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

gitignore_lines = [
    "# Python",
    "__pycache__/",
    "*.py[cod]",
    "*.pyo",
    ".pytest_cache/",
    "",
    "# Jupyter",
    ".ipynb_checkpoints/",
    "",
    "# Local environments",
    ".venv/",
    "venv/",
    "env/",
    "",
    "# Local databases",
    "*.db",
    "*.sqlite",
    "*.sqlite3",
    "",
    "# Large/raw data",
    "data/raw/",
    "",
    "# OS files",
    ".DS_Store",
    "Thumbs.db",
    "",
    "# IDE files",
    ".vscode/",
    ".idea/",
    "",
    "# Temporary files",
    "*.tmp",
    "*.bak",
    "*.log",
]

gitignore_path = project_root / ".gitignore"
gitignore_path.write_text(
    "\n".join(gitignore_lines) + "\n",
    encoding="utf-8"
)

print(".gitignore created:")
print(gitignore_path)
print()
print(gitignore_path.read_text(encoding="utf-8"))

# %%
from pathlib import Path
import nbformat as nbf

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

notebook = nbf.v4.new_notebook()

notebook["metadata"] = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python"
    }
}

cells = [
    nbf.v4.new_markdown_cell(
        "# Winnipeg Rental Market Intelligence\n\n"
        "## Census-Tract Analysis of Rental Prices, Supply, Vacancy, and Market Affordability\n\n"
        "This notebook presents the reproducible analytical workflow for the Winnipeg rental-market project."
    ),

    nbf.v4.new_markdown_cell(
        "## 1. Research Question\n\n"
        "**How do rental prices, vacancy rates, rental-housing supply, and local economic "
        "characteristics vary across Winnipeg, and what factors are associated with "
        "rental-market pressure and affordability?**"
    ),

    nbf.v4.new_markdown_cell(
        "## 2. Data Sources\n\n"
        "- CMHC Rental Market Survey: rental supply, average rents, and vacancy rates.\n"
        "- Statistics Canada Census table 98-10-0058-01: median household income.\n\n"
        "The primary geographic unit is the Winnipeg census tract. "
        "The CMHC rental segment used for the tract analysis is **Apartment & Other**."
    ),

    nbf.v4.new_code_cell(
        "from pathlib import Path\n"
        "import pandas as pd\n"
        "import numpy as np\n\n"
        "PROJECT_ROOT = Path('/Users/abbas90/winnipeg_rental_market_intelligence')\n"
        "DATA_PATH = PROJECT_ROOT / 'data/processed/winnipeg_ct_rental_market_analytical.csv'\n\n"
        "df = pd.read_csv(DATA_PATH)\n\n"
        "print('Dataset shape:', df.shape)\n"
        "print('Unique census tracts:', df['ct_id'].nunique())\n        " 
    ),

    nbf.v4.new_markdown_cell(
        "## 3. Data Quality\n\n"
        "CMHC suppression and availability codes are treated as missing rather than zero. "
        "Variable coverage differs across the rental-market measures, so each analysis "
        "uses the observations available for the relevant variables."
    ),

    nbf.v4.new_code_cell(
        "print('Duplicate CT IDs:', df['ct_id'].duplicated().sum())\n"
        "print('\\nMissing observations by variable:')\n"
        "print(df.isna().sum().sort_values(ascending=False).head(15))"
    ),

    nbf.v4.new_markdown_cell(
        "## 4. Rental Market Descriptives\n\n"
        "Summary statistics for rental supply, total average rent, vacancy, and household income."
    ),

    nbf.v4.new_code_cell(
        "summary_cols = [\n"
        "    'units_total',\n"
        "    'rent_total',\n"
        "    'vacancy_total',\n"
        "    'median_household_income_2020'\n"
        "]\n\n"
        "df[summary_cols].describe().round(2)"
    ),

    nbf.v4.new_markdown_cell(
        "## 5. Market Affordability Indicator\n\n"
        "The project uses an ecological market indicator:\n\n"
        "**Annualized total average rent / median household income × 100**\n\n"
        "This is a geographic market indicator and should not be interpreted as "
        "individual household rent burden."
    ),

    nbf.v4.new_code_cell(
        "affordability = df[['ct_id', 'rent_total', 'median_household_income_2020']].dropna().copy()\n"
        "affordability['rent_income_pct'] = (\n"
        "    affordability['rent_total'] * 12 /\n"
        "    affordability['median_household_income_2020'] * 100\n"
        ")\n\n"
        "print('Observations:', len(affordability))\n"
        "print(affordability['rent_income_pct'].describe().round(2))"
    ),

    nbf.v4.new_markdown_cell(
        "## 6. Correlation Analysis\n\n"
        "Spearman correlation is used alongside Pearson correlation to assess monotonic "
        "relationships without relying exclusively on linear association."
    ),

    nbf.v4.new_code_cell(
        "from scipy.stats import pearsonr, spearmanr\n\n"
        "rent_income = df[['rent_total', 'median_household_income_2020']].dropna()\n\n"
        "pearson_r, pearson_p = pearsonr(\n"
        "    rent_income['rent_total'],\n"
        "    rent_income['median_household_income_2020']\n"
        ")\n\n"
        "spearman_rho, spearman_p = spearmanr(\n"
        "    rent_income['rent_total'],\n"
        "    rent_income['median_household_income_2020']\n"
        ")\n\n"
        "print(f'Pearson r = {pearson_r:.3f}, p = {pearson_p:.4g}')\n"
        "print(f'Spearman rho = {spearman_rho:.3f}, p = {spearman_p:.4g}')"
    ),

    nbf.v4.new_markdown_cell(
        "## 7. Multivariable Rent Model\n\n"
        "Total average rent is modelled using log-transformed rental supply and "
        "median household income.\n\n"
        "The model is observational and coefficients are interpreted as associations, "
        "not causal effects."
    ),

    nbf.v4.new_code_cell(
        "import statsmodels.api as sm\n\n"
        "model_data = df[\n"
        "    ['units_total', 'rent_total', 'median_household_income_2020']\n"
        "].dropna().copy()\n\n"
        "model_data['log_units_total'] = np.log1p(model_data['units_total'])\n\n"
        "X = model_data[['log_units_total', 'median_household_income_2020']]\n"
        "X = sm.add_constant(X)\n"
        "y = model_data['rent_total']\n\n"
        "model = sm.OLS(y, X).fit()\n"
        "print(model.summary())"
    ),

    nbf.v4.new_markdown_cell(
        "## 8. Model Diagnostics\n\n"
        "Diagnostics include residual normality, heteroskedasticity, multicollinearity, "
        "and influential observations."
    ),

    nbf.v4.new_code_cell(
        "from statsmodels.stats.diagnostic import het_breuschpagan\n"
        "from statsmodels.stats.outliers_influence import variance_inflation_factor\n\n"
        "bp = het_breuschpagan(model.resid, model.model.exog)\n"
        "print('Breusch-Pagan p-value:', round(bp[1], 4))\n\n"
        "vif = pd.DataFrame({\n"
        "    'variable': X.columns,\n"
        "    'VIF': [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]\n"
        "})\n"
        "print('\\nVIF:')\n"
        "print(vif.round(3))"
    ),

    nbf.v4.new_markdown_cell(
        "## 9. Interpretation\n\n"
        "The final model explains approximately 68% of the variation in observed total "
        "average rent across the model sample. Higher median household income and larger "
        "rental-market inventories are positively associated with total average rent "
        "after accounting for the other predictor.\n\n"
        "These relationships should not be interpreted as evidence of causation."
    ),

    nbf.v4.new_markdown_cell(
        "## 10. Limitations\n\n"
        "- CMHC variables have different geographic coverage.\n"
        "- Suppressed and unavailable values reduce sample sizes for some analyses.\n"
        "- The affordability indicator is ecological rather than household-level.\n"
        "- The analysis is cross-sectional and observational.\n"
        "- The Manitoba rural/small-centre benchmark uses a much smaller sample and a different geographic scale."
    )
]

notebook["cells"] = cells

notebook_path = project_root / "notebooks" / "01_winnipeg_rental_market_analysis.ipynb"

with open(notebook_path, "w", encoding="utf-8") as f:
    nbf.write(notebook, f)

print("Notebook created successfully:")
print(notebook_path)
print("Cells:", len(notebook["cells"]))

# %%
import nbformat
from pathlib import Path

notebook_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "notebooks/01_winnipeg_rental_market_analysis.ipynb"
)

nb = nbformat.read(notebook_path, as_version=4)

markdown_text = "\n".join(
    cell["source"]
    for cell in nb.cells
    if cell.cell_type == "markdown"
)

print("Notebook QA")
print("-" * 50)
print("Exists:", notebook_path.exists())
print("Cells:", len(nb.cells))
print("Code cells:", sum(c.cell_type == "code" for c in nb.cells))
print("Markdown cells:", sum(c.cell_type == "markdown" for c in nb.cells))
print("Valid notebook:", True)

print("\nRequired sections:")
sections = [
    "Research Question",
    "Data Sources",
    "Data Quality",
    "Rental Market Descriptives",
    "Market Affordability Indicator",
    "Correlation Analysis",
    "Multivariable Rent Model",
    "Model Diagnostics",
    "Interpretation",
    "Limitations",
]

for section in sections:
    print(f"{section}: {'FOUND' if section in markdown_text else 'MISSING'}")

# %%
import pandas as pd
from pathlib import Path

data_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "data/processed/winnipeg_ct_rental_market_analytical.csv"
)

df_check = pd.read_csv(data_path)

required_columns = [
    "ct_id",
    "units_total",
    "rent_total",
    "vacancy_total",
    "median_household_income_2020"
]

missing_columns = [
    col for col in required_columns
    if col not in df_check.columns
]

print("Reproducibility data check")
print("-" * 50)
print("Rows:", len(df_check))
print("Columns:", len(df_check.columns))
print("Missing required columns:", missing_columns)
print("All required columns present:", len(missing_columns) == 0)

# %%
from pathlib import Path
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "winnipeg_ct_rental_market_analytical.csv"
)

df = pd.read_csv(DATA_PATH)

print("Winnipeg Rental Market Intelligence")
print("-" * 50)
print(f"Dataset: {DATA_PATH.name}")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns):,}")
print(f"Unique census tracts: {df['ct_id'].nunique():,}")
print(f"Duplicate CT IDs: {df['ct_id'].duplicated().sum():,}")

# %%
import nbformat
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

notebook_path = (
    project_root
    / "notebooks"
    / "01_winnipeg_rental_market_analysis.ipynb"
)

nb = nbformat.read(notebook_path, as_version=4)

# Find the first code cell and replace it with the self-contained loader.
first_code_index = next(
    i for i, cell in enumerate(nb.cells)
    if cell.cell_type == "code"
)

nb.cells[first_code_index]["source"] = """from pathlib import Path
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "winnipeg_ct_rental_market_analytical.csv"
)

df = pd.read_csv(DATA_PATH)

print("Winnipeg Rental Market Intelligence")
print("-" * 50)
print(f"Dataset: {DATA_PATH.name}")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns):,}")
print(f"Unique census tracts: {df['ct_id'].nunique():,}")
print(f"Duplicate CT IDs: {df['ct_id'].duplicated().sum():,}")
"""

# Clear old execution outputs so the repository notebook is clean.
for cell in nb.cells:
    if cell.cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []

nbformat.write(nb, notebook_path)

print("Notebook updated successfully.")
print("Path:", notebook_path)
print("First code cell:", first_code_index)
print("Execution outputs cleared: True")

# %%
import nbformat
from nbclient import NotebookClient
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

notebook_path = (
    project_root
    / "notebooks"
    / "01_winnipeg_rental_market_analysis.ipynb"
)

nb = nbformat.read(notebook_path, as_version=4)

client = NotebookClient(
    nb,
    timeout=300,
    kernel_name="python3"
)

client.execute()

nbformat.write(nb, notebook_path)

print("Clean notebook execution: PASSED")
print("Notebook:", notebook_path)
print("Executed cells:", len(nb.cells))

# %%
import nbformat
from pathlib import Path

notebook_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "notebooks/01_winnipeg_rental_market_analysis.ipynb"
)

nb = nbformat.read(notebook_path, as_version=4)

print("Executed notebook QA")
print("-" * 50)

for i, cell in enumerate(nb.cells, start=1):
    if cell.cell_type == "code":
        output_count = len(cell.get("outputs", []))
        print(
            f"Cell {i:02d} | "
            f"outputs={output_count} | "
            f"status={'OK' if output_count > 0 else 'NO OUTPUT'}"
        )

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

data_dictionary = [
    "# Data Dictionary",
    "",
    "## Winnipeg Census-Tract Rental Market Analytical Dataset",
    "",
    "File: `data/processed/winnipeg_ct_rental_market_analytical.csv`",
    "",
    "| Variable | Description | Unit / Interpretation |",
    "|---|---|---|",
    "| `ct_id` | Winnipeg census tract identifier | Census tract code |",
    "| `geo` | Census tract geography label | Geographic identifier |",
    "| `units_total` | Total rental units in CMHC universe | Units |",
    "| `units_bachelor` | Bachelor rental units | Units |",
    "| `units_1br` | One-bedroom rental units | Units |",
    "| `units_2br` | Two-bedroom rental units | Units |",
    "| `units_3br_plus` | Three-bedroom-plus rental units | Units |",
    "| `share_bachelor` | Bachelor share of rental supply | Proportion |",
    "| `share_1br` | One-bedroom share of rental supply | Proportion |",
    "| `share_2br` | Two-bedroom share of rental supply | Proportion |",
    "| `share_3br_plus` | Three-bedroom-plus share of rental supply | Proportion |",
    "| `rent_bachelor` | Average bachelor rent | Monthly dollars |",
    "| `rent_1br` | Average one-bedroom rent | Monthly dollars |",
    "| `rent_2br` | Average two-bedroom rent | Monthly dollars |",
    "| `rent_3br_plus` | Average three-bedroom-plus rent | Monthly dollars |",
    "| `rent_total` | Total average rent across reported rental units | Monthly dollars |",
    "| `vacancy_bachelor` | Bachelor vacancy rate | Percent |",
    "| `vacancy_1br` | One-bedroom vacancy rate | Percent |",
    "| `vacancy_2br` | Two-bedroom vacancy rate | Percent |",
    "| `vacancy_3br_plus` | Three-bedroom-plus vacancy rate | Percent |",
    "| `vacancy_total` | Total vacancy rate | Percent |",
    "| `median_household_income_2020` | Median household total income for 2020 | 2020 constant dollars |",
    "| `annual_rent_total` | Annualized total average rent | `rent_total × 12` |",
    "| `rent_income_pct` | Annualized rent-to-median-household-income indicator | Percent |",
    "| `affordability_tier` | Relative quartile classification of rent-income indicator | Lower / Moderate / Higher / Highest |",
    "",
    "## Important Interpretation Notes",
    "",
    "### Rental Supply",
    "",
    "Rental-unit counts represent the CMHC Rental Market Survey universe and should not be interpreted as the complete housing stock.",
    "",
    "### Rent",
    "",
    "Average rents are monthly rental-market measures. Suppressed or unavailable observations remain missing.",
    "",
    "### Vacancy",
    "",
    "Vacancy rates are reported as percentages. Missing or suppressed observations are not converted to zero.",
    "",
    "### Household Income",
    "",
    "The income variable represents median household total income for 2020 from the 2021 Census, expressed in 2020 constant dollars.",
    "",
    "### Rent-to-Income Indicator",
    "",
    "The project calculates:",
    "",
    "**Annualized total average rent / median household income × 100**",
    "",
    "This is an ecological market-level indicator. It is **not** an individual household rent-burden measure.",
    "",
    "### Reliability and Suppression",
    "",
    "CMHC reliability information is retained in the source processing workflow. Suppressed (`**`) and unavailable (`--`) observations are treated as missing rather than zero.",
    ""
]

dictionary_path = project_root / "docs" / "data_dictionary.md"
dictionary_path.write_text(
    "\n".join(data_dictionary),
    encoding="utf-8"
)

print("Data dictionary created successfully.")
print("Path:", dictionary_path)
print("Lines:", len(data_dictionary))

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

sql_doc = [
    "# SQL Analysis Documentation",
    "",
    "## Winnipeg Rental Market Intelligence",
    "",
    "The project uses SQLite to store the integrated census-tract analytical dataset and create reusable analytical views for dashboard reporting.",
    "",
    "## Database",
    "",
    "Primary table:",
    "",
    "`ct_rental_market`",
    "",
    "The table contains the integrated Winnipeg census-tract rental-market dataset.",
    "",
    "## Analytical Views",
    "",
    "### `vw_dashboard`",
    "",
    "Tract-level dashboard view containing:",
    "",
    "- Census tract identifier",
    "- Rental supply",
    "- Bedroom composition",
    "- Average rents",
    "- Vacancy rates",
    "- Median household income",
    "- Annualized rent",
    "- Rent-to-income indicator",
    "- Relative affordability tier",
    "",
    "The view contains 187 census tracts.",
    "",
    "### `vw_dashboard_kpis`",
    "",
    "Provides aggregate dashboard metrics such as average rental supply, rent, vacancy, and income.",
    "",
    "### `vw_dashboard_kpis_median`",
    "",
    "Provides median-based dashboard metrics used where the median is more representative of the cross-tract distribution.",
    "",
    "## Example Analytical Queries",
    "",
    "### Rental supply distribution",
    "",
    "```sql",
    "SELECT",
    "    COUNT(*) AS tracts,",
    "    AVG(units_total) AS mean_units,",
    "    MIN(units_total) AS min_units,",
    "    MAX(units_total) AS max_units",
    "FROM ct_rental_market",
    "WHERE units_total IS NOT NULL;",
    "```",
    "",
    "### Rental prices by bedroom type",
    "",
    "```sql",
    "SELECT",
    "    AVG(rent_1br) AS avg_1br_rent,",
    "    AVG(rent_2br) AS avg_2br_rent",
    "FROM ct_rental_market",
    "WHERE rent_1br IS NOT NULL",
    "   OR rent_2br IS NOT NULL;",
    "```",
    "",
    "### Highest observed vacancy",
    "",
    "```sql",
    "SELECT",
    "    ct_id,",
    "    vacancy_total,",
    "    rent_total,",
    "    median_household_income_2020",
    "FROM ct_rental_market",
    "WHERE vacancy_total IS NOT NULL",
    "ORDER BY vacancy_total DESC",
    "LIMIT 10;",
    "```",
    "",
    "### Rent-to-income indicator",
    "",
    "```sql",
    "SELECT",
    "    ct_id,",
    "    rent_total,",
    "    median_household_income_2020,",
    "    rent_total * 12.0",
    "        / median_household_income_2020 * 100 AS rent_income_pct",
    "FROM ct_rental_market",
    "WHERE rent_total IS NOT NULL",
    "  AND median_household_income_2020 IS NOT NULL;",
    "```",
    "",
    "## SQL Design Principles",
    "",
    "- Preserve missing values rather than converting them to zero.",
    "- Keep the integrated tract-level table as the analytical source of truth.",
    "- Use views for reusable dashboard calculations.",
    "- Keep transformations transparent and reproducible.",
    "- Report sample sizes for analyses affected by missing CMHC observations.",
    ""
]

sql_doc_path = project_root / "sql" / "README.md"

sql_doc_path.write_text(
    "\n".join(sql_doc),
    encoding="utf-8"
)

print("SQL documentation created successfully.")
print("Path:", sql_doc_path)
print("Lines:", len(sql_doc))

# %%
from pathlib import Path

sql_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/sql/README.md"
)

text = sql_path.read_text(encoding="utf-8")

checks = {
    "File exists": sql_path.exists(),
    "Database documented": "ct_rental_market" in text,
    "Dashboard view documented": "vw_dashboard" in text,
    "KPI view documented": "vw_dashboard_kpis" in text,
    "Supply query included": "units_total" in text,
    "Vacancy query included": "vacancy_total" in text,
    "Rent-income query included": "rent_income_pct" in text,
    "Missing-value principle included": "missing values" in text,
}

print("SQL documentation QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

report_outline = [
    "# Winnipeg Rental Market Intelligence — Statistical Report",
    "",
    "## 1. Executive Summary",
    "",
    "- Business/research problem",
    "- Data sources",
    "- Primary findings",
    "- Key analytical implications",
    "",
    "## 2. Research Objectives",
    "",
    "- Primary research question",
    "- Supporting questions",
    "- Analytical scope",
    "",
    "## 3. Data Sources and Study Design",
    "",
    "- CMHC Rental Market Survey",
    "- Statistics Canada Census",
    "- Winnipeg census-tract geography",
    "- Manitoba rural/small-centre benchmark",
    "",
    "## 4. Data Preparation and Quality",
    "",
    "- Source-file ingestion",
    "- Standardization",
    "- Missing values",
    "- Suppression codes",
    "- Reliability indicators",
    "- Dataset integration",
    "- Analytical coverage",
    "",
    "## 5. Descriptive Analysis",
    "",
    "### 5.1 Rental Supply",
    "",
    "### 5.2 Bedroom Composition",
    "",
    "### 5.3 Rental Prices",
    "",
    "### 5.4 Vacancy",
    "",
    "### 5.5 Household Income",
    "",
    "## 6. Rental Prices and Income",
    "",
    "- Pearson correlation",
    "- Spearman correlation",
    "- Interpretation",
    "- Statistical limitations",
    "",
    "## 7. Market Affordability Indicator",
    "",
    "- Indicator definition",
    "- Distribution",
    "- Relationship with income",
    "- Interpretation",
    "- Why this is not household-level affordability",
    "",
    "## 8. Rental Supply and Market Affordability",
    "",
    "- Bivariate association",
    "- Multivariable model",
    "- Coefficient interpretation",
    "- Model fit",
    "- Diagnostics",
    "- Influence and sensitivity analysis",
    "",
    "## 9. Rental Price Model",
    "",
    "- Model specification",
    "- Coefficient estimates",
    "- R-squared",
    "- Prediction error",
    "- Multicollinearity",
    "- Influential observations",
    "- Sensitivity analysis",
    "",
    "## 10. Vacancy and Market Pressure",
    "",
    "- Vacancy distribution",
    "- Rent-vacancy association",
    "- Income-vacancy association",
    "- Outlier sensitivity analysis",
    "",
    "## 11. Manitoba Benchmark",
    "",
    "- Winnipeg versus rural/small-centre rents",
    "- Winnipeg versus rural/small-centre vacancy",
    "- Sample-size limitations",
    "- Geographic-scale limitations",
    "",
    "## 12. Business Interpretation",
    "",
    "- What the analysis suggests",
    "- What decision-makers could monitor",
    "- What the analysis cannot establish",
    "",
    "## 13. Limitations",
    "",
    "- Cross-sectional design",
    "- Missing CMHC observations",
    "- Suppression",
    "- Ecological affordability indicator",
    "- Geographic differences",
    "- Observational rather than causal inference",
    "",
    "## 14. Conclusion",
    "",
    "- Main findings",
    "- Analytical contribution",
    "- Potential future work",
    "",
    "## Appendix A — Statistical Results",
    "",
    "## Appendix B — Data Dictionary",
    "",
    "## Appendix C — Reproducibility",
    "",
    "- Repository structure",
    "- Python environment",
    "- SQL database",
    "- Dashboard outputs",
]

outline_path = project_root / "reports" / "statistical_report_outline.md"

outline_path.write_text(
    "\n".join(report_outline),
    encoding="utf-8"
)

print("Statistical report outline created successfully.")
print("Path:", outline_path)
print("Sections:", sum(line.startswith("#") for line in report_outline))

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

executive_summary = [
    "# Executive Summary",
    "",
    "Winnipeg's rental market varies substantially across census tracts in terms of rental supply, average rents, vacancy, and the relationship between rental costs and local household income.",
    "",
    "This project integrates Canada Mortgage and Housing Corporation (CMHC) Rental Market Survey data with 2021 Census household-income data from Statistics Canada to examine these patterns at the census-tract level.",
    "",
    "The integrated analytical dataset contains **187 Winnipeg census tracts and 25 analytical variables**. Because CMHC reporting coverage varies across rental-market measures, individual analyses use the observations available for the relevant variables rather than restricting the entire project to a single complete-case sample.",
    "",
    "### Key Findings",
    "",
    "1. **Rental prices are positively associated with household income.** Among 77 census tracts with usable total-rent and income observations, the Pearson correlation was **r = 0.577** and the Spearman correlation was **rho = 0.498**. Higher-income areas therefore tend to have higher average rents.",
    "",
    "2. **Higher-income areas tend to have lower relative rental-cost indicators.** The annualized total-rent-to-median-household-income indicator had a median value of **19.3%** across 77 observations and was negatively associated with household income (**Spearman rho = -0.506**). This indicates that higher-income areas generally have higher rents but rental costs represent a smaller share of median household income.",
    "",
    "3. **Rental supply is concentrated geographically.** Among 135 census tracts with usable supply data, median rental supply was **223 units per tract**, with a maximum of **954 units**. Approximately **91%** of observed rental units were 1- or 2-bedroom units.",
    "",
    "4. **Vacancy is low in most observed census tracts but varies considerably.** Among 57 tracts with usable total vacancy data, median vacancy was **0.7%**, while the maximum observed value was **26.0%**. The 26% observation was retained because it is a legitimate reported value and was assessed through sensitivity analysis rather than arbitrarily removed.",
    "",
    "5. **The multivariable rent model explains substantial cross-tract variation.** A model using log-transformed rental supply and median household income explained approximately **68% of the variation in total average rent** across 59 census tracts (**R2 = 0.678; adjusted R2 = 0.666**). Mean absolute error was approximately **$138** and RMSE was approximately **$166**.",
    "",
    "6. **The model relationships are observational.** Larger rental inventories and higher median household income are positively associated with total average rent after accounting for the other predictor. These coefficients should not be interpreted as causal effects.",
    "",
    "7. **Winnipeg rents are higher than the selected rural/small-centre benchmark.** The Winnipeg census-tract median total average rent was **$1,124**, compared with **$848** among 10 Manitoba rural/small-centre CSDs with usable observations. The rural/small-centre median was approximately **24.6% lower**.",
    "",
    "### Business Interpretation",
    "",
    "The analysis suggests that Winnipeg's rental market should not be evaluated using rent alone. Rental prices, rental supply, vacancy, and local income provide different perspectives on market conditions.",
    "",
    "In particular, the results show why a high-rent area is not necessarily the least affordable area when rental costs are evaluated relative to local median household income. Conversely, lower-rent areas can have higher relative rental-cost indicators when local household incomes are substantially lower.",
    "",
    "For analysts and decision-makers, this supports monitoring rental-market conditions using multiple indicators rather than relying on a single citywide average.",
    "",
    "### Important Caveat",
    "",
    "The rent-to-income measure is an **ecological market indicator**, not a household-level affordability or rent-burden measure. It combines area-level average market rent with area-level median household income and should therefore be interpreted as a geographic comparison rather than evidence about individual households.",
]

summary_path = (
    project_root
    / "reports"
    / "executive_summary.md"
)

summary_path.write_text(
    "\n".join(executive_summary),
    encoding="utf-8"
)

print("Executive Summary created successfully.")
print("Path:", summary_path)
print("Lines:", len(executive_summary))

# %%
from pathlib import Path

summary_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/executive_summary.md"
)

text = summary_path.read_text(encoding="utf-8")

checks = {
    "File exists": summary_path.exists(),
    "187 tracts": "187 Winnipeg census tracts" in text,
    "Rent-income correlation": "0.577" in text and "0.498" in text,
    "Affordability correlation": "-0.506" in text,
    "Median supply": "223 units" in text,
    "Median vacancy": "0.7%" in text,
    "Rent model R2": "0.678" in text,
    "Model MAE": "$138" in text,
    "Winnipeg benchmark": "$1,124" in text,
    "Rural benchmark": "$848" in text,
    "24.6% benchmark difference": "24.6% lower" in text,
    "Ecological indicator caveat": "ecological market indicator" in text,
    "Causal caveat": "not be interpreted as causal" in text,
}

print("Executive Summary QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

section = [
    "## 6. Rental Prices and Income",
    "",
    "### 6.1 Objective",
    "",
    "This analysis examines whether census tracts with higher median household income also tend to have higher average rental prices.",
    "",
    "The analysis focuses on total average monthly rent and median household total income for 2020. Because both measures are aggregated at the census-tract level, the results describe geographic associations rather than individual household behaviour.",
    "",
    "### 6.2 Sample",
    "",
    "There are **77 Winnipeg census tracts** with non-missing observations for both total average rent and median household income.",
    "",
    "The remaining census tracts are not treated as zero-rent observations. CMHC suppression and availability codes are retained as missing during data preparation.",
    "",
    "### 6.3 Correlation Results",
    "",
    "The Pearson correlation between total average rent and median household income is **r = 0.577**, indicating a moderately strong positive linear association.",
    "",
    "The Spearman rank correlation is **rho = 0.498**, also indicating a positive monotonic association.",
    "",
    "Both relationships are statistically significant.",
    "",
    "The two correlation measures provide complementary evidence. Pearson correlation assesses linear association, while Spearman correlation assesses whether higher values of one variable generally correspond to higher values of the other without requiring the relationship to be strictly linear.",
    "",
    "### 6.4 Interpretation",
    "",
    "The results indicate that higher-income Winnipeg census tracts tend to have higher average rental prices.",
    "",
    "This does not mean that household income causes rents to be higher. Census tracts differ in many characteristics that are not captured by this bivariate analysis, including housing composition, neighbourhood characteristics, and rental-market structure.",
    "",
    "The finding is therefore best interpreted as a **cross-sectional geographic association**.",
    "",
    "### 6.5 Analytical Implication",
    "",
    "A citywide rental-price statistic can conceal important geographic differences. The positive rent-income relationship demonstrates why rental-market analysis benefits from considering local economic context alongside rental prices.",
    "",
    "The next section extends this analysis by examining rental costs relative to median household income using a market-level affordability indicator."
]

section_path = (
    project_root
    / "reports"
    / "section_06_rental_prices_income.md"
)

section_path.write_text(
    "\n".join(section),
    encoding="utf-8"
)

print("Section 6 created successfully.")
print("Path:", section_path)
print("Lines:", len(section))

# %%
from pathlib import Path

section_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/section_06_rental_prices_income.md"
)

text = section_path.read_text(encoding="utf-8")

checks = {
    "File exists": section_path.exists(),
    "77-tract sample": "77 Winnipeg census tracts" in text,
    "Pearson r": "0.577" in text,
    "Spearman rho": "0.498" in text,
    "Statistical significance": "statistically significant" in text,
    "Geographic interpretation": "geographic associations" in text,
    "No causal claim": "does not mean that household income causes" in text,
    "Next-section transition": "affordability indicator" in text,
}

print("Section 6 QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

section = [
    "## 7. Market Affordability Indicator",
    "",
    "### 7.1 Indicator Definition",
    "",
    "To place rental prices in the context of local household income, the project calculates an annualized rent-to-median-household-income indicator:",
    "",
    "**Annualized total average rent / median household income × 100**",
    "",
    "For example, a value of 20% means that annualized average market rent is equivalent to 20% of the area's median household income.",
    "",
    "This measure is intended for **geographic market comparison**, not as a measure of an individual household's actual rent burden.",
    "",
    "### 7.2 Distribution",
    "",
    "The indicator can be calculated for **77 Winnipeg census tracts** with both total average rent and median household income available.",
    "",
    "Across these observations:",
    "",
    "- Mean indicator: **19.95%**",
    "- Median indicator: **19.32%**",
    "- First quartile: **16.39%**",
    "- Third quartile: **22.67%**",
    "- Minimum: **12.44%**",
    "- Maximum: **32.33%**",
    "",
    "The distribution demonstrates meaningful geographic variation in the relationship between market rents and local household incomes.",
    "",
    "### 7.3 Relative Affordability Tiers",
    "",
    "For descriptive dashboard purposes, census tracts are divided into four groups using the observed quartiles of the indicator:",
    "",
    "- **Lower relative burden**",
    "- **Moderate relative burden**",
    "- **Higher relative burden**",
    "- **Highest relative burden**",
    "",
    "These categories are relative to the Winnipeg census-tract distribution. They are **not formal affordability thresholds** and should not be interpreted as policy-defined affordability classifications.",
    "",
    "### 7.4 Relationship with Household Income",
    "",
    "The Spearman rank correlation between the affordability indicator and median household income is **rho = -0.506**, based on 77 census tracts.",
    "",
    "This indicates that higher-income census tracts generally have lower annualized rent-to-median-household-income indicators.",
    "",
    "Combined with the positive rent-income correlation from Section 6, the result produces an important market pattern: **higher-income areas tend to have higher rents, but rental costs represent a smaller proportion of median household income in those areas**.",
    "",
    "### 7.5 Interpretation",
    "",
    "The result suggests that examining rental prices alone can produce an incomplete picture of geographic affordability. A tract may have relatively high rents while still having a comparatively low rent-to-income indicator because household incomes are also higher.",
    "",
    "Conversely, a tract with lower nominal rents can have a higher relative indicator if local household incomes are substantially lower.",
    "",
    "This distinction is particularly important when comparing neighbourhoods with different socioeconomic profiles.",
    "",
    "### 7.6 Limitation",
    "",
    "The indicator combines an area-level average rental price with an area-level median household income. It does not observe the income or rent paid by the same household.",
    "",
    "It therefore should **not** be described as the percentage of income that households actually spend on rent, nor as a household-level shelter-cost-to-income ratio.",
    "",
    "The measure is best described as an **annualized market rent-to-median-household-income indicator**."
]

section_path = (
    project_root
    / "reports"
    / "section_07_market_affordability.md"
)

section_path.write_text(
    "\n".join(section),
    encoding="utf-8"
)

print("Section 7 created successfully.")
print("Path:", section_path)
print("Lines:", len(section))

# %%
from pathlib import Path

section_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/section_07_market_affordability.md"
)

text = section_path.read_text(encoding="utf-8")

checks = {
    "File exists": section_path.exists(),
    "77-tract sample": "77 Winnipeg census tracts" in text,
    "Mean 19.95%": "19.95%" in text,
    "Median 19.32%": "19.32%" in text,
    "Q1 16.39%": "16.39%" in text,
    "Q3 22.67%": "22.67%" in text,
    "Minimum 12.44%": "12.44%" in text,
    "Maximum 32.33%": "32.33%" in text,
    "Spearman -0.506": "-0.506" in text,
    "Relative tiers identified": "Lower relative burden" in text,
    "Not formal thresholds": "not formal affordability thresholds" in text,
    "Ecological limitation": "area-level average rental price" in text,
    "No household-level claim": "household-level shelter-cost-to-income ratio" in text,
}

print("Section 7 QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

section = [
    "## 8. Rental Supply and Market Affordability",
    "",
    "### 8.1 Objective",
    "",
    "This analysis examines whether rental-market inventory is associated with the annualized rent-to-median-household-income indicator after accounting for local household income.",
    "",
    "The analysis is designed to distinguish the relationship between rental supply and relative rental costs from the separate relationship between income and the affordability indicator.",
    "",
    "### 8.2 Analytical Sample",
    "",
    "The multivariable analysis uses **59 census tracts** with complete observations for total rental supply, total average rent, and median household income.",
    "",
    "The smaller sample reflects the limited availability of tract-level CMHC rent observations. It is used for the regression analysis only and is not treated as representative of all 187 Winnipeg census tracts.",
    "",
    "### 8.3 Descriptive Relationships",
    "",
    "Rental supply has a positive association with the rent-to-income indicator.",
    "",
    "For the 59 complete observations:",
    "",
    "- Pearson correlation between rental supply and the indicator: **r = 0.658**",
    "- Spearman correlation: **rho = 0.639**",
    "",
    "Rental supply is also positively associated with total average rent in this complete-case sample, while its bivariate relationship with median household income is weak and negative.",
    "",
    "### 8.4 Multivariable Model",
    "",
    "An ordinary least squares regression was estimated with the annualized rent-to-median-household-income indicator as the dependent variable and total rental supply plus median household income as explanatory variables.",
    "",
    "The model explained approximately **50% of the cross-tract variation** in the indicator:",
    "",
    "- R-squared: **0.499**",
    "- Adjusted R-squared: **0.481**",
    "- Number of observations: **59**",
    "",
    "The estimated rental-supply coefficient was **0.0084** and statistically significant (**p < 0.001**). The median-income coefficient was **-0.0000517** and was also statistically significant in the primary specification (**p = 0.009**).",
    "",
    "The positive supply coefficient indicates that, conditional on median household income, census tracts with larger rental inventories tend to have higher values of the rent-to-income indicator.",
    "",
    "The negative income coefficient indicates that, conditional on rental supply, higher-income census tracts tend to have lower values of the indicator.",
    "",
    "These are conditional statistical associations and should not be interpreted as causal effects.",
    "",
    "### 8.5 Model Diagnostics",
    "",
    "Diagnostic testing did not identify substantial evidence of non-normal residuals or heteroskedasticity in the primary specification.",
    "",
    "The Shapiro-Wilk test produced **W = 0.977, p = 0.321**, while the Breusch-Pagan test produced **p = 0.301**.",
    "",
    "The Durbin-Watson statistic was approximately **1.63**.",
    "",
    "Variance inflation factors for the two explanatory variables were approximately **1.03**, indicating very little evidence of multicollinearity between rental supply and median household income.",
    "",
    "### 8.6 Influence and Sensitivity Analysis",
    "",
    "Four observations exceeded the project's Cook's-distance screening threshold of **4/n**. These observations were retained in the primary model because their underlying values appeared plausible rather than being obvious data errors.",
    "",
    "As a sensitivity check, all four observations were excluded simultaneously. The resulting model produced an R-squared of **0.501**, compared with **0.499** in the primary model.",
    "",
    "The rental-supply coefficient changed from **0.0084** to approximately **0.0087**, while remaining statistically significant.",
    "",
    "The income coefficient remained negative but was no longer statistically significant after excluding the influential observations (**p = 0.102**).",
    "",
    "This suggests that the positive association between rental supply and the rent-to-income indicator is more robust than the income coefficient in this particular complete-case sample.",
    "",
    "### 8.7 Interpretation",
    "",
    "The analysis does not support the claim that increasing rental supply causes affordability to improve or worsen. Instead, it shows that rental-market inventory is statistically associated with the observed rent-to-income indicator after accounting for local median household income.",
    "",
    "The result should also be interpreted in light of the substantial missingness in tract-level CMHC rent and vacancy data. The 59-tract regression sample represents the subset of Winnipeg census tracts for which all required variables were reported.",
]

section_path = (
    project_root
    / "reports"
    / "section_08_supply_affordability.md"
)

section_path.write_text(
    "\n".join(section),
    encoding="utf-8"
)

print("Section 8 created successfully.")
print("Path:", section_path)
print("Lines:", len(section))

# %%
from pathlib import Path

section_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/section_08_supply_affordability.md"
)

text = section_path.read_text(encoding="utf-8")

checks = {
    "File exists": section_path.exists(),
    "59-tract sample": "59 census tracts" in text,
    "Pearson 0.658": "0.658" in text,
    "Spearman 0.639": "0.639" in text,
    "R-squared 0.499": "0.499" in text,
    "Adjusted R-squared 0.481": "0.481" in text,
    "Supply coefficient": "0.0084" in text,
    "Income coefficient": "-0.0000517" in text,
    "Supply significance": "p < 0.001" in text,
    "Shapiro-Wilk": "W = 0.977, p = 0.321" in text,
    "Breusch-Pagan": "p = 0.301" in text,
    "VIF": "1.03" in text,
    "Cook threshold": "4/n" in text,
    "Sensitivity R-squared": "0.501" in text,
    "Sensitivity supply coefficient": "0.0087" in text,
    "Sensitivity income p-value": "p = 0.102" in text,
    "Causal caveat": "should not be interpreted as causal" in text,
}

print("Section 8 QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

section = [
    "## 9. Rental Price Model",
    "",
    "### 9.1 Objective",
    "",
    "The rental-price model examines which tract-level characteristics are associated with differences in total average monthly rent.",
    "",
    "The model uses median household income and the logarithm of total rental supply as explanatory variables. The log transformation reduces the influence of very large rental inventories and provides a more appropriate functional form for the highly right-skewed supply variable.",
    "",
    "### 9.2 Model Specification",
    "",
    "The estimated ordinary least squares model is:",
    "",
    "**Total average rent = -702.91 + 168.75 × log(rental supply + 1) + 0.0112 × median household income + error**",
    "",
    "The model is estimated using **59 census tracts** with complete observations for total rent, rental supply, and median household income.",
    "",
    "### 9.3 Model Fit",
    "",
    "The model explains approximately **68% of the cross-tract variation in total average rent**:",
    "",
    "- R-squared: **0.678**",
    "- Adjusted R-squared: **0.666**",
    "- F-statistic: **58.87**",
    "- Model p-value: **1.71 × 10^-14**",
    "",
    "Out-of-sample prediction is not claimed because the analysis is primarily explanatory and uses a relatively small cross-sectional sample.",
    "",
    "Within the observed sample, mean absolute error was approximately **$138**, while root mean squared error was approximately **$166**.",
    "",
    "### 9.4 Coefficient Interpretation",
    "",
    "The coefficient on log rental supply was **168.75** and statistically significant.",
    "",
    "Because supply is log-transformed, this coefficient should not be interpreted as an additional $168.75 of rent for every additional rental unit. Instead, the result indicates that census tracts with larger rental-market inventories tend to have higher average rents after accounting for median household income.",
    "",
    "Median household income had a coefficient of approximately **0.0112** and was statistically significant.",
    "",
    "Holding logged rental supply constant, a **$10,000 difference in median household income corresponds to approximately a $112 difference in predicted monthly total average rent**.",
    "",
    "Both coefficients represent conditional associations rather than causal effects.",
    "",
    "### 9.5 Multicollinearity",
    "",
    "Variance inflation factors were approximately **1.01** for both explanatory variables.",
    "",
    "This provides little evidence of problematic multicollinearity between logged rental supply and median household income.",
    "",
    "The large condition number reported by the regression software is primarily attributable to differences in variable scale, particularly the dollar-valued income variable, rather than strong correlation between the predictors.",
    "",
    "### 9.6 Model Diagnostics",
    "",
    "The residual diagnostics did not indicate substantial departures from normality.",
    "",
    "The Jarque-Bera test produced **p = 0.609**, with residual skewness of approximately **0.031** and kurtosis of approximately **2.37**.",
    "",
    "The Durbin-Watson statistic was approximately **1.68**.",
    "",
    "These diagnostics provide reasonable support for the primary OLS specification, while the cross-sectional geographic structure means that the results should still be interpreted cautiously.",
    "",
    "### 9.7 Influence Analysis",
    "",
    "Using a Cook's-distance screening threshold of **4/n**, one observation was identified as influential: census tract **0110.06**.",
    "",
    "The observation was retained in the primary model because its rent, rental supply, and income values appeared plausible rather than representing an obvious data error.",
    "",
    "A sensitivity model excluding this observation produced:",
    "",
    "- R-squared: **0.699**, compared with 0.678 in the primary model",
    "- Logged supply coefficient: **169.61**, compared with 168.75",
    "- Income coefficient: **0.0120**, compared with 0.0112",
    "",
    "The supply coefficient changed by approximately **0.5%**, while the income coefficient changed by approximately **7.2%**.",
    "",
    "Both explanatory variables remained statistically significant in the sensitivity model.",
    "",
    "The results therefore suggest that the primary model's substantive conclusions are not dependent on the single influential observation.",
    "",
    "### 9.8 Interpretation",
    "",
    "The model provides evidence that rental supply and local household income are both associated with cross-tract differences in average rental prices.",
    "",
    "The relatively high R-squared indicates that these two variables capture a substantial portion of the observed geographic variation, but it should not be interpreted as proof that they determine rental prices.",
    "",
    "Other factors—including neighbourhood characteristics, building age, housing quality, location, and broader market conditions—may also contribute to differences in rental prices and are not included in this model.",
]

section_path = (
    project_root
    / "reports"
    / "section_09_rental_price_model.md"
)

section_path.write_text(
    "\n".join(section),
    encoding="utf-8"
)

print("Section 9 created successfully.")
print("Path:", section_path)
print("Lines:", len(section))

# %%
from pathlib import Path

section_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/section_09_rental_price_model.md"
)

text = section_path.read_text(encoding="utf-8")

checks = {
    "File exists": section_path.exists(),
    "59-tract sample": "59 census tracts" in text,
    "Model specification": "168.75" in text and "0.0112" in text,
    "R-squared": "0.678" in text,
    "Adjusted R-squared": "0.666" in text,
    "F-statistic": "58.87" in text,
    "MAE": "$138" in text,
    "RMSE": "$166" in text,
    "Supply interpretation": "should not be interpreted as an additional $168.75" in text,
    "Income interpretation": "$10,000 difference in median household income" in text,
    "VIF": "1.01" in text,
    "Jarque-Bera": "p = 0.609" in text,
    "Cook threshold": "4/n" in text,
    "Influential CT": "0110.06" in text,
    "Sensitivity R-squared": "0.699" in text,
    "Sensitivity supply coefficient": "169.61" in text,
    "Sensitivity income coefficient": "0.0120" in text,
    "Causal caveat": "conditional associations rather than causal effects" in text,
}

print("Section 9 QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

section = [
    "## 10. Vacancy and Market Pressure",
    "",
    "### 10.1 Objective",
    "",
    "Vacancy provides a complementary view of rental-market conditions. While rent measures the price of available rental housing, vacancy indicates the proportion of surveyed rental units that were unoccupied and available within the CMHC Rental Market Survey universe.",
    "",
    "This section examines the distribution of vacancy across Winnipeg census tracts and its association with rental prices and local household income.",
    "",
    "### 10.2 Vacancy Distribution",
    "",
    "Total vacancy is available for **57 of the 187 Winnipeg census tracts** in the integrated dataset.",
    "",
    "Among these observations:",
    "",
    "- Mean vacancy: **1.82%**",
    "- Median vacancy: **0.70%**",
    "- First quartile: **0.40%**",
    "- Third quartile: **1.80%**",
    "- Maximum vacancy: **26.0%**",
    "",
    "The distribution is therefore highly concentrated at relatively low vacancy rates, with a small number of tracts reporting substantially higher values.",
    "",
    "### 10.3 Highest Observed Vacancy",
    "",
    "The highest reported total vacancy rate is **26.0%** in census tract **0538.00**.",
    "",
    "This observation corresponds to 96 rental units in the CMHC supply data, a total average rent of $1,097, and median household income of $90,000.",
    "",
    "The observation is retained in the primary analysis because it is a reported market value rather than an identified data-entry error.",
    "",
    "### 10.4 Vacancy and Rental Prices",
    "",
    "Among **54 census tracts** with complete total vacancy, total rent, and income observations, the Spearman correlation between vacancy and total average rent is **rho = -0.328 (p = 0.015)**.",
    "",
    "This indicates that higher-rent tracts tend to have lower observed vacancy rates within the available sample.",
    "",
    "The relationship should be interpreted as an association rather than evidence that higher rents cause lower vacancy.",
    "",
    "### 10.5 Vacancy and Household Income",
    "",
    "Among the **57 tracts** with usable total vacancy and income data, the Spearman correlation between vacancy and median household income is **rho = -0.371 (p = 0.0045)**.",
    "",
    "Higher-income census tracts therefore tend to have lower observed vacancy rates in the available data.",
    "",
    "This relationship remains present when the 26% vacancy observation in CT 0538.00 is excluded: the Spearman correlation becomes approximately **rho = -0.415 (p = 0.0015)**.",
    "",
    "### 10.6 Sensitivity Analysis",
    "",
    "The 26% observation is potentially influential because it is substantially larger than the rest of the observed vacancy distribution.",
    "",
    "Rather than removing it from the primary dataset, the analysis evaluates its influence through sensitivity testing.",
    "",
    "For the vacancy-income relationship, excluding CT 0538.00 changes the Spearman correlation from **-0.371 to -0.415**, while statistical significance remains strong.",
    "",
    "For the vacancy-rent relationship, excluding the observation changes the Spearman correlation from **-0.328 to approximately -0.314**, with the relationship remaining statistically significant.",
    "",
    "These results indicate that the broad negative associations are not dependent on the single highest-vacancy observation.",
    "",
    "### 10.7 Interpretation",
    "",
    "The observed vacancy pattern suggests that Winnipeg's rental-market conditions differ across census tracts. Most observed tracts have relatively low vacancy, while a small number have substantially higher vacancy.",
    "",
    "The negative associations with rent and income suggest that higher-rent and higher-income areas generally have lower observed vacancy in the available sample.",
    "",
    "However, vacancy coverage is limited to 57 of 187 tracts. The analysis therefore describes the reported CMHC observations rather than estimating vacancy for all Winnipeg census tracts.",
    "",
    "### 10.8 Analytical Limitation",
    "",
    "The vacancy results should not be interpreted as a complete measure of rental-market pressure across Winnipeg. CMHC survey coverage, suppression, and the structure of the Rental Market Survey universe limit the geographic coverage of the measure.",
    "",
    "Missing vacancy observations are retained as missing throughout the analysis rather than being interpreted as zero vacancy."
]

section_path = (
    project_root
    / "reports"
    / "section_10_vacancy_market_pressure.md"
)

section_path.write_text(
    "\n".join(section),
    encoding="utf-8"
)

print("Section 10 created successfully.")
print("Path:", section_path)
print("Lines:", len(section))

# %%
from pathlib import Path

section_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/section_10_vacancy_market_pressure.md"
)

text = section_path.read_text(encoding="utf-8")

checks = {
    "File exists": section_path.exists(),
    "57-tract vacancy sample": "57 of the 187 Winnipeg census tracts" in text,
    "Median vacancy": "0.70%" in text,
    "Mean vacancy": "1.82%" in text,
    "Maximum vacancy": "26.0%" in text,
    "Highest vacancy CT": "0538.00" in text,
    "Rent-vacancy correlation": "-0.328 (p = 0.015)" in text,
    "Income-vacancy correlation": "-0.371 (p = 0.0045)" in text,
    "Income sensitivity": "-0.415 (p = 0.0015)" in text,
    "Rent sensitivity": "-0.314" in text,
    "Outlier retained": "retained in the primary analysis" in text,
    "Missing values preserved": "retained as missing" in text,
    "Coverage limitation": "57 of 187 tracts" in text,
    "No causal claim": "rather than evidence that higher rents cause lower vacancy" in text,
}

print("Section 10 QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

section = [
    "## 11. Manitoba Benchmark",
    "",
    "### 11.1 Objective",
    "",
    "To provide geographic context for the Winnipeg results, the project compares selected Winnipeg census-tract rental-market statistics with a secondary benchmark consisting of Manitoba rural and small-centre census subdivision (CSD) observations.",
    "",
    "The rural/small-centre benchmark is descriptive and is not intended to represent all rental housing outside Winnipeg.",
    "",
    "### 11.2 Rental Prices",
    "",
    "The median total average rent among Winnipeg census tracts with usable observations is **$1,124 per month**.",
    "",
    "The corresponding median among the selected Manitoba rural/small-centre CSD observations is **$848 per month**.",
    "",
    "The rural/small-centre benchmark is therefore approximately **24.6% lower** than the Winnipeg census-tract median.",
    "",
    "This difference provides a useful descriptive indication of the rental-price gap between Winnipeg and the selected smaller Manitoba markets.",
    "",
    "### 11.3 Vacancy",
    "",
    "The median observed total vacancy rate is **0.70%** among Winnipeg census tracts with usable vacancy data.",
    "",
    "The corresponding median among the selected Manitoba rural/small-centre CSD observations is **0.85%**.",
    "",
    "The rural/small-centre benchmark is therefore approximately **0.15 percentage points higher** than the Winnipeg census-tract median.",
    "",
    "The difference should not be interpreted as statistically significant because this benchmarking exercise is descriptive and the available sample sizes are small.",
    "",
    "### 11.4 Sample Coverage",
    "",
    "The Winnipeg rent comparison is based on **77 census tracts**, while the rural/small-centre rent comparison is based on only **10 CSD observations** with usable total-rent values.",
    "",
    "For vacancy, the comparison uses **57 Winnipeg census tracts** and **8 rural/small-centre CSD observations**.",
    "",
    "These differences in sample size substantially limit the strength of any generalization from the benchmark.",
    "",
    "### 11.5 Geographic Comparability",
    "",
    "The Winnipeg analysis is conducted at the census-tract level within a large urban rental market, while the rural/small-centre benchmark uses census subdivisions representing smaller markets.",
    "",
    "The two geographic systems therefore should not be treated as perfectly equivalent analytical units.",
    "",
    "The benchmark is used to provide context rather than to establish a causal or population-level estimate of the difference between urban and rural rental markets.",
    "",
    "### 11.6 Interpretation",
    "",
    "The benchmark indicates that observed rental prices are materially lower in the selected Manitoba rural/small-centre markets than in Winnipeg.",
    "",
    "At the same time, the observed vacancy medians are relatively close, with the rural/small-centre benchmark slightly higher.",
    "",
    "Taken together, these descriptive results reinforce the importance of considering both rental prices and vacancy when comparing rental-market conditions across geographic contexts.",
    "",
    "### 11.7 Limitation",
    "",
    "The rural/small-centre benchmark is based only on observations with usable CMHC values and should not be interpreted as a complete estimate of Manitoba's non-Winnipeg rental market.",
    "",
    "The benchmark also uses different geographic scales and survey contexts from the Winnipeg census-tract analysis. It is therefore best presented as a **descriptive comparison**, not as formal statistical inference."
]

section_path = (
    project_root
    / "reports"
    / "section_11_manitoba_benchmark.md"
)

section_path.write_text(
    "\n".join(section),
    encoding="utf-8"
)

print("Section 11 created successfully.")
print("Path:", section_path)
print("Lines:", len(section))


# %%
from pathlib import Path

section_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/section_11_manitoba_benchmark.md"
)

text = section_path.read_text(encoding="utf-8")

checks = {
    "File exists": section_path.exists(),
    "Winnipeg median rent": "$1,124" in text,
    "Rural median rent": "$848" in text,
    "Rent difference": "24.6% lower" in text,
    "Winnipeg vacancy median": "0.70%" in text,
    "Rural vacancy median": "0.85%" in text,
    "Vacancy difference": "0.15 percentage points higher" in text,
    "Winnipeg rent sample": "77 census tracts" in text,
    "Rural rent sample": "10 CSD observations" in text,
    "Winnipeg vacancy sample": "57 Winnipeg census tracts" in text,
    "Rural vacancy sample": "8 rural/small-centre CSD observations" in text,
    "Descriptive comparison": "descriptive comparison" in text,
    "Small-sample caveat": "sample sizes are small" in text,
    "Geographic-scale caveat": "different geographic scales" in text,
    "No formal inference": "not as formal statistical inference" in text,
}

print("Section 11 QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")


# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

section = [
    "## 12. Business Interpretation",
    "",
    "### 12.1 Why a Multi-Indicator View Matters",
    "",
    "The analysis demonstrates that Winnipeg's rental market cannot be adequately described using a single rental-price statistic.",
    "",
    "Rental prices, rental supply, vacancy, and household income capture different dimensions of the market. Examining them together provides a more informative view of geographic differences in rental-market conditions.",
    "",
    "### 12.2 Rental Price and Local Economic Context",
    "",
    "Higher-income census tracts tend to have higher average rents. The positive rent-income relationship indicates that nominal rent comparisons should be interpreted alongside local economic conditions.",
    "",
    "A high-rent area is therefore not automatically the least affordable area when rental costs are considered relative to local median household income.",
    "",
    "### 12.3 Relative Rental-Cost Pressure",
    "",
    "The market affordability indicator provides a second perspective on rental costs.",
    "",
    "The negative relationship between the indicator and household income shows that areas with higher household incomes generally have lower relative rental-cost indicators, despite tending to have higher nominal rents.",
    "",
    "This suggests that decision-makers interested in rental-market pressure should monitor both the level of rent and the economic context in which those rents occur.",
    "",
    "### 12.4 Rental Supply",
    "",
    "Rental supply is geographically concentrated. The median observed rental inventory is 223 units per census tract, while the largest observed tract contains 954 units.",
    "",
    "Approximately 91% of observed rental units are either one- or two-bedroom units.",
    "",
    "This composition suggests that the one- and two-bedroom segments are particularly important when evaluating the structure of Winnipeg's purpose-built rental-market inventory.",
    "",
    "### 12.5 Vacancy and Market Conditions",
    "",
    "Most observed census tracts have relatively low vacancy, although the distribution includes substantial geographic variation.",
    "",
    "The negative associations between vacancy and both rent and household income suggest that vacancy should be monitored alongside price and income rather than interpreted independently.",
    "",
    "The limited geographic coverage of tract-level vacancy data means that these findings should be treated as evidence about the observed CMHC sample rather than the entire Winnipeg market.",
    "",
    "### 12.6 Potential Analytical Uses",
    "",
    "The integrated dataset and dashboard could support several recurring analytical tasks:",
    "",
    "- Identifying census tracts with relatively high rental costs.",
    "- Comparing rental prices with local household-income conditions.",
    "- Monitoring the geographic concentration and bedroom composition of rental supply.",
    "- Identifying areas with unusually high or low observed vacancy.",
    "- Benchmarking Winnipeg rental prices against selected smaller Manitoba markets.",
    "- Prioritizing locations for deeper investigation using additional neighbourhood or housing-market data.",
    "",
    "### 12.7 What the Analysis Does Not Establish",
    "",
    "The results do not establish that rental supply causes rents to increase or decrease, that household income causes rents or vacancy to change, or that a particular neighbourhood is objectively affordable or unaffordable for individual households.",
    "",
    "The analysis is observational and cross-sectional. The statistical relationships should therefore be interpreted as associations that can motivate further investigation rather than as causal estimates.",
    "",
    "### 12.8 Decision-Making Implication",
    "",
    "The strongest practical conclusion is that rental-market monitoring benefits from an integrated framework.",
    "",
    "A useful market-monitoring system should combine **price, supply, vacancy, and local income context**, while explicitly reporting data coverage and uncertainty.",
    "",
    "The project's dashboard is designed around this principle by presenting the four dimensions separately and then connecting them through statistical analysis."
]

section_path = (
    project_root
    / "reports"
    / "section_12_business_interpretation.md"
)

section_path.write_text(
    "\n".join(section),
    encoding="utf-8"
)

print("Section 12 created successfully.")
print("Path:", section_path)
print("Lines:", len(section))

# %%
from pathlib import Path

section_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/section_12_business_interpretation.md"
)

text = section_path.read_text(encoding="utf-8")

checks = {
    "File exists": section_path.exists(),
    "Multi-indicator framework": "single rental-price statistic" in text,
    "Rent-income interpretation": "Higher-income census tracts tend to have higher average rents" in text,
    "Affordability interpretation": "lower relative rental-cost indicators" in text,
    "Median supply": "223 units per census tract" in text,
    "Bedroom composition": "91% of observed rental units" in text,
    "Vacancy interpretation": "Most observed census tracts have relatively low vacancy" in text,
    "Analytical uses": "Potential Analytical Uses" in text,
    "No causal claim": "do not establish that rental supply causes" in text,
    "Cross-sectional limitation": "observational and cross-sectional" in text,
    "Decision framework": "price, supply, vacancy, and local income context" in text,
}

print("Section 12 QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

section = [
    "## 13. Limitations",
    "",
    "### 13.1 Cross-Sectional Design",
    "",
    "The primary analysis is cross-sectional, using rental-market and household-income measures associated with Winnipeg census tracts. The analysis therefore identifies geographic associations at a point in time rather than estimating changes over time or causal effects.",
    "",
    "The regression coefficients should not be interpreted as causal effects of rental supply or income on rental prices or affordability.",
    "",
    "### 13.2 Incomplete CMHC Coverage",
    "",
    "CMHC observations are not available for every census tract for every rental-market measure.",
    "",
    "Income is available for 185 of 187 tracts, while total average rent is available for 77 and total vacancy for 57.",
    "",
    "The most complete four-variable analysis contains only 36 census tracts. For this reason, the project does not use the complete-case subset as its universal analytical dataset.",
    "",
    "Instead, each analysis uses the observations available for the variables required for that specific question.",
    "",
    "### 13.3 Suppression and Reliability",
    "",
    "CMHC source data contain suppression and reliability indicators. Suppressed (`**`) and unavailable (`--`) values are retained as missing rather than converted to zero.",
    "",
    "This approach prevents the analysis from incorrectly treating unavailable rental-market observations as evidence of zero units, zero rent, or zero vacancy.",
    "",
    "### 13.4 Rental Market Survey Coverage",
    "",
    "The CMHC Rental Market Survey does not represent every form of rental housing. Its survey universe has specific inclusion criteria, and social or affordable housing outside the survey frame may not be represented.",
    "",
    "Consequently, the rental-unit counts and market statistics should be understood as measures of the CMHC survey universe rather than the complete Winnipeg rental-housing stock.",
    "",
    "### 13.5 Market-Level Affordability Indicator",
    "",
    "The rent-to-income indicator combines census-tract average market rent with census-tract median household income.",
    "",
    "It does not observe the income and rent of the same household and therefore cannot be interpreted as an individual household's rent burden or shelter-cost-to-income ratio.",
    "",
    "The indicator is intended for relative geographic comparison.",
    "",
    "### 13.6 Geographic Aggregation",
    "",
    "The project operates primarily at the census-tract level. Census tracts contain multiple households and housing units, so relationships observed across tracts cannot automatically be applied to individual households.",
    "",
    "This is an important ecological-inference limitation.",
    "",
    "### 13.7 Small Analytical Samples",
    "",
    "Several analyses use relatively small samples because of incomplete CMHC coverage.",
    "",
    "For example, the rental-price regression uses 59 census tracts, while the vacancy analysis uses 57 for total vacancy.",
    "",
    "Statistical estimates from these subsets should therefore be interpreted with appropriate caution.",
    "",
    "### 13.8 Influential Observations",
    "",
    "Influence diagnostics identified observations that could materially affect some model estimates.",
    "",
    "Rather than removing observations solely because they were influential, the project retains plausible observations and evaluates their influence through sensitivity analysis.",
    "",
    "This approach preserves potentially meaningful market variation while making the robustness of the statistical conclusions explicit.",
    "",
    "### 13.9 Rural and Small-Centre Benchmark",
    "",
    "The Manitoba rural/small-centre benchmark uses a small number of CSD observations with usable CMHC values.",
    "",
    "The benchmark also operates at a different geographic scale from the Winnipeg census-tract analysis.",
    "",
    "It is therefore intended as descriptive context rather than formal statistical inference about urban versus rural rental markets.",
    "",
    "### 13.10 Future Improvements",
    "",
    "Future versions of the project could strengthen the analysis by incorporating additional years of rental-market observations, longitudinal methods, neighbourhood characteristics, building characteristics, and more detailed measures of household housing costs.",
    "",
    "Additional geographic and socioeconomic variables could also support more comprehensive multivariable modelling while reducing the risk of omitted-variable bias."
]

section_path = (
    project_root
    / "reports"
    / "section_13_limitations.md"
)

section_path.write_text(
    "\n".join(section),
    encoding="utf-8"
)

print("Section 13 created successfully.")
print("Path:", section_path)
print("Lines:", len(section))

# %%
from pathlib import Path

section_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/section_13_limitations.md"
)

text = section_path.read_text(encoding="utf-8")

checks = {
    "File exists": section_path.exists(),
    "Cross-sectional design": "Cross-Sectional Design" in text,
    "CMHC coverage": "Incomplete CMHC Coverage" in text,
    "Income coverage": "185 of 187 tracts" in text,
    "Rent coverage": "77" in text,
    "Vacancy coverage": "57" in text,
    "36-tract complete case": "36 census tracts" in text,
    "Suppression handling": "retained as missing" in text,
    "CMHC universe limitation": "does not represent every form of rental housing" in text,
    "Ecological limitation": "ecological-inference limitation" in text,
    "Small samples": "Small Analytical Samples" in text,
    "Influence analysis": "sensitivity analysis" in text,
    "Benchmark limitation": "formal statistical inference" in text,
    "Future improvements": "Future Improvements" in text,
    "Causal limitation": "should not be interpreted as causal effects" in text,
}

print("Section 13 QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

section = [
    "## 14. Conclusion",
    "",
    "This project provides an integrated statistical view of Winnipeg's rental market using census-tract-level rental supply, average rent, vacancy, and household-income data.",
    "",
    "The analysis finds substantial geographic variation across Winnipeg. Higher-income census tracts tend to have higher average rents, while also tending to have lower annualized rent-to-median-household-income indicators. Rental supply is concentrated in particular census tracts, with one- and two-bedroom units accounting for approximately 91% of observed rental inventory.",
    "",
    "Vacancy is relatively low in most observed census tracts but varies substantially across the available sample. The observed relationships between vacancy, rent, and household income remain broadly similar after sensitivity analysis of the highest-vacancy observation.",
    "",
    "The rental-price regression provides additional evidence that both rental-market inventory and local household income are associated with cross-tract differences in average rent. The model explains approximately 68% of observed variation in total average rent, with similar conclusions after sensitivity analysis.",
    "",
    "The Manitoba benchmark provides additional context: the selected rural/small-centre markets have a lower median observed rent than Winnipeg, although the comparison is based on substantially smaller samples and different geographic units.",
    "",
    "The project's central analytical contribution is therefore not a single ranking or prediction. It is an integrated framework for examining rental-market conditions through multiple dimensions while explicitly accounting for missing data, suppression, geographic aggregation, and statistical uncertainty.",
    "",
    "Future work could extend the project longitudinally by incorporating multiple years of CMHC observations, adding neighbourhood and building characteristics, and developing models that better account for spatial structure and changes over time.",
    "",
    "Overall, the project demonstrates an end-to-end analytical workflow combining **data integration, data quality assessment, SQL, descriptive statistics, correlation analysis, regression modelling, diagnostics, sensitivity analysis, visualization, and business interpretation**."
]

section_path = (
    project_root
    / "reports"
    / "section_14_conclusion.md"
)

section_path.write_text(
    "\n".join(section),
    encoding="utf-8"
)

print("Section 14 created successfully.")
print("Path:", section_path)
print("Lines:", len(section))

# %%
from pathlib import Path

section_path = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence/"
    "reports/section_14_conclusion.md"
)

text = section_path.read_text(encoding="utf-8")

checks = {
    "File exists": section_path.exists(),
    "Integrated market view": "integrated statistical view" in text,
    "Geographic variation": "substantial geographic variation" in text,
    "91% bedroom finding": "approximately 91%" in text,
    "Vacancy sensitivity": "sensitivity analysis" in text,
    "Rent model": "68% of observed variation" in text,
    "Manitoba benchmark": "rural/small-centre markets" in text,
    "Missing-data awareness": "missing data" in text,
    "Future longitudinal work": "multiple years of CMHC observations" in text,
    "End-to-end workflow": "end-to-end analytical workflow" in text,
    "Statistical methods": "regression modelling" in text,
}

print("Section 14 QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")


# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

reports_dir = project_root / "reports"

files_to_combine = [
    reports_dir / "executive_summary.md",
    reports_dir / "section_06_rental_prices_income.md",
    reports_dir / "section_07_market_affordability.md",
    reports_dir / "section_08_supply_affordability.md",
    reports_dir / "section_09_rental_price_model.md",
    reports_dir / "section_10_vacancy_market_pressure.md",
    reports_dir / "section_11_manitoba_benchmark.md",
    reports_dir / "section_12_business_interpretation.md",
    reports_dir / "section_13_limitations.md",
    reports_dir / "section_14_conclusion.md",
]

title = """# Winnipeg Rental Market Intelligence

## Statistical and Business Analysis Report

**Geographic scope:** Winnipeg census tracts  
**Primary market data:** CMHC Rental Market Survey  
**Income data:** Statistics Canada 2021 Census  
**Analytical period:** 2023 rental-market observations with 2021 Census income context

---

"""

parts = [title]

for path in files_to_combine:
    if not path.exists():
        raise FileNotFoundError(f"Missing report section: {path}")

    parts.append(
        path.read_text(encoding="utf-8").strip()
    )
    parts.append("\n\n---\n\n")

master_report = "".join(parts).rstrip() + "\n"

report_path = (
    reports_dir
    / "winnipeg_rental_market_statistical_report.md"
)

report_path.write_text(
    master_report,
    encoding="utf-8"
)

print("Master statistical report created successfully.")
print("Path:", report_path)
print("Characters:", len(master_report))
print("Words:", len(master_report.split()))
print("Sections combined:", len(files_to_combine))

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

report_path = (
    project_root
    / "reports"
    / "winnipeg_rental_market_statistical_report.md"
)

text = report_path.read_text(encoding="utf-8")

required_sections = [
    "# Winnipeg Rental Market Intelligence",
    "## Executive Summary",
    "## 6. Rental Prices and Income",
    "## 7. Market Affordability Indicator",
    "## 8. Rental Supply and Market Affordability",
    "## 9. Rental Price Model",
    "## 10. Vacancy and Market Pressure",
    "## 11. Manitoba Benchmark",
    "## 12. Business Interpretation",
    "## 13. Limitations",
    "## 14. Conclusion",
]

checks = {
    "File exists": report_path.exists(),
    "Report has substantial content": len(text.split()) > 4000,
    "187 tracts": "187 Winnipeg census tracts" in text,
    "Rent-income correlation": "0.577" in text and "0.498" in text,
    "Affordability correlation": "-0.506" in text,
    "Supply-affordability R2": "0.499" in text,
    "Rental-price R2": "0.678" in text,
    "Vacancy median": "0.70%" in text,
    "Vacancy sensitivity": "-0.415" in text,
    "Manitoba rent benchmark": "$1,124" in text and "$848" in text,
    "Ecological indicator caveat": "ecological market indicator" in text,
    "Causal limitation": "should not be interpreted as causal" in text,
}

print("Master Statistical Report QA")
print("-" * 50)

print("\nSection checks:")
for section in required_sections:
    print(
        f"{section}: "
        f"{'PASS' if section in text else 'FAIL'}"
    )

print("\nContent checks:")
for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

all_pass = all(section in text for section in required_sections) and all(checks.values())

print("\nOverall:", "PASS" if all_pass else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

report_path = (
    project_root
    / "reports"
    / "winnipeg_rental_market_statistical_report.md"
)

text = report_path.read_text(encoding="utf-8")

text = text.replace(
    "\n# Executive Summary\n",
    "\n## Executive Summary\n",
    1
)

report_path.write_text(
    text,
    encoding="utf-8"
)

print("Executive Summary heading corrected.")
print("Heading present:", "## Executive Summary" in text)

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

report_path = (
    project_root
    / "reports"
    / "winnipeg_rental_market_statistical_report.md"
)

text = report_path.read_text(encoding="utf-8")

required_sections = [
    "# Winnipeg Rental Market Intelligence",
    "## Executive Summary",
    "## 6. Rental Prices and Income",
    "## 7. Market Affordability Indicator",
    "## 8. Rental Supply and Market Affordability",
    "## 9. Rental Price Model",
    "## 10. Vacancy and Market Pressure",
    "## 11. Manitoba Benchmark",
    "## 12. Business Interpretation",
    "## 13. Limitations",
    "## 14. Conclusion",
]

checks = {
    "File exists": report_path.exists(),
    "Report has substantial content": len(text.split()) > 4000,
    "187 tracts": "187 Winnipeg census tracts" in text,
    "Rent-income correlation": "0.577" in text and "0.498" in text,
    "Affordability correlation": "-0.506" in text,
    "Supply-affordability R2": "0.499" in text,
    "Rental-price R2": "0.678" in text,
    "Vacancy median": "0.70%" in text,
    "Vacancy sensitivity": "-0.415" in text,
    "Manitoba rent benchmark": "$1,124" in text and "$848" in text,
    "Ecological indicator caveat": "ecological market indicator" in text,
    "Causal limitation": "should not be interpreted as causal" in text,
}

print("Master Statistical Report QA")
print("-" * 50)

print("\nSection checks:")
for section in required_sections:
    print(
        f"{section}: "
        f"{'PASS' if section in text else 'FAIL'}"
    )

print("\nContent checks:")
for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

all_pass = (
    all(section in text for section in required_sections)
    and all(checks.values())
)

print("\nOverall:", "PASS" if all_pass else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

reports_readme = """# Reports

This directory contains the written statistical analysis supporting the Winnipeg Rental Market Intelligence project.

## Main Report

**`winnipeg_rental_market_statistical_report.md`**

The master report integrates the project's statistical findings, business interpretation, limitations, and conclusion.

It covers:

- Rental prices and household income
- Market-level affordability
- Rental supply and affordability
- Multivariable rental-price modelling
- Vacancy and market pressure
- Manitoba rural/small-centre benchmarking
- Business interpretation
- Statistical limitations

## Supporting Sections

The report was developed as modular sections so individual analytical components can be reviewed independently:

- `executive_summary.md`
- `section_06_rental_prices_income.md`
- `section_07_market_affordability.md`
- `section_08_supply_affordability.md`
- `section_09_rental_price_model.md`
- `section_10_vacancy_market_pressure.md`
- `section_11_manitoba_benchmark.md`
- `section_12_business_interpretation.md`
- `section_13_limitations.md`
- `section_14_conclusion.md`

## Report Development

The report is supported by:

- A reproducible Python analysis notebook
- A SQLite analytical database
- SQL dashboard views
- A data dictionary
- SVG dashboard visualizations
- Processed analytical datasets

The master report should be treated as the primary written analytical deliverable.
"""

reports_path = project_root / "reports" / "README.md"

reports_path.write_text(
    reports_readme,
    encoding="utf-8"
)

print("Reports README created successfully.")
print("Path:", reports_path)
print("Characters:", len(reports_readme))

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

reports_path = project_root / "reports" / "README.md"

text = reports_path.read_text(encoding="utf-8")

checks = {
    "File exists": reports_path.exists(),
    "Main report documented": "winnipeg_rental_market_statistical_report.md" in text,
    "Executive summary documented": "executive_summary.md" in text,
    "Rental price model documented": "section_09_rental_price_model.md" in text,
    "Vacancy analysis documented": "section_10_vacancy_market_pressure.md" in text,
    "Benchmark documented": "section_11_manitoba_benchmark.md" in text,
    "Limitations documented": "section_13_limitations.md" in text,
    "Notebook mentioned": "reproducible Python analysis notebook" in text,
    "SQL mentioned": "SQLite analytical database" in text,
    "SVG mentioned": "SVG dashboard visualizations" in text,
}

print("Reports README QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

readme_path = project_root / "README.md"

readme_lines = [
    "# Winnipeg Rental Market Intelligence",
    "",
    "## Statistical Analysis of Rental Supply, Prices, Vacancy, and Affordability",
    "",
    "An end-to-end data analytics and statistical analysis project examining Winnipeg's rental market at the census-tract level.",
    "",
    "The project integrates **CMHC Rental Market Survey** data with **Statistics Canada 2021 Census** household-income data and combines Python, SQL, statistical modelling, data visualization, and business interpretation.",
    "",
    "---",
    "",
    "## Executive Summary",
    "",
    "This project examines:",
    "",
    "- Rental supply and bedroom composition",
    "- Geographic variation in average rents",
    "- Rental vacancy and market pressure",
    "- Rental costs relative to local household income",
    "- Relationships between rental supply, income, rent, and vacancy",
    "- Winnipeg versus selected Manitoba rural/small-centre markets",
    "",
    "The analytical dataset contains **187 Winnipeg census tracts**.",
    "",
    "### Key Findings",
    "",
    "- Median observed total average rent: **$1,124/month**",
    "- Median observed vacancy: **0.7%**",
    "- Median rental supply: **223 units/tract**",
    "- Approximately **91%** of observed rental units are one- or two-bedroom units",
    "- Rent and median household income: **Spearman rho = 0.498**",
    "- Rent-to-income indicator and income: **Spearman rho = -0.506**",
    "- Rental-price model: **R² = 0.678**",
    "- Rental-price model prediction error: **MAE ≈ $138**",
    "- Selected Manitoba rural/small-centre median rent: **$848**",
    "",
    "The affordability measure is an **annualized market rent-to-median-household-income indicator**, not a household-level rent-burden measure.",
    "",
    "## Research Question",
    "",
    "> How do rental prices, vacancy rates, housing supply, and neighbourhood characteristics vary across Winnipeg, and what factors are associated with rental-market pressure and affordability?",
    "",
    "The analysis is observational and cross-sectional. Statistical relationships are interpreted as associations rather than causal effects.",
    "",
    "## Project Deliverables",
    "",
    "### Statistical Report",
    "",
    "**[Statistical Analysis Report](reports/winnipeg_rental_market_statistical_report.md)**",
    "",
    "The main written deliverable covering methodology, descriptive analysis, correlations, regression models, diagnostics, sensitivity analysis, business interpretation, and limitations.",
    "",
    "### Reproducible Analysis",
    "",
    "**[Analysis Notebook](notebooks/01_winnipeg_rental_market_analysis.ipynb)**",
    "",
    "A self-contained Python notebook designed to execute from the processed analytical dataset.",
    "",
    "### Dashboard",
    "",
    "The dashboard is organized into six analytical views:",
    "",
    "1. Market Overview",
    "2. Rental Supply & Composition",
    "3. Rental Prices & Affordability",
    "4. Vacancy & Market Pressure",
    "5. Rent Model & Statistical Evidence",
    "6. Manitoba Benchmarking",
    "",
    "Dashboard visuals are stored as SVG files in:",
    "",
    "`data/processed/dashboard/`",
    "",
    "### SQL",
    "",
    "**[SQL Documentation](sql/README.md)**",
    "",
    "Documents the SQLite analytical database, dashboard views, and example analytical queries.",
    "",
    "### Data Dictionary",
    "",
    "**[Data Dictionary](docs/data_dictionary.md)**",
    "",
    "Defines the analytical variables, units, interpretation, and important data-quality conventions.",
    "",
    "## Data Sources",
    "",
    "### Canada Mortgage and Housing Corporation",
    "",
    "CMHC Rental Market Survey data provide rental supply, average rent, vacancy, and rental-market measures.",
    "",
    "### Statistics Canada",
    "",
    "2021 Census data provide median household total income for 2020 at the census-tract level.",
    "",
    "### Manitoba Benchmark",
    "",
    "Additional CMHC rural/small-centre data are used for descriptive comparison with selected Manitoba CSD observations.",
    "",
    "## Methodology",
    "",
    "The project workflow includes:",
    "",
    "1. Source-data acquisition",
    "2. Data cleaning and standardization",
    "3. Suppression and missing-value handling",
    "4. Integration of CMHC and Statistics Canada data",
    "5. Exploratory and descriptive analysis",
    "6. Correlation analysis",
    "7. OLS regression modelling",
    "8. Model diagnostics",
    "9. Influence and sensitivity analysis",
    "10. SQL analytical views",
    "11. Dashboard development",
    "12. Business interpretation",
    "",
    "### Statistical Methods",
    "",
    "- Descriptive statistics",
    "- Pearson correlation",
    "- Spearman rank correlation",
    "- Ordinary least squares regression",
    "- Log-transformed rental supply",
    "- Shapiro-Wilk normality testing",
    "- Breusch-Pagan heteroskedasticity testing",
    "- Variance inflation factors",
    "- Cook's distance",
    "- Sensitivity analysis",
    "",
    "## Data Quality",
    "",
    "CMHC suppression and availability indicators are preserved during processing.",
    "",
    "Values such as `**` and `--` are treated as missing rather than zero.",
    "",
    "Analytical sample sizes vary by question because CMHC coverage differs across rental-market measures.",
    "",
    "| Measure | Available observations |",
    "|---|---:|",
    "| Median household income | 185 |",
    "| Rental supply | 135 |",
    "| Total average rent | 77 |",
    "| Total vacancy | 57 |",
    "| Rent + vacancy + income | 54 |",
    "| Supply + rent + vacancy + income | 36 |",
    "",
    "The project deliberately avoids forcing all analyses onto the smallest complete-case sample.",
    "",
    "## Limitations",
    "",
    "- Cross-sectional rather than longitudinal design",
    "- Incomplete tract-level CMHC coverage",
    "- CMHC survey-universe limitations",
    "- Suppressed observations",
    "- Ecological rather than household-level affordability measurement",
    "- Geographic aggregation",
    "- Small samples for some statistical analyses",
    "- Potential omitted variables",
    "- Rural/small-centre benchmark uses different geographic units",
    "",
    "The project does not establish causal effects.",
    "",
    "## Repository Structure",
    "",
    "```text",
    "winnipeg_rental_market_intelligence/",
    "├── data/",
    "│   ├── raw/",
    "│   │   ├── cmhc/",
    "│   │   └── statcan/",
    "│   └── processed/",
    "│       ├── dashboard/",
    "│       └── statcan/",
    "├── dashboard/",
    "├── docs/",
    "│   └── data_dictionary.md",
    "├── notebooks/",
    "│   └── 01_winnipeg_rental_market_analysis.ipynb",
    "├── reports/",
    "│   ├── README.md",
    "│   ├── executive_summary.md",
    "│   └── winnipeg_rental_market_statistical_report.md",
    "├── sql/",
    "│   └── README.md",
    "├── src/",
    "├── .gitignore",
    "├── README.md",
    "└── requirements.txt",
    "```",
    "",
    "## Tools",
    "",
    "**Python** · pandas · NumPy · SciPy · statsmodels · Matplotlib",
    "",
    "**SQL** · SQLite",
    "",
    "**Statistics** · Correlation · OLS · Diagnostics · Sensitivity Analysis",
    "",
    "**Visualization** · SVG · Dashboard Design",
    "",
    "**Data Sources** · CMHC · Statistics Canada",
    "",
    "## Author",
    "",
    "Statistics Honours student at the University of Manitoba with an interest in data analytics, statistical analysis, and evidence-based decision-making.",
    "",
    "This project demonstrates an end-to-end workflow from raw public data through statistical analysis, reproducible documentation, SQL, visualization, and business interpretation.",
]

readme_path.write_text(
    "\n".join(readme_lines),
    encoding="utf-8"
)

print("Root README updated successfully.")
print("Path:", readme_path)
print("Lines:", len(readme_lines))
print("Characters:", len(readme_path.read_text(encoding="utf-8")))

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

readme_path = project_root / "README.md"

text = readme_path.read_text(encoding="utf-8")

checks = {
    "File exists": readme_path.exists(),
    "Project title": "# Winnipeg Rental Market Intelligence" in text,
    "Project description": "end-to-end data analytics" in text,
    "187 census tracts": "187 Winnipeg census tracts" in text,
    "Median rent": "$1,124/month" in text,
    "Median vacancy": "0.7%" in text,
    "Median supply": "223 units/tract" in text,
    "Rent-income correlation": "0.498" in text,
    "Affordability correlation": "-0.506" in text,
    "Rental model R2": "0.678" in text,
    "MAE": "$138" in text,
    "Statistical report link": "reports/winnipeg_rental_market_statistical_report.md" in text,
    "Notebook link": "notebooks/01_winnipeg_rental_market_analysis.ipynb" in text,
    "SQL documentation": "sql/README.md" in text,
    "Data dictionary": "docs/data_dictionary.md" in text,
    "SVG dashboard": "data/processed/dashboard/" in text,
    "Methods documented": "Cook's distance" in text,
    "Limitations documented": "Ecological rather than household-level affordability" in text,
    "No causal claim": "does not establish causal effects" in text,
}

print("Root README QA")
print("-" * 50)

for name, result in checks.items():
    print(f"{name}: {'PASS' if result else 'FAIL'}")

print("\nOverall:", "PASS" if all(checks.values()) else "REVIEW NEEDED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

required_files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "notebooks/01_winnipeg_rental_market_analysis.ipynb",
    "docs/data_dictionary.md",
    "sql/README.md",
    "reports/README.md",
    "reports/executive_summary.md",
    "reports/winnipeg_rental_market_statistical_report.md",
    "data/processed/winnipeg_ct_rental_market_analytical.csv",
    "data/processed/winnipeg_ct_rental_market_master_2023.csv",
    "data/winnipeg_rental_market.db",
    "data/processed/dashboard/dashboard_tracts.csv",
    "data/processed/dashboard/dashboard_affordability.csv",
    "data/processed/dashboard/dashboard_kpis.csv",
    "data/processed/dashboard/page6_manitoba_benchmarking.svg",
    "data/processed/dashboard/benchmark_winnipeg_vs_manitoba_rural_rent.svg",
    "data/processed/dashboard/benchmark_winnipeg_vs_manitoba_rural_vacancy.svg",
]

print("Repository Artifact QA")
print("-" * 60)

results = []

for relative_path in required_files:
    path = project_root / relative_path
    exists = path.exists()
    results.append(exists)

    if exists:
        size_kb = path.stat().st_size / 1024
        print(f"PASS | {relative_path} | {size_kb:.1f} KB")
    else:
        print(f"FAIL | {relative_path}")

print("-" * 60)
print(f"Artifacts checked: {len(required_files)}")
print(f"Artifacts present: {sum(results)}")
print("Overall:", "PASS" if all(results) else "REVIEW NEEDED")

# %%
import nbformat
from nbclient import NotebookClient
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

notebook_path = (
    project_root
    / "notebooks"
    / "01_winnipeg_rental_market_analysis.ipynb"
)

nb = nbformat.read(notebook_path, as_version=4)

# Execute a fresh in-memory copy so the saved notebook remains clean.
test_nb = nbformat.from_dict(nb)

client = NotebookClient(
    test_nb,
    timeout=300,
    kernel_name="python3"
)

client.execute()

print("Final notebook reproducibility test")
print("-" * 50)
print("Notebook exists:", notebook_path.exists())
print("Cells executed:", len(test_nb.cells))
print("Execution status: PASSED")

# %%
from pathlib import Path

project_root = Path(
    "/Users/abbas90/winnipeg_rental_market_intelligence"
)

print("FINAL REPOSITORY HEALTH CHECK")
print("=" * 60)

# Required top-level components
required_dirs = [
    "data",
    "docs",
    "notebooks",
    "reports",
    "sql",
    "src",
    "dashboard",
]

required_files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
]

print("\nTop-level directories:")
dir_results = []

for name in required_dirs:
    exists = (project_root / name).is_dir()
    dir_results.append(exists)
    print(f"{'PASS' if exists else 'FAIL'} | {name}/")

print("\nTop-level files:")
file_results = []

for name in required_files:
    exists = (project_root / name).is_file()
    file_results.append(exists)
    print(f"{'PASS' if exists else 'FAIL'} | {name}")

# Check for accidental notebook checkpoints
checkpoint_dirs = list(project_root.rglob(".ipynb_checkpoints"))

print("\nRepository cleanliness:")
print(
    "Notebook checkpoints:",
    len(checkpoint_dirs),
    "|",
    "PASS" if len(checkpoint_dirs) == 0 else "REVIEW"
)

# Final status
overall = (
    all(dir_results)
    and all(file_results)
    and len(checkpoint_dirs) == 0
)

print("\n" + "=" * 60)
print("Overall:", "PASS" if overall else "REVIEW NEEDED")

# %%
