# Input variables
variable "region" {
    description = "Region of AWS in which to deploy"
    type = string
}
variable "profile" {
    description = "AWS CLI profile name"
    type = string
}
variable "public_key_ec2_airflow" {
    description = "Public key for EC2 instance"
    type = string
}
variable "key_name" {
    description = "EC2 key pair name"
    type = string
}
variable "db_name" {
    description = "Postgres database name"
    type = string
}

# Airflow Database Variables
variable "airflow_db_username" {
    description = "Postgres master username for Airflow database"
    type = string
}
variable "airflow_db_password" {
    description = "Postgres master password for Airflow database"
    type = string
    sensitive = true
}

# dbt Database Variables
variable "dbt_db_username" {
    description = "Postgres master username for dbt database"
    type = string
}
variable "dbt_db_password" {
    description = "Postgres master password for dbt database"
    type = string
    sensitive = true
}

variable "airflow_env_variables" {
  description = "Map of all environment variables for Airflow"
  type = map(string)
  sensitive = true  # Making it sensitive since it might contain sensitive values
}