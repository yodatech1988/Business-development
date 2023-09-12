```python
from google.cloud import storage
from google.cloud import pubsub_v1
from schemas import SystemInfrastructureSchema
import json

system_infrastructure = None

def developSystem():
    global system_infrastructure
    # Create a storage client.
    storage_client = storage.Client()

    # TODO: Replace 'your-bucket-name' with your bucket name.
    bucket_name = 'your-bucket-name'
    bucket = storage_client.get_bucket(bucket_name)

    # TODO: Replace 'your-object-name' with your object name.
    object_name = 'your-object-name'
    blob = bucket.blob(object_name)

    # Set the encryption configuration for the blob.
    blob.csek_key = {
        'key': 'your-base64-encoded-256-bit-aes-key',
        'key_sha256': 'your-base64-encoded-sha256-of-the-encryption-key',
    }

    # TODO: Replace 'source-file-name' with your source file name.
    source_file_name = 'source-file-name'
    blob.upload_from_filename(source_file_name)

    # The ID of your GCP project
    project_id = "your-project-id"

    # The ID of your GCS bucket
    bucket_id = "your-bucket-id"

    # The ID of your new Pub/Sub topic
    topic_id = "your-topic-id"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    future = publisher.publish(topic_path, b'System developed', infrastructure='developed')
    print(future.result())

    # Define the system infrastructure
    system_infrastructure = SystemInfrastructureSchema({
        'storage_client': storage_client,
        'bucket': bucket,
        'blob': blob,
        'publisher': publisher,
        'topic_path': topic_path
    })

    # Convert the system infrastructure to JSON
    system_infrastructure_json = json.dumps(system_infrastructure, default=lambda o: o.__dict__)

    # Save the system infrastructure to a file
    with open('system_infrastructure.json', 'w') as file:
        file.write(system_infrastructure_json)

    print('System development completed.')

if __name__ == "__main__":
    developSystem()
```