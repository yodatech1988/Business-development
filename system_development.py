```python
from google.cloud import storage
from google.cloud import secretmanager
from google.cloud import automl
from google.cloud import securitycenter
from google.cloud import compliance
from schemas import SystemDevelopmentSchema

google_cloud_infrastructure = {}

def designSystemInfrastructure():
    # Create a storage client.
    storage_client = storage.Client()

    # Create a bucket in Google Cloud Storage (GCS)
    bucket = storage_client.create_bucket('business_plan_bucket')
    google_cloud_infrastructure['storage_bucket'] = bucket.name

    # Create a Secret Manager client.
    secret_client = secretmanager.SecretManagerServiceClient()

    # Create a secret in Secret Manager
    secret = secret_client.create_secret('business_plan_secret')
    google_cloud_infrastructure['secret_manager'] = secret.name

    # Create an AutoML client.
    automl_client = automl.AutoMlClient()

    # Create a model in AutoML
    model = automl_client.create_model('business_plan_model')
    google_cloud_infrastructure['automl_model'] = model.name

    # Create a Security Command Center client.
    security_client = securitycenter.SecurityCenterClient()

    # Create a security policy in Security Command Center
    policy = security_client.create_policy('business_plan_policy')
    google_cloud_infrastructure['security_policy'] = policy.name

    # Create a Compliance client.
    compliance_client = compliance.ComplianceClient()

    # Create a compliance policy in Compliance
    compliance_policy = compliance_client.create_policy('business_plan_compliance')
    google_cloud_infrastructure['compliance_policy'] = compliance_policy.name

    # Validate the infrastructure schema
    SystemDevelopmentSchema().load(google_cloud_infrastructure)

    return google_cloud_infrastructure
```