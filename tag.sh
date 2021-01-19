#!/bin/bash
AWS_ID="your aws account id"
new_tag=$(git rev-parse --short HEAD)-$(date +%F)
docker build -t s3-uploader .
docker tag s3-uploader:latest s3-uploader:${new_tag}
docker tag s3-uploader:latest ${AWS_ID}.dkr.ecr.us-east-1.amazonaws.com/s3-uploader:latest
docker tag s3-uploader:${new_tag} ${AWS_ID}.dkr.ecr.us-east-1.amazonaws.com/s3-uploader:${new_tag}
docker push $AWS_ID.dkr.ecr.us-east-1.amazonaws.com/s3-uploader:latest
docker push $AWS_ID.dkr.ecr.us-east-1.amazonaws.com/s3-uploader:${new_tag}
