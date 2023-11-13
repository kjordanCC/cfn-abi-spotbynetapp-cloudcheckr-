---
weight: 9
title: Postdeployment Options
description: Post deployment options
---
# Postdeployment steps

## Verifying the solution functionality

After deploying the AWS Built-in solution, do the following steps to verify its functionality:

1. Log in to the AWS Management Console and navigate to the CloudFormation service console.

Wait for the CloudFormation stack to finish deploying. You can check the status of the deployment either via the console or by running the following command:

   ```
   aws cloudformation describe-stacks --stack-name <YOUR_STACK_NAME>
   ```

   The stack status is returned in the output. Wait until the status is `CREATE_COMPLETE` before proceeding to the next step. When the stack finishes deploying, you can access the created resources via the AWS Management Console or AWS Command Line Interface (AWS CLI).

After the deployment completes, you will see the root stack and nested stacks in the AWS Control Tower management account with status `CREATE_COMPLETE`.

From the stack details, check the `Resources` tab to confirm that resources were created and configured as expected.

2. Log in to the CloudCheckr account dashboard and confirm that the AWS account has been credentialed and is pulling in the expected data from AWS.

**Next**: [Test the deployment](/test-deployment/index.html)