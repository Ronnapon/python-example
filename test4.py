emp_name = ""
emp_amt = 0
emp_ind = ""
total_amt = 0
list_emp = []
set_emp = {}
while emp_ind != "N":
    emp_ind = ""
    emp_name = input("Input Name   : ")
    emp_amt = int(input("Input Amount : "))
    total_amt += emp_amt
    if emp_name in set_emp:
        set_emp[emp_name] += emp_amt
    else:
        set_emp[emp_name] = emp_amt
    while emp_ind != "Y" and emp_ind != "N":
        emp_ind = input("Next (Y), Stop (N): ")

print("*" * 70)
total_emp = len(set_emp)
share_amt = total_amt / total_emp
print(
    f"There are {total_emp} people, Total {round(total_amt)} Bath , Pay {round(share_amt)} Bath per people")
print("*" * 70)
set_pay = {}
set_rec = {}
for name, amt in set_emp.items():
    diff_amt = amt - share_amt
    diff_amt = round(diff_amt)
    print(f"{'{:10}'.format(name)} pay {'{:4d}'.format(round(amt))} Bath ({'{:4d}'.format(round(diff_amt))})")

    if diff_amt > 0:
        set_rec[name] = diff_amt

    if diff_amt < 0:
        set_pay[name] = abs(diff_amt)
print("*" * 70)

for pay_name, pay_amt in set_pay.items():
    print(pay_name)
    for rec_name, rec_amt in set_rec.items():
        if set_rec[rec_name] == 0 or set_pay[pay_name] == 0:
            break
        elif pay_amt >= rec_amt:
            print(
                f" - pay {'{:10}'.format(rec_name)} {'{:4d}'.format(rec_amt)} Bath")
            set_pay[pay_name] -= rec_amt
            set_rec[rec_name] = 0
        else:
            print(
                f" - pay {'{:10}'.format(rec_name)} {'{:4d}'.format(pay_amt)} Bath")
            set_pay[pay_name] = 0
            set_rec[rec_name] -= pay_amt
print("*" * 70)
