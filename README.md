# Pressure Service

A FastAPI-based web service for tracking and managing blood pressure measurements. The service allows users to register and log their pressure readings with systolic, diastolic, and pulse measurements.

## Features

- RESTful API for user registration and pressure measurement logging
- SQLAdmin interface for database management
- Type-safe with Pydantic models
- Database migrations with Alembic
- Comprehensive testing with pytest
- Code quality with Ruff, Pyright, and formatting tools

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager (recommended) or pip

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pressure/service
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```


## Running the Application

### Development
To run the application in development mode with auto-reload:
```bash
make dev
```
or directly:
```bash
uv run uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`.

### Production
For production deployment:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Code Quality

### Check Everything
Run all quality checks (linting, formatting, type checking, and lock verification):
```bash
make check
```

### Individual Quality Checks
- **Linting**: `make lint`
- **Formatting**: `make format`
- **Type checking**: `make type-check`
- **Dependency lock**: `make lock`

### Testing
Run tests with coverage:
```bash
make tests
```

## API Endpoints

- `GET /` - Health check endpoint
- `POST /users/` - Register a new user
- `POST /users/{user_id}/pressure/` - Log pressure measurements for a user
- `GET /admin/` - SQLAdmin interface for database management

## Database Configuration

The application uses SQLite by default (`sqlite:///./test.db`). For production, configure a PostgreSQL connection by setting the DATABASE_URL environment variable.

## Development

### Project Structure

- `app/main.py` - FastAPI application entry point
- `app/api/endpoints/` - API route definitions
- `app/schemas/` - Pydantic models for request/response validation
- `app/services/` - Business logic implementation
- `app/db/` - Database models and session management
- `app/admin.py` - SQLAdmin configuration
- `tests/` - Test suite
- `alembic/` - Database migration scripts

### Environment Variables

Use a `.env` file to configure:
- `DATABASE_URL` - Database connection string
- Other environment-specific settings


