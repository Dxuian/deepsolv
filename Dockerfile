# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install dependencies for mysqlclient
RUN apt-get update && \
    apt-get install -y build-essential libmariadb-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run when the container starts
# ...existing code...
# CMD ["sh", "-c", "./wait-for-it.sh && python insta/manage.py makemigrations && python insta/manage.py migrate && python insta/manage.py runserver 0.0.0.0:8000"]