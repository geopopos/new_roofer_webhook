import json
import boto3
import os

StateMachine = boto3.client('stepfunctions')


def create_new_roofer_webhook(event, context):
    stateMahcineArn = os.environ.get('STATE_MACHINE_ARN') 
    print(stateMahcineArn)
    response = StateMachine.start_execution(
        stateMachineArn=stateMahcineArn,
        name='Create-New-Roofer',
        input=json.dumps(event)
    )
    response = {"statusCode": 200, "body": json.dumps(response)}

    return response
