# -*- coding: utf-8 -*-

import uuid
import boto3
import json
from boto3.dynamodb.conditions import Key


class Bbs:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table('serverless_bbs')

    def write(self, username, message):
        res = self.table.put_item(
            Item={
                "uuid": uuid.uuid4().hex,
                "username": username,
                "message": message
            }
        )
        return json.dumps(res)

    def read_all(self):
        res = self.table.scan()
        return json.dumps(res)

    def select(self, uuid):
        res = self.table.query(
            KeyConditionExpression=Key('uuid').eq(uuid)
        )
        return json.dumps(res)

    # Not working...
    def delete(self, uuId):
        res = self.table.delete_item(Key={'uuid': uuId})
        return json.dumps(res)


def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        bbs = Bbs()
        res = bbs.read_all()
        return res
    elif event['httpMethod'] == 'POST':
        bbs = Bbs()
        res = bbs.write(event['username'], event['message'])
        return res
    else:
        return 'ng'
