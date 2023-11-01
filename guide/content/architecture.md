---
weight: 5
title: Architecture
description: Solution architecture.
---

Deploying this ABI package with default parameters builds the following architecture.

![Architecture diagram](/images/architecture.png)

As shown in the diagram, the CloudCheckr ABI solution sets up the following:

* In every account where the CloudCheckr ABI CloudFormation template is deployed:
    * IAM Role with read permissions to various AWS services required by CloudCheckr.
    * Lambda functions for creating and credentialing AWS accounts in CloudCheckr.
    * S3 staging bucket for the CloudCheckr ABI solution resources.

This architecture allows CloudCheckr customers to monitor their environment for CloudWatch events automatically and efficiently, as well as access other valuable cloud management features within CloudCheckr.

**Next:** Choose [Deployment Options](/deployment-options/index.html) to get started.


