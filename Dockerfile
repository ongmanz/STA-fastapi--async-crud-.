# Python base image 3.9
FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git

# Clone GitHub repository
RUN git clone https://github.com/ongmanz/STA-fastapi-async-crud.git /app

# Working directory to /app
WORKDIR /app

# Install dependencies from requirements.txt
# RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir fastapi uvicorn SQLAlchemy pydantic

# Open port 8000 for FastAPI
EXPOSE 8000

# Run container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
