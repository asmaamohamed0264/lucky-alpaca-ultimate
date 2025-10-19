# 🦙 Lucky Alpaca - Ultimate Trading System Dockerfile
# ===================================================
# Dockerfile pentru sistemul integrat Lucky Alpaca cu toate API-urile

FROM python:3.11-slim

# Metadata
LABEL maintainer="Lucky Alpaca Team"
LABEL description="Ultimate Trading System with Advanced APIs Integration"
LABEL version="1.0.0"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    wget \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create necessary directories
RUN mkdir -p \
    /app/logs \
    /app/data \
    /app/results \
    /app/integrated_trading_results \
    /app/ultimate_trading_results \
    /app/backups \
    /app/certs

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set permissions
RUN chmod +x /app/ultimate_trading_system.py && \
    chmod +x /app/setup_advanced_apis.py && \
    chmod +x /app/integrated_social_trading_system.py

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash alpaca && \
    chown -R alpaca:alpaca /app
USER alpaca

# Expose ports
EXPOSE 8000 8001

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default command - Start Lucky Alpaca
CMD ["python", "app.py"]