
from aws_cdk import (
    core,
    aws_s3 as _s3
)
from constructs import Construct


class S3CreateProject(core.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="my-s3buckets-got-a-hole-in-it",  # hat tip to Clarence Williams
            encryption=_s3.BucketEncryption.KMS_MANAGED
            ## Add others as needed.  See https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3/Bucket.html
        )
