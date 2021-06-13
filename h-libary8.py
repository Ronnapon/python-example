# SQL Lite & Time stamp
import sqlite3
import json
from pathlib import Path
import time

# products = json.loads(Path("product.json").read_text())
# print(products)
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Products VALUES(?, ?, ?)"
#     for product in products:
#         conn.execute(command, tuple(product.values()))
#     conn.commit()

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Products"
    cusor = conn.execute(command)
    # for product in cusor:
    #     print(product)
    product = cusor.fetchall()
    print(product)
