---
weight: 9
title: PostDeployment Options
description: Post deployment options
---

## Verifying the solution functionality

After deploying the ABI package, you can verify its functionality by checking the following:

1. **AWS Console**: Log in to your AWS Console and navigate to the CloudFormation service console.
Wait for the CloudFormation stack to finish deploying. You can check the status of the deployment either via the AWS console or by running the following command:

   ```
   aws cloudformation describe-stacks --stack-name <YOUR_STACK_NAME>
   ```

   The stack status is returned in the output. Wait until the status is `CREATE_COMPLETE` before proceeding to the next step. When the stack finishes deploying, you can access the created resources via the AWS Management Console or AWS CLI.

After the deployment completes, you will see the root stack and nested stacks in the AWS Control Tower management account with status `CREATE_COMPLETE`.
Check if the resources were created and configured as expected by checking the `Resources` tab in the details of the CloudFormation stack.

2. **CloudCheckr Dashboard**: Log in to your CloudCheckr account and check if the AWS account has been credentialed and if the expected data is being pulled in from AWS.


**Next:** Choose [Test the Deployment](/test-deployment/index.html) to get started.