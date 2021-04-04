#!/usr/bin/env bash

docker-compose --env-file .env.dev -f ./docker/docker-compose.yaml run --rm backend python -m pytest
