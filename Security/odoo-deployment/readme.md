# Odoo 13 Bitnami CI/CD Pipeline (deploy custom module)

This repository contains the configuration and scripts for a comprehensive CI/CD pipeline for Odoo 13 Bitnami deployment on AWS.

## Overview

This pipeline automates the process of building, testing, securing, and deploying Odoo 13 Bitnami custom modules and addons. It utilizes AWS services including CodePipeline, CodeBuild, and CodeDeploy to create a robust and secure deployment process.

## Pipeline Stages

1. **Source**: Code is pulled from AWS CodeCommit when changes are pushed.
2. **Build**: 
   - Installs dependencies
   - Runs unit tests
   - Builds Odoo modules
   - Performs SAST (Static Application Security Testing) and SCA (Software Composition Analysis)
3. **Deploy to Staging**: Automatically deploys to a staging environment.
4. **DAST**: Runs Dynamic Application Security Testing on the staging environment.
5. **Manual Approval**: Requires manual approval before proceeding to production.
6. **Deploy to Production**: Deploys approved changes to the production environment.

## Key Components

- **buildspec.yml**: Defines the build process for CodeBuild.
- **appspec.yml**: Configures the deployment process for CodeDeploy.
- **Security Scripts**: Includes scripts for SAST, SCA, and DAST scans.
- **Deployment Scripts**: Contains scripts for installing and starting Odoo.

## Security Measures

- Static Application Security Testing (SAST) using Bandit
- Software Composition Analysis (SCA) using Safety
- Dynamic Application Security Testing (DAST) using OWASP ZAP

## Prerequisites

- AWS account with appropriate permissions
- Odoo 13 Bitnami instance on EC2
- CodeDeploy agent installed on EC2 instances
- Proper IAM roles and policies configured

## IAM roles configuration
Assigning roles:
- Assign the OdooCICDPipelineRole to your CodePipeline pipeline.
- Assign the OdooCICDBuildRole to your CodeBuild projects.
- Assign the OdooCICDDeployRole to your CodeDeploy application.
- Assign the OdooEC2InstanceRole to your EC2 instances running Odoo.

*** Remember to replace placeholders like your-region, your-account-id, your-repo-name, and your-pipeline-artifact-bucket with your actual AWS details.

## Setup Instructions

1. Set up your CodeCommit repository with Odoo custom modules and scripts.
2. Create a CodeBuild project using the provided buildspec.yml.
3. Set up CodeDeploy applications for staging and production.
4. Create a CodePipeline with all the stages mentioned in the Pipeline Stages section.
5. Configure IAM roles for CodeBuild, CodeDeploy, and CodePipeline.
6. Adjust Odoo configuration to work with custom addons.
7. Set up monitoring and logging using AWS CloudWatch.

## Best Practices

- Regularly update the Bitnami Odoo image for security patches.
- Keep custom modules separate from core Odoo files.
- Backup the Odoo database and filestore before major changes.
- Regularly review and update security scans and DAST tests.
- Consider implementing blue/green deployments for zero-downtime updates.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
