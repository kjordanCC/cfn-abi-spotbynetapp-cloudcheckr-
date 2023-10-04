---
weight: 5
title: Architecture
description: Solution architecture.
---

Deploying this ABI package with default parameters builds the following architecture.

![Architecture diagram](/images/architecture.png)

As shown in the diagram, the ABI for CloudCheckr sets up the following:

* In all current and AWS accounts in your AWS organization:
    * Amazon CloudWatch Events rules to detect changes in AWS Config configuration items (CIs) and trigger AWS Lambda functions.
    * IAM Roles to perform various tasks and manage permissions.

* In the management account:
    * S3 bucket policy and CloudFormation stacks to manage and deploy resources.

* In the log archive account:
    * Lambda functions for creating AWS accounts in CloudCheckr and credentialing.

* In the security tooling account:
    * Custom resources and Lambda functions for managing external IDs and copying objects between S3 buckets.

This architecture allows CloudCheckr customers to monitor their environment for CloudWatch events automatically and efficiently, as well as access other valuable cloud management features within CloudCheckr.

**Next:** Choose [Deployment Options](/deployment-options/index.html) to get started.


