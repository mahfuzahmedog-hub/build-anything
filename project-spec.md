# Build Anything — Web App

## Overview
A web application built with AI-assisted development using the supervisor-agent pattern.

## Tech Stack
- **Backend:** Python + FastAPI
- **Frontend:** HTML + CSS + vanilla JS (served via FastAPI)
- **Database:** SQLite (via SQLAlchemy)
- **Testing:** pytest
- **Linting:** ruff

## Features

### 1. Landing Page
- `/` — Welcome page with description
- Clean, modern dark-theme UI

### 2. Dashboard
- `/dashboard` — Main app interface with dynamic content

### 3. API Endpoints
- `GET /api/status` — Health check + uptime
- `GET /api/items` — List items
- `POST /api/items` — Create an item
- `DELETE /api/items/{id}` — Delete an item

### 4. Database
- SQLite database
- Items table: id, title, description, created_at

## Verification
- [ ] All tests pass: `pytest -q --tb=short`
- [ ] No lint errors: `ruff check .`
- [ ] App starts: `python -c "from app.main import app"`
- [ ] Each API endpoint returns correct status codes
