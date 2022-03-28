locals {
  data_lake_bucket = "datalake"
}

variable "project" {
  description = "Your GCP Project ID"
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default = "asia-south1"
  type = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET1" {
  description = "BigQuery Dataset that stores the raw data"
  type = string
  default = "raw"
}

variable "BQ_DATASET2" {
  description = "BigQuery Dataset that stores the staging data"
  type = string
  default = "staging"
}

variable "BQ_DATASET3" {
  description = "BigQuery Dataset that stores the production data"
  type = string
  default = "production"
}

