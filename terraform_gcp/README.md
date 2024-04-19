## Project infrastructure modules in GCP:

- Google Cloud Storage (GCS): Data Lake
- BigQuery: Data Warehouse
- Compute VM intance

### itial Setup

1. Create an account GCP with your Google email ID
2. Setup your first project if you haven't already
   eg. "estore analytics", and note down the "Project ID" (we'll use this later when deploying infra with TF)
3. Setup service account & authentication for this project

- Grant Viewer, Storage Admin, Storage Object Admin, BigQuery Admin, Compute Admin roles to begin with.
- Download service-account-keys (.json) for auth.

5. Download SDK for local setup
6. Set environment variable to point to your downloaded GCP keys

```shell
# Refresh service-account's auth-token for this session
export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
```

Now authenticate:

```
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
```

# Initialize state file (.tfstate)

terraform init

# Check changes to new infra plan

terraform plan

````

```shell
# Create new infra
terraform apply -var="project=<your-gcp-project-id>"
````

```shell
# Delete infra after your work, to avoid costs on any running services
terraform destroy
```
