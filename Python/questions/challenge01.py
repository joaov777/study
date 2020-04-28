

# Accept two int values from the user and return their product. If the product is greater than 1000, then return their sum

#possible function 01
def mult_or_sum(num1, num2):
    prod = num1 * num2
    
    if prod < 1000:
        print('The sum is: {}'.format(num1+num2))
    else:
        print('The product is: {}'.format(num1*num2))

#possible function 02
def mult_or_sum2(num1, num2):
    if (num1*num2) < 1000:
        return num1+num2
    else:
        return num1*num2



number01=float(input("Number 1: "))
number02=float(input("Number 2: "))

result2 = mult_or_sum2(number01,number02)
print("Function 2: ",result2)

mult_or_sum(number01,number02)

