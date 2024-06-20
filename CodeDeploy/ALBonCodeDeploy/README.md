### To ensure that deployment failures (as determined by failing ALB health checks) trigger a rollback, you need to explicitly handle the health check status within your CodeDeploy lifecycle events. Here’s how to do it:

#### 1. Custom Health Check Script:

- During the ValidateService lifecycle event, include a custom script that checks the health status of the instance as reported by the ALB.
- This script should make use of AWS CLI or SDK to query the health status of the instance from the ALB.

#### 2. Automatic Rollback Configuration:

- Configure the deployment group to enable automatic rollback on deployment failure. This ensures that if the custom health check script detects a failure, the deployment will be rolled back.
