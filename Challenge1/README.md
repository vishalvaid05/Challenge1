gcloud auth application-default login
./terraform.exe plan --var-file var.tfvars
./terraform.exe apply --var-file var.tfvars
./terraform.exe destroy --var-file var.tfvars