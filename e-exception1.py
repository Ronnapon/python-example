# Handing Exception
sucess = False
while not sucess:
    try:
        age = int(input("Input Age :"))
    except ValueError as ex:  # ex Valiable for show Error Message
        print("Please input age agian!")
        print(ex)
    else:
        sucess = True
        print("Complete")
