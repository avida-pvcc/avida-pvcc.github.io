# Name: Andrew Vida
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

# formating time to YYYY-MM-DD HH:MM:SS
import datetime
current_time = str(datetime.datetime.now()).split('.')[0]

######## Define global variables #########
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

############## Define program functions #####################
def main():
    more_data = True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to purchase more tickets?  (Y/N): ")
        if yesno == "n" or yesno == "N":
            more_data = False
            print("Thank you for choosing CINEMA HOUSE MOVIES!")
            
print("\nThank you for using our temperature converter! Have a nice day!")
def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets:  "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('-------------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('-------------------------------')
    print('Tickets      $ ' + format(subtotal,'10,.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'10,.2f'))
    print('Total        $ ' + format(total,'10,.2f'))
    print('-------------------------------')
    print(current_time)

######### call on main program to execute ###########

main()

