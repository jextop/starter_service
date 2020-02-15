#!/bin/bash

./stop.sh

# build image
# docker build -t srv .

# run image
# docker run --rm --name srv -p 8001:8001 -d starter_service

docker port srv
docker ps

# docker exec -it srv bash
# docker logs srv -f
