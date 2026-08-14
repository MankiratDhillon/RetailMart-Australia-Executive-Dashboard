# Data Dictionary

The RetailMart Australia dataset uses a dimensional structure designed for business intelligence analysis in Power BI.

## FactSales

**Grain:** One row represents one product line within a customer order.

**Purpose:** Primary transactional fact table used for sales, revenue, profitability, customer, store and product analysis.

Key fields include:

- `SaleID` — unique identifier for each sales line
- `OrderID` — identifier shared by sales lines belonging to the same order
- `OrderDate` — transaction date
- `DateKey` — date dimension key
- `CustomerID` — customer foreign key
- `StoreID` — store foreign key
- `ProductID` — product foreign key
- `EmployeeID` — employee foreign key where applicable
- `PromotionID` — promotion foreign key where applicable
- `Quantity` — units purchased
- `GrossSales` — sales value before discounts
- `NetSales` — sales value after discounts
- `CostOfGoods` — associated product cost
- `Profit` — Net Sales less Cost of Goods
- `DiscountRate` — line-level discount
- `SalesChannel` — transaction channel
- `PaymentMethod` — customer payment method

## FactReturns

**Grain:** One row represents a returned sales line.

**Purpose:** Supports return-volume, return-rate and refund-cost analysis.

Key fields include:

- `ReturnID` — unique return identifier
- `SaleID` — associated sales-line identifier
- `ReturnDate` — date the return occurred
- `ReturnQuantity` — quantity returned
- `ReturnReason` — recorded reason for return
- `RefundAmount` — financial value refunded
- `DaysAfterPurchase` — elapsed time between purchase and return
- `ReturnStatus` — return/refund processing status

`FactReturns` links to `FactSales` through `SaleID`.

An inactive relationship between `DimDate[Date]` and `FactReturns[ReturnDate]` supports return-date analysis using DAX `USERELATIONSHIP`.

## DimCustomer

**Purpose:** Customer segmentation and demographic analysis.

Key attributes include:

- `CustomerID`
- `Gender`
- `Age`
- `City`
- `State`
- `JoinDate`
- `LoyaltyTier`
- `AcquisitionChannel`

The finished dashboard primarily uses customer identity and loyalty tier for customer-volume and customer-value analysis.

## DimProduct

**Purpose:** Product and category-level commercial analysis.

Key attributes include:

- `ProductID`
- `ProductName`
- `Category`
- `Subcategory`
- `Brand`
- product cost
- selling price
- launch date
- product status

The Category → Subcategory hierarchy supports interactive drill-down within the report.

## DimStore

**Purpose:** Store and regional performance analysis.

Key attributes include:

- `StoreID`
- store name
- city
- state
- region
- store format
- opening date
- floor area

Store attributes support dynamic ranking and regional filtering.

## DimEmployee

**Purpose:** Employee and store-assignment information.

Includes employee role, assigned store, hire date and employment status.

The table remains part of the analytical model even though employee-level reporting is not a primary focus of the final dashboard.

## DimDate

**Purpose:** Central date dimension supporting chronological filtering and time-based analysis.

Includes:

- calendar date
- year
- month
- month number
- quarter
- Australian financial-year attributes

Month-number fields are used to ensure month names display chronologically in report visuals.

## Promotions

Contains promotion periods and attributes including:

- promotion identifier
- promotion dates
- applicable categories
- discount rates
- applicable sales channels

Promotion information is retained within the model for transactional context but is not a primary analytical focus of the final report.

## SalesTargets

**Grain:** Monthly target by store.

Contains targets for:

- revenue
- orders
- profit margin

The table supports target achievement and variance analysis within the Executive Overview.