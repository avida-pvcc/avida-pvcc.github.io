#Michael Pressel
#Andrew Vida
#Prog Purpose: This program finds employee weekly pay.

# formatting time to YYYY-MM-DD HH:MM:SS
import datetime
current_time = str(datetime.datetime.now()).split('.')[0]

############ define global variables ###########
#define tax rate and prices (constants)
CASHIER_PAY_RATE = 16.50
STOCK_PAY_RATE = 15.75
JAN_PAY_RATE = 15.75
MAINT_PAY_RATE = 19.50

FED_TAX = .12
STATE_TAX = .03
SS_TAX = .062
MED_TAX = .0145

#define global variables
num_hours = 0
total_deductions = 0
job = 0
gross_pay = 0
net_pay = 0
fed_total = 0
state_total = 0
ss_total = 0
med_total = 0
epr = 0

############ define program functions ##########
def main() :
    more_data = True #Loop to ask to process more data
    while more_data:#Loop to ask to process more data
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to process more data?  (Y/N): ")#Loop to ask to proccess more data
        if yesno == "n" or yesno == "N":
            more_data = False
            print("Thank you for using our app!")

def get_user_data() :
    global num_hours, job
    job = int(input("Please enter your job tile: \n 1 for Cashier \n 2 for Stocker \n 3 for Janitor \n 4 for Maintenance\n Enter here: "))
    num_hours = float(input("Number of hours worked: "))

def perform_calculations() :
    global gross_pay, total_deductions, net_pay, fed_total, state_total, ss_total, med_total, epr
    match job:
        case 1:  ###removed quotes
            epr = CASHIER_PAY_RATE
        case 2:
            epr = STOCK_PAY_RATE
        case 3:
            epr = JAN_PAY_RATE
        case 4:
            epr = MAINT_PAY_RATE
        

            
    gross_pay = num_hours * epr
    fed_total = gross_pay * FED_TAX
    state_total = gross_pay * STATE_TAX
    ss_total = gross_pay * SS_TAX
    med_total = gross_pay * MED_TAX
    total_deductions = fed_total + state_total + ss_total + med_total
    net_pay = gross_pay - total_deductions


def display_results() :
    print ('\n----------------------------------------')###added \n to provide a space between last user input and displayed results
    print ('******* Fresh Food Marketplace *******')
    print ('   Your neighborhood grocery store')
    print ('        ' + current_time)
    print ('----------------------------------------')
    print ('Hours                      : ' + format(num_hours, '10,.2f'))#changed format based on canvas announcement
    print ('Gross Pay                  $ ' + format(gross_pay, '10,.2f'))#changed format based on canvas announcement
    print ('Federal Income Tax         $ ' + format(fed_total, '10,.2f'))#changed format based on canvas announcement
    print ('State Income Tax           $ ' + format(state_total, '10,.2f'))#changed format based on canvas announcement
    print ('Social Security Tax        $ ' + format(ss_total, '10,.2f'))#changed format based on canvas announcement
    print ('Medicare Tax               $ ' + format(med_total, '10,.2f'))#changed format based on canvas announcement
    print ('----------------------------------------')
    print ('Net Pay                    $ ' + format(net_pay, '10,.2f'))#changed format based on canvas announcement
    print ('----------------------------------------')
    

######## call on main program to execute ######
main()
