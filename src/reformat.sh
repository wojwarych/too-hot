#!/usr/bin/env bash

black . "${CHECK}" --config ./pyproject.toml
isort . "${DIFF}"
