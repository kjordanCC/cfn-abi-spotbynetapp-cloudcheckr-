---
weight: 6
title: Deployment options
description: Various deployment options for the ABI package.
---
# Deployment options

This AWS Built-in solution provides various deployment options to cater to different organizational needs and requirements. Choose the one that fits your environment and infrastructure setup.

Features include
- Automated configuration and setup.
- Seamless integration with existing AWS services.
- Comprehensive monitoring and management capabilities.

The following deployment options offer flexibility and control in deploying the solution across various environments.

## Option 1: Launch the CloudFormation template in individual AWS account

Choose this option to deploy the solution using a CloudFormation template in each individual account.

Do the following steps:
1. Navigate to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).
2. Follow the instructions in the [Launch the CloudFormation template in the management account](https://github.com/aws-ia/cfn-abi-spotbynetapp-cloudcheckr/blob/main/guide/content/deployment-steps.md#launch-the-cloudformation-template-in-the-management-account) section.

## Option 2: Launch using Customizations for Control Tower

This method is for organizations using AWS Control Tower. It uses Customizations for AWS Control Tower (CfCT) to facilitate deployment, ensuring alignment with organizational policies and standards.

Do the following steps:
1. Navigate to the [CfCT console](https://console.aws.amazon.com/controltower/).
2. Follow the instructions in the [Launch Using Customizations for Control Tower](https://github.com/aws-ia/cfn-abi-spotbynetapp-cloudcheckr/blob/main/guide/content/deployment-steps.md#launch-using-customizations-for-control-tower-cfct) section.

**Next**: [Predeployment steps](/pre-deployment-steps/index.html)
