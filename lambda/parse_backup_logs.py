import json
import boto3
import os

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('AUDIT_TABLE', 'BackupAuditTable')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        log_data = json.loads(content)

        summary = {
            'BackupId': log_data.get('backup_id'),
            'Status': log_data.get('status'),
            'SizeMB': log_data.get('size_mb'),
            'Timestamp': log_data.get('timestamp')
        }

        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item=summary)

    return {'statusCode': 200, 'body': 'Backup audit logs processed successfully'}
