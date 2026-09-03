# 📊 Quantium Retail Analytics — Customer & Sales Analysis

## 📌 Project Overview

This project analyzes retail transaction data from **Quantium's QVI dataset** to uncover actionable insights into sales performance, customer purchasing behavior, product performance, brand contribution, store performance, pack-size preferences, and sales trends over time.

The project uses **Python-based Exploratory Data Analysis (EDA)** to transform raw transaction data into meaningful business insights and recommendations.

The goal was not only to analyze the data, but also to answer important business questions such as:

* Which products and brands generate the most revenue?
* When are sales highest and lowest?
* Which pack sizes are most popular?
* How strong is customer retention?
* Which stores perform best?
* Is revenue concentrated among a small number of products or brands?
* Are there unusual customer purchasing patterns?
* What actions can the business take based on the findings?

---

## 🎯 Business Objective

The primary objective of this project was to understand purchasing patterns and identify opportunities for:

* Revenue optimization
* Customer retention
* Product portfolio optimization
* Brand strategy
* Store performance improvement
* Promotional planning
* Data-driven decision making

---

## 📂 Dataset

The analysis uses the **QVI Transaction Data** provided as part of the Quantium retail analytics case study.

### Dataset Statistics

| Metric              |      Value |
| ------------------- | ---------: |
| Transaction Records |    264,836 |
| Unique Transactions |    263,127 |
| Unique Customers    |     72,637 |
| Unique Products     |        114 |
| Stores              |        272 |
| Total Revenue       | $1,934,415 |
| Total Units Sold    |    505,124 |

### Key Columns

* `DATE` — Transaction date
* `STORE_NBR` — Store identifier
* `LYLTY_CARD_NBR` — Customer loyalty card number
* `TXN_ID` — Transaction identifier
* `PROD_NBR` — Product identifier
* `PROD_NAME` — Product name
* `PROD_QTY` — Quantity purchased
* `TOT_SALES` — Transaction sales value

---

## 🛠️ Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Exploratory Data Analysis (EDA)**
* Data Cleaning
* Feature Engineering
* Data Aggregation
* Statistical Analysis
* Correlation Analysis
* Business Analytics

---

## 🔎 Analysis Performed

### 1. Data Preparation

* Converted Excel date values into standard datetime format
* Extracted product pack sizes using regular expressions
* Extracted brand names from product names
* Created month-based features
* Created day-of-week features
* Created weekend indicators
* Checked transaction-level data
* Prepared datasets for customer, product, brand, store, and time analysis

### 2. Customer Analysis

Analyzed:

* Unique customers
* Purchase frequency
* Repeat customers
* Customer revenue contribution
* Customer purchase quantities
* Potential purchasing anomalies

### 3. Product Analysis

Analyzed:

* Product revenue
* Units sold
* Product rankings
* Top-performing products
* Revenue contribution by product

### 4. Brand Analysis

Analyzed:

* Brand revenue
* Brand unit sales
* Leading brands
* Revenue concentration among top brands

### 5. Store Analysis

Analyzed:

* Store revenue
* Store transactions
* Store customers
* Top-performing stores

### 6. Pack-Size Analysis

Analyzed revenue and units sold across different product pack sizes.

### 7. Time-Based Analysis

Analyzed:

* Monthly sales
* Day-of-week sales
* Peak periods
* Low-performing periods
* Weekend versus overall sales

### 8. Correlation Analysis

Examined the relationship between:

* Product quantity and transaction revenue
* Pack size and transaction revenue

---

# 📈 Key Insights

## 💰 Overall Sales Performance

The dataset generated approximately:

**$1.93M in total revenue**

with:

* **505,124 units sold**
* **263,127 unique transactions**
* **72,637 unique customers**
* **114 products**
* **272 stores**

The average transaction value was approximately **$7.35**, with an average of **1.92 units per transaction**.

---

## 👥 Customer Retention

Approximately **73.7% of customers made more than one transaction**.

This indicates a strong repeat-purchase base and creates an opportunity for targeted customer retention and loyalty strategies.

---

## 📅 Monthly Sales Performance

### Highest-Revenue Month

**December 2018 — $167,913.40**

### Lowest-Revenue Month

**February 2019 — $150,665.00**

The difference between strong and weak months suggests opportunities for targeted promotions and demand planning.

---

## 🥇 Top Product

The highest-revenue product was:

**Dorito Corn Chp Supreme 380g**

* Revenue: **$40,352**
* Units Sold: **6,509**

---

## 🏆 Top Brand

The highest-revenue brand was:

**Kettle**

* Revenue: **$390,239.80**
* Units Sold: **79,051**

The **top five brands generated approximately 55.3% of total revenue**, demonstrating meaningful brand-level concentration.

---

## 🏪 Top Store

The highest-revenue store was:

**Store 226**

* Revenue: **$18,905.45**
* Transactions: **2,010**

