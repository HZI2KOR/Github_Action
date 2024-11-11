# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

AWSAcyID-AKIAVFIWJBN6IV3EF6UF

Sey-dwRs/ADb70N16H2bZjwMm0PGe6e5KJTAR393P4wa

#!/bin/bash
VIDEO_PATH="/home/rasberryp1/output.avi"
BUCKET_NAME="rpi400bucket"
AWS_PATH="s3://$BUCKET_NAME/recordings/$(date +\%Y\%m\%d\%H\%M\%S)_output.avi"

# Upload to S3
aws s3 cp "$VIDEO_PATH" "$AWS_PATH" --acl public-read

