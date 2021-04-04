#!/usr/bin/env bash

black . --config ./pyproject.toml
isort .
