variable "db_name" {
  description = "Nom de la base PostgreSQL"
  type        = string
}

variable "db_username" {
  description = "Nom d'utilisateur PostgreSQL"
  type        = string
}

variable "db_password" {
  description = "Mot de passe de la base PostgreSQL"
  type        = string
  sensitive   = true
}

variable "my_ip" {
  description = "Adresse IP autorisée à accéder à PostgreSQL"
  type        = string
}
