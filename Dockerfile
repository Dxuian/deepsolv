# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /code

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /code/

# Copy the wait-for-it script
COPY wait-for-it.sh /code/
RUN chmod +x /code/wait-for-it.sh
