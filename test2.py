# Filter
items = [1, 2, 3, 4, 5]
a_filter = [item for item in items if item >= 2]
print(a_filter)

items = {'a': 1, 'b': 2, 'c': 3}
a_filter = [item for item in items.items() if item[1] >= 2]
print(dict(a_filter))

item = (1, 2, 3, 4, 5)
a_filter = [item for item in item if item >= 2]
print(tuple(a_filter))

# Sort
items = [1, 2, 3, 4, 5]
a_sort = sorted(items, key=lambda item: item, reverse=True)
print(a_sort)

items = {'a': 1, 'b': 2, 'c': 3}
a_sort = dict(sorted(items.items(), key=lambda item: item[1], reverse=True))
print(a_sort)

items = (1, 2, 3, 4, 5)
a_sort = tuple(sorted(items, key=lambda item: item, reverse=True))
print(a_sort)


class bank:
    def __init__(self):
        self.bal = 50000

    def deb(self):
        print(self.bal - 15000)


ba = bank()
ba.deb()
