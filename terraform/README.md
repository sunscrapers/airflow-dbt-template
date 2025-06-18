# Terraform Infrastructure for Airflow and dbt

This directory contains Terraform configurations for deploying the infrastructure required to run Airflow and dbt in AWS.

## Infrastructure Components

The following AWS resources are provisioned:

- **VPC and Networking**:
  - VPC with CIDR `10.0.0.0/16`
  - 2 Public Subnets in different availability zones
  - Internet Gateway
  - Route Tables for public access

- **Security**:
  - Security Group for Airflow (allows SSH and port 8080)
  - Security Group for RDS (allows Postgres access from Airflow)
  - EC2 Key Pair for SSH access

- **Compute**:
  - EC2 instance (t3.large) running Ubuntu 20.04 for Airflow
  - 20GB GP3 root volume

- **Databases**:
  - RDS Postgres instance for Airflow metadata
  - RDS Postgres instance for dbt transformations

## Prerequisites

1. AWS CLI installed and configured
2. Terraform installed (version specified in `versions.tf`)
3. SSH key pair for EC2 access

## Configuration

1. Copy `terraform.tfvars.example` to `terraform.tfvars`
2. Update the variables in `terraform.tfvars` with your values:
   ```hcl
   region = "eu-central-1"
   profile = "your-aws-profile"
   key_name = "your-key-name"
   public_key_ec2_airflow = "your-public-key"
   airflow_db_username = "airflow"
   airflow_db_password = "your-password"
   dbt_db_username = "dbt"
   dbt_db_password = "your-password"
   ```

## Usage

1. Initialize Terraform:
   ```bash
   terraform init
   ```

2. Review the planned changes:
   ```bash
   terraform plan
   ```

3. Apply the configuration:
   ```bash
   terraform apply
   ```

4. To destroy the infrastructure:
   ```bash
   terraform destroy
   ```

## Important Notes

- The RDS instances are publicly accessible but restricted to Airflow security group
- Both RDS instances use `db.t3.micro` instance class suitable for development
- EC2 instance has basic user data script to install Python and AWS CLI
- All resources are tagged with "AirflowDbtTemplateBlogPost"

## Outputs

The following outputs are available after deployment:
- EC2 instance public IP
- Airflow RDS endpoint
- dbt RDS endpoint

For more details, see `outputs.tf`.
