#!/usr/bin/env bash

if [[ $1 -eq "CI" ]]; then
  CHECK="--check"
  DIFF="--diff"
fi

docker-compose -f ./docker/docker-compose.yaml exec -e CHECK=$CHECK -e DIFF=$DIFF backend reformat.sh
