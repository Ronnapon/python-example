# Cost raise exception
from timeit import timeit
# ------------------------------------------------>
# Format 1
code1 = """
def caculate_age(year_fr, year_to=2562):
    if year_fr <= 0:
        raise ValueError("Year is incorrect") # Next Line don't work
    return year_to - year_fr  


try:
    age = caculate_age(int(-1))
except ValueError:
    pass
"""
print("first Code", timeit(code1, number=1000))

# ------------------------------------------------>
# Format2
code2 = """
def caculate_age(year_fr, year_to=2562):
    if year_fr <= 0:
        return None
    return year_to - year_fr


age = caculate_age(int(-1))
if age == "":
    pass
"""
print("Second Code", timeit(code2, number=1000))
