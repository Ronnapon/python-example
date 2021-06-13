# raise exception https://docs.python.org/3/library/exceptions.html
def caculate_age(year_fr, year_to=2562):
    if year_fr < 0:
        raise ValueError("Year is incorrect")
    return year_to - year_fr


sucess = False
while not sucess:
    try:
        age = caculate_age(int(input("Input year :")))
    except (ValueError, TypeError) as ex:
        print(ex)
    else:
        print("Goot Bye")
        sucess = True
