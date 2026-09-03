import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(
    r"C:\Users\lenovo\Desktop\quantrium projet\QVI_transaction_data.xlsx"
)
df["DATE"] = pd.to_datetime(df["DATE"], unit="D", origin="1899-12-30")
df["PACK_SIZE_G"] = pd.to_numeric(
    df["PROD_NAME"].str.extract(r"(\d+)\s*g", expand=False),
    errors="coerce"
)
df["BRAND"] = df["PROD_NAME"].str.split().str[0]
df["MONTH"] = df["DATE"].dt.to_period("M").astype(str)
df["DAY"] = df["DATE"].dt.day_name()
df["WEEKEND"] = df["DATE"].dt.dayofweek >= 5

df = df.drop_duplicates()

total_sales = df["TOT_SALES"].sum()
total_units = df["PROD_QTY"].sum()
total_transactions = df["TXN_ID"].nunique()
total_customers = df["LYLTY_CARD_NBR"].nunique()
total_products = df["PROD_NBR"].nunique()
total_stores = df["STORE_NBR"].nunique()

transaction_summary = df.groupby("TXN_ID").agg(
    sales=("TOT_SALES", "sum"),
    units=("PROD_QTY", "sum")
)

customer_summary = df.groupby("LYLTY_CARD_NBR").agg(
    sales=("TOT_SALES", "sum"),
    transactions=("TXN_ID", "nunique"),
    units=("PROD_QTY", "sum")
)

monthly = df.groupby("MONTH").agg(
    sales=("TOT_SALES", "sum"),
    units=("PROD_QTY", "sum"),
    transactions=("TXN_ID", "nunique")
)

product_summary = df.groupby(
    ["PROD_NBR", "PROD_NAME"]
).agg(
    sales=("TOT_SALES", "sum"),
    units=("PROD_QTY", "sum"),
    transactions=("TXN_ID", "nunique")
).sort_values("sales", ascending=False)

brand_summary = df.groupby("BRAND").agg(
    sales=("TOT_SALES", "sum"),
    units=("PROD_QTY", "sum")
).sort_values("sales", ascending=False)

store_summary = df.groupby("STORE_NBR").agg(
    sales=("TOT_SALES", "sum"),
    units=("PROD_QTY", "sum"),
    transactions=("TXN_ID", "nunique"),
    customers=("LYLTY_CARD_NBR", "nunique")
).sort_values("sales", ascending=False)

pack_summary = df.groupby("PACK_SIZE_G").agg(
    sales=("TOT_SALES", "sum"),
    units=("PROD_QTY", "sum")
).sort_values("sales", ascending=False)

day_summary = df.groupby("DAY")["TOT_SALES"].sum()

avg_transaction_value = transaction_summary["sales"].mean()
avg_units_transaction = transaction_summary["units"].mean()
median_transaction_value = transaction_summary["sales"].median()

repeat_customer_rate = (
    (customer_summary["transactions"] > 1).mean() * 100
)

peak_month = monthly["sales"].idxmax()
peak_month_sales = monthly["sales"].max()

lowest_month = monthly["sales"].idxmin()
lowest_month_sales = monthly["sales"].min()

top_product = product_summary.index[0][1]
top_product_sales = product_summary.iloc[0]["sales"]

top_brand = brand_summary.index[0]
top_brand_sales = brand_summary.iloc[0]["sales"]

top_store = store_summary.index[0]
top_store_sales = store_summary.iloc[0]["sales"]

top_pack = pack_summary.index[0]
top_pack_sales = pack_summary.iloc[0]["sales"]

top_product_share = top_product_sales / total_sales * 100

top_5_brand_share = (
    brand_summary.head(5)["sales"].sum() / total_sales * 100
)

top_10_product_share = (
    product_summary.head(10)["sales"].sum() / total_sales * 100
)

weekend_sales = df.loc[df["WEEKEND"], "TOT_SALES"].sum()
weekend_sales_share = weekend_sales / total_sales * 100

large_pack_sales = df.loc[
    df["PACK_SIZE_G"] > 100,
    "TOT_SALES"
].sum()

large_pack_share = large_pack_sales / total_sales * 100

quantity_sales_correlation = (
    df["PROD_QTY"].corr(df["TOT_SALES"])
)

pack_sales_correlation = (
    df["PACK_SIZE_G"].corr(df["TOT_SALES"])
)

peak_day = day_summary.idxmax()
peak_day_sales = day_summary.max()

lowest_day = day_summary.idxmin()
lowest_day_sales = day_summary.min()

