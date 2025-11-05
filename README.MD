# FastAPI To-Do App (Postgres)

## Overview
Simple To-Do REST API built with FastAPI and PostgreSQL using SQLAlchemy.

## Requirements
- Python 3.9+
- PostgreSQL (or use provided docker-compose)
- pip

## Setup (quick)
1. Clone or copy project files.
2. Copy `.env.example` to `.env` and adjust values OR set env variables.
3. Start Postgres:
   - Option A (recommended quick): `docker compose up -d`
   - Option B: use your own Postgres & set `DATABASE_URL` in `.env`

4. Create virtualenv & install:
