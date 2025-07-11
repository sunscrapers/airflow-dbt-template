terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.87.0"
    }
  }

  required_version = ">= 1.0.0"

  backend "s3" {
    bucket         = "airflow-dbt-template-part-2-going-into-cloud"
    key            = "state/terraform.tfstate"
    region         = "eu-central-1"
    encrypt        = true
    dynamodb_table = "airflow-dbt-template-part-2-going-into-cloud-terraform-state-lock"
    profile        = "airflow-dbt-template-part-2-going-into-cloud-mfa"
  }
}
