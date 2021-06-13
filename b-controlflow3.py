# Age should be 18 and 65
Age = 65
#------------------------->
# Format1
if Age >= 18 and Age <= 65:
    message1 = "Eligible"
else:
    message1 = "Not Eligible"
#------------------------->
# Format2
if 18 <= Age <= 65:
    message2 = "Eligible"
else:
    message2 = "Not Eligible"
#------------------------->
# Format3"
message3 = "Eligible" if 18 <= Age <= 65 else "Not Eligible"
#------------------------->
# Output
print("Format1 = " + message1)
print("Format2 = " + message2)
print("Format3 = " + message3)
