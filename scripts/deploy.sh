#!/bin/bash

git log -1 > templates/sync.txt
cat templates/sync.txt
aws s3 sync templates/ s3://$CF_S3_BUCKET --delete --region $AWS_REGION
