# EC2 Instance Outputs
output "airflow_instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.airflow.id
}

output "airflow_instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.airflow.public_ip
}

output "airflow_instance_public_dns" {
  description = "Public DNS of the EC2 instance"
  value       = aws_instance.airflow.public_dns
}

# Airflow RDS Outputs
output "airflow_rds_endpoint" {
  description = "The connection endpoint for the Airflow RDS instance"
  value       = aws_db_instance.airflow_postgres.endpoint
}

output "airflow_rds_port" {
  description = "The port the Airflow RDS instance is listening on"
  value       = aws_db_instance.airflow_postgres.port
}

output "airflow_rds_database_name" {
  description = "The Airflow database name"
  value       = aws_db_instance.airflow_postgres.db_name
}

output "airflow_rds_username" {
  description = "The master username for the Airflow database"
  value       = aws_db_instance.airflow_postgres.username
  sensitive   = true
}

# dbt RDS Outputs
output "dbt_rds_endpoint" {
  description = "The connection endpoint for the dbt RDS instance"
  value       = aws_db_instance.dbt_postgres.endpoint
}

output "dbt_rds_port" {
  description = "The port the dbt RDS instance is listening on"
  value       = aws_db_instance.dbt_postgres.port
}

output "dbt_rds_database_name" {
  description = "The dbt database name"
  value       = aws_db_instance.dbt_postgres.db_name
}

output "dbt_rds_username" {
  description = "The master username for the dbt database"
  value       = aws_db_instance.dbt_postgres.username
  sensitive   = true
}

# Network Outputs
output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = [aws_subnet.public.id, aws_subnet.public2.id]
}

# Region Output
output "aws_region" {
  description = "The AWS region used"
  value       = var.region
}
