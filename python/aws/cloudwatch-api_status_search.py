# Query specific log group to find API status code

import boto3
import json
from boto3 import Session
from botocore.exceptions import ClientError


# import AWS Session

SOURCE_PROFILE = 'sandbox'
LOG_GROUP = 'path/to/log/group'

source_session = boto3.Session(profile_name=SOURCE_PROFILE)
source_client = source_session.client('logs')

# sub-routine to parse desired information from log stream

def get_caller_info(logStream):
    client_response = source_client.get_log_events(logGroupName=LOG_GROUP, logStreamName=logStream, startFromHead=True)
    try:
        message_body = client_response['events'][0]['message']
        json_message_body = json.loads(message_body)
        print(json_message_body['ip'] + " --- " + json_message_body['resourcePath'] + "---" + json_message_body['statuscode'])

    except Exception:
        print(logStream + "- empty?")
        pass

def getLogStreamNames(logGroup):
    streams = []

    paginator = source_client.get_paginator('describe_log_streams')
    logstream_pages = paginator.paginate(logGropuname=logGroup, orderBy='LastEventTime')

    for page in logstream_pages:
        for item in page:
            streams.append( item['logStreamName'])
        
    return streams

def main():
    streams = getLogStreamNames(LOG_GROUP)

    print(len(streams))

    for stream in streams:
        get_caller_info(stream)


if __name__  == "__main__":
    main()