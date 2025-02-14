#!/bin/bash

# Only proceed if 2 arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <language> <year>-<day>"
    exit 1
fi

# Check if hyperfine is installed
if ! command -v hyperfine &> /dev/null; then
    echo "Error: hyperfine is not installed. Install it with 'cargo install hyperfine'."
    exit 1
fi

if [ "$1" = "python" ]; then
    mkdir -p benchmark-output/python

    # Getting the output to the terminal first
    # This run will also do some stuff so it can be used later, no need more warmup run from hyperfine
    python "./python/$2.py"

    echo "Testing Python solution"
    hyperfine "python ./python/$2.py" --export-markdown "benchmark-output/python/$2.md"

elif [ "$1" = "rust" ]; then
    # Preprocessing
    mkdir -p benchmark-output/rust

    echo "Building the solution"
    cargo build --release --manifest-path ./rust/Cargo.toml --bin "$2"

    # Getting the output to the terminal first
    # This run will also do some stuff so it can be used later, no need more warmup run from hyperfine
    "./rust/target/release/$2"
    
    echo "Testing Rust solution"
    hyperfine "./rust/target/release/$2" --export-markdown "benchmark-output/rust/$2.md"
else
    echo "Only \"python\" or \"rust\" is allowed for the first argument"
    exit 1
fi
