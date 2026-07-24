# Dataset Generation Notes

The RetailMart Australia data was generated programmatically in Python with a fixed random seed of `4701`.

Generation design included:

- 2023–2025 transaction dates
- Australian state, city and store structure
- customer loyalty tiers and weighted purchase frequency
- product categories, pricing and category-specific margins
- Black Friday, Christmas, EOFY and seasonal demand patterns
- online, in-store and click-and-collect sales channels
- promotion and loyalty discounts
- category- and channel-sensitive return probabilities
- monthly targets informed by actual store performance

The distributed portfolio package contains the generated CSV outputs and a validation script. The complete generation notebook is not included in this release.
