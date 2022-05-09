def check_operator(op,num1,num2):
    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(num1*num2)
    elif op == "/":
        print(num1/num2)
    else:
        print("Invalid operator inserted!")

i = 1
while i <= 3:

    num1 = float(input("Enter the first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter the second number: "))

    check_operator(op,num1,num2)

    i+=1
