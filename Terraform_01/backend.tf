terraform {
    required_version = "1.11.4"
    backend "s3" {
        bucket = "hunter-bucket-terraform-tfstate"
        key    = "terraform.tfstate"
        region = "ap-northeast-1"
    }
}

provider "aws" {
    region = "ap-northeast-1"
}