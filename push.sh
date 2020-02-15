#!/bin/bash

# ./build.sh

# img:tag repo:tag namespace server
set starter_service:latest starter_service:latest jext registry.cn-shanghai.aliyuncs.com

# workaround on windows: prefix command with winpty
# docker login --username=xxx $4

docker rmi $4/$3/$2
docker tag $1 $4/$3/$2
docker push $4/$3/$2
