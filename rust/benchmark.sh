#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

# Check if the folder exists or not
mkdir -p ../outputs

# Capture the argument
# Use one warmup run for file retrieval
hyperfine "./target/release/$1 > ../outputs/$1.txt" \
    --export-markdown benchmark-output/"$1.md" --warmup 1