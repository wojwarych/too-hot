#!/usr/bin/env bash

docker-compose --env-file .env.dev -f docker/docker-compose.yaml up --build
