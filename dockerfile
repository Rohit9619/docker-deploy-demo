FROM nginx:alpine

# Remove default nginx static resources
RUN rm -rf /usr/share/nginx/html/*

# Copy static resources from current directory
COPY . /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]