# 🛒 Simple E-Commerce Analysis Project

**Super simple and efficient e-commerce data analysis!**

---

## 📁 What's Included (4 Files)

1. **simple_data_generator.py** - Creates sample data
2. **simple_analysis.py** - Analyzes data & creates charts
3. **simple_schema.sql** - Database structure
4. **simple_queries.sql** - SQL analysis queries

---

## ⚡ Quick Start (3 Steps!)

### Step 1: Install (30 seconds)
```bash
pip install pandas matplotlib seaborn
```

### Step 2: Generate Data (10 seconds)
```bash
python simple_data_generator.py
```
**Creates 4 CSV files:**
- categories.csv (5 categories)
- products.csv (100 products)
- customers.csv (1,000 customers)
- orders.csv (5,000 orders)

### Step 3: Run Analysis (30 seconds)
```bash
python simple_analysis.py
```
**Creates:**
- ✅ Analysis report in console
- ✅ monthly_sales.csv
- ✅ top_customers.csv
- ✅ sales_dashboard.png

**That's it! 🎉**

---

## 📊 What The Analysis Shows

### Console Output:
1. **Basic Stats** - Total revenue, orders, customers
2. **Monthly Sales** - Sales trends over time
3. **Top 10 Customers** - Best customers
4. **Sales by City** - Geographic breakdown
5. **Order Status** - Delivery statistics

### Visual Dashboard (PNG):
- 📈 Monthly revenue trend
- 🌆 Sales by city
- 🥧 Order status pie chart
- 👥 Top 10 customers bar chart

---

## 🗄️ Using PostgreSQL (Optional)

### Setup Database:
```bash
# Login to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE simple_ecommerce;
\q

# Run schema
psql -U postgres -d simple_ecommerce -f simple_schema.sql
```

### Import Data:
```bash
# Copy CSV to PostgreSQL data directory or use pgAdmin
# Then use COPY command or pgAdmin import wizard
```

### Run Queries:
```bash
psql -U postgres -d simple_ecommerce -f simple_queries.sql
```

---

## 💡 Using Your Own Data

Replace the CSV files with your own! Just match this format:

**categories.csv:**
```
category_id,category_name
1,Electronics
2,Clothing
```

**customers.csv:**
```
customer_id,name,email,city
1,John Smith,john@email.com,New York
```

**products.csv:**
```
product_id,product_name,category_id,price
1,Headphones,1,49.99
```

**orders.csv:**
```
order_id,customer_id,order_date,total_amount,status
1,123,2024-01-15,99.99,Delivered
```

Then run: `python simple_analysis.py`

---

## 🎯 What This Demonstrates

### For Your Resume:
✅ Data cleaning and preprocessing  
✅ SQL database design  
✅ Data analysis with Python  
✅ Data visualization  
✅ Working with CSV files  
✅ Statistical analysis  

### Key Metrics:
✅ Sales performance tracking  
✅ Customer analysis  
✅ Geographic insights  
✅ Trend analysis  

---

## 📈 Sample SQL Queries

**Total Revenue:**
```sql
SELECT SUM(total_amount) AS total_revenue 
FROM orders;
```

**Top 5 Customers:**
```sql
SELECT c.name, SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 5;
```

**Monthly Sales:**
```sql
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
```

---

## 🔧 Troubleshooting

**Error: Module not found?**
```bash
pip install pandas matplotlib seaborn
```

**No CSV files?**
- Make sure you run `python simple_data_generator.py` first

**Charts not showing?**
- Check for `sales_dashboard.png` file
- Open it with any image viewer

---

## 📝 Resume Bullet Points

Use these on your resume:

✨ **E-commerce Data Analysis**
- Analyzed 5,000+ sales transactions using Python and SQL
- Created automated sales reports and visualizations
- Identified top-performing customers and cities
- Designed normalized database schema for efficient data storage
- Generated monthly sales trends and KPI dashboards

---

## 🎓 What You Learn

1. **Python Skills:**
   - pandas for data analysis
   - matplotlib/seaborn for visualization
   - Reading/writing CSV files

2. **SQL Skills:**
   - Database design
   - JOIN operations
   - GROUP BY and aggregations
   - Date functions

3. **Business Analytics:**
   - Sales trend analysis
   - Customer segmentation
   - Performance metrics

---

## 📚 File Details

| File | Lines | Purpose |
|------|-------|---------|
| simple_data_generator.py | ~80 | Creates sample data |
| simple_analysis.py | ~130 | Main analysis script |
| simple_schema.sql | ~40 | Database structure |
| simple_queries.sql | ~120 | Analysis queries |

**Total:** ~370 lines of well-commented code!

---

## ✅ Next Steps

1. Run the 3-step quick start
2. Explore the CSV files
3. Try the SQL queries (optional)
4. Customize with your own data
5. Add to your portfolio!

---

**Good luck! 🚀**

*Simple, efficient, and perfect for your resume!*
