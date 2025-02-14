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
| 2015 | 1 | Simulation | 240ms ([Link](./benchmark-output/python/2015-01.md)) | 8ms ([Link](./benchmark-output/rust/2015-01.md)) | **30x** |
| 2015 | 2  | Math & Geometry | 236ms ([Link](./benchmark-output/python/2015-02.md)) | 7ms ([Link](./benchmark-output/rust/2015-02.md)) | **33x** |

For full benchmarking results with more details, check the `benchmark-output` folder inside each language directory, or click the links above.

## 📂 Project Structure
```
📂 Advent-of-Code
 ┣ 📂 benchmark-output   # Benchmark results for all programs
 ┃ ┣ 📂 rust/            # Benchmark for Rust files
 ┃ ┗ 📂 python/          # Benchmark for Python files
 ┣ 📂 rust/              # Solutions implemented in Rust, managed by Cargo
 ┃ ┣ 📂 src/             # Rust source code
 ┃ ┗ 📜 Cargo.toml       # Rust package manager file
 ┣ 📂 python/            # Initial solutions written in Python & Jupyter Notebook
 ┃ ┗ 📜 requirements.txt # Python dependencies
 ┣ 📂 inputs/            # Cached input files for problems
 ┣ 📜 README.md          # This file
 ┗ 📜 cookies.json       # Stores session cookie (not included in the repo, have to be created manually)
```

## 🛠 How to Run

### 🔑 Setting Up `cookies.json`
Before running the solutions, create a `cookies.json` file to retrieve input files from AoC's server. The location of this file depends on where you run the program:

- **If you run the program from the root directory** (e.g., when executing commands like ./benchmark.sh), place `cookies.json` in the **root** folder.
- **If you run the program from within the rust or python folder**, place the `cookies.json` file **inside the respective folder** (either `/rust` or `/python`).

Here’s an example of the `cookies.json` file format:

```json
{
    "session": "..."  // Your session value from Advent of Code
}
```

> **Warning:** Do **NOT** commit `cookies.json` to a public repository to avoid exposing your session.

### 🦀 Running Rust Solutions
```sh
cargo build --release --manifest-path ./rust/Cargo.toml
./rust/target/release/<yyyy>-<dd>
```

Or:
```sh
cd rust
cargo build --release
./target/release/<yyyy>-<dd>
```

Adding the `--bin <yyyy>-<dd>` option in `cargo build` command if you only want to build for specific day

### 🐍 Running Python Solutions
```sh
pip install -r python/requirements.txt
python python/<yyyy>-<dd>.py
```

Or:

```sh
cd python
pip install -r requirements.txt
python <yyyy>-<dd>.py
```

### Benchmarking solutions on your own

```sh
./benchmark.sh <language> <yyyy>-<dd>
```

For `language` option, it can only either be `python` or `rust`. For example:

```sh
./benchmark.sh python 2015-01
./benchmark.sh rust 2015-01
```