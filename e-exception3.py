# The with statement
sucess = False
while not sucess:
    try:
        # automaticly call file.close
        with open("e-exception1.py") as file1, open("e-exception2.py") as file2:
            print("openfile")
        age = int(input("Input Age :"))
        age1 = 10 / age
    except (ValueError, ZeroDivisionError) as ex:
        print("Please input age agian!", ex)
    else:
        sucess = True
        print("Complete")
