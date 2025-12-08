import csv
import timeit
from reader import CustomCSVReader
from writer import CustomCSVWriter


ROWS = 10000
COLS = 5


def generate_data():
    """Generate reproducible synthetic CSV data."""
    data = []
    for i in range(ROWS):
        row = [
            f"name_{i}",
            f"city_{i}",
            f"note_{i}",
            f"address_line_{i}",
            f"value_{i}"
        ]
        data.append(row)
    return data


def benchmark_write_custom(data):
    start = timeit.default_timer()
    writer = CustomCSVWriter("custom_output.csv")
    writer.writerows(data)
    writer.close()
    end = timeit.default_timer()
    return end - start


def benchmark_write_builtin(data):
    start = timeit.default_timer()
    with open("builtin_output.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerows(data)
    end = timeit.default_timer()
    return end - start


def benchmark_read_custom():
    start = timeit.default_timer()
    reader = CustomCSVReader("custom_output.csv")
    for _ in reader:
        pass
    end = timeit.default_timer()
    return end - start


def benchmark_read_builtin():
    start = timeit.default_timer()
    with open("builtin_output.csv", "r", encoding="utf-8") as f:
        r = csv.reader(f)
        for _ in r:
            pass
    end = timeit.default_timer()
    return end - start


def main():
    print("Generating synthetic data...")
    data = generate_data()

    print("\n--- WRITE BENCHMARK ---")
    custom_write_time = benchmark_write_custom(data)
    builtin_write_time = benchmark_write_builtin(data)

    print(f"Custom Writer:  {custom_write_time:.6f} seconds")
    print(f"Builtin Writer: {builtin_write_time:.6f} seconds")

    print("\n--- READ BENCHMARK ---")
    custom_read_time = benchmark_read_custom()
    builtin_read_time = benchmark_read_builtin()

    print(f"Custom Reader:  {custom_read_time:.6f} seconds")
    print(f"Builtin Reader: {builtin_read_time:.6f} seconds")


if __name__ == "__main__":
    main()
