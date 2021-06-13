successful = True
for number in range(5):
    if successful:
        print("you correct")
        break
else:
    print("Bye")
print("*" * 5)

# nested Loop
for a in range(1):
    for b in range(1, 13):
        c = 2 * b
        print(f"2 * {b} = {c}")

for k in "Python":
    print(k)

for j in [1, 2, 3]:
    print(j)
