```python
from google.cloud import storage
from google.cloud import secretmanager
import os

# Define the system configuration schema
class SystemConfigSchema:
    def __init__(self, project_id, bucket_name, secret_id, version_id):
        self.project_id = project_id
        self.bucket_name = bucket_name
        self.secret_id = secret_id
        self.version_id = version_id

# Define the system configuration
system_config = SystemConfigSchema(os.getenv('PROJECT_ID'), os.getenv('BUCKET_NAME'), os.getenv('SECRET_ID'), os.getenv('VERSION_ID'))

def deploySystem():
    # Create a storage client
    storage_client = storage.Client(system_config.project_id)

    # Get the bucket with the name
    bucket = storage_client.get_bucket(system_config.bucket_name)

    # Create a blob with the name
    blob = bucket.blob('business_plan')

    # Upload the business plan to the blob
    blob.upload_from_filename('business_plan.txt')

    # Create the Secret Manager client
    secret_client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version
    secret_name = f"projects/{system_config.project_id}/secrets/{system_config.secret_id}/versions/{system_config.version_id}"

    # Access the secret version
    response = secret_client.access_secret_version(secret_name)

    # Return the decoded payload
    return response.payload.data.decode('UTF-8')

# Call the function to deploy the system
deploySystem()
```