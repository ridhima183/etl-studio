<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:1a0b2e,50:5b21b6,100:a855f7&height=260&section=header&text=etl-Studio&fontSize=68&fontColor=f3e8ff&fontAlignY=38&desc=CSV%20%2B%20API%20%E2%86%92%20Pandas%20%E2%86%92%20MySQL%20%7C%20A%20Beginner-Friendly%20ETL%20Pipeline&descSize=17&descAlignY=58&animation=fadeIn" />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=900&color=C084FC&center=true&vCenter=true&width=650&lines=Extract+%E2%86%92+Transform+%E2%86%92+Load;CSV+%2B+REST+API+%E2%86%92+One+Clean+Dataset;Deduplicated.+Validated.+Production-Minded.;Built+with+Python+%2B+Pandas+%2B+Flask+%2B+MySQL" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-6D28D9?style=for-the-badge&logo=python&logoColor=E9D5FF)](#)
[![Flask](https://img.shields.io/badge/Flask-REST_API-7C3AED?style=for-the-badge&logo=flask&logoColor=E9D5FF)](#)
[![Pandas](https://img.shields.io/badge/Pandas-Transform-8B5CF6?style=for-the-badge&logo=pandas&logoColor=E9D5FF)](#)
[![MySQL](https://img.shields.io/badge/MySQL-Storage-9333EA?style=for-the-badge&logo=mysql&logoColor=E9D5FF)](#)
[![Pytest](https://img.shields.io/badge/Pytest-9%20passed-A855F7?style=for-the-badge&logo=pytest&logoColor=E9D5FF)](#)

<img src="https://img.shields.io/badge/status-validated_%E2%9C%94-c084fc?style=flat-square&labelColor=2e1065" />
<img src="https://img.shields.io/badge/final_records-10-c084fc?style=flat-square&labelColor=2e1065" />
<img src="https://img.shields.io/badge/duplicates_removed-1-c084fc?style=flat-square&labelColor=2e1065" />
<img src="https://img.shields.io/badge/tests-9%2F9_passing-c084fc?style=flat-square&labelColor=2e1065" />

</div>

<br/>

## 🔮 What is DataWeave?

> Two messy, disconnected data sources walk into a pipeline... and leave as **one clean, validated, deduplicated dataset.**

**DataWeave** is a hands-on, fully-documented **ETL (Extract → Transform → Load)** pipeline that shows what actually happens when data engineers merge data from multiple systems in the real world — a legacy **CSV export** and a live **REST API** — clean it with **Pandas**, enforce **business rules + validation**, and load it safely into **MySQL**.

No black boxes. Every transformation, every dedup rule, every validation check is broken down step-by-step.

<table>
<tr>
<td width="50%" valign="top">

### 🧵 The Problem
Real companies pull customer data from:
- 🗂️ Legacy databases → **CSV**
- 🌐 CRMs / websites → **API**
- 📊 Marketing tools → Excel

...and it's full of duplicates, casing chaos, stray whitespace, and broken emails.

</td>
<td width="50%" valign="top">

### 🧶 The Solution
```
Collect → Clean → Combine
   → Validate → Store
```
A single, testable, modular pipeline — the same shape used in production data platforms.

</td>
</tr>
</table>

---

## 🕸️ Architecture at a Glance

```mermaid
flowchart TB
    subgraph SOURCES["🌌 DATA SOURCES"]
        direction LR
        CSV[("📄 customers.csv<br/>6 records")]
        API[("🔌 Flask REST API<br/>/customers • 5 records")]
    end

    CSV -->|Extract| EX1["etl/extract_csv.py"]
    API -->|Extract| EX2["etl/extract_api.py"]

    EX1 --> COMBINE
    EX2 --> COMBINE

    COMBINE["🧬 Combine<br/>6 + 5 = 11 rows"] --> CLEAN

    subgraph TRANSFORM["🪄 TRANSFORM  ·  etl/transform.py"]
        CLEAN["✨ Clean & Strip Text"] --> NORM["📧 Normalize Emails"]
        NORM --> IDS["🔢 Coerce Customer IDs"]
        IDS --> PRIORITY["⚖️ Apply Source Priority<br/><i>API wins over CSV</i>"]
        PRIORITY --> DEDUPE["🧹 Deduplicate<br/>11 → 10 rows"]
    end

    DEDUPE --> VALIDATE

    subgraph VALIDATION["🛡️ VALIDATE  ·  etl/validate.py"]
        VALIDATE["Check: empty? nulls?<br/>duplicate IDs? bad emails?"]
    end

    VALIDATE -->|✅ PASSED| LOAD[("🗄️ MySQL<br/>api_etl_demo.customers")]
    VALIDATE -->|❌ FAILED| STOP["🛑 Pipeline Halts"]

    classDef source fill:#4c1d95,stroke:#c084fc,color:#f3e8ff,stroke-width:2px
    classDef process fill:#5b21b6,stroke:#a855f7,color:#f3e8ff,stroke-width:2px
    classDef transform fill:#6d28d9,stroke:#d8b4fe,color:#f3e8ff,stroke-width:2px
    classDef validate fill:#7c3aed,stroke:#e9d5ff,color:#f3e8ff,stroke-width:2px
    classDef terminal fill:#2e1065,stroke:#c084fc,color:#e9d5ff,stroke-width:2px

    class CSV,API source
    class EX1,EX2,COMBINE process
    class CLEAN,NORM,IDS,PRIORITY,DEDUPE transform
    class VALIDATE validate
    class LOAD,STOP terminal
```

---

## 🧿 The Deduplication Rule — API Always Wins

The heart of `transform.py`. When the same `customer_id` appears in **both** sources, the API record is treated as the freshest truth.

```mermaid
sequenceDiagram
    participant C as 📄 CSV Record (103)
    participant A as 🔌 API Record (103)
    participant T as 🪄 transform()
    participant M as 🗄️ MySQL

    C->>T: Suresh Old · old@example.com · Hyderabad
    A->>T: Suresh New · new@example.com · Bengaluru
    Note over T: sort by (customer_id, source_priority)<br/>API priority = 1 > CSV priority = 0
    T->>T: drop_duplicates(keep="last")
    T->>M: ✅ Suresh New · new@example.com · Bengaluru
    Note over M: CSV version is discarded —<br/>API is the source of truth
```

---

## 🌠 Full Execution Flow

```mermaid
flowchart LR
    A["▶️ python app.py"] --> B["Flask server up<br/>127.0.0.1:5000"]
    B --> C["▶️ python -m scripts.run_etl"]
    C --> D["Extract CSV<br/>6 records"]
    C --> E["Extract API<br/>5 records"]
    D --> F["Transform<br/>11 → 10 rows"]
    E --> F
    F --> G{"Validate"}
    G -->|Pass| H["Load to MySQL"]
    G -->|Fail| I["🛑 Halt + report errors"]
    H --> J["✅ LOAD COMPLETED"]

    style A fill:#2e1065,stroke:#c084fc,color:#f3e8ff
    style B fill:#4c1d95,stroke:#c084fc,color:#f3e8ff
    style C fill:#2e1065,stroke:#c084fc,color:#f3e8ff
    style D fill:#5b21b6,stroke:#a855f7,color:#f3e8ff
    style E fill:#5b21b6,stroke:#a855f7,color:#f3e8ff
    style F fill:#6d28d9,stroke:#d8b4fe,color:#f3e8ff
    style G fill:#7c3aed,stroke:#e9d5ff,color:#f3e8ff
    style H fill:#9333ea,stroke:#f3e8ff,color:#f3e8ff
    style I fill:#3b0764,stroke:#f472b6,color:#fce7f3
    style J fill:#a855f7,stroke:#f3e8ff,color:#f3e8ff
```

---

## 🪐 Project Structure

```
api_etl_project-main/
│
├── 🌸 app.py                     # Flask REST API (the second data source)
├── 📜 requirements.txt
├── 🔐 .env / .env.example
│
├── 📁 data/
│   ├── api_customers.json       # API's backing store (5 records)
│   └── customers.csv            # Legacy export (6 records)
│
├── 🧪 etl/
│   ├── extract_csv.py           # Reads + schema-checks the CSV
│   ├── extract_api.py           # Calls the API, handles timeouts/errors
│   ├── transform.py             # Combine · clean · dedupe (the heart 💜)
│   ├── validate.py              # Quality gate before loading
│   └── load.py                  # SQLAlchemy → MySQL
│
├── 🚀 scripts/
│   └── run_etl.py               # Orchestrator — runs every stage in order
│
├── 🗃️ sql/
│   ├── 01_create_database.sql
│   └── 02_validation_queries.sql
│
└── 🧵 tests/
    ├── test_api.py              # Flask endpoint tests
    ├── test_etl.py              # Proves "API wins" dedup rule
    └── test_validation.py       # Quality-check tests
```

---

## 🔬 Tech Stack

<div align="center">

| Layer | Technology | Why |
|:--|:--|:--|
| 🌐 API | **Flask** | Lightweight REST layer simulating a real CRM/website source |
| 🐼 Transform | **Pandas** | Combine, clean, normalize, deduplicate at scale |
| 🔗 HTTP | **Requests** | Talks to the Flask API with timeout protection |
| 🗄️ Database | **MySQL** | Final structured destination, `customer_id` as primary key |
| 🧩 ORM | **SQLAlchemy + PyMySQL** | Safe, pooled connection between Python and MySQL |
| 🔑 Config | **python-dotenv** | Keeps credentials out of source code |
| ✅ Testing | **Pytest** | 9 automated tests across API, transform, and validation |

</div>

---

## 🌙 API Reference

<div align="center">

| Method | Endpoint | Purpose | Success | Failure |
|:--|:--|:--|:--:|:--:|
| `GET` | `/health` | Liveness check | `200` | — |
| `GET` | `/customers` | List all (supports `?city=`) | `200` | — |
| `GET` | `/customers/<id>` | Fetch one customer | `200` | `404` |
| `POST` | `/customers` | Create a customer | `201` | `400` / `409` |
| `PUT` | `/customers/<id>` | Update fields (merge patch) | `200` | `404` |
| `DELETE` | `/customers/<id>` | Remove a customer | `204` | `404` |

</div>

---

## 🛡️ Validation Gate

Before anything touches MySQL, every row must survive:

- 🚫 **Not empty** — the dataset itself can't be blank
- 🆔 **No null `customer_id`** — it's the primary key
- 🧬 **No duplicate IDs** — uniqueness is non-negotiable
- ✍️ **Required text fields present** — name, city, state
- 📧 **Valid email format** — checked via regex `^[^@\s]+@[^@\s]+\.[^@\s]+$`

```
Transform → Validate → Load
     (never Load → "oops, bad data" 🙅‍♀️)
```

---

## 📈 Sample Run

<div align="center">

```
════════════════════════════════════════════════════════
   CSV + API → Pandas → MySQL ETL
════════════════════════════════════════════════════════
CSV records: 6
API records: 5
Final records after deduplication: 10
VALIDATION PASSED
LOAD COMPLETED
```

```
✅ 9 passed in 5s
```

</div>

---

## ⚡ Quickstart

```bash
# 1️⃣ Create + activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows PowerShell

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Configure environment
cp .env.example .env           # then set your MySQL password

# 4️⃣ Create the database
mysql -u root -p < sql/01_create_database.sql

# 5️⃣ Start the API   (Terminal 1 — keep running)
python app.py

# 6️⃣ Run the pipeline   (Terminal 2)
python -m scripts.run_etl

# 7️⃣ Run the test suite
pytest -q
```

---

## 🔮 Roadmap

<table>
<tr>
<td valign="top" width="33%">

**⚙️ Engineering**
- Database upserts
- Retry mechanisms
- Structured logging
- API authentication

</td>
<td valign="top" width="33%">

**☁️ Infrastructure**
- Docker containers
- Airflow / Prefect scheduling
- Cloud deployment (AWS/Azure/GCP)
- CI/CD via GitHub Actions

</td>
<td valign="top" width="33%">

**📊 Visibility**
- React dashboard
- Data quality metrics
- Pipeline run history
- Monitoring & alerts

</td>
</tr>
</table>

---

## 💜 One-Minute Interview Summary

> A Python-based ETL pipeline that merges customer data from a CSV file and a Flask REST API. Pandas handles cleaning, email/ID normalization, and deduplication — with the API treated as the source of truth for conflicting records. Before loading, the pipeline runs quality checks for nulls, duplicate keys, and malformed emails, then loads the validated dataset into MySQL via SQLAlchemy — all backed by an automated Pytest suite covering the API, transformation logic, and validation rules.

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:a855f7,50:5b21b6,100:1a0b2e&height=140&section=footer" width="100%"/>

**Extract → Transform → Load, woven with 💜**

</div>
