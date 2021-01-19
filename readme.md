# AWS S3 Uploader
A tool upload file to AWS s3 bucket,python3.8

## build Docker image
1. `sh version.sh || exit 1`
2. `docker build -t s3-uploader:dev . || exit 3`


## Set local environment variables
```
cat<<EOF>env.list
FLASK_APP=app.py
APP_SETTINGS=config.ProductionConfig｜config.DevelopmentConfig
S3_BUCKET_NAME="your s3 bucket name"
S3_BUCKET_KEY="your s3 bucket key"
SECRET_KEY="your-random-secret-key"
EOF
```
##set AWS access key
```
export AWS_ACCESS_KEY_ID="your aws access key id"
export AWS_SECRET_ACCESS_KEY="your aws secret access key"
export AWS_SESSION_TOKEN="your aws session token"
```
## Run it on Docker
1. `docker run --rm  -d   -p 5050:80 --env-file ./env.list  --name s3-uploader-dev s3-uploader:dev  || docker logs s3-uploader-dev`
