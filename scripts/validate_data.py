"""Validate the RetailMart Australia portfolio dataset.

Run from the repository root:
    python scripts/validate_data.py
"""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

EXPECTED_FILES = {
    "DimDate.csv",
    "DimStore.csv",
    "DimEmployee.csv",
    "DimCustomer.csv",
    "DimProduct.csv",
    "Promotions.csv",
    "FactSales.csv",
    "FactReturns.csv",
    "SalesTargets.csv",
}

missing = sorted(name for name in EXPECTED_FILES if not (DATA / name).exists())
if missing:
    raise FileNotFoundError(f"Missing dataset files: {missing}")

def read_ids(filename, column):
    with (DATA / filename).open(newline="", encoding="utf-8") as f:
        return {row[column] for row in csv.DictReader(f)}

customers = read_ids("DimCustomer.csv", "CustomerID")
products = read_ids("DimProduct.csv", "ProductID")
stores = read_ids("DimStore.csv", "StoreID")
sales_ids = read_ids("FactSales.csv", "SaleID")

sales_count = 0
with (DATA / "FactSales.csv").open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        assert row["CustomerID"] in customers
        assert row["ProductID"] in products
        assert row["StoreID"] in stores
        sales_count += 1

returns_count = 0
with (DATA / "FactReturns.csv").open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        assert row["SaleID"] in sales_ids
        returns_count += 1

print(f"Validation passed: {sales_count:,} sales lines and {returns_count:,} returns.")
