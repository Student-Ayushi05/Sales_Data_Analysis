import pandas as pd

#Load dataset
df = pd.read_csv("sales_data.csv")

#Handle missing values
df.fillna(0, inplace=True)

#Total Sales
total_sales = df["Total_Sales"].sum()

#Best Selling Product
best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)

print("~~~~~ SALES REPORT ~~~~~")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Best Selling Product: {best_product}")

