#!/bin/bash

# Log file for debugging
LOG_FILE="/tmp/docker-deploy.log"

# Function to log messages
log_message() {
    echo "$(date): $1" | tee -a $LOG_FILE
}

# Set up error handling
set -e
trap 'log_message "Error occurred. Deployment failed."' ERR

# Start deployment
log_message "Starting deployment process"

# Navigate to the project directory
cd /path/to/your/local/repo  # Replace with your actual local repository path
log_message "Changed to project directory"

# Pull the latest changes from GitHub
log_message "Pulling latest changes from GitHub"
git pull origin main

# Build the Docker image
log_message "Building Docker image"
docker build -t docker-deploy-demo:latest .

# Stop and remove any existing container
if docker ps -a | grep -q docker-deploy-demo; then
    log_message "Stopping and removing existing container"
    docker stop docker-deploy-demo || true
    docker rm docker-deploy-demo || true
fi

# Run the new container
log_message "Starting new container"
docker run -d -p 8080:80 --name docker-deploy-demo docker-deploy-demo:latest

# Verify deployment
log_message "Verifying deployment"
if docker ps | grep -q docker-deploy-demo; then
    log_message "Deployment successful. Container is running."
else
    log_message "Deployment failed. Container is not running."
    exit 1
fi

log_message "Deployment process completed"