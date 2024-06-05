# Dynamic NGINX Log Level Configuration with AWS CodeDeploy

## Overview

This guide provides a detailed approach to dynamically configure the NGINX log level based on the deployment group in AWS CodeDeploy. This setup allows different log levels for TEST, STAGING, and PROD environments without requiring different application revisions for each environment.

## Solution Components

1. **Custom Shell Script**: A script to update the NGINX log level based on the `DEPLOYMENT_GROUP_NAME` environment variable.
2. **AppSpec File**: Configuration file for AWS CodeDeploy to execute the shell script during the deployment process.

## Directory Structure

```
.
├── appspec.yml
└── scripts
    ├── update_nginx_log_level.sh
    ├── stop_server.sh
    ├── start_server.sh
    └── validate_service.sh
```

## Shell Script: `update_nginx_log_level.sh`

This script reads the `DEPLOYMENT_GROUP_NAME` environment variable and updates the NGINX log level accordingly.

```sh
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
```

## AppSpec File: `appspec.yml`

The `appspec.yml` file is configured to run the `update_nginx_log_level.sh` script during the `BeforeInstall` lifecycle event.

```yaml
version: 0.0
os: linux
files:
  - source: /
    destination: /your/app/directory
hooks:
  BeforeInstall:
    - location: scripts/update_nginx_log_level.sh
      timeout: 300
      runas: root
  ApplicationStop:
    - location: scripts/stop_server.sh
      timeout: 300
      runas: root
  ApplicationStart:
    - location: scripts/start_server.sh
      timeout: 300
      runas: root
  ValidateService:
    - location: scripts/validate_service.sh
      timeout: 300
      runas: root
```

## Scripts Overview

### `update_nginx_log_level.sh`

This script determines the appropriate log level based on the deployment group and updates the NGINX configuration file accordingly. It then restarts the NGINX service to apply the changes.

### `stop_server.sh`

Script to stop your server/application gracefully before the new deployment. Example content:

```sh
#!/bin/bash
sudo systemctl stop your-service
```

### `start_server.sh`

Script to start your server/application after the new deployment. Example content:

```sh
#!/bin/bash
sudo systemctl start your-service
```

### `validate_service.sh`

Script to validate that your application is running correctly after deployment. Example content:

```sh
#!/bin/bash
curl -f http://localhost/health || exit 1
```

## Deployment Instructions

1. **Prepare Your Code**: Ensure your repository includes the `appspec.yml` and `scripts` directory with the necessary scripts.
2. **Create Deployment Group**: Set up deployment groups for TEST, STAGING, and PROD environments in AWS CodeDeploy.
3. **Deploy**: Use AWS CodeDeploy to deploy your application. The `update_nginx_log_level.sh` script will dynamically set the NGINX log level based on the deployment group.

## Testing and Validation

1. **TEST Environment**: Deploy to the TEST environment and verify that the NGINX log level is set to `debug`.
2. **STAGING Environment**: Deploy to the STAGING environment and verify that the NGINX log level is set to `info`.
3. **PROD Environment**: Deploy to the PROD environment and verify that the NGINX log level is set to `error`.

By following this guide, you can dynamically configure the NGINX log level for different deployment groups, ensuring appropriate logging for each environment.
