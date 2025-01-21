#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

# Capture the argument
hyperfine "./target/release/$1 > output" --export-markdown benchmark-output/"$1.md"