data "aws_vpc" "default" {
  default = true
}

resource "aws_security_group" "rds_access" {
  name        = "rds-access"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["${var.my_ip}/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "autonote_db" {
  identifier             = "autonote-db"                     # Nom unique de la ressource RDS
  allocated_storage      = 20                                # Taille en Go
  engine                 = "postgres"                        # Type de base
  engine_version         = "15"                            # Version précise
  instance_class         = "db.t3.micro"                     # Petite instance gratuite aws
  db_name                = var.db_name                       # Nom de la base dans PostgreSQL
  username               = var.db_username                   # Utilisateur PostgreSQL
  password               = var.db_password                   # Mot de passe 
  publicly_accessible    = true                              # RDS accessible via Internet
  skip_final_snapshot    = true                              # Pas de snapshot à la suppression 

  # Optionnel : tags pour mieux organiser sur AWS
  tags = {
    Name = "autonote-db"
    Env  = "dev"
  }
}
