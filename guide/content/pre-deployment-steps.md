---
weight: 7
title: Predeployment options
description: Pre Deployment Options
---

# Predeployment options

Before deploying this AWS Built-in solution, complete the following steps:

1. Subscribe to the CloudCheckr - Govern and Optimize AWS at Scale [AWS Marketplace listing](https://aws.amazon.com/marketplace/pp/prodview-s3pimhbls2qpm).
2. In your AWS account, confirm that you have an IAM role to run the AWS Built-in solution, the necessary permissions to create and manage CloudFormation stacks, and access to the required services such as S3 and Lambda.
3. Purchase CloudCheckr on AWS Marketplace. For private pricing options, reach to the sales team at CloudCheckr.
4. After purchasing CloudCheckr, an account is created, a user is automatically generated, and an email is sent to you with login instructions.
5. Using the activation link, log in to CloudCheckr.
6. Do the following steps to create an API key and secret within CloudCheckr:
    1. Click the three vertical dots in the top right corner.
    2. Choose **Access Management > API Management**.
    3. Choose **Clients** and click **+NEW**.
    4. Name your API client and set the client role to **Full administrator**.
    5. Save the new client.
    6. Click **+New** to generate an access key, provide a name, and choose **Create**.
    7. Copy the API secret.
7. Run an AWS Cost and Usage Report on your S3 bucket in your AWS account. If you don't have a report, follow the steps in [Setting up an Amazon S3 bucket for Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-s3.html).
8. Review the [CloudCheckr additional resources documentation](https://success.cloudcheckr.com) and keep it handy while you navigate this guide.

**Next**: [Deployment steps](/deployment-steps/index.html)
