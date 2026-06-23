
#  NL2SQL App (Natural Language to SQL)

A backend system that converts natural language questions into SQL queries using an LLM, safely executes them on a PostgreSQL database, and returns structured results via a FastAPI API.

---

##  Features

- Convert natural language → SQL using LLM
- SQL safety validation layer (prevents unsafe queries)
- FastAPI backend for REST APIs
- PostgreSQL database integration
- Modular and scalable architecture

---

##  Architecture

User Input (Natural Language)  
→ LLM (Generate SQL)  
→ SQL Validator (Safety Check)  
→ FastAPI Backend  
→ PostgreSQL Database  
→ JSON Response  

---

##  Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- OpenAI API
- SQLGlot

---

##  Project Structure

backend/
│
├── app/
│   ├── main.py            # FastAPI entry point
│   ├── config.py          # Environment variables
│   ├── db.py              # Database connection
│   ├── models.py          # DB models
│   ├── schemas.py         # Request/Response models
│   ├── llm.py             # NLP → SQL conversion
│   ├── sql_validator.py   # SQL safety checks
│   ├── services.py        # Core business logic
│   └── routers/
│       └── query.py       # API endpoints
│
├── requirements.txt
└── .env

---

##  Installation & Setup


### 1. Clone Repository
```bash
git clone https://github.com/your-username/nl2sql-app.git
cd nl2sql-app/backend
```bash
git clone https://github.com/your-username/nl2sql-app.git
cd nl2sql-app/backend
