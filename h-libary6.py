import csv
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ProductID", "ProductName", "ProductPrice"])
    writer.writerow([1, "Milk", 500])
    writer.writerow([2, "Cookie", 100])
    writer.writerow(["", "Total", 600])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for textline in list(reader):
        print(textline)
