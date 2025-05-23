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

# RDS Outputs
output "rds_endpoint" {
  description = "The connection endpoint for the RDS instance"
  value       = aws_db_instance.postgres.endpoint
}

output "rds_port" {
  description = "The port the RDS instance is listening on"
  value       = aws_db_instance.postgres.port
}

output "rds_database_name" {
  description = "The database name"
  value       = aws_db_instance.postgres.db_name
}

output "rds_username" {
  description = "The master username for the database"
  value       = aws_db_instance.postgres.username
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
