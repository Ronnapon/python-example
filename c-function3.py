# xargs class tuple
def mutiple_tuple(*number):
    print(number)
    print(type(number))
    a, b, c, d = number
    print("*" * 25)
    total = 0
    for i in number:
        print(i)
        total += i
    return f"2 + 4 + 6 + 8 = {total}"


print("start")
print(mutiple_tuple(2, 4, 6, 8))
print("*" * 25)
# xxargs class dict


def save_user(**user):
    print(user)
    print(f"Idno: {user['id']} Username: {user['fname']}")


save_user(id=1, fname="Ronnapon", password=1111)
