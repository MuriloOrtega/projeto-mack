import boto3

def send_message(queue_url, message):
    sqs = boto3.client('sqs')
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    print(f"Mensagem enviada: {response['MessageId']}")

# Exemplo de uso
if __name__ == "__main__":
    send_message('your-queue-url', 'Hello, SQS!')
