import boto3

# Set up your SQS queue URL and boto3 client
queue_url = "https://sqs.us-east-1.amazonaws.com/440848399208/yaq7fm"
sqs = boto3.client('sqs')

def check_queue_attributes():
    try:
        # Get queue attributes
        response = sqs.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=[
                'All'
            ]
        )
        # Print queue attributes
        print("Queue Attributes:")
        for key, value in response['Attributes'].items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error: {e}")

# Call the function to check queue attributes
check_queue_attributes()
