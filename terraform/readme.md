# Setting up the Project Infrastructure 

There are plenty of Iac tools (Terraform, Pulumi, Cloud Formation) available to setup your infrastructure. I have used Terraform in this project. If you like to proceed with Terraform, Install the Terraform in your local machine or in your virtual machine (Refer prerequsites) and Kindly follow the below instructions.

## Configuring the Infrastructre

For this project, I need to setup one Google Cloud Storage bucket and three BigQuery datasets.
- The GCS bucket will be the data lake and contains all the raw files.
- The BigQuery datasets will be the data warehouse and contains the raw, staging and production tables respectively.

I have configured the neccesary resources in the terraform configuration files (Kindly check)

## Spinning up the Infrastructure

- Initiate the terraform and download the required dependencies
  ```
  terraform init
  ```
- To view your terraform execution plan
  > **Note:** I have configured to ask Project ID during run time, so enter your Project ID and proceed
  ```
  terraform plan
  ```
  The plan will show the creation of the below configured files
  - GCS bucket : datalake-"Your Project ID"
  - Three BigQuery Datasets : raw, staging, production

- To apply the plan and make changes in the cloud
  ```
  terraform apply
  ```
***Now you have successfully configured the infrastructure for this project!!!*** 
  
- Delete your infrastructure after completing the project, to avoid costs on any running services
  ```
  terraform destroy
  ```
  
