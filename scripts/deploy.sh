#!/bin/bash

aws s3 sync templates/ s3://$CF_S3_BUCKET --delete --region $AWS_REGION
echo fooo
