#!/bin/bash

# Define log levels for different deployment groups
case "$DEPLOYMENT_GROUP_NAME" in
  "TEST")
    LOG_LEVEL="debug"
    ;;
  "STAGING")
    LOG_LEVEL="info"
    ;;
  "PROD")
    LOG_LEVEL="error"
    ;;
  *)
    LOG_LEVEL="info"
    ;;
esac

# Update NGINX configuration
sed -i "s/error_log .*/error_log \/var\/log\/nginx\/error.log $LOG_LEVEL;/" /etc/nginx/nginx.conf

# Restart NGINX to apply changes
sudo systemctl restart nginx
