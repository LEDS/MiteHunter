#!/bin/bash
docker stop $(docker ps -a -q)

docker rm $(docker ps -a -q)

docker image prune -a -f

docker volume prune -a -f
