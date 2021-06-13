# Scope (Global & Local Valiable)
message = "XX"  # Global


def greet1(name):
    global message  # Global
    message = name
    return "Hi"


def greet2(name):
    message = name  # Local
    return "Hi"


print(message)
greet1("Big")
print(message)
greet2("Ron")
print(message)
