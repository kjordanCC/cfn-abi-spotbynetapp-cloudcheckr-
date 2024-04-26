---
weight: 99
title: Cleanup instructions
description: Instructions to clean up the resources created by the ABI package
---

# Cleanup instructions

To remove all resources created by the AWS Built-in solution and avoid unexpected costs, follow these instructions. The cleanup process involves deleting the CloudFormation stack and all associated resources.

## Deleting the CloudFormation stack

1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).
2. Locate the stack created by the AWS Built-in solution.
3. Choose **Delete**, and confirm the deletion.

CloudFormation automatically deletes all related resources.

## Deleting additional resources

If you created additional resources outside of the CloudFormation stack, manually delete those resources. Additional resources typically include S3 buckets, IAM roles, and Lambda functions.

### Deleting S3 buckets

1. Navigate to the [AWS S3 console](https://s3.console.aws.amazon.com/s3/).
2. Locate the buckets created by the AWS Built-in solution and delete them.

### Deleting IAM roles

1. Navigate to [AWS IAM console](https://console.aws.amazon.com/iam/).
2. Locate the roles created by the AWS Built-in solution and delete them.

### Deleting Lambda functions

1. Navigate to the [AWS Lambda console](https://console.aws.amazon.com/lambda/).
2. Locate the Lambda functions created by the AWS Built-in solution and delete them.

### Deleting Previous ARN in CloudCheckr

1. Navigate to the [CloudCheckr Account Management Console].
2. Edit the credentialing field of the account and select "Delete" to remove the arn from the preexisting account.

## Verifying resource deletions

In each service console, verify that all AWS Built-in resources are removed. If any resources remain, they may continue to incur costs.

**Note:** Avoid accidentally deleting important resources. Be sure that you delete only resources related to the AWS Built-in solution.
