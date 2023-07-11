terraform {
  required_version = ">= 0.13"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.69.1"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "4.69.1"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 2.2"
    }
  }

}
