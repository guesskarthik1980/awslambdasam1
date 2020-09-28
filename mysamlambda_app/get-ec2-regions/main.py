import json
import boto3

ecclient = boto3.client('ec2')

def lambda_handler(event, context):
    ecRegions = ecclient.describe_regions()
    return {
        "statusCode":200,
        "body":ecRegions['Regions']
    }