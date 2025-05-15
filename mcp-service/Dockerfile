FROM python:3.12-slim

# Set Work Directory
WORKDIR /app

# Install Build-Essential, Curl and Git
RUN apt-get update && apt-get install -y \
    build-essential curl git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Server Code
COPY . . 

# Expose FastAPI Port
EXPOSE 8000

# Run The Server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
