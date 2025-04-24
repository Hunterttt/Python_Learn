FROM nginx:alpine
RUN apk add --no-cache aws-cli
COPY nginx.conf /etc/nginx/nginx.conf
CMD aws s3 sync s3://hunter-bucket-docker-002/web-content /usr/share/nginx/html && nginx -g 'daemon off;'