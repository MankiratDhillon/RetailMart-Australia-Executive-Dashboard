# Power BI Data Model

The RetailMart Australia Power BI solution uses a dimensional analytical model centred primarily on the `FactSales` transaction table.

## Model Structure

```text
                    DimDate
                       |
DimCustomer ─────── FactSales ─────── DimProduct
                       |
                    DimStore
                       |
                  DimEmployee

Promotions ───────── FactSales

FactSales ───────── FactReturns

DimStore ────────── SalesTargets
DimDate ─────────── SalesTargets

DimDate - - - - - - FactReturns
          inactive ReturnDate relationship
```

## Primary Fact Table

### FactSales

`FactSales` is the primary transactional fact table.

Its grain is one product line within an order.

The table connects sales activity to the relevant customer, product, store, employee, promotion and date dimensions.

## Supporting Fact Tables

### FactReturns

`FactReturns` contains returned sales lines and connects to the original transaction through `SaleID`.

Returns have a separate business date (`ReturnDate`). An inactive relationship between `DimDate[Date]` and `FactReturns[ReturnDate]` allows DAX measures to analyse returns according to the date on which the return occurred.

This relationship is activated when required using `USERELATIONSHIP`.

### SalesTargets

`SalesTargets` contains monthly store-level business targets for:

- Revenue
- Orders
- Profit Margin

The table connects to the store and date context required for actual-versus-target analysis.

## Dimension Tables

The model includes the following supporting dimensions:

### DimDate

Provides the central calendar structure used for chronological filtering, monthly analysis, year-based comparisons and time intelligence.

### DimCustomer

Contains customer attributes used for customer segmentation and loyalty analysis.

### DimProduct

Contains the product hierarchy and product attributes used for category, subcategory and individual product analysis.

### DimStore

Contains store and regional attributes used for geographical filtering, store comparison and dynamic ranking.

### DimEmployee

Contains employee and store-assignment information associated with sales transactions.

### Promotions

Contains promotion information associated with relevant sales transactions.

## Relationship Design

The model primarily uses:

- one-to-many relationships from dimensions to fact tables
- single-direction filtering
- a dedicated date dimension
- active relationships for primary analytical paths
- inactive relationships where alternative date contexts are required

This structure reduces relationship ambiguity and supports predictable filter propagation throughout the report.

## Date Modelling

`DimDate` provides the primary date context for the model.

Sales activity is analysed through the relationship between:

`DimDate[Date]` → `FactSales[OrderDate]`

Returns require a different date context because the date of a return can differ from the date of the original purchase.

An inactive relationship therefore exists between:

`DimDate[Date]` → `FactReturns[ReturnDate]`

Return-specific measures activate this relationship using DAX `USERELATIONSHIP`, allowing monthly return analysis to reflect when returns actually occurred.

## Analytical Design

Business calculations are implemented using explicit DAX measures rather than relying primarily on implicit visual aggregations.

A dedicated Measures table centralises reusable business calculations including:

- Total Revenue
- Total Profit
- Profit Margin %
- Total Orders
- Average Order Value
- Total Customers
- Revenue per Customer
- Year-on-year performance
- Target achievement
- Target variance
- Store ranking
- Total Returns
- Return Rate %
- Total Refund Amount

This approach separates analytical business logic from the underlying data tables and improves maintainability.

## Target Performance Model

The Executive Overview compares actual performance against business targets for:

- Revenue
- Orders
- Profit Margin

A disconnected `Target Metrics` table is used to control the presentation of these different metrics within a single target-performance visual.

DAX `SWITCH` logic determines which underlying measure is displayed for each metric.

This allows measures with different units — currency, counts, percentages and percentage-point variances — to be presented within a consistent reporting structure.

## Filter Behaviour

Measures are designed to respect Power BI filter context so analytical results dynamically respond to relevant report selections.

The analytical pages support filtering by:

- Year
- Region
- Category

Visual interactions also enable cross-filtering between stores, products, categories and other analytical dimensions.

## Design Rationale

The model was designed to:

- separate transactional and descriptive data
- minimise unnecessary duplication
- maintain predictable relationship behaviour
- centralise reusable business logic
- support multiple analytical date contexts
- enable interactive filtering and drill-down
- support both executive reporting and detailed analysis

The resulting structure provides a scalable foundation for the three-page Power BI reporting solution.

## Model Diagram

A screenshot of the implemented Power BI data model is available at:

`assets/data-model.png`