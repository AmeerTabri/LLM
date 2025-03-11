# Use the official Nginx image as a parent image
FROM nginx:alpine

# Copy the static files to the Nginx web root
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80


# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . /app

# Install required Python packages with timeout
RUN pip install --no-cache-dir  -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Command to run Flask app on container start
CMD ["python", "Backend/app.py"]
