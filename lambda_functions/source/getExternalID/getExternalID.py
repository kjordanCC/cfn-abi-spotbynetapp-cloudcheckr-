import json
import base64
import boto3
import urllib.request
import urllib.parse


def lambda_handler(event, context):
    print("event: ", event)
    print("context: ", context)
    APIKey = event['ResourceProperties']['pAPIKey']
    APISecret = event['ResourceProperties']['pAPISecret']
    customerNumber = event['ResourceProperties']['pCustomerNumber']
    accountNumber = event['ResourceProperties']['AccountNumber']

    print("getting token")
    bearerToken = get_access_token("https://auth-us.cloudcheckr.com/auth/connect/token", APIKey, APISecret)
    

    response = getExternalID(customerNumber, accountNumber, bearerToken)
    print("response: ", response)

    response_data = {'externalAccount': response['awsAccountId'], 'ExternalId': response['externalIdValue']}

    sendResponse = send_response(event, context, 'SUCCESS', response_data)
    print("sendResponse: ", sendResponse)

    return response_data

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
        'Content-Type': '',
        'Content-Length': str(len(response_body))
    }

    req = urllib.request.Request(event['ResponseURL'], data=response_body.encode('utf-8'), headers=headers, method='PUT')
    with urllib.request.urlopen(req) as f:
        print('Status code:', f.status)
        print('Status message:', f.reason)

    

 
def getExternalID(customerNumber, accountNumber, bearerToken):
    region = "Commercial"
    url = "https://api-us.cloudcheckr.com/credential/v1/customers/"+str(customerNumber)+"/accounts/"+str(accountNumber)+"/external-id/aws/"+region
    print("url: ", url)
    headers = {
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearerToken
    }
    response = urllib.request.urlopen(urllib.request.Request(
        url,
        headers=headers,
        method='GET'),
        timeout=15)
    
    response_text = response.read().decode()
    print("response: ", response_text)

    # Extract the ID from the response
    response_json = json.loads(response_text)
    externalIdValue = response_json.get('externalIdValue')  # Using the key 'id' to extract the account ID
    awsAccountId = response_json.get('awsAccountId')


    return {
        'statusCode': 200,
        'body': 'completed!',
        'externalIdValue': externalIdValue,  # Return the extracted account ID
        'awsAccountId': awsAccountId
    }




def get_access_token(url, client_id, client_secret):
    # Prepare the basic authentication header
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")

    # Prepare the data payload
    data = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode("utf-8")

    # Create the request object
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        method='POST'
    )

    response = urllib.request.urlopen(req)
    response_json = json.loads(response.read().decode())
    return response_json["access_token"]
