```python
from project_management_integration import project_management_tool
from google.cloud import pubsub_v1

approval_status = False

class ApprovalSchema:
    def __init__(self, stage, update, feedback):
        self.stage = stage
        self.update = update
        self.feedback = feedback

def createApprovalMechanism():
    global approval_status
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('business-plan-project', 'ApprovalMechanismUpdate')

    while not approval_status:
        for task in project_management_tool.tasks:
            if task.status == 'Pending Approval':
                update = f"Task {task.name} is pending your approval."
                approval_request = ApprovalSchema(task.name, update, None)
                publisher.publish(topic_path, approval_request)
                print(f"Approval request for {task.name} has been sent.")
                break
        else:
            continue
        break

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path('business-plan-project', 'ApprovalMechanismUpdate')

    def callback(message):
        global approval_status
        feedback = message.data
        if feedback == 'Approved':
            approval_status = True
            print("Approval received. Proceeding to the next stage.")
        else:
            print("Approval not received. Waiting for feedback.")
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)
    print("Listening for approval...")

if __name__ == "__main__":
    createApprovalMechanism()
```