# Ternary Operator
hight_income = True
good_credit = False
student = False
# ---------------------------------------------->
# Question 1
if hight_income and not good_credit and not student:
    print("Question1 = Eligible")
else:
    print("Question1 = Not Eligible")
# ---------------------------------------------->
# Question 2
if not hight_income and not good_credit and not student:
    print("Question2 = Eligible")
else:
    print("Question2 = Not Eligible")
# ---------------------------------------------->
# Question 3
if hight_income or good_credit and student:
    print("Question3 = Eligible")
else:
    print("Question3 = Not Eligible")
# ---------------------------------------------->
# Question 4
if (hight_income or good_credit) and student:
    print("Question4 = Eligible")
else:
    print("Question4 = Not Eligible")
# ---------------------------------------------->
