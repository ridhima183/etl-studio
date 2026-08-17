# REST API + Flask + API-Based ETL

Hands-on project based on the REST API / Flask / API ETL training presentation.

## Architecture

```text
Flask REST API
      |
      v
   requests
      |
      +---------+
      |         |
      v         v
    JSON       CSV
      \         /
       \       /
        Pandas
           |
           v
       Transform
           |
           v
        Validate
           |
           v
         MySQL
           |
           v
     SQL Validation
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create the database:

```bash
mysql -u root -p < sql/01_create_database.sql
```

Configure credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```text
TARGET_DB_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/api_etl_demo
```

Do not commit `.env`.

## Start API

```bash
python3 app.py
```

API base URL:

```text
http://127.0.0.1:5000
```

Try:

```bash
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/customers
curl http://127.0.0.1:5000/customers/101
curl "http://127.0.0.1:5000/customers?city=Hyderabad"
```

## Run ETL

Keep Flask running and use another terminal:

```bash
source venv/bin/activate
python3 -m scripts.run_etl
```

The ETL performs:

1. CSV extraction
2. API extraction
3. CSV + API combination
4. Transformation
5. Deduplication
6. Validation
7. MySQL load

When the same `customer_id` exists in both sources, the API record is treated as the latest/preferred record.

## Validate SQL

```bash
mysql -u root -p < sql/02_validation_queries.sql
```

## Run tests

```bash
pytest -q
```

## API as Data Sink

```bash
curl -X POST http://127.0.0.1:5000/customers   -H "Content-Type: application/json"   -d '{"customer_id":111,"customer_name":"New Customer","email":"new@example.com","city":"Hyderabad","state":"Telangana"}'
```

Expected status: `201`.

## Learning Outcomes

practice REST, HTTP methods, Flask routing, JSON, requests, Pandas, CSV/API integration, validation, SQLAlchemy, MySQL and pytest.

## Production extensions

Authentication, pagination, retries/backoff, rate limiting, structured logging, secret management, transactions, observability and CI/CD.
