#!/bin/bash

set -a
source .env
set +a

python -m pytest "$@"
