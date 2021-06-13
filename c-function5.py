# question make Function fizz_buzz
# argument 3 return fizz
# argument 5 return buzz
# argument 15 return fizzbuzz
# argument anouther return number


def fizz_buzz(argument1):
    if argument1 % 3 == 0 and argument1 % 5 == 0:
        return("Fizz_Buzz")
    if argument1 % 3 == 0:
        return("Fizz")
    if argument1 % 5 == 0:
        return("Buzz")
    return argument1


argument1 = ""
while str(argument1.lower()) != "quit":
    argument1 = input("Input Number? ")
    print(fizz_buzz(int(argument1)))
