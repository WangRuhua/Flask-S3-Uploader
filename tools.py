import boto3
from app import app

s3 = boto3.client(
   "s3"
   #aws_access_key_id=app.config['S3_KEY'],
   #aws_secret_access_key=app.config['S3_SECRET']
)


def upload_file_to_s3(file, bucket_name, bucket_key,acl="public-read"):
    print(bucket_key)
    bucket_key=bucket_key+"/"+file.filename
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            bucket_key,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return [1,e]

    return [0,"{}{}".format(app.config["S3_LOCATION"], bucket_key)]
