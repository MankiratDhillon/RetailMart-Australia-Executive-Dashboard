# DAX Measures

This document highlights selected DAX measures used in the RetailMart Australia Power BI report.

The report uses a dedicated Measures table to separate analytical logic from the underlying fact and dimension tables.

## Core Business KPIs

### Total Revenue

```DAX
Total Revenue =
SUM ( FactSales[Revenue] )
```

Calculates total sales revenue within the current filter context.

### Total Profit

```DAX
Total Profit =
SUM ( FactSales[Profit] )
```

Calculates total profit within the current filter context.

### Profit Margin %

```DAX
Profit Margin % =
DIVIDE (
    [Total Profit],
    [Total Revenue],
    0
)
```

Calculates profitability relative to revenue while safely handling division by zero.

### Total Orders

```DAX
Total Orders =
DISTINCTCOUNT ( FactSales[OrderID] )
```

Counts unique customer orders rather than individual sales-line records.

### Average Order Value

```DAX
Average Order Value =
DIVIDE (
    [Total Revenue],
    [Total Orders],
    0
)
```

Measures average revenue generated per order.

---

## Customer Analytics

### Total Customers

```DAX
Total Customers =
DISTINCTCOUNT ( FactSales[CustomerID] )
```

Counts customers who generated transactions within the current filter context rather than simply counting all records in the customer dimension.

### Revenue per Customer

```DAX
Revenue per Customer =
DIVIDE (
    [Total Revenue],
    [Total Customers],
    0
)
```

Measures average revenue generated per purchasing customer.

This measure is used to compare customer value across loyalty tiers and other customer segments.

---

## Returns Analysis

Returns require separate date handling because a product may be purchased on one date and returned on another.

The model therefore contains an inactive relationship between:

`DimDate[Date]` → `FactReturns[ReturnDate]`

### Total Returns

```DAX
Total Returns =
CALCULATE (
    DISTINCTCOUNT ( FactReturns[ReturnID] ),
    USERELATIONSHIP (
        DimDate[Date],
        FactReturns[ReturnDate]
    )
)
```

`USERELATIONSHIP` activates the return-date relationship for the calculation, allowing returns to be analysed according to when they occurred rather than when the original sale occurred.

### Return Rate %

```DAX
Return Rate % =
DIVIDE (
    [Total Returns],
    DISTINCTCOUNT ( FactSales[SaleID] )
)
```

Compares return events with sales activity within the selected reporting context.

### Total Refund Amount

```DAX
Total Refund Amount =
CALCULATE (
    SUM ( FactReturns[RefundAmount] ),
    USERELATIONSHIP (
        DimDate[Date],
        FactReturns[ReturnDate]
    )
)
```

Calculates the financial impact of returns according to return date.

---

## Target Performance

The report compares actual business performance against monthly store targets.

Measures were developed for revenue, orders and profit-margin targets and their respective variances.

Target performance is presented through a disconnected metric table, allowing several KPIs with different formats to be displayed in a single analytical visual.

### Target Metric Selection

```DAX
Target Metric Variance Value =
SWITCH (
    SELECTEDVALUE ( 'Target Metrics'[Metric] ),
    "Revenue", [Revenue Variance %],
    "Orders", [Orders Variance %],
    "Profit Margin", [Profit Margin Variance pp]
)
```

`SWITCH` dynamically returns the appropriate calculation based on the metric represented by each table row.

This approach allows Revenue, Orders and Profit Margin to share a single target-performance visual despite using different units and formatting.

### Conditional Variance Colour

```DAX
Target Variance Colour =
VAR V = [Target Metric Variance Value]
RETURN
    IF (
        ISBLANK ( V ),
        BLANK(),
        IF (
            V >= 0,
            "#059669",
            "#EF4444"
        )
    )
```

Provides dynamic conditional formatting for positive and negative target variance.

---

## Ranking

Store performance uses dynamic ranking so rankings respond to the report's filter context rather than remaining static.

The ranking logic is based on `RANKX` and Total Revenue, allowing store rankings to recalculate when users change year, region or category filters.

This supports the dynamic Top 10 Store Performance analysis on the Store & Product Analysis page.

---

## Time Intelligence

The Executive Overview includes year-on-year analysis and a user-selectable comparison year.

Time-based measures enable:

- current-period revenue
- comparison-period revenue
- revenue variance
- current-period profit
- comparison-period profit
- profit variance

The comparison logic responds dynamically to report context and the selected comparison period rather than relying on static values.

---

## DAX Design Principles

Measures in this project were designed around several principles:

- use explicit measures rather than relying on implicit aggregations
- use `DIVIDE` for safe ratio calculations
- preserve filter context so visuals respond dynamically to slicers
- separate calculation logic from display formatting where necessary
- use disconnected tables where a reporting structure does not belong in the transactional model
- activate inactive relationships only for calculations requiring an alternative date context
- keep reusable business logic in a dedicated Measures table

These techniques allow the report to remain interactive while keeping analytical logic centralised and maintainable.