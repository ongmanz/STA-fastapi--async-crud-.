# STA-fastapi-async-crud
FastAPI technical test for SRI TRANG

### Installation

_To use this APIs please following these steps._

1. Clone the repo
   ```sh
   git clone https://github.com/ongmanz/STA-fastapi-async-crud.git
   ```
2. Install dependency packages
   ```sh
   pip install fastapi sqlalchemy uvicorn pydantic pytest pytest-asyncio httpx
   ```
3. To start APIs service
   ```sh
   uvicorn main:app --reload
   ```

If docker below
1. Create docker image
   ```sh
   docker build -t sta-fastapi-app .
   ```
2. Run docker container
   ```sh
   docker run -d -p 8000:8000 sta-fastapi-app
   ```

## How it work

This APIs available at port 8000.
Using SQLite for database engine with schema
   ```sh
   id integer,
   name text,
   description text
   ```

To start backend engine.
   ```sh
   uvicorn main:app --reload
   ```

To list all users.
   ```sh
   curl -X "GET" "http://127.0.0.1:8000/users/?limit=10" -H "accept: application/json"
   ```

To add new user.
   ```sh
   curl -X "POST" "http://127.0.0.1:8000/users/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name": "test01", "description": "Test01 description"}'
   ```

To update user.
   ```sh
   curl -X 'PUT' \
   'http://127.0.0.1:8000/users/1' \
   -H 'accept: application/json' \
   -H 'Content-Type: application/json' \
   -d '{
   "name": "001",
   "description": "001"
   }'
   ```

To delete user.
   ```sh
   curl -X 'DELETE' \
   'http://127.0.0.1:8000/users/1' \
   -H 'accept: application/json'
   ```

To use web interface to test access below
   ```sh
   http://127.0.0.1:8000/docs
   ```

## Unit test

This project using pytest and pytest-asyncio for unit test.
Details of unit test available in `test_api.py`

To run unit test
   ```sh
   pytest
   ```

* Need to backup `users.db` then REMOVE `users.db` before start APIs services and unit test run