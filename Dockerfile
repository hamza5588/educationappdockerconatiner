FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better cache utilization
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"] 