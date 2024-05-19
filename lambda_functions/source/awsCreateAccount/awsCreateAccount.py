########################################################################
# Copyright NetApp, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
########################################################################

import json
import base64
import boto3
import urllib.request
import urllib.parse
import threading
import logging

def lambda_handler(event, context):
    response = {'accountId': None}
    timer = threading.Timer((context.get_remaining_time_in_millis() / 1000.00) - 0.5, timeout, args=[event, context])
    timer.start()
    try:
        APIKey = event['ResourceProperties']['pAPIKey']
        APISecret = event['ResourceProperties']['pAPISecret']
        Environment = event['ResourceProperties']['pEnvironment']
        customerNumber = event['ResourceProperties']['pCustomerNumber']

        if event['RequestType'] == 'Delete':
            send_response(event, context, 'SUCCESS', {'Message': 'Resource deletion completed'})
        else:
            account_aliases, account_number = get_account_name()
            accountName = account_aliases[0] if account_aliases else None
            bearerToken = get_access_token("https://auth-"+Environment+".cloudcheckr.com/auth/connect/token", APIKey, APISecret)
            response = getPreviousAccountNameID(customerNumber, bearerToken, account_number, Environment)
            if response != None:
                response = send_response(event, context, 'SUCCESS', {'accountNumber': response})
            elif response is None:
                response = createAccount(customerNumber, accountName, account_number, bearerToken, Environment)
                if response['statusCode'] == 200:
                    response = send_response(event, context, 'SUCCESS', {'accountNumber': response['accountId']})
                else:
                    response = send_response(event, context, 'FAILED', {'Error': response['body']})
            
    except Exception as e:
        timer.cancel()
        sendResponse = send_response(event, context, 'FAILED', {'Error': 'An error occurred during the Lambda execution: ' + str(e)})
        return {
            'statusCode': 500,
            'body': 'An error occurred during the Lambda execution: ' + str(e)
        }

    finally:
        timer.cancel()
        sendResponse = send_response(event, context, 'SUCCESS', {'accountNumber': response['accountId']})

def timeout(event, context):
    logging.error('Execution is about to time out, sending failure response to CloudFormation')
    send_response(event, context, 'FAILED', {'Error': 'Execution is about to time out'})


def send_response(event, context, response_status, response_data):
    response_body = json.dumps({
        'Status': response_status,
        'Reason': 'See the details in CloudWatch Log Stream: ' + context.log_stream_name,
        'PhysicalResourceId': context.log_stream_name,
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'Data': response_data
    })

    headers = {
        'Content-Type': 'application/json',
        'Content-Length': str(len(response_body))
    }

    req = urllib.request.Request(event['ResponseURL'], data=response_body.encode('utf-8'), headers=headers, method='PUT')
    with urllib.request.urlopen(req) as f:
        pass

def getPreviousAccountNameID(customer_number, bearer_token, accountname, environment):
    url = f"https://api-"+environment+".cloudcheckr.com/customer/v1/customers/"+customer_number+"/account-management/accounts?search="+accountname
    headers = {
        'accept': 'text/plain',
        'content-type': 'application/json',
        'authorization': 'bearer ' + bearer_token
    }
    try:
        request = urllib.request.Request(url, headers=headers, method='GET')
        with urllib.request.urlopen(request, timeout=15) as response:
            response_text = response.read().decode()
            response_json = json.loads(response_text)
            if 'items' in response_json and len(response_json['items']) == 1:
                account_id = response_json['items'][0]['id']
                return account_id
            else:
                print("No account found or multiple accounts found.")
                return None
                
    except Exception as e:
        print(f"error retrieving previous account id: {e}")
        return None



def createAccount(customer_number, accountname, account_number, bearer_token, environment):
    url = f"https://api-"+environment+".cloudcheckr.com/customer/v1/customers/"+customer_number+"/account-management/accounts"
    payload = json.dumps({
        "item": {
            "name": account_number + " - " + accountname,
            "provider": "aws"
        }
    })
    headers = {
        'accept': 'text/plain',
        'content-type': 'application/json',
        'authorization': 'bearer ' + bearer_token
    }
    try:
        request = urllib.request.Request(url, data=payload.encode(), headers=headers, method='POST')
        with urllib.request.urlopen(request, timeout=15) as response:
            response_text = response.read().decode()
            response_json = json.loads(response_text)
            if 'id' in response_json:
                return {
                    'statuscode': 200,
                    'body': 'completed!',
                    'accountid': response_json['id'],
                    'bearertoken': bearer_token
                }
            else:
                return {
                    'statuscode': 200,
                    'body': 'no id found, errors',
                    'accountid': None,
                    'bearertoken': bearer_token
                }
    except Exception as e:
        print(f"unexpected error: {e}")
        return {
            'statuscode': 500,
            'body': 'an unexpected error occurred',
            'accountid': None
        }


def get_access_token(url, client_id, client_secret):
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")
    data = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        method='POST'
    )

    with urllib.request.urlopen(req) as response:
        response_json = json.loads(response.read().decode())
    return response_json["access_token"]

def get_account_name():
    iam = boto3.client('iam')
    response = iam.list_account_aliases()
    account_number = boto3.client('sts').get_caller_identity()['Account']
    print(response['AccountAliases'], account_number)
    return response['AccountAliases'], account_number

