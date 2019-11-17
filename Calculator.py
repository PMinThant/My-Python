print("""
########################
# Simple Calaculator #
########################
""")
number1 =int(input("Enter The Number 1:"))
number2 =int(input("Enter The Number 2:"))
operators = input("Enter The Operators:")
if (operators == "+"):
    sum = number1 + number2
    print(("Sum of Number1 and Number2 %d")%sum)
elif(operators == "-"):
    sub = number1 - number2
    print(("Sub of Number1 - Number2 %d")%sub)
elif (operators == "*"):
    mul = number1 * number2
    print(("Mul of Number1 x Number2 %d")%mul)
elif (operators == "/"):
    div = number1 / number2
    print(("div of Number1 / Number2 %f")%div)
elif (operators =="%"):
    mod = number1 % number2
    print(("Moud of Number1 and Number2 %d")%mod)
else:
    print("Error Input")
