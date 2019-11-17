cho = ""
while (cho !="end"):
    print("""
#####################################
## Simple Calculator with Forever ##
## Loop ##
## Mcoder Python Tutorial ##
## ##
## ##
#####################################
""")
    print("""
Choice The Number =>
1.Calculate Number:
2.Exit Program
""")
    inp = input("Input Number :")
    if (inp =="1"):
        number1 = int(input("Enter The First Number:"))
        number2 = int(input("Enter The Second Number:"))
        operator = input("Enter The Operators:")
        if(operator =="+"):
            sum = number1 + number2
            print("Answer is %d"%sum)
        elif(operator =="-"):
            sub = number1 - number2
            print("Answer is %d"%sub)
        elif(operator == "*"):
            mul = number1 * number2
            print("Anser is %d" % mul)
        elif (operator == "/"):
            div = number1 / number2
            print("Answer is %f" % div)
        elif (operator == "%"):
            mod = number1 % number2
            print("Answer is %d" % mod)
        else:
            print("Input Error")
    elif (inp == "2"):
        print("GoodBye!!!!")
        cho = "end"

