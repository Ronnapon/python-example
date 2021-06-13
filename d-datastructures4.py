# List Over Loop
letters = ['a', 'b', 'c']
test1 = enumerate(letters)
print(type(test1))

for number in enumerate(letters):
    print(number[0], number[1])

for index, letter in enumerate(letters):  # unpack with Loop
    print(index, letter)
