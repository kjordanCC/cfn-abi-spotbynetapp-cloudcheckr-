import json
import base64
import urllib.request
import urllib.parse


def lambda_handler(event, context):
    resource_properties = event['ResourceProperties']
    APIKey = resource_properties['pAPIKey']
    APISecret = resource_properties['pAPISecret']
    customerNumber = resource_properties['pCustomerNumber']
    accountNumber = resource_properties['AccountNumber']
    RoleArn = resource_properties['RoleArn']

    bearerToken = get_access_token("https://auth-us.cloudcheckr.com/auth/connect/token", APIKey, APISecret)

    response = credentialAccount(customerNumber, accountNumber, RoleArn, bearerToken)

    send_response(event, context, 'SUCCESS', {})
    return response


def credentialAccount(customerNumber, accountNumber, RoleArn, bearerToken):
    url = f"https://api-us.cloudcheckr.com/credential/v1/customers/{customerNumber}/accounts/{accountNumber}/credentials/aws"
    
    payload = json.dumps({
        "item": {
            "regionGroup": "Commercial",
            "crossAccountRole": {
                "roleArn": RoleArn
            }
        }
    })

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {bearerToken}'
    }

    request = urllib.request.Request(url, headers=headers, data=payload.encode(), method='PUT')
    try:
        response = urllib.request.urlopen(request, timeout=15)
    except urllib.error.HTTPError as e:
        raise

    response_text = response.read().decode()

    return {
        'statusCode': 200,
        'body': 'completed!',
    }


def send_response(event, context, response_status, response_data):
    response_body = json.dumps({
        'Status': response_status,
        'Reason': f'See the details in CloudWatch Log Stream: {context.log_stream_name}',
        'PhysicalResourceId': context.log_stream_name,
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'Data': response_data
    })

    headers = {
        'Content-Type': '',
        'Content-Length': str(len(response_body))
    }

    request = urllib.request.Request(event['ResponseURL'], data=response_body.encode('utf-8'), headers=headers, method='PUT')
    with urllib.request.urlopen(request) as f:
        pass


def get_access_token(url, client_id, client_secret):
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")
    data = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        method='POST'
    )

    response = urllib.request.urlopen(request)
    response_json = json.loads(response.read().decode())
    return response_json["access_token"]
