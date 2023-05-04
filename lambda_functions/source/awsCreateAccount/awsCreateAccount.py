import json
import base64
import boto3
import urllib.request
import urllib.parse
import threading
import logging

def lambda_handler(event, context):
    timer = threading.Timer((context.get_remaining_time_in_millis() / 1000.00) - 0.5, timeout, args=[event, context])
    timer.start()
    try:
        APIKey = event['ResourceProperties']['pAPIKey']
        APISecret = event['ResourceProperties']['pAPISecret']
        customerNumber = event['ResourceProperties']['pCustomerNumber']
        if event['RequestType'] == 'Delete':
            print("delete eventt")
        else:
            account_aliases, account_number = get_account_name()
            print("test")
            accountName = account_aliases[0] if account_aliases else account_number
            print("accountName: ", accountName)

            bearerToken = get_access_token("https://auth-us.cloudcheckr.com/auth/connect/token", APIKey, APISecret)
            print("bearerToken: ", bearerToken)

            response = createAccount(customerNumber, accountName, bearerToken)
            print("response: ", response)

    except Exception as e:
        timer.cancel()
        sendResponse = send_response(event, context, 'FAILED', {'Error': 'An error occurred during the Lambda execution: ' + str(e)})
        print("sendResponse: ", sendResponse)
        return {
            'statusCode': 500,
            'body': 'An error occurred during the Lambda execution: ' + str(e)
        }

    finally:
        timer.cancel()
        sendResponse = send_response(event, context, 'SUCCESS', {'accountNumber': response['accountId']})
        print("sendResponse: ", sendResponse)

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

def createAccount(customer_number, accountName, bearer_token):
    url = "https://api-us.cloudcheckr.com/customer/v1/customers/" + str(customer_number) + "/account-management/accounts"
    payload = json.dumps({
        "item": {
            "name": accountName,
            "provider": "AWS"
        }
    })
    headers = {
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearer_token
    }
    response = urllib.request.urlopen(urllib.request.Request(
        url,
        headers=headers,
        data=payload.encode(),
        method='POST'),
        timeout=15)
    
    response_text = response.read().decode()

    response_json = json.loads(response_text)
    account_id = response_json.get('id')

    return {
        'statusCode': 200,
        'body': 'completed!',
        'accountId': account_id,
        'bearerToken': bearer_token
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
    return response['AccountAliases'], account_number

