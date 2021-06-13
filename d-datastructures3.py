# List Unpack
number = [1, 2, 3, 4, 4, 4, 4, 4, 9]
a, b, *c = number
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

a, *b, c = number
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


def mutiple(*number):
    print(number)


mutiple(1, 2, 3, 4)
