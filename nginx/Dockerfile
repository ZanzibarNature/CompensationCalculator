FROM nginxinc/nginx-unprivileged

# Copy nginx.conf to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
