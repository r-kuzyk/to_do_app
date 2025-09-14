# 📝 Todo API (FastAPI + PostgreSQL + JWT)

A simple **Todo REST API** built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.  
Supports authentication with **JWT tokens**, CRUD operations on todos, pagination, and filtering.

---

## 🚀 Features
- User registration & login (JWT auth)
- CRUD operations for Todos
- Pagination (`skip`, `limit`)
- Filtering by `completed` status
- PostgreSQL with SQLAlchemy ORM
- Alembic migrations
- Unit tests with Pytest

---

## 📦 Installation

### 1. Clone repo
```bash
git clone https://github.com/r-kuzyk/to_do_app.git
cd todo_api
```

### 2. Create virtual environment & install dependencies
```bash
python -m venv .venv
source .venv/bin/activate   # on macOS/Linux
.venv\Scripts\activate      # on Windows
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the project root with the following variables:
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 4. Run migrations
```bash
alembic upgrade head
```

### 5. Start the server
```bash
uvicorn app.main:app --reload
```

### 6. Test the API
```bash
pytest -v
```