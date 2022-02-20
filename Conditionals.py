

x = int(input("Choose an integer for x: "))
y = int(input("Choose an integer for y: "))

print("x + y = " + str(x + y))
print("x - y = " + str(x - y))
print("x * y = " + str(x * y))
if y == 0:
    print("x / y = ?")
    print("x % y = ?")
    print("You cannot divide by 0!")
elif y != 0:
    print("x / y = " + str(x / y))
    print("x % y = " + str(x % y))

