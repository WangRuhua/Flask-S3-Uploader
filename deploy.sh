cluster_name=""
service_name=""
task_d=`aws ecs register-task-definition  --cli-input-json file://taskdef.json | jq -r ".taskDefinition| .taskDefinitionArn"`

aws ecs update-service --service $service_name --cluster $cluster_name --task-definition ${task_d} |jq .

sed -i '/image/ c "image": "$AWS_ID.dkr.ecr.us-east-1.amazonaws.com/s3-uploader:${new_tag}"'  taskdef.json

##trigger a new deployment
aws ecs update-service --cluster ${cluster_name} --service ${service_name} --force-new-deployment
