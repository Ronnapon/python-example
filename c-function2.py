# Defult Argument
def age(yearfr, yearto=2562):
    age = yearto - yearfr
    return f"you are {age} years old."


year_fr = int(input("Input DOB Year ? "))
print(age(year_fr))
# ------------------>
year_fr = int(input("Input DOB Year ? "))
print(age(year_fr, 2560))
# ------------------>
# def age(yearfr, yearto=2562, another): # Canot add parameter
