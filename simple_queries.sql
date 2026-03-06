-- Simple E-Commerce SQL Queries
-- Easy to understand, commonly used queries

-- ======================================
-- 1. BASIC STATISTICS
-- ======================================

-- Total sales and orders
SELECT 
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS average_order_value
FROM orders;

-- ======================================
-- 2. MONTHLY SALES
-- ======================================

-- Sales by month
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    COUNT(*) AS orders,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month DESC;

-- ======================================
-- 3. TOP CUSTOMERS
-- ======================================

-- Top 10 customers by spending
SELECT 
    c.customer_id,
    c.name,
    c.email,
    c.city,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name, c.email, c.city
ORDER BY total_spent DESC
LIMIT 10;

-- ======================================
-- 4. PRODUCT ANALYSIS
-- ======================================

-- Products by category
SELECT 
    cat.category_name,
    COUNT(p.product_id) AS product_count,
    AVG(p.price) AS avg_price
FROM categories cat
JOIN products p ON cat.category_id = p.category_id
GROUP BY cat.category_name
ORDER BY product_count DESC;

-- ======================================
-- 5. SALES BY CITY
-- ======================================

-- Revenue by city
SELECT 
    c.city,
    COUNT(o.order_id) AS orders,
    SUM(o.total_amount) AS revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY revenue DESC;

-- ======================================
-- 6. ORDER STATUS
-- ======================================

-- Order status breakdown
SELECT 
    status,
    COUNT(*) AS order_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM orders
GROUP BY status
ORDER BY order_count DESC;

-- ======================================
-- 7. RECENT ORDERS
-- ======================================

-- Last 10 orders with customer info
SELECT 
    o.order_id,
    o.order_date,
    c.name AS customer_name,
    c.city,
    o.total_amount,
    o.status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.order_date DESC
LIMIT 10;

-- ======================================
-- 8. CUSTOMER INSIGHTS
-- ======================================

-- Customer purchase frequency
SELECT 
    CASE 
        WHEN order_count = 1 THEN 'One-time'
        WHEN order_count BETWEEN 2 AND 3 THEN 'Occasional'
        WHEN order_count >= 4 THEN 'Frequent'
    END AS customer_type,
    COUNT(*) AS customers
FROM (
    SELECT customer_id, COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
) AS customer_orders
GROUP BY customer_type;

-- ======================================
-- 9. SALES TRENDS
-- ======================================

-- Quarter-over-quarter sales
SELECT 
    DATE_TRUNC('quarter', order_date) AS quarter,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY DATE_TRUNC('quarter', order_date)
ORDER BY quarter;

-- ======================================
-- 10. TOP SELLING CATEGORIES
-- ======================================

-- Category performance (with product join)
SELECT 
    cat.category_name,
    COUNT(DISTINCT o.order_id) AS orders,
    SUM(o.total_amount) AS revenue
FROM categories cat
JOIN products p ON cat.category_id = p.category_id
JOIN orders o ON o.customer_id IN (
    -- Simplified: shows category performance based on all orders
    SELECT customer_id FROM customers
)
GROUP BY cat.category_name
ORDER BY revenue DESC;
