

def greet_client(client_name="None"):
    if client_name == "None":
        print("Insert a name!")
    else:
        print("Hello, " + client_name)

def get_client_initials(client_name):
    final_initials = []
    i = 0
    total_names = (client_name.split(" "))
    
    while i < len(total_names):
        if total_names[i][0].isupper():
            final_initials.append(total_names[i][0])
            #print(total_names[i][0])   
        i = i + 1

    return final_initials

client_name = ""

while client_name == "":
    client_name = input("Insert your name: ") 
    
    if client_name.lower() == "quit":
        break

    greet_client(client_name)    
    print("Your initials are: " + str(get_client_initials(client_name)))


