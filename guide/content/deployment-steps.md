---
weight: 10
title: Deployment steps
description: Deployment steps
---

## Launch the CloudFormation Template in the Management Account

1. Download the CloudFormation template from the source: `https://<abi-template-location>`
2. Launch the CloudFormation template in your AWS Control Tower home region.
    * Stack name: `template-cfn-abi-spotbynetapp-cloudcheckr-enable-integrations`
    * List Parameters:
        * **pAPIKey**: The API ID created in the CloudCheckr environment.
        * **pAPISecret**: The secret associated with the APIKey.
        * **pCustomerNumber**: Found in the URL when logged into CloudCheckr. Example: https://app-us.cloudcheckr.com/customers/1234567 (The number after /customers/  in this case the customer number would be 1234567).
        * **pCurBucketName**: Name of the S3 bucket for CUR data (If master payer account).
        * **pBillingBucketName**: Name of the S3 bucket for billing data.(depricated)
        * **pCloudTrailBucketName**: Name of the S3 bucket for CloudTrail logs.
        * **pABIStagingS3Key**: The staging S3 key for ABI.
        * **pABISourceS3BucketName**: The source S3 bucket name for ABI.
        * **pABIS3BucketRegion**: The region of the S3 bucket for ABI.
   
3. Choose both the **Capabilities** and select **Submit** to launch the stack.
   - [] I acknowledge that AWS CloudFormation might create IAM resources with custom names.
   - [] I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND   

Wait for the CloudFormation status to change to `CREATE_COMPLETE` state.

## Launch using Customizations for Control Tower (CfCT)

The templates provided as part of the ABI packages are deployable using Customizations for Control Tower. Please check below for additional details.

#### Pre-requisites

1. The CfCT solution does not have the ability to launch resources on the Management account. Hence, you need to create the role with required permissions in the Management account.

#### How it works

To deploy this sample partner integration page using the CfCT solution, add the following blurb to the `manifest.yaml` file from your CfCT solution and update the account/ou names as needed.

```yaml
resources:
  - name: sra-enable-partner1-solution
    resource_file: https://aws-abi-pilot.s3.us-east-1.amazonaws.com/cfn-abi-aws-reference-guide/templates/abi-enable-partner1-securityhub-integration.yaml
    deploy_method: stack_set
    parameters:
      - parameter_key: pProductArn
        parameter_value: arn:aws:securityhub:us-east-1::product/cloud-custodian/cloud-custodian
      - parameter_key: pSRASourceS3BucketName
        parameter_value: aws-abi-pilot
      - parameter_key: pSRAStagingS3KeyPrefix
        parameter_value: cfn-abi-aws-reference-guide
    deployment_targets:
      accounts:
        - [[MANAGEMENT-AWS-ACCOUNT-ID]]
