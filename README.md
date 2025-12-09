## Build Custom CSV Reader & Writer with Benchmarking

This project implements a complete Custom CSV Parsing and Writing System required for **Global Placement Program – Week 3 (Core Task)**.

It includes:

-A streaming CSV Reader built using a state machine

-A CSV Writer with quoting and escaping logic

-Handling of complex CSV cases

-Benchmarking against Python’s built-in csv module

-Synthetic dataset generation

-Complete documentation and reproducible results
 
 ---

## 1. Repository Information

## GitHub Repository
```
https://github.com/Prasanna-manepalli/-Custom-CSV-Parser-from-Scratch-in-Python__23A91A1236
```

This repository contains the full implementation, benchmarking script, and documentation.

---

## 2. System Overview

This project explains how CSV parsing works internally through:

-Character-by-character streaming input

-Row detection using newline boundaries

-Quote-aware parsing

-Detection and conversion of escaped quotes ("")

-Efficient writing using join()

-Benchmarking is performed using:

-timeit.default_timer()

-A consistent dataset of 10,000 rows × 5 columns

-This allows performance comparison between the custom implementation and Python’s optimized csv module.

---

3. Directory Structure
```
.
├── reader.py
├── writer.py
├── benchmark.py
├── sample.csv
└── README.md
```

---

### 4. CSV Reader Design

### 4.1 Reading Strategy

-File is streamed character by character

-A state machine tracks when the parser is inside quotes

-Commas act as delimiters only when not inside quotes

-Escaped quotes ("") are handled and converted to "

-Multiline fields are supported when enclosed in quotes

### 4.2 Iterator Protocol

### The reader implements:

-iter() → returns the iterator

-next() → returns next row or raises StopIteration

### 4.3 Stream Processing

-Does not load the entire file into memory

-Suitable for large CSV files

---

### 5. CSV Writer Design

### 5.1 Quoting Rules

-A field is automatically quoted if it contains:

-A comma ,

-A double quote "

-A newline \n

### 5.2 Escaping Logic

-Internal quotes are escaped by doubling them:

-"  →  ""

### 5.3 Efficient Row Construction

-Rows are written using:

-",".join(formatted_fields)


---

### 6. Benchmarking
### 6.1 Dataset Generation

-A reproducible dataset is generated with:

-10,000 rows

-5 columns

-Deterministic values (name_i, city_i, etc.)

### 6.2 Timing Method

-Benchmarks use:

-timeit.default_timer()

-to measure:

-Custom Writer vs csv.writer

-Custom Reader vs csv.reader

### 6.3 Example Benchmark Output
-Generating synthetic data...

--- WRITE BENCHMARK ---
-Custom Writer:  0.085123 seconds
-Builtin Writer: 0.010482 seconds

--- READ BENCHMARK ---
-Custom Reader:  0.120823 seconds
-Builtin Reader: 0.013941 seconds

### 6.4 Interpretation

-Python’s CSV module is C-optimized → significantly faster

-Custom implementation provides deeper understanding of CSV parsing

-Demonstrates performance vs. control tradeoffs


---

### 7. How to Run Locally
-Run Benchmark
-python benchmark.py

-Test Reader
-from reader import CustomCSVReader
```
with CustomCSVReader("sample.csv") as reader:
    for row in reader:
        print(row)
```
-Test Writer
-from writer import CustomCSVWriter

```
rows = [
    ["name", "city", "note"],
    ["John", "New York", "Hello, world"]
]
```

```
with CustomCSVWriter("output.csv") as writer:
    writer.writerows(rows)
```

---

### 8. Common Pitfalls

-Forgetting to escape quotes before writing

-Not resetting inside_quotes state correctly

-Incorrect handling of newline inside quoted fields

-Missing file close operations

-Treating commas inside quotes as delimiters

-Incorrect handling of escaped quotes ("")

---

### 9. Limitations

-Only supports comma-separated CSV

-No dialect support

-Slower than Python’s built-in CSV (expected)

-Minimal handling of malformed CSV input

---

### 10. Future Improvements

-Support for configurable delimiters

-Add RFC 4180 compliance checks

-Add automated unit tests

-Improve benchmark and reporting

-Enhance EOF edge-case handling

---

### 11. Final Notes

-This implementation fully satisfies the requirements for Week-3:

-Custom CSV Reader

-Custom CSV Writer

-Quoting, escaping, and multiline field handling

-Iterator-based streaming

-Benchmark with synthetic dataset

-Complete documentation

-This project provides a strong foundation for understanding CSV internals and low-level parsing techniques.