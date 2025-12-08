from writer import CustomCSVWriter

rows = [
    ["name", "city", "note"],
    ["John", "New York", "Hello, world"],
    ["Mike", "LA", 'He said "Hi"'],
    ["Alice", "Paris", "Line1\nLine2"],
]

writer = CustomCSVWriter("output.csv")
writer.writerows(rows)
writer.close()

print("CSV written!")
