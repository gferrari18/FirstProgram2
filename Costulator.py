pay = float(input("Paycheck amount (after taxes) = "))
rent = 900
utility = 120
gas = 15
grocery = 250
savings = (pay*0.2)

FunMoney = pay-rent-utility-gas-grocery-savings

if FunMoney < 0:
    print("You have $0 dollars to spend on random things you dont need")
    print("Maybe its time for a second  job")
    print("As you are short $" + str(FunMoney) + " to pay for your bills")

if FunMoney > 0:
    print("You have $" + str(FunMoney) + " to spend on random things you don't need")

if FunMoney > 200:
    print("...Maybe you should rethink your spending habits")

print("You are currently saving $" + (str(savings)) + " dollars for your future")
