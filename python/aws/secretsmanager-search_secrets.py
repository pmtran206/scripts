# Search SecretsManager keys/values for specific string


import boto3
import json
from boto3 import Session
from botocore.exceptions import ClientError


ENV = 'sandbox'

SECRETS = []

SEARCHSTRING = 'xyz'

session = boto3.Session(profile_name=ENV)
client = session.client('secretsmanager')

# Retrieve list of all secrets and store in List

def list_secrets():
    paginator = client.get_paginate('list_secrets')
    response = paginator.paginate()
    for page in response:
        for item in page['SecretList']:
            SECRETS.apped(item['Name'])

# return secret value from secret name

def get_secret(secret):
    try:
        response  = client.get_secret_value(SecretId=secret)
        try:
            return response['SecretString']
        except KeyError:
            print(secret + " - SecretString missing")

    except ClientError as err:
        if err.response['Error']['Code'] == 'ResourceNotFoundException':
            print("Source: " + secret + "- not found")
        else:
            print("Unknown error: %s" % err)
        return False
    
def main():
    list_secrets()
    
    for i in SECRETS:
        secret_data = get_secret(i)
        if(secret_data)
            if(secret_data.lower().find(SEARCHSTRING.lower()) != -1):
                print(i)

if __name__ == "__main__":
    main()