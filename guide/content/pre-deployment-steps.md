---
weight: 7
title: PreDeployment Options
description: Pre Deployment Options
---

# PreDeployment Options

Before deploying this ABI package, complete the following steps:

1. **Subscribe to Partner Product**: Subscribe to the partner product from the AWS Marketplace using [AWS Marketplace Listing](https://aws.amazon.com/marketplace/pp/prodview-s3pimhbls2qpm).
    - Follow the subscription process outlined on the AWS Marketplace listing page.

2. **Things to be Done Before Deployment**:
    - Ensure you have an IAM role in your AWS account to run the ABI, and that you have the necessary permissions to create and manage CloudFormation stacks, as well as access to the required services such as S3 and Lambda.
    - Purchase CloudCheckr on AWS Marketplace at AWS Marketplace. For private pricing options reach to CloudCheckr at Contact Sales
    - Upon purchasing CloudCheckr, a CloudCheckr account is created, a user is automatically generated, and an email is sent to you with login instructions.
    - Using the activation link, login into CloudCheckr.
    - Create an API key and Secret within CloudCheckr:
        - Click the three vertical dots in the top right corner.
        - Select Access Management > API Management.
        - Choose Clients and click +NEW.
        - Name your API client and set the client Role to “Full administrator”.
        - Save the new client.
        - Click +new to generate an access key, provide a name, and select Create.
        - Copy the API secret
    - Have an AWS Cost and Usage Report S3 bucket on your AWS Account. If you don't have one you can create one by following these (steps) [https://docs.aws.amazon.com/cur/latest/userguide/cur-s3.html].

3. **Become Familiar with Additional Resources**:
    - Ensure to review and become familiar with the [additional resources](https://success.cloudcheckr.com), which will be helpful later in this guide.


**Next:** Choose **[Deployment Steps](/deployment-steps/index.html)** to get started.
