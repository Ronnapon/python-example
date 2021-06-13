# Set
letters = [1, 1, 2, 3, 4]
first = set(letters)   # ยูเนียทกัน (ไม่มีเลขซ้ำ)
print("first = ", first)
second = {1, 5}
print("second = ", second)

print(first | second)  # Union (เอามาทั้งหมด)
print(first & second)  # Intersec (เอามาเฉพาะตัวที่ Diff)
print(first - second)  # Except (Set แรก ที่ไม่มีใน Set สอง)
print(first ^ second)  # Different (ที่ไม่เหมือนกัน)

if 1 in first:
    print("Ronnapon")
