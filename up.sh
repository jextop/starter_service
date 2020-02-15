#!/bin/bash

# ./build.sh

./down.sh

# compose
docker-compose up -d
docker-compose ps

# alias dcmp=docker-compose && dcmp logs -f
# docker exec -it starter_service_srv_1 bash
