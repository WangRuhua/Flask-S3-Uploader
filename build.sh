#!/bin/bash
sh version.sh || exit 1
docker build -t s3-uploader:dev . || exit 3

docker stop s3-uploader-dev
docker run --rm  -d   -p 5050:80 --env-file ./env.list  --name s3-uploader-dev s3-uploader:dev  || docker logs s3-uploader-dev

docker ps