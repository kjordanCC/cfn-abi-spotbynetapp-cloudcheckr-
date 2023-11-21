---
weight: 5
title: Architecture
description: Solution architecture
---

Deploying this AWS Built-in solution with default parameters builds the following architecture:

![Architecture diagram](/images/cloudcheckr-abi-architecture-diagram.png)

As shown in the diagram, the solution sets up the following:

* In every account where the AWS CloudFormation template is deployed:
    * AWS Identity and Access Management (IAM) role with read permissions to various AWS services required by CloudCheckr.
    * AWS Lambda functions for creating and credentialing AWS accounts in CloudCheckr.
    * Amazon Simple Storage Service (Amazon S3) staging bucket for the CloudCheckr AWS Built-in solution resources.

Using this architecture, CloudCheckr customers can monitor their environment for Amazon CloudWatch events automatically and efficiently. They can also access other valuable cloud management features within CloudCheckr.

**Next**: [Deployment options](/deployment-options/index.html)
