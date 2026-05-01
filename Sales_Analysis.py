import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales.csv")

# Clean data
df['Order Date'] = pd.to_datetime(df['Order Date'])
df = df.dropna()

# Analysis
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print(top_products)

# Visualization
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot()
plt.show()