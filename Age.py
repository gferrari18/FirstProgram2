age = int(input("How old are you? "))

if age < 0:
    print("Invalid Age")
if age >= 16 and age < 18: print("You can drive")
if age >= 18 and age < 21: print("You can vote")
if age >= 21 and age < 55: print("You can enjoy a beer")
if age >= 55: print("You get the senior discount")
