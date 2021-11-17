#!/use/bin/env python3

#Applying discount based on the type of user.

# base price for ticket 
TICKET_PRICE = 1000

# discount constant
DISCOUNT = 0.0

# calculate final ticket price for client (either Standard or VIP)
def calculateFinalPrice(clientName, clientType):

    #declaring global variable in the local scope
    global TICKET_PRICE, DISCOUNT
    
    #calculating discount rate
    DISCOUNT = 0.1 if clientType.lower() == "s" else 0.5  

    #returning final price
    return f"Final price for {clientName} is R${TICKET_PRICE - (TICKET_PRICE * DISCOUNT):,.2f}"

# parameters
clientNameArgument = input("Name: ")
clientTypeArgument = input("Type: (s) - standard, (v) - vip : ")

#calling main function
print(calculateFinalPrice(clientName = clientNameArgument,clientType =  clientTypeArgument))
