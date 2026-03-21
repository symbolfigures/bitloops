#!/bin/bash

# run from local host
#$ zip -r ami.zip ami
#$ aws s3 cp ami.zip s3://mcp.symbolfigures.io

# run from EC2 instance

export AWS_ACCOUNT_ID=476322507760;

# delete old container and image
docker rm -f mcp
docker rmi mcp
docker rmi $AWS_ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com/mcp

# download new files and build new image
aws s3 cp s3://mcp.symbolfigures.io/mcp.zip .
unzip mcp
docker build -t mcp mcp

# upload to ECR
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com;
docker tag mcp:latest $AWS_ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com/mcp:latest;
docker push $AWS_ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com/mcp:latest

# run
docker run -d \
	--name mcp \
	--network host \
	--restart unless-stopped \
	476322507760.dkr.ecr.us-west-2.amazonaws.com/mcp:latest











