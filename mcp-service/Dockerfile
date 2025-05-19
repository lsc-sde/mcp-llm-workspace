FROM python:3.12-slim

# Set Work Directory
WORKDIR /app

# Install system tools and Node.js (for fastmcp dev)
RUN apt-get update && apt-get install -y \
    build-essential curl git && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install uv globally via pipx
RUN pip install pipx && pipx ensurepath && \
    pipx install uv

# Make uv available in PATH for this shell
ENV PATH="${PATH}:/root/.local/bin"

# Install FastMCP with uv
RUN uv pip install --system fastmcp

# Copy Server Code
COPY . . 

# Expose FastMCP Port
EXPOSE 8000 6274

# Run The Server
#CMD ["python", "main.py"]
#CMD ["fastmcp", "dev", "main.py"]
CMD ["fastmcp", "run", "main.py"]
