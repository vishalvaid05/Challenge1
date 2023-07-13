# Execution Commands
```
gcloud auth application-default login
./terraform.exe init
./terraform.exe plan --var-file var.tfvars
./terraform.exe apply --var-file var.tfvars
./terraform.exe destroy --var-file var.tfvars
```
<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 0.13 |
| <a name="requirement_google"></a> [google](#requirement\_google) | 4.69.1 |
| <a name="requirement_google-beta"></a> [google-beta](#requirement\_google-beta) | 4.69.1 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_google"></a> [google](#provider\_google) | 4.69.1 |
| <a name="provider_google-beta"></a> [google-beta](#provider\_google-beta) | 4.69.1 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_project-factory_project_services"></a> [project-factory\_project\_services](#module\_project-factory\_project\_services) | terraform-google-modules/project-factory/google//modules/project_services | 14.2.1 |

## Resources

| Name | Type |
|------|------|
| [google-beta_google_cloud_run_service.api](https://registry.terraform.io/providers/hashicorp/google-beta/4.69.1/docs/resources/google_cloud_run_service) | resource |
| [google-beta_google_compute_network.main](https://registry.terraform.io/providers/hashicorp/google-beta/4.69.1/docs/resources/google_compute_network) | resource |
| [google_cloud_run_service.fe](https://registry.terraform.io/providers/hashicorp/google/4.69.1/docs/resources/cloud_run_service) | resource |
| [google_project_iam_member.allrun](https://registry.terraform.io/providers/hashicorp/google/4.69.1/docs/resources/project_iam_member) | resource |
| [google_redis_instance.main](https://registry.terraform.io/providers/hashicorp/google/4.69.1/docs/resources/redis_instance) | resource |
| [google_service_account.runsa](https://registry.terraform.io/providers/hashicorp/google/4.69.1/docs/resources/service_account) | resource |
| [google_sql_database.database](https://registry.terraform.io/providers/hashicorp/google/4.69.1/docs/resources/sql_database) | resource |
| [google_sql_database_instance.main](https://registry.terraform.io/providers/hashicorp/google/4.69.1/docs/resources/sql_database_instance) | resource |
| [google_sql_user.main](https://registry.terraform.io/providers/hashicorp/google/4.69.1/docs/resources/sql_user) | resource |
| [google_project.project](https://registry.terraform.io/providers/hashicorp/google/4.69.1/docs/data-sources/project) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_deployment_name"></a> [deployment\_name](#input\_deployment\_name) | The name of this particular deployment, will get added as a prefix to most resources. | `string` | `"three-tier-app"` | no |
| <a name="input_enable_apis"></a> [enable\_apis](#input\_enable\_apis) | Whether or not to enable underlying apis in this solution. . | `string` | `true` | no |
| <a name="input_labels"></a> [labels](#input\_labels) | A map of labels to apply to contained resources. | `map(string)` | <pre>{<br>  "three-tier-app": true<br>}</pre> | no |
| <a name="input_project_id"></a> [project\_id](#input\_project\_id) | The project ID to deploy to | `string` | n/a | yes |
| <a name="input_region"></a> [region](#input\_region) | The Compute Region to deploy to | `string` | n/a | yes |
| <a name="input_run_roles_list"></a> [run\_roles\_list](#input\_run\_roles\_list) | The list of roles that run needs | `list(string)` | <pre>[<br>  "roles/cloudsql.instanceUser",<br>  "roles/cloudsql.client"<br>]</pre> | no |
| <a name="input_zone"></a> [zone](#input\_zone) | The Compute Zone to deploy to | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_endpoint"></a> [endpoint](#output\_endpoint) | The url of the front end which we want to surface to the user |
<!-- END_TF_DOCS -->