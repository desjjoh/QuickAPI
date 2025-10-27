# ⚡ QuickAPI

A minimal, production-ready Python REST API built with **FastAPI**, designed for speed, type safety, and clean architecture.

## 🧭 Overview

QuickAPI demonstrates a lightweight service layout following modern backend conventions:s

- **FastAPI** for asynchronous endpoints and automatic OpenAPI documentation
- **Pydantic Settings** for typed configuration via environment variables
- **Structlog** for structured JSON logging
- Clean modular layout inspired by larger frameworks (e.g., NestJS)

This template serves as a foundation for building small but scalable Python services.

## 📁 Project Structure

quickapi/
├─ app/
│ ├─ api/ # Routers and endpoints
│ ├─ core/ # Config, logging, middleware
│ ├─ models/ # Pydantic schemas
│ └─ main.py # Application entry point
└─ .venv/ # Local virtual environment

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/quickapi.git
cd quickapi
```

### 2. Create a virtual environment

```bash
Copy code
python -m venv .venv
.venv\Scripts\Activate.ps1   # On Windows
```

### 3. Install dependencies

```bash
Copy code
pip install -r requirements.txt
(Or manually: pip install fastapi uvicorn[standard] pydantic-settings structlog)
```

### 4. Run the development server

```bash
Copy code
python -m uvicorn app.main:app --reload
Then open:

Swagger UI → http://127.0.0.1:8000/docs

Root endpoint → http://127.0.0.1:8000/
```

### 5. Example request

```bash
curl http://127.0.0.1:8000/items/42
```

Response:

```json
{
  "id": 42,
  "name": "Widget",
  "price": 10.99
}
```

## ⚙️ Configuration

Environment variables can be defined in a .env file:

```ini
APP_NAME=QuickAPI
DEBUG=true
```

## 🧩 Features Planned

- Request/response logging middleware
- Centralized exception handling
- SQLite or Redis integration for persistence
- Dockerfile for containerized deployment

## 📄 License

MIT © 2025 John Desjardins
You’re free to use, modify, and distribute this project with attribution.
