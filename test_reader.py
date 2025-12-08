from reader import CustomCSVReader

reader = CustomCSVReader("sample.csv")

for row in reader:
    print(row)
