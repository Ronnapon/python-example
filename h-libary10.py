# Generate Random Value
import random
import string
print(random.random())
print(random.randint(1, 5))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print(random.choices("123456789", k=13))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))
print(string.digits)
print(string.ascii_letters)

number = [1,2,3,4]
random.shuffle(number)
print(number)
