# ---- Base image ----
FROM python:3.11-slim

# Prevents Python from writing .pyc files and enables unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies required by PyMySQL / mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run with the Flask dev server bound to all interfaces
CMD ["python", "-m", "flask", "--app", "src.app:app", "run", "--host", "0.0.0.0", "--port", "5000"]
