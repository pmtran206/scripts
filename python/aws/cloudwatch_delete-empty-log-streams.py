# Query specific log group to find empty log streams and delete them

import boto3
import json
from boto3 import Session
from botocore.exceptions import ClientError

# import AWS Session

SOURCE_PROFILE = 'sandbox'

LOG_GROUP  = 'name\of\log\group'

source_session = boto3.Session(profile_name=SOURCE_PROFILE)
source_client = source_session.client('logs')

# retrieve all log stream names in a given log group

def get_logStreamNames(logGroup):
    streams = []
    paginator = source_client.get_paginator('describe_log_streams')
    logstream_pages = paginator.paginate(
        logGroupName = logGroup,
        orderBy = 'LastEventTime'
    )

    for page in logstream_pages:
        for item in page['logStreams']:
            streams.append( item['logStreamname' ])
            
    return streams