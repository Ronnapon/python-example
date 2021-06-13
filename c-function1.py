def Login(firstname, lastname, dob):  # Parameter (Get)
    age = 2562 - dob
    if firstname.lower() == "ronnapon" and lastname.lower() == "prathombud":
        print(f"Hi {firstname} {lastname} Age {age}")
        print("Login Success")
        return True
    else:
        print(f"Hi {firstname} {lastname} Age {age}")
        print("Login Faile")
        return False


sucess = False
while sucess != True:
    name = input("Input Name: ")
    name_count = int(name.find(" "))
    fname = name[0:name_count]
    lname = (name[name_count+1:])
    sucess = Login(fname, lname, 2535)  # Argument (Send)
    print(sucess)
