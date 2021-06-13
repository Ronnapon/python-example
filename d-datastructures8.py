# ------------- Sort by Lamda functiion   ------------>
items = [
    ("Product1", 9),
    ("Product2", 1),
    ("Product3", 5),
]
items.sort(key=lambda item: item[0])  # parameter:expresstion
print(items)

sentence_sort1 = sorted(items, key=lambda item: item[1])
print(sentence_sort1)

# -------------- Map function     -------------------->
x = map(lambda item: item[1], items)
for value in x:
    print(value)

# items = iterables การวนซ้ำ List Dict Tuple
x = list(map(lambda item: item[1], items))
print(x)
q = [50, 30, 40]
x = list(map(lambda item: item*5, q))
print(x)

# ------------- Filter functiion   -------------------->
items = [
    ('product1', 500),
    ('product2', 400),
    ('product3', 450)
]

x = list(filter(lambda item: item[1] >= 450, items))
print(f"Format 1 = {x}")

x = [item[1] for item in items if item[1] >= 450]
print(f"Format 2 = {x}")

# ------------- zip functiion   -------------------->
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))
