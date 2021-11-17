#!/use/bin/env python3

#Applying discount based on the type of user.

# base price for ticket 
TICKET_PRICE = 193.50

# discount applied for VIP clients
DISCOUNT_FOR_VIP = 0.0

# calculate final ticket price for client (either Standard or VIP)
def calculateFinalPrice(clientName, clientType):
    DISCOUNT_FOR_VIP = 0.1 if clientType.lower() == "v" else 0.0
    return f"Final price for {clientName} is R${TICKET_PRICE - TICKET_PRICE * DISCOUNT_FOR_VIP:,.2f}"


# parameters
clientNameArgument = input("Name: ")
clientTypeArgument = input("Type: (s) - standard, (v) - vip : ")

#calling main function
print(calculateFinalPrice(clientName = clientNameArgument,clientType =  clientTypeArgument))