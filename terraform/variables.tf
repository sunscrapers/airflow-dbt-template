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
variable "db_username" {
    description = "Postgres master username"
    type = string
}
variable "db_password" {
    description = "Postgres master password"
    type = string
}

variable "airflow_env_variables" {
  description = "Map of all environment variables for Airflow"
  type = map(string)
  sensitive = true  # Making it sensitive since it might contain sensitive values
}