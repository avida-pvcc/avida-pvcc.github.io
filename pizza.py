#   Name: Andrew Vida
#   Program Purpose: This program finds the cost of a pizza order

import datetime
current_time = str(datetime.datetime.now()).split('.')[0]

### Define global variables
SALES_TAX_RATE = .055
PRICE_SMALL = 9.99
PRICE_MED = 12.99
PRICE_LARGE = 14.99
PRICE_XL = 17.99

num_pizza = 0
size_pizza = 0
za_rate = 0
za_size = "blank"
subtotal = 0
sales_tax = 0
total = 0

def main() :
    more_data = True #Loop to ask to process more data
    while more_data:#Loop to ask to process more data
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to place another order?  (Y/N): ")#Loop to ask to proccess more data
        if yesno == "n" or yesno == "N":
            more_data = False
            print("\nThank you for picking Palermo!")

def get_user_data():
    global num_pizza, size_pizza
    size_pizza = str.lower(input("\nWhat is the size of pizza you would like to order (S, M, L, or XL)?:  "))
    num_pizza = int(input("\nHow many pizzas would you like to order?:  "))

def perform_calculations():
    global  subtotal, sales_tax, total, za_rate, za_size
    match size_pizza:
        case "s":  
            za_rate = PRICE_SMALL
            za_size = "      Small"
        case "m":
            za_rate = PRICE_MED
            za_size = "     Medium"
        case "l":
            za_rate = PRICE_LARGE
            za_size = "      Large"
        case "xl":
            za_rate = PRICE_XL
            za_size = "Extra Large"

    subtotal = num_pizza * za_rate
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax


def display_results():
    dash = "---------------------------------------"
    dashes = "======================================="
    print('\n' + dash)
    print('       **** Palermo Pizza ****')
    print('      Your neighborhood Pizzeria')
    print(dash)
    print('Pizzas Ordered:        ' + str(num_pizza) + ' ' + za_size)
    print(dash)
    print('Cost of Pizzas         $  ' + format(subtotal,'10,.2f'))
    print('Sales Tax              $  ' + format(sales_tax,'10,.2f'))
    print(dashes)
    print('Total                  $  ' + format(total,'10,.2f'))
    print(dash)
    print("        " + current_time + "\n")

main()
