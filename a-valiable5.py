# String method
print("*" * 30)
course = "Python Programming"
print(course.upper())
print(course.lower())
# ----------------------->
print("*" * 30)
course = "python programming"
print(course.title())
# ----------------------->
print("*" * 30)
course = " python programming "
print(course.strip())
print(course.lstrip())
print(course.rstrip())
# ----------------------->
print("*" * 30)
course = "Python Programming"
print(course.find("Python"))
print(course.replace("Py", "Bi"))
# ----------------------->
print("*" * 30)
print("Pro" in course)
print("AAA" not in course)
