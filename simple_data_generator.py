"""
Simple E-Commerce Data Generator
Creates easy-to-understand sample data
"""

import pandas as pd
import random
from datetime import datetime, timedelta

# Set seed for consistent results
random.seed(42)

print("📊 Generating e-commerce data...")

# 1. Categories (simple)
categories = pd.DataFrame({
    'category_id': [1, 2, 3, 4, 5],
    'category_name': ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
})

# 2. Products (100 products)
products = []
product_names = {
    'Electronics': ['Headphones', 'Charger', 'Mouse', 'Keyboard', 'Speaker'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Shoes', 'Dress'],
    'Home': ['Coffee Maker', 'Blender', 'Toaster', 'Lamp', 'Pillow'],
    'Books': ['Novel', 'Cookbook', 'Biography', 'Comic', 'Magazine'],
    'Sports': ['Yoga Mat', 'Water Bottle', 'Dumbbells', 'Ball', 'Shoes']
}

product_id = 1
for cat_id, cat_name in zip(categories['category_id'], categories['category_name']):
    for prod_name in product_names[cat_name]:
        for i in range(4):  # 4 variants of each
            products.append({
                'product_id': product_id,
                'product_name': f'{prod_name} - Type {i+1}',
                'category_id': cat_id,
                'price': round(random.uniform(10, 200), 2)
            })
            product_id += 1

products_df = pd.DataFrame(products)

# 3. Customers (1000 customers)
first_names = ['John', 'Jane', 'Mike', 'Emily', 'David', 'Sarah', 'Chris', 'Lisa']
last_names = ['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson', 'Moore', 'Taylor']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

customers = pd.DataFrame({
    'customer_id': range(1, 1001),
    'name': [f'{random.choice(first_names)} {random.choice(last_names)}' for _ in range(1000)],
    'email': [f'customer{i}@email.com' for i in range(1, 1001)],
    'city': [random.choice(cities) for _ in range(1000)]
})

# 4. Orders (5000 orders over last year)
orders = []
start_date = datetime.now() - timedelta(days=365)

for order_id in range(1, 5001):
    order_date = start_date + timedelta(days=random.randint(0, 365))
    customer_id = random.randint(1, 1000)
    
    # Each order has 1-3 items
    num_items = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    total = 0
    
    for _ in range(num_items):
        product = products_df.sample(1).iloc[0]
        quantity = random.randint(1, 2)
        total += product['price'] * quantity
    
    orders.append({
        'order_id': order_id,
        'customer_id': customer_id,
        'order_date': order_date.strftime('%Y-%m-%d'),
        'total_amount': round(total, 2),
        'status': random.choices(['Delivered', 'Shipped', 'Processing'], weights=[0.7, 0.2, 0.1])[0]
    })

orders_df = pd.DataFrame(orders)

# Save to CSV
categories.to_csv('categories.csv', index=False)
products_df.to_csv('products.csv', index=False)
customers.to_csv('customers.csv', index=False)
orders_df.to_csv('orders.csv', index=False)

print(f"✅ Done! Created:")
print(f"   📁 categories.csv - {len(categories)} categories")
print(f"   📁 products.csv - {len(products_df)} products")
print(f"   📁 customers.csv - {len(customers)} customers")
print(f"   📁 orders.csv - {len(orders_df)} orders")
