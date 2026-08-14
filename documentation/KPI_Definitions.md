# KPI Definitions

This document defines the primary business metrics used throughout the RetailMart Australia Power BI report.

| KPI | Definition |
|---|---|
| Total Revenue | Sum of Net Sales within the selected filter context. |
| Total Profit | Sum of Net Sales less Cost of Goods. |
| Profit Margin % | Total Profit divided by Total Revenue. |
| Total Orders | Distinct count of OrderID. |
| Units Sold | Sum of Quantity sold. |
| Average Order Value | Total Revenue divided by Total Orders. |
| Total Customers | Distinct count of purchasing CustomerID values within the selected filter context. |
| Revenue per Customer | Total Revenue divided by Total Customers. |
| Total Returns | Distinct count of ReturnID analysed according to ReturnDate. |
| Return Rate % | Returned sales lines relative to sales-line activity in the selected reporting context. |
| Total Refund Amount | Sum of RefundAmount analysed according to ReturnDate. |
| Revenue Target Achievement % | Actual Total Revenue divided by Target Revenue. |
| Revenue Variance % | Difference between actual and target revenue relative to Target Revenue. |
| Orders Variance % | Difference between actual and target orders relative to Target Orders. |
| Profit Margin Variance | Difference between actual and target profit margin, expressed in percentage points. |
| Year-on-Year Revenue Change % | Percentage change in Total Revenue between the current and comparison period. |
| Year-on-Year Profit Change % | Percentage change in Total Profit between the current and comparison period. |
| Store Revenue Rank | Dynamic ranking of stores according to Total Revenue within the current report filter context. |

## KPI Design Notes

### Revenue

`NetSales` is treated as report revenue because it represents sales value after line-level discounts.

### Customer Count

Customer KPIs count customers appearing in `FactSales` rather than all records in `DimCustomer`. This ensures the measure represents customers who actually purchased within the selected reporting context.

### Returns

Returns are analysed according to `ReturnDate`, rather than the date of the original transaction. An inactive date relationship is activated within relevant DAX measures using `USERELATIONSHIP`.

### Profit Margin Variance

Unlike revenue and order variance, profit-margin variance is expressed in **percentage points**.

For example:

- Actual Margin: 28.4%
- Target Margin: 24.8%
- Variance: +3.6 percentage points

This avoids incorrectly representing the difference as a percentage growth rate.

### Dynamic Filtering

KPIs are designed to respond to report filter context, including Year, Region and Category selections where applicable.