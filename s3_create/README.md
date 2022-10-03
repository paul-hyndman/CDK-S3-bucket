A sample project showing how to deploy an S3 bucket using CDK with Python

Requires installs for:
 - CKD
 - Python
 - IDE of your choice
 - Node JS (for npm, for other installs)
 - AWS CLI and a personal AWS account
 - Gitbash, or similar

Check out https://github.com/paul-hyndman/CDK-S3-bucket, then run:
cdk init app --language python

If you are a Windows platform, you would activate the virtualenv like this: (** Important before starting development **)
% .venv\Scripts\activate.bat

Once the virtualenv is activated, you can install the required dependencies.
$ pip install -r requirements.txt

# CDK commands in Gitbash:
1. cdk bootstrap  # Typically a one time thing per account per region.
2. cdk ls 	# shows resources created by scripts, checks for syntax errors
3. cdk.out is created showing resources to created
4. cdk synth # Create cloud formation template
     See file S3CreateProject.template.json in cdk.out directory for S3 resource to create

# Ensure you're attached to AWS account via "aws configure"

$ cdk bootstrap  # one-time thing per account & region, showing output like:
    ⏳  Bootstrapping environment aws://991417388566/us-east-1...
    Trusted accounts for deployment: (none)
    Trusted accounts for lookup: (none)
    Using default execution policy of 'arn:aws:iam::aws:policy/AdministratorAccess'. Pass '--cloudformation-execution-policies' to customize.
    ✅  Environment aws://991417388566/us-east-1 bootstrapped (no changes).

# To deploy:
    $ cdk deploy
      # Output such as:
      ✨  Synthesis time: 6.64s

		MyFirstCdkProjectStack: deploying...
		MyFirstCdkProjectStack: creating CloudFormation changeset...
		MyFirstCdkProjectStack | 0/3 | 2:56:52 PM | REVIEW_IN_PROGRESS   | AWS::CloudFormation::Stack | MyFirstCdkProjectStack User Initiated
		MyFirstCdkProjectStack | 0/3 | 2:56:59 PM | CREATE_IN_PROGRESS   | AWS::CloudFormation::Stack | MyFirstCdkProjectStack User Initiated
		MyFirstCdkProjectStack | 0/3 | 2:57:04 PM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata | CDKMetadata/Default (CDKMetadata)
		MyFirstCdkProjectStack | 0/3 | 2:57:05 PM | CREATE_IN_PROGRESS   | AWS::S3::Bucket    | myBucketId (myBucketId9D590DD7)
		MyFirstCdkProjectStack | 0/3 | 2:57:06 PM | CREATE_IN_PROGRESS   | AWS::S3::Bucket    | myBucketId (myBucketId9D590DD7) Resource creation Initiated
		MyFirstCdkProjectStack | 0/3 | 2:57:06 PM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata | CDKMetadata/Default (CDKMetadata) Resource creation Initiated
		MyFirstCdkProjectStack | 1/3 | 2:57:07 PM | CREATE_COMPLETE      | AWS::CDK::Metadata | CDKMetadata/Default (CDKMetadata)
		MyFirstCdkProjectStack | 2/3 | 2:57:26 PM | CREATE_COMPLETE      | AWS::S3::Bucket    | myBucketId (myBucketId9D590DD7)
		MyFirstCdkProjectStack | 3/3 | 2:57:27 PM | CREATE_COMPLETE      | AWS::CloudFormation::Stack | MyFirstCdkProjectStack

		 ✅  MyFirstCdkProjectStack

		✨  Deployment time: 40.91s

# You can verify S3 Bucket on AWS console 

## Useful commands
 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

