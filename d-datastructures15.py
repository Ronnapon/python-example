# Dict
point = {"A": 5, "B": 6}
point = dict(A=5, B=6)
print(point)

point["A"] = 50
print(point)

point["C"] = 40
print(point)

point["D"] = 40
print(point)

if "D" in point:
    print("Found D")

for key in point:
    print(key, point[key])

print(point.items())

for key, value in point.items():  # Change Tuple
    print(key, value)

print(point.get("E", 1))
