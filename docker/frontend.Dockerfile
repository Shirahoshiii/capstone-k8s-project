# docker/frontend.Dockerfile
FROM nginx:alpine

# Remove default NGINX content
RUN rm -rf /usr/share/nginx/html/*

# COPY the correct dist folder
COPY frontend/dist/ /usr/share/nginx/html/

# Expose port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]