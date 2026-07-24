# Data Dictionary

## FactSales
Primary transaction-grain table. One row represents one product line within an order.

Key fields:
- `SaleID`: unique sales-line key
- `OrderID`: order identifier shared across one or more lines
- `OrderDate`, `DateKey`: transaction date
- dimension foreign keys: `CustomerID`, `StoreID`, `ProductID`, `EmployeeID`, `PromotionID`
- financial fields: `GrossSales`, `NetSales`, `CostOfGoods`, `Profit`
- commercial fields: `SalesChannel`, `PaymentMethod`, `Quantity`, `DiscountRate`

## FactReturns
One row per returned sales line. Links to `FactSales` through `SaleID`.

## DimCustomer
Customer demographics, location, acquisition channel, join date and loyalty tier.

## DimProduct
Product hierarchy, brand, cost, price, launch date and status.

## DimStore
Store geography, regional grouping, format, opening date and floor area.

## DimEmployee
Employee role, assigned store, hire date and employment status.

## DimDate
Calendar attributes, including Australian-style financial year fields.

## Promotions
Promotion periods, applicable categories, discount rates and channels.

## SalesTargets
Monthly targets by store for revenue, profit margin and orders.
