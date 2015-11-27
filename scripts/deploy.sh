#!/bin/bash

git log -2 > templates/sync.txt
echo "--- LATEST COMMIT ---"
cat templates/sync.txt
aws s3 sync templates/ s3://$CF_S3_BUCKET --delete --region $AWS_REGION
