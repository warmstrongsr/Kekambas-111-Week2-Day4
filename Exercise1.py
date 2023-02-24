### 1) Create a program that allows a user to continue to add people to an address book until the user quits. Once the user quits, break out of the loop and print out the name and address of everyone in the address book
"""
1. Create a function that will ask user for name and addresses and stores them in a dictionary
2. Define an empty dictionary with which to work (global or local variable?)
3. Begin a loop that will continue to ask a user for information until the user "quits"
4. If the user does not quit, ask for a name and address and store the variables into variables
5. Add information to the dictionary with name as the key and address as the value
6. If the user does quit, end the loop
7. Print out the information from the dictionary in a formatted way
8. Execute/Call the function
"""


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)  #<---Codewars


address_book = {}



def run():

    while True:
        # user_name = input("Lets start with who I'm speaking with.  What is your name? ")
        # user_name = str(user_name.title())
        # q_name = input(f"Hello, {user_name}!  Who would you like to add? ")
        q_name = input("Who would you like to add? ")
        q_name = str(q_name.title())
        add_name = input(f"Ok! Let's add {q_name}. (press enter to continue)")
        q_address = input(f"What is {q_name}'s address? ")
        q_address = str(q_address.title())
        q_phone = input(f"Ok, got it!  What's {q_name}'s phone number? (format: 1231231234) ")
        q_phone = create_phone_number(q_phone)
    
        address_book[q_name] = {'address': q_address, 'phone': q_phone }

        more_inputs = input(f" Do you want to add more people?  (y for (yes) / n for (no): ")
        if more_inputs.lower() == 'n':
            break  
    return address_book
run()

print(address_book)
print(type(address_book))
### 2) Best Time to Meet


    
    

