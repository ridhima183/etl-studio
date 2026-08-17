USE api_etl_demo;

SELECT COUNT(*) AS total_customers FROM customers;

SELECT customer_id, COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT COUNT(*) AS null_customer_ids
FROM customers
WHERE customer_id IS NULL;

SELECT COUNT(*) AS null_customer_names
FROM customers
WHERE customer_name IS NULL;

SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
ORDER BY customer_count DESC;

SELECT state, COUNT(*) AS customer_count
FROM customers
GROUP BY state
ORDER BY customer_count DESC;

SELECT customer_id, email
FROM customers
WHERE email IS NULL OR email NOT LIKE '%@%';
