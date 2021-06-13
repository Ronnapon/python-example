# Array (Cannot Change Type)
from array import array
a = array("i", [1, 2, 3])
print(a)
a.append(4)
print(a)
a.insert(2, 3)
print(a)
