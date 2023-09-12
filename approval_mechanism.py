```python
from project_management_integration import project_management_tool
from google.cloud import pubsub_v1

approval_status = False

def requireApproval():
    global approval_status
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('business-plan-project', 'ApprovalRequired')

    def callback(message_future):
        if message_future.exception(timeout=30):
            print('Publishing message on {} threw an Exception {}.'.format(
                topic_path, message_future.exception()))
        else:
            print('Message {} published.'.format(message_future.result()))

    data = 'Approval required for the next stage of the business plan.'
    data = data.encode('utf-8')
    message_future = publisher.publish(topic_path, data=data)
    message_future.add_done_callback(callback)

    # Block until the message is published.
    message_future.result()

    # Wait for the owner's approval
    while not approval_status:
        pass

def updateApprovalStatus(status):
    global approval_status
    approval_status = status
    print('Approval status updated to: ', approval_status)
```