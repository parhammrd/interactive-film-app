#!/bin/bash

echo "Starting server"

uvicorn src.main:app --port=8000 --host=0.0.0.0