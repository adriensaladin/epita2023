FROM debian:stable

# Install dependencies for ModSecurity
RUN apt-get update && \
    apt-get install -y libmodsecurity3 modsecurity-crs libnginx-mod-http-modsecurity nginx vim less locate


COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir /etc/nginx/modsecurity/

RUN cp /etc/modsecurity/crs/crs-setup.conf /etc/nginx/modsecurity/

RUN nginx -V
RUN updatedb

# Expose the NGINX port
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
