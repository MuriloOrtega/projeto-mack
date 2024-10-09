#!/bin/bash
# Script para configurar a instância EC2

# Instalar dependências
sudo apt-get update
sudo apt-get install -y python3-pip

# Configurar o ambiente
pip3 install boto3
