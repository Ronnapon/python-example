# Unpacking
a = [1, 2, 3]
print(*a)


value = [*range(5), *'Hello']
print(value)

first = [1, 2]
second = [3, 4]
value = [*first, 'b', *second]
print(value)

first = dict(a=1, b=2)
second = dict(c=3, d=4)
value = {**first, **second, "e": 50}
print(value)
