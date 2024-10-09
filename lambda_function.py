import json

def lambda_handler(event, context):
    # Processa os dados recebidos do S3
    print("Dados recebidos:", event)
    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído!')
    }