Store-level analysis can be used to identify practices that distinguish stronger-performing locations.

---

## 📦 Best-Performing Pack Size

The highest-revenue pack size was:

**175g**

* Revenue: **$477,112.40**
* Units Sold: **123,692**

Products above **100g accounted for approximately 97.2% of total revenue**.

---

## 📆 Day-of-Week Performance

### Highest-Revenue Day

**Sunday — $283,229.10**

### Lowest-Revenue Day

**Tuesday — $270,644.00**

This indicates that sales performance varies across the week and can support more targeted promotional planning.

---

## 📊 Revenue Concentration

The analysis found:

* Top 10 products contributed approximately **17.9% of total revenue**
* Top 5 brands contributed approximately **55.3% of total revenue**
* The highest-revenue individual product contributed approximately **2.1% of total revenue**

This suggests that brand-level revenue is more concentrated than individual-product revenue.

---

## 🔗 Quantity vs Revenue

The correlation between product quantity and transaction revenue was approximately:

**0.72**

This indicates a strong positive relationship between quantity purchased and transaction revenue.

---

## 🚨 Customer Purchasing Anomaly

Customer **226000** recorded:

* **2 transactions**
* **400 units purchased**
* **$1,300 total sales**

This unusual purchasing pattern should be investigated further to determine whether it represents legitimate bulk purchasing or a potential data-quality issue.

---

# 💡 Business Recommendations

## 1. Improve Low-Performing Periods

Focus promotional campaigns and customer engagement strategies on weaker periods, particularly:

* February
* Lower-performing weekdays such as Tuesday

### Business Benefit

Can help reduce sales fluctuations and improve performance during weaker periods.

---

## 2. Prioritize High-Performing Pack Sizes

Give greater attention to high-performing pack sizes such as **175g**.

Use sales data to support:

* Inventory planning
* Shelf placement
* Promotional bundles
* Product assortment

### Business Benefit

Helps allocate inventory and shelf space toward products with demonstrated customer demand.

---

## 3. Strengthen Leading Brands

Prioritize strong-performing brands such as **Kettle, Smiths, and Doritos** through merchandising and promotional strategies.

### Business Benefit

Protects existing revenue drivers while creating opportunities for cross-selling and product bundling.

---

## 4. Develop Customer Retention Strategies

Since approximately **73.7% of customers are repeat customers**, customer segmentation can be used to identify:

* High-value customers
* Frequent customers
* Low-frequency customers
* Potentially inactive customers

### Business Benefit

Targeted loyalty and engagement strategies can encourage additional purchases and improve customer relationships.

---

## 5. Investigate Unusual Purchasing Behavior

Investigate high-volume customers such as customer **226000**.

### Business Benefit

This can help distinguish legitimate bulk purchases from potential data-quality issues while potentially identifying valuable bulk-buying opportunities.

---

# 📊 Visualizations

The project includes visual analysis of:

* Monthly Sales Trends
* Top 10 Products by Revenue
* Top 10 Brands by Revenue
* Top 10 Stores by Revenue
* Revenue by Pack Size
* Revenue by Day of Week
* Transaction Value Distribution
* Quantity vs Revenue
* Pack Size vs Revenue

---

# 📁 Project Structure

```text
Quantium-Retail-Analytics/
│
├── data/
│   └── QVI_transaction_data.xlsx
│
├── notebook/
│   └── Quantium_EDA.ipynb
│
├── report/
│   └── Quantium_Retail_Analytics_Report.pdf
│
├── images/
│   ├── monthly_sales.png
│   ├── top_products.png
│   ├── top_brands.png
│   ├── top_stores.png
│   └── pack_size_analysis.png
│
└── README.md
```

---

# 🚀 Key Skills Demonstrated

This project demonstrates practical experience in:

* Data Cleaning
* Exploratory Data Analysis
* Data Wrangling
* Feature Engineering
* GroupBy & Aggregation
* Customer Analytics
* Product Analytics
* Brand Analytics
* Store Analytics
* Time-Series Analysis
* Statistical Analysis
* Correlation Analysis
* Data Visualization
* Business Insight Generation
* Recommendation Development

---

# 🎯 Project Outcome

This project demonstrates how raw retail transaction data can be transformed into actionable business insights.

The analysis identified key revenue drivers, customer purchasing patterns, product and brand performance, pack-size preferences, store performance, and temporal sales trends.

The resulting recommendations provide a data-driven foundation for improving:

**Revenue → Customer Retention → Product Strategy → Promotional Planning → Store Performance**

---

## 👨‍💻 Author

**Uttkarsh Mishra**

CSE — Artificial Intelligence & Machine Learning
Galgotias University

### Areas of Interest

* Data Analytics
* Business Intelligence
* SQL
* Python
* Power BI
* Machine Learning

---

⭐ **If you found this project useful, feel free to explore the analysis, notebook, and report.**
