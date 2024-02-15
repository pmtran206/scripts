# Pull secrets from one environment and copy them into new environment

import boto3
import json
from boto3 import Session
from botocore.exceptions import ClientError

SECRETS = [
    'secret-name-1',
    'secret-name-2',
    'secret-name-3'
]

### CREATE SESSIONS TO SOURCE AND TARGET
### REQ: .aws profile must exist on machine running script
### Label of profile must match these two variables

SOURCE_ENV = 'sandbox'
TARGET_ENV = 'prod'

# Open session to each env

source_session = boto3.session(profile_name=SOURCE_ENV)
source_client = source_session.client('secretsmanager')
target_session = boto3.session(profile_name=TARGET_ENV)
target_client = target_session.client('secretsmanager')

# Check if secret exists in source and retrieve its SecretString

def get_source_secret(secret):
    try:
        response = source_client.get_secret_value(SecretId=secret)
        return response['SecretString']
    except ClientError as err:
        if err.response['Error']['Code'] == 'ResourceNotFoundException':
            print("source: " + secret + " not found")
        else:
            print("unknown error: %s" % err)
        return False

# Check if the secret name already exists in TARGET
    
def exists_in_target(secret):
    try:
        response = target_client.describe_secret(SecretId=secret)
        return True
    except ClientError as err:
        if err.response['Error']['Code'] == 'ResourceNotFoundException':
            print("Target: " + secret + " not found")
        else:
            print("Unknown error: %s" % err)
        return False

# Update secret in Target
    
def update_target(secret_name, secret_value):
    print("Target: "  + secret_name + " Updating")
    target_client.update_secret(SecretId=secret_name, SecretString=secret_value)
        
def main():
    for i in SECRETS:
        secret_data = get_source_secret(i)
        if secret_data and (exists_in_target(i)):
            update_target(i, secret_data)

if __name__ == "__main__":
    main()