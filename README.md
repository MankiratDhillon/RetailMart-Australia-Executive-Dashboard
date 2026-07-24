# RetailMart Australia BI Dataset

A synthetic, reproducible business-intelligence dataset designed for an end-to-end Power BI portfolio project.

## Business Scenario

RetailMart Australia is a fictional national omnichannel retailer operating physical stores, online sales, click-and-collect, a loyalty program, seasonal promotions, and monthly store targets.

The dataset models realistic commercial patterns, including:

- year-on-year sales growth
- Australian retail seasonality
- Black Friday, Christmas, EOFY and back-to-work promotions
- different store formats and regional performance
- customer loyalty tiers and purchasing frequency
- product-level margins and discounting
- online, in-store and click-and-collect channels
- returns, refund amounts and return reasons
- monthly store revenue, margin and order targets

## Dataset Scale

| Table | Rows |
|---|---:|
| DimDate | 1,096 |
| DimStore | 36 |
| DimEmployee | 220 |
| DimCustomer | 18,000 |
| DimProduct | 480 |
| Promotions | 18 |
| FactSales | 150,000 |
| FactReturns | 7,430 |
| SalesTargets | 1,296 |

## Suggested Power BI Model

- `FactSales` is the primary fact table.
- `FactReturns` links to `FactSales` through `SaleID`.
- Dimensions link to `FactSales` through their business keys.
- `DimDate[Date]` links to `FactSales[OrderDate]`.
- `DimStore[StoreID]` links to both `FactSales` and `SalesTargets`.
- `Promotions[PromotionID]` links to `FactSales[PromotionID]`.

## Data Quality Features

The dataset intentionally includes a small number of missing customer email values and inactive employees. These support realistic Power Query cleaning and data-quality discussion without compromising key relationships.

## Data Generation and Validation

The dataset was generated programmatically in Python with a fixed random seed (`4701`). Generation methodology is documented in `scripts/GENERATION_NOTES.md`, and `scripts/validate_data.py` verifies key relationships and file integrity.

## Disclaimer

All companies, people, transactions and values are fictional and generated solely for portfolio and educational purposes.