outlier_customer = customer_summary["units"].idxmax()
outlier_units = customer_summary.loc[outlier_customer, "units"]
outlier_sales = customer_summary.loc[outlier_customer, "sales"]
outlier_transactions = customer_summary.loc[
    outlier_customer,
    "transactions"
]

insights = {

    "Basic Insights": [
        f"1. Total revenue generated was ${total_sales:,.2f}.",
        f"2. Total units sold were {total_units:,}.",
        f"3. The dataset contains {total_transactions:,} transactions.",
        f"4. The business served {total_customers:,} unique customers.",
        f"5. The product portfolio contains {total_products:,} unique products.",
        f"6. The business operates across {total_stores:,} stores.",
        f"7. Average transaction value was ${avg_transaction_value:.2f}.",
        f"8. Customers purchased an average of {avg_units_transaction:.2f} units per transaction.",
        f"9. Median transaction value was ${median_transaction_value:.2f}.",
        f"10. {repeat_customer_rate:.1f}% of customers made more than one purchase."
    ],

    "Business Insights": [
        f"11. {peak_month} was the highest-revenue month with ${peak_month_sales:,.2f} in sales.",
        f"12. {lowest_month} was the lowest-revenue month with ${lowest_month_sales:,.2f} in sales.",
        f"13. {top_product} was the top-performing product with ${top_product_sales:,.2f} in revenue.",
        f"14. {top_brand} was the leading brand with ${top_brand_sales:,.2f} in revenue.",
        f"15. Store {top_store} generated the highest store-level revenue at ${top_store_sales:,.2f}.",
        f"16. {int(top_pack)}g was the highest-revenue pack size with ${top_pack_sales:,.2f} in sales.",
        f"17. The top 5 brands contributed {top_5_brand_share:.2f}% of total revenue.",
        f"18. The top 10 products contributed {top_10_product_share:.2f}% of total revenue.",
        f"19. Weekend purchases contributed {weekend_sales_share:.2f}% of total revenue.",
        f"20. Product quantity and sales showed a correlation of {quantity_sales_correlation:.2f}."
    ],

    "Recommendations": [
        f"21. Increase promotional activity around {peak_month} and other high-performing periods to capitalize on stronger customer demand.",
        f"22. Prioritize {int(top_pack)}g products in promotions and shelf placement because this pack size generated the highest revenue.",
        f"23. Strengthen partnerships and promotional campaigns around {top_brand}, while using other brands to diversify the revenue mix.",
        f"24. Investigate customer {outlier_customer}, who purchased {outlier_units:,} units across {outlier_transactions} transactions and generated ${outlier_sales:,.2f}, to determine whether this represents legitimate bulk purchasing or a data anomaly.",
        f"25. Develop targeted promotions for {lowest_day} and {lowest_month} to improve performance during weaker demand periods."
    ]
}

print("\n" + "=" * 90)
print("TOP 25 BUSINESS INSIGHTS")
print("=" * 90)

for category, category_insights in insights.items():
    print(f"\n{category.upper()}")
    print("-" * 90)

    for insight in category_insights:
        print(insight)

plt.figure(figsize=(12, 6))
plt.plot(
    monthly.index,
    monthly["sales"],
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(
    product_summary.head(10).index.get_level_values("PROD_NAME"),
    product_summary.head(10)["sales"]
)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=75, ha="right")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(
    brand_summary.head(10).index,
    brand_summary.head(10)["sales"]
)
plt.title("Top 10 Brands by Revenue")
plt.xlabel("Brand")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(
    store_summary.head(10).index.astype(str),
    store_summary.head(10)["sales"]
)
plt.title("Top 10 Stores by Revenue")
plt.xlabel("Store")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(
    pack_summary.index.astype(str),
    pack_summary["sales"]
)
plt.title("Revenue by Pack Size")
plt.xlabel("Pack Size (g)")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_plot = day_summary.reindex(day_order)

plt.figure(figsize=(10, 6))
plt.bar(
    day_plot.index,
    day_plot.values
)
plt.title("Revenue by Day of Week")
plt.xlabel("Day")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(
    transaction_summary["sales"],
    bins=40
)
plt.title("Transaction Value Distribution")
plt.xlabel("Transaction Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(
    df["PROD_QTY"],
    df["TOT_SALES"],
    alpha=0.25
)
plt.title("Quantity vs Revenue")
plt.xlabel("Product Quantity")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(
    df["PACK_SIZE_G"],
    df["TOT_SALES"],
    alpha=0.25
)
plt.title("Pack Size vs Revenue")
plt.xlabel("Pack Size (g)")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()