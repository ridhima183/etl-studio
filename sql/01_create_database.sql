CREATE DATABASE IF NOT EXISTS api_etl_demo;
USE api_etl_demo;

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(120) NOT NULL,
    email VARCHAR(160),
    city VARCHAR(80) NOT NULL,
    state VARCHAR(80) NOT NULL
);
