#!/usr/bin/env bash

docker-compose -f ../docker/docker-compose.yaml exec backend reformat.sh
