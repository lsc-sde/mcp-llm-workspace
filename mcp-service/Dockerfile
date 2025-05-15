FROM python:3.12-slim

# Set Work Directory
WORKDIR /app

# Install Curl and Git
RUN apt-get update && apt-get install -y \
    build-essential curl git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

