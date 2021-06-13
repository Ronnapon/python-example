# Tuple (Cannot Add or Remove or Change)
Tuple1 = (1, 2) + (3, 4)
print('Format1', Tuple1)
a, b, c, d = Tuple1
print(a, b, c, d)
a, b = c, d  # Swaping Changes
print(a, b, c, d)
# -------------------->
Tuple2 = (1, 2) * 2
print('Format2', Tuple2)
# --------------------->
Tuple3 = tuple([1, 2, 3])
print('Format3', Tuple3)
# --------------------->
Tuple4 = tuple("Python")
print('Format4', Tuple4)
print(Tuple4[0:3])
# --------------------->
if "P" in Tuple4:
    print("exit")
