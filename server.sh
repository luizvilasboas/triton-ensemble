#!/usr/bin/env bash

docker run -d --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 -v ./models:/models --name triton-server triton-inference-server
