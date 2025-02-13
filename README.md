# Advent of Code Solutions

## 📌 Project Overview
This repository contains my solutions for **Advent of Code**, implemented in **Rust** and **Python**. While not all years are completed yet, I plan to add more solutions over time. Additionally, I have benchmarked Python vs. Rust solutions using **Hyperfine** to compare their performance.

## 🚀 Benchmarking Results
All code was run on a 2017 Macbook Pro, with the below configuration:
- OS: MacOS Ventura 13.7.3
- CPU: 2,8 GHz Quad-Core Intel Core i7
- RAM: 16 GB 2133 MHz LPDDR3

Benchmarks show that Rust significantly outperforms Python in most cases, often running **2-10x faster**, 
with extreme cases being **100x faster**. Below is the performance comparison for problems I have done so far:

| Year | Day | Problem Type | Python Time | Rust Time | Speedup |
|------|----|--------------|-------------|-----------|---------|
| 2015 | 1  | Simulation   | 240ms         | 8ms      | **30x** 🚀 |

For full benchmarking results with more details, check the `benchmark-output` folder inside each language directory.

## 📂 Project Structure
```
📂 Advent-of-Code
 ┣ 📂 rust/              # Solutions implemented in Rust, managed by Cargo
 ┃ ┣ 📂 benchmark-output # Benchmark results for Rust files
 ┃ ┣ 📂 src/             # Rust source code
 ┃ ┗ 📜 Cargo.toml       # Rust package manager file
 ┣ 📂 python/            # Initial solutions written in Python & Jupyter Notebook
 ┃ ┣ 📂 benchmark-output # Benchmark results for Python files
 ┃ ┗ 📜 requirements.txt # Python dependencies
 ┣ 📂 inputs/            # Input files for each problem
 ┣ 📂 outputs/           # Output files from executed programs
 ┣ 📜 README.md          # This file
 ┗ 📜 cookies.json       # Stores session cookie (not included in the repo, have to be created manually)
```

## 🛠 How to Run

### 🔑 Setting Up `cookies.json`
Before running the solutions, create a `cookies.json` file in the root directory to retrieve input files from AoC's server:

```json
{
    "session": "..."  // Your session value from Advent of Code
}
```

> **Warning:** Do **NOT** commit `cookies.json` to a public repository to avoid exposing your session.

### 🦀 Running Rust Solutions
```sh
cd rust
cargo build --release --bin <yyyy>-<dd>
./target/release/<yyyy>-<dd>
```

### 🐍 Running Python Solutions
```sh
cd python
pip install -r requirements.txt
# Then run the notebook files, or execute a script directly:
python <file_name>.py
```

