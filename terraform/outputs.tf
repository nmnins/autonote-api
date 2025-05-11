output "rds_endpoint" {
  value = aws_db_instance.autonote_db.endpoint
}

output "ec2_public_ip" {
  description = "Adresse IP publique de l'instance EC2 AutoNote"
  value       = aws_instance.autonote_ec2.public_ip
}
