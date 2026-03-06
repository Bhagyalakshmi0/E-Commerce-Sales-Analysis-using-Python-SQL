"""
Simple E-Commerce Analysis
Easy to understand, efficient analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("📊 E-COMMERCE DATA ANALYSIS")
print("=" * 50)

# Load data
print("\n1️⃣ Loading data...")
categories = pd.read_csv('categories.csv')
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')

# Convert date
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders['month'] = orders['order_date'].dt.to_period('M')

print("✅ Data loaded successfully!")

# ============================================
# BASIC STATISTICS
# ============================================
print("\n2️⃣ BASIC STATISTICS")
print("=" * 50)
print(f"Total Revenue: ${orders['total_amount'].sum():,.2f}")
print(f"Total Orders: {len(orders):,}")
print(f"Average Order: ${orders['total_amount'].mean():.2f}")
print(f"Total Customers: {len(customers):,}")
print(f"Total Products: {len(products):,}")

# ============================================
# MONTHLY SALES
# ============================================
print("\n3️⃣ MONTHLY SALES")
print("=" * 50)
monthly_sales = orders.groupby('month').agg({
    'order_id': 'count',
    'total_amount': 'sum'
}).rename(columns={'order_id': 'orders', 'total_amount': 'revenue'})

print(monthly_sales.tail(6).to_string())

# Save to CSV
monthly_sales.to_csv('monthly_sales.csv')
print("\n💾 Saved to: monthly_sales.csv")

# ============================================
# TOP CUSTOMERS
# ============================================
print("\n4️⃣ TOP 10 CUSTOMERS")
print("=" * 50)
top_customers = orders.groupby('customer_id').agg({
    'order_id': 'count',
    'total_amount': 'sum'
}).rename(columns={'order_id': 'orders', 'total_amount': 'total_spent'})

top_customers = top_customers.merge(customers, on='customer_id')
top_customers = top_customers.nlargest(10, 'total_spent')

for _, row in top_customers.iterrows():
    print(f"{row['name']:20} | ${row['total_spent']:8,.2f} | {row['orders']:2} orders")

# Save to CSV
top_customers.to_csv('top_customers.csv', index=False)
print("\n💾 Saved to: top_customers.csv")

# ============================================
# SALES BY CITY
# ============================================
print("\n5️⃣ SALES BY CITY")
print("=" * 50)
city_sales = orders.merge(customers, on='customer_id')
city_sales = city_sales.groupby('city')['total_amount'].sum().sort_values(ascending=False)

for city, total in city_sales.items():
    print(f"{city:15} | ${total:,.2f}")

# ============================================
# ORDER STATUS
# ============================================
print("\n6️⃣ ORDER STATUS")
print("=" * 50)
status_counts = orders['status'].value_counts()
for status, count in status_counts.items():
    pct = (count / len(orders) * 100)
    print(f"{status:12} | {count:4} orders ({pct:.1f}%)")

# ============================================
# VISUALIZATIONS
# ============================================
print("\n7️⃣ Creating visualizations...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('E-Commerce Sales Dashboard', fontsize=16, fontweight='bold')

# Chart 1: Monthly Revenue
monthly_sales['revenue'].plot(ax=axes[0, 0], marker='o', color='blue', linewidth=2)
axes[0, 0].set_title('Monthly Revenue Trend', fontweight='bold')
axes[0, 0].set_ylabel('Revenue ($)')
axes[0, 0].grid(True, alpha=0.3)

# Chart 2: Sales by City
city_sales.plot(kind='bar', ax=axes[0, 1], color='green')
axes[0, 1].set_title('Revenue by City', fontweight='bold')
axes[0, 1].set_ylabel('Revenue ($)')
axes[0, 1].tick_params(axis='x', rotation=45)

# Chart 3: Order Status
status_counts.plot(kind='pie', ax=axes[1, 0], autopct='%1.1f%%', startangle=90)
axes[1, 0].set_title('Order Status Distribution', fontweight='bold')
axes[1, 0].set_ylabel('')

# Chart 4: Top 10 Customers
top_10 = top_customers.nlargest(10, 'total_spent')
axes[1, 1].barh(range(len(top_10)), top_10['total_spent'].values, color='coral')
axes[1, 1].set_yticks(range(len(top_10)))
axes[1, 1].set_yticklabels(top_10['name'].values)
axes[1, 1].set_xlabel('Total Spent ($)')
axes[1, 1].set_title('Top 10 Customers', fontweight='bold')

plt.tight_layout()
plt.savefig('sales_dashboard.png', dpi=300, bbox_inches='tight')
print("✅ Dashboard saved as: sales_dashboard.png")

print("\n" + "=" * 50)
print("✅ ANALYSIS COMPLETE!")
print("=" * 50)
print("\n📁 Output Files:")
print("   • monthly_sales.csv")
print("   • top_customers.csv")
print("   • sales_dashboard.png")
