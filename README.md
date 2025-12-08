Custom CSV Reader & Writer with Benchmarking

This project implements a fully custom CSV parsing and writing system in Python, required for Global Placement Program – Week 3 (Core Task).

It includes:

→ A streaming CSV Reader built using a state machine
→ A CSV Writer with quoting & escaping logic
→ Handling of complex CSV cases such as:
 → Quoted fields
 → Escaped double quotes
 → Newline characters inside fields
→ Benchmarking against Python's built-in csv module
→ Synthetic dataset generation
→ Complete documentation and reproducible results

1. Repository Information
GitHub Repository
https://github.com/Prasanna-manepalli/-Custom-CSV-Parser-from-Scratch-in-Python__23A91A1236


This repository contains the full implementation, benchmarking script, and documentation.

2. System Overview

This project demonstrates how CSV parsing works internally by manually implementing:

→ Character-by-character streaming input
→ Row detection using newline boundaries
→ Quote-aware parsing
→ Escape detection for ""
→ Efficient writing using join()

Benchmarking is performed using:

→ timeit.default_timer()
→ A consistent dataset of 10,000 rows × 5 columns

This allows accurate performance comparison between the custom implementation and Python’s optimized CSV module.

3. Directory Structure
csv_custom/
→ reader.py           
# Custom CSV Reader (Iterator + State Machine)
→ writer.py          
 # Custom CSV Writer (Quoting + Escaping)
→ benchmark.py        
# Performance Benchmark Script
→ sample.csv    
# Optional demo CSV
→ README.md           
# Documentation

4. CSV Reader Design
4.1 Reading Strategy

→ File is streamed character by character
→ A state machine tracks whether the parser is inside quotes
→ Commas act as delimiters only when not inside quotes
→ Escaped quotes ("") are converted into "
→ Multiline fields are supported when enclosed in quotes

4.2 Iterator Protocol

The reader implements:

→ __iter__() → returns the iterator
→ __next__() → returns the next row or raises StopIteration

4.3 Stream Processing

→ Does not load the entire file into memory
→ Suitable for large CSV datasets

5. CSV Writer Design
5.1 Quoting Rules

A field is automatically quoted if it contains:

→ A comma ( , )
→ A double quote ( " )
→ A newline ( \n )

5.2 Escaping Logic

Internal quotes are escaped by doubling them:

"  →  ""

5.3 Efficient Row Construction

Rows are written using:

",".join(formatted_fields)

6. Benchmarking
6.1 Dataset Generation

A reproducible synthetic dataset is generated:

→ 10,000 rows
→ 5 columns
→ Deterministic content (name_i, city_i, etc.)

6.2 Timing Method

Benchmarks use:

→ timeit.default_timer()

To measure:

→ Custom Writer vs csv.writer
→ Custom Reader vs csv.reader

6.3 Example Benchmark Output
Generating synthetic data...

--- WRITE BENCHMARK ---
Custom Writer:  0.085123 seconds
Builtin Writer: 0.010482 seconds

--- READ BENCHMARK ---
Custom Reader:  0.120823 seconds
Builtin Reader: 0.013941 seconds

6.4 Interpretation

→ Python’s built-in CSV module is C-optimized → drastically faster
→ Custom implementation provides deeper understanding of CSV parsing
→ Shows real-world tradeoffs between performance and control

7. How to Run Locally
Install Python

Ensure Python 3.8+ is installed.

Run Benchmark
python benchmark.py

Test Reader
from reader import CustomCSVReader

with CustomCSVReader("sample.csv") as reader:
    for row in reader:
        print(row)

Test Writer
from writer import CustomCSVWriter

rows = [
    ["name", "city", "note"],
    ["John", "New York", "Hello, world"],
]

with CustomCSVWriter("output.csv") as writer:
    writer.writerows(rows)

8. Common Pitfalls

→ Forgetting to escape quotes before writing
→ Not resetting inside_quotes state correctly
→ Incorrect handling of newline inside quotes
→ Missing file close operations
→ Treating commas as delimiters even inside quotes
→ Incorrect order when checking for escaped quotes ("")

9. Limitations

→ Only supports comma-delimited CSV
→ No dialect support (tabs, semicolons, etc.)
→ Slower than built-in CSV module
→ Limited error handling for malformed rows

10. Future Improvements

→ Support configurable delimiters
→ Add RFC 4180 compliance validation
→ Add unit tests using pytest
→ Expand benchmark metrics
→ Improve handling of EOF edge cases

11. Final Notes

This project fully satisfies the requirements of Week 3 Core Task:

→ Custom CSV Reader
→ Custom CSV Writer
→ Quoting, escaping, and multiline field handling
→ Iterator-based streaming
→ Benchmark against Python’s csv module
→ Complete documentation and reproducible results

The implementation provides a strong foundation for understanding CSV internals and low-level parsing techniques.