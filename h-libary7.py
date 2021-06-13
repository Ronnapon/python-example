# json File
import json
from pathlib import Path
# write
product = [
    {"ProductID": 1, "ProductName": "Milk", "ProductPrice": 500},
    {"ProductID": 2, "ProductName": "Cookie", "ProductPrice": 500}
]
data = json.dumps(product)
print(data)
path = Path("product.json")
path.write_text(data)

# read
path = Path("product.json")
data = path.read_text()
product = json.loads(data)
print(product)
print(product[0]["ProductID"])
print(product[0]["ProductName"])
print(product[0]["ProductPrice"])
