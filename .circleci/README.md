# CircleCI Pipeline Configuration

This directory contains the CircleCI pipeline configuration for automating the deployment of the Airflow and dbt infrastructure.

## Pipeline Overview

The pipeline consists of the following jobs:

### 1. Lint, Build and Test (`lint-build-and-test`)
- Uses Python Docker image
- Installs project dependencies
- Runs Ruff linting checks
- Executes project structure tests
- Runs DAG import tests with coverage reporting

### 2. Terraform Plan (`terraform-plan`)
- Sets up AWS CLI and Terraform
- Configures AWS credentials
- Creates terraform.tfvars from CircleCI environment variables
- Initializes Terraform
- Generates and stores Terraform plan

### 3. Terraform Apply (`terraform-apply`)
- Applies the Terraform plan
- Retrieves infrastructure outputs
- Generates environment variables file
- Stores infrastructure information for deployment

### 4. Deploy (`deploy`)
- Deploys the application to the provisioned EC2 instance
- Uses the environment variables generated in previous steps

## Required Environment Variables

The pipeline requires the following CircleCI environment variables:

- `AWS_ACCESS_KEY_ID`: AWS access key for infrastructure deployment
- `AWS_SECRET_ACCESS_KEY`: AWS secret key for infrastructure deployment
- `TFVARS_JSON`: JSON string containing Terraform variables
- `AIRFLOW_DB_PASSWORD`: Password for Airflow RDS instance
- `DBT_DB_PASSWORD`: Password for dbt RDS instance

## Workflow

The pipeline is triggered on:
- Pushes to the main branch
- Pull request creation/updates

Jobs run in sequence:
1. Lint and test
2. Infrastructure planning
3. Infrastructure deployment
4. Application deployment

## Pipeline Artifacts

The pipeline preserves the following artifacts between jobs:
- Terraform state and plan files
- Generated environment variables
- Infrastructure output values

## Security Notes

- AWS credentials are securely stored in CircleCI environment variables
- Database passwords are managed through environment variables
- Infrastructure state is preserved between jobs using CircleCI workspaces

## Customization

To modify the pipeline:
1. Edit `config.yml` to add/modify jobs
2. Update environment variables in CircleCI project settings
3. Adjust resource configurations in Terraform files
