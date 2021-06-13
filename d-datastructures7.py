# Sorting List
items = [9, 1, 8, 6]

items.sort()
print(items)

items.sort(reverse=True)
print(items)

print(sorted(items))
print(sorted(items, reverse=True))

items = [
    ("Product1", 9),
    ("Product2", 1),
    ("Product3", 5),
]


def sort_item(item):   # index 0 = Product1 , index 1 = number
    return item[1]


items.sort(key=sort_item)
print(items)
