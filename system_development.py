```python
from google.cloud import storage
from google.cloud import secretmanager
import os

def design_system(business_plan, owner_operator, email_address):
    # Create a storage client.
    storage_client = storage.Client()

    # Create a bucket in Google Cloud Storage (GCS)
    bucket_name = f"{owner_operator}-business-plan"
    bucket = storage_client.create_bucket(bucket_name)

    # Upload the business plan to the bucket
    blob = bucket.blob('business_plan.json')
    blob.upload_from_string(str(business_plan))

    # Create a secret manager client
    secret_client = secretmanager.SecretManagerServiceClient()

    # Create a secret for the email address
    secret_name = f"{owner_operator}-email"
    secret = secret_client.create_secret(
        request={"parent": f"projects/{os.getenv('PROJECT_ID')}", "secret_id": secret_name, "secret": {"replication": {"automatic": {}}}}
    )

    # Add the email address as a secret version
    secret_version = secret_client.add_secret_version(
        request={"parent": secret.name, "payload": {"data": email_address.encode('UTF-8')}}
    )

    return bucket_name, secret_name
```