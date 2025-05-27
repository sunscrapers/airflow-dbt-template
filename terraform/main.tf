provider "aws" {
  region = var.region
  profile = var.profile
}

# Networking: VPC, Subnet, IGW, Route Table
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = { Name = "main-vpc" }
}

resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "eu-central-1a"
  tags = { Name = "public-subnet-1a" }
}

resource "aws_subnet" "public2" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "eu-central-1b"
  tags = { Name = "public-subnet-1b" }
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id
  tags   = { Name = "main-igw" }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
  tags = { Name = "public-rt" }
}

resource "aws_route_table_association" "public_assoc" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "public_assoc2" {
  subnet_id      = aws_subnet.public2.id
  route_table_id = aws_route_table.public.id
}

# Security Groups
resource "aws_security_group" "airflow_sg" {
  name        = "airflow-sg"
  description = "Allow SSH and Airflow web"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = { Name = "airflow-sg" }
}

resource "aws_security_group" "rds_sg" {
  name        = "rds-sg"
  description = "Allow Postgres from Airflow"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.airflow_sg.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = { Name = "rds-sg" }
}

# Key pair for EC2
resource "aws_key_pair" "deployer" {
  key_name   = var.key_name
  public_key = var.public_key_ec2_airflow
}

# EC2 for Airflow
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical Ubuntu
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

resource "aws_instance" "airflow" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = "t3.micro"
  subnet_id                   = aws_subnet.public.id
  vpc_security_group_ids      = [aws_security_group.airflow_sg.id]
  key_name                    = var.key_name
  associate_public_ip_address = true

  # Basic user_data to install Airflow via pip
  user_data = <<-EOF
              #!/bin/bash
              apt-get update

              # Install Python
              apt-get install -y python3-pip awscli

              EOF

  tags = { Name = "AirflowDbtTemplateBlogPost" }
}

# RDS Postgres
resource "aws_db_subnet_group" "rds_subnets" {
  name       = "rds-subnet-group"
  subnet_ids = [aws_subnet.public.id, aws_subnet.public2.id]
  tags       = { Name = "AirflowDbtTemplateBlogPost" }
}

# RDS Postgres for Airflow
resource "aws_db_instance" "airflow_postgres" {
  identifier              = "airflow-db"
  engine                  = "postgres"
  instance_class          = "db.t3.micro"
  allocated_storage       = 20
  db_name                 = "airflow"
  username                = var.airflow_db_username
  password                = var.airflow_db_password
  publicly_accessible     = true
  skip_final_snapshot     = true
  vpc_security_group_ids  = [aws_security_group.rds_sg.id]
  db_subnet_group_name    = aws_db_subnet_group.rds_subnets.name
  tags = {
    Name = "AirflowDbtTemplateBlogPost"
    Purpose = "Airflow"
  }
}

# RDS Postgres for dbt
resource "aws_db_instance" "dbt_postgres" {
  identifier              = "dbt-db"
  engine                  = "postgres"
  instance_class          = "db.t3.micro"
  allocated_storage       = 20
  db_name                 = "dbtpostgres"
  username                = var.dbt_db_username
  password                = var.dbt_db_password
  publicly_accessible     = true
  skip_final_snapshot     = true
  vpc_security_group_ids  = [aws_security_group.rds_sg.id]
  db_subnet_group_name    = aws_db_subnet_group.rds_subnets.name
  tags = {
    Name = "AirflowDbtTemplateBlogPost"
    Purpose = "dbt"
  }
}
