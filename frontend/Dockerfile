FROM nginx:1.11-alpine

COPY conf /conf
COPY src /app/src

ENTRYPOINT nginx -c /conf/nginx.conf
