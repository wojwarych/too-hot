#!/usr/bin/env bash

docker-compose -f ../docker/docker-compose.yaml run --rm backend python -m pytest
