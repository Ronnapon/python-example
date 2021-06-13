# int1
student_count = 1000

# float
rate = 4.75

# boolean (Start Capital Character)
student_leave = True
student_leave = False

# string
student_name = "Big1"
student_course = "Python Programming"


try:
    age = int(input("Input Age :"))
except:
    age = -1
print(age)
if age >= 0:
    print(age)
else:
    print("incorrect")
