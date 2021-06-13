# Handing different Exception
# Format 1
sucess = False
while not sucess:
    try:
        file = open("e-exception2.py")
        age = int(input("Input Age :"))
        age1 = 10 / age
    except (ValueError, ZeroDivisionError) as ex:
        print("Please input age agian!", ex)
    else:
        sucess = True
        print("Complete")
    finally:
        file.close()
