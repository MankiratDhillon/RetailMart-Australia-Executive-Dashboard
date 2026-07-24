# Proposed Data Model

```text
DimDate -----------+
DimCustomer -------|
DimProduct --------| 
DimStore ----------|---- FactSales ---- FactReturns
DimEmployee -------|
Promotions --------+

DimStore ---------------- SalesTargets
DimDate/YearMonth -------- SalesTargets
```

Recommended cardinality: one-to-many from each dimension to its fact table, with single-direction filtering.
