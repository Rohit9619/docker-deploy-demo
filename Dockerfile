# Use an Nginx base image
FROM nginx:latest

# Remove default index.html and copy our own
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80
