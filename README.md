# Projeto AWS - Murilo

Este projeto demonstra a utilização de vários serviços da AWS, incluindo S3, Lambda, EC2 e SQS.

## Funcionalidades

- **Amazon S3**: Upload e armazenamento de arquivos.
- **AWS Lambda**: Processamento de dados carregados no S3.
- **Amazon EC2**: Hospedagem de uma aplicação simples.
- **Amazon SQS**: Mensageria para comunicação entre serviços.

## Configuração

1. **Credenciais AWS**:
   - Configure sua conta AWS e crie as credenciais necessárias.
   - Siga as instruções no [AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) para criar um usuário com permissões adequadas.

2. **Configuração de Serviços**:
   - Siga as instruções abaixo para configurar cada serviço mencionado:
     - **Amazon S3**: 
       - Crie um bucket no S3 através do [console da AWS](https://console.aws.amazon.com/s3/).
     - **AWS Lambda**:
       - Crie uma função Lambda e vincule-a ao bucket S3 criado.
     - **Amazon EC2**:
       - Lance uma nova instância EC2 através do [console da AWS](https://console.aws.amazon.com/ec2/).
     - **Amazon SQS**:
       - Crie uma fila SQS através do [console da AWS](https://console.aws.amazon.com/sqs/).

3. **Deploy do Projeto**:
   - Faça o deploy do projeto conforme necessário. Utilize o [AWS CLI](https://aws.amazon.com/cli/) para facilitar o gerenciamento dos serviços.

## Exemplo de Uso

- Para fazer upload de um arquivo no S3:
  1. Utilize a função Lambda configurada.
  2. Siga as instruções abaixo:
     - [Como fazer upload de arquivos para o S3 usando a função Lambda](URL_EXEMPLO_DE_DOCUMENTACAO).

## Considerações

- Certifique-se de monitorar o uso da AWS para não ultrapassar os limites do Free Tier.
- Utilize o [AWS CloudWatch](https://aws.amazon.com/cloudwatch/) para monitorar o desempenho e os logs dos serviços.
