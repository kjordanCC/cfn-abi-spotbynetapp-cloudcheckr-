# CloudFormation Template Readme

This CloudFormation template is designed to automate the building of an IAM Role and credentialing against a CloudCheckr account. It sets up resources such as S3 buckets, Lambda functions, and CloudFormation stacks.

```plaintext
Built-In Documentation
This documentation offers guidance on purchasing CloudCheckr from the AWS Marketplace and provides a CloudFormation stack for quick and easy AWS account credentialing within the CMx platform.

Prerequisites (Manual)
1. Enable Cost Explorer in your AWS Payer account: Follow the instructions at AWS Cost Management Documentation.
2. Enable Cost Allocation Tags: Refer to the CloudCheckr Knowledge Base for more information.
3. Ensure you have an IAM role in your AWS account to run the CloudFormation stack.
4. Purchase CloudCheckr on the AWS Marketplace: This will create a CloudCheckr account, automatically generate a user, and send you an email with login instructions.
5. Create an API key and Secret within CloudCheckr:
   - Log in to CloudCheckr.
   - Click the three vertical dots in the top right corner.
   - Select Access Management > API Management.
   - Choose Clients and click +NEW.
   - Name your API client and set the client Role to "Full administrator".
   - Save the new client.
   - Click +new to generate an access key, provide a name, and select Create.
   - Copy the API secret and API ID number for later use in the CloudFormation stack.

Running the CloudFormation Template
After completing the prerequisites, you can now run the CloudFormation template to automatically provision your AWS account within the CloudCheckr environment. The template will require the following information:
- APIKey: The API ID created in the CloudCheckr environment.
- APISecret: The secret associated with the APIKey.
- BillingBucketName: Name of the S3 bucket for billing data.
- CloudTrailBucketName: Name of the S3 bucket for CloudTrail logs.
- CurBucketName: Name of the S3 bucket for CUR data.
- CustomerNumber: Found in the URL when logged into CloudCheckr. Example: https://app-us.cloudcheckr.com/customers/1234567 (The number after /customers/).

After CloudFormation Stack Successfully Runs
Once the account is successfully credentialed in CloudCheckr, you can configure the cost and usage report within the platform. Follow the instructions at CloudCheckr Knowledge Base.




## Parameters

The template includes the following parameters:

- `pAPIKey`: The API key for CloudCheckr.
- `pAPISecret`: The API secret for CloudCheckr.
- `pCustomerNumber`: The customer number for CloudCheckr.
- `pCurBucketName`: The name of the S3 bucket for CUR (Cost and Usage Report) data.
- `pBillingBucketName`: The name of the S3 bucket for billing data.
- `pCloudTrailBucketName`: The name of the S3 bucket for CloudTrail logs.
- `pSRAStagingS3Key`: The S3 key for staging resources. Default value: `cfn-abi-spotbynetapp-cloudcheckr`.
- `pSRASourceS3BucketName`: The name of the source S3 bucket for Lambda function packages. Default value: `aws-abi-pilot`.

## Resources

The CloudFormation template creates the following resources:

- `rABIStagingS3Bucket`: An S3 bucket for staging resources.
- `rABIStagingS3BucketPolicy`: A bucket policy for the staging S3 bucket.
- `rLambdaExecutionRole`: An IAM role for Lambda execution.
- `rLambdaawsCreateAccountFunction`: A Lambda function for creating AWS accounts.
- `rCustomResourceAwsCreateAccountInvoke`: A custom resource that invokes the `rLambdaawsCreateAccountFunction` Lambda function.
- `rgetExternalIDFunction`: A Lambda function for getting the external ID.
- `rCustomResourceGetExternalIDInvoke`: A custom resource that invokes the `rgetExternalIDFunction` Lambda function.
- `rdeployIAMstack`: A CloudFormation stack that deploys an IAM stack using an external template.
- `rLambdaAwsCredentialAccountFunction`: A Lambda function for credentialing the AWS account.
- `rCustomResourceAwsCredentialAccountInvoke`: A custom resource that invokes the `rLambdaAwsCredentialAccountFunction` Lambda function.
- `rCopyZips`: A custom resource that copies Lambda function packages from the source S3 bucket to the staging S3 bucket.
- `rCopyZipsRole`: An IAM role for the `rCopyZips` custom resource.
- `rCopyZipsFunction`: A Lambda function for copying objects between S3 buckets.

## Usage

To use this CloudFormation template, follow these steps:

1. Create an S3 bucket for storing the CloudFormation template and make it publicly accessible.
2. Copy the contents of this template into a new file and upload it to the S3 bucket.
3. Open the AWS CloudFormation service in the AWS Management Console.
4. Click on "Create stack" and choose "With new resources (standard)".
5. Specify the S3 URL of the template file you uploaded.
6. Fill in the required parameters:
   - `pAPIKey`: Provide the CloudCheckr API key.
   - `pAPISecret`: Provide the CloudCheckr API secret.
   - `pCustomerNumber`: Provide the customer number for CloudCheckr.
   - `pCurBucketName`: Specify the name of the S3 bucket for CUR data.
   - `pBillingBucketName`: Specify the name of the S3 bucket for billing data.
   - `pCloudTrailBucketName`: Specify the name of the S3 bucket for CloudTrail logs.
   - `pSRAStagingS3Key`: (Optional) You can leave the default value or specify a custom S3 key for staging resources.
   - `pSRASourceS3BucketName`: (Optional) You can leave the default value or specify a different source S3 bucket name for Lambda function packages.

7. Review the configuration and click "Next" to proceed.
8. Optionally, you can specify additional stack options and tags.
9. Click "Next" to configure any stack options or tags if desired.
10. Review the stack details and click "Create stack" to initiate the stack creation process.
11. Wait for the stack creation to complete. You can monitor the progress in the AWS CloudFormation console.
12. Once the stack creation is finished, you can access and manage the resources created by the template, such as the S3 buckets and Lambda functions.

Note: Ensure that you have the necessary permissions to create and manage CloudFormation stacks, as well as access to the required services such as S3 and Lambda.

Remember to clean up the resources created by deleting the CloudFormation stack when you no longer need them to avoid incurring unnecessary costs.
