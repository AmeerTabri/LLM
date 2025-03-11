# Use an official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project to the container
COPY . .

# Install backend dependencies from the root requirements.txt
RUN pip install -r requirements.txt

# Expose ports for both backend (5000) and frontend (8000)
EXPOSE 5000 8000

# Copy the entrypoint script and give it execution permissions
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Start both the backend and frontend when the container runs
CMD ["/entrypoint.sh"]
