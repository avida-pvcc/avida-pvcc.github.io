# Name: Andrew Vida
# Prog Purpose: This program finds the cost of tuition and fees for PVCC

# formating time to YYYY-MM-DD HH:MM:SS
import datetime
current_time = str(datetime.datetime.now()).split('.')[0]

######## Define global variables #########
# define tuition rate and fees
TUITION_IN = 155.00
TUITION_OUT = 331.60
INST_FEE = 1.75
STU_ACT_FEE = 2.90
CAP_FEE = 23.50

# define global variables
residency = 1
num_credits = 0
scholar_amt = 0
total = 0
balance = 0

############## Define program functions #####################
def main():
    more_data = True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to process more data?  (Y/N): ")
        if yesno == "n" or yesno == "N":
            more_data = False
            print("Thank you for using our app!")
            
def get_user_data():
    global residency, num_credits, scholar_amt
    residency = int(input("Please enter residency status: \n\t1 for In-state \n\t2 for Out-of-state \n\n\tEnter number here:  "))
    num_credits = int(input("\nNumber of credits:  "))
    scholar_amt = int(input("\nAmount of scholarship awarded:  "))

def perform_calculations():
    global tuition_amt, inst_amt, act_amt, cap_amt, total, balance
    if residency == 2:  #2 means out-of-state
        tuition_amt = num_credits * TUITION_OUT
        cap_amt = num_credits * CAP_FEE
    else:
        tuition_amt = num_credits * TUITION_IN
        cap_amt = 0
        
    inst_amt = num_credits * INST_FEE
    act_amt = num_credits * STU_ACT_FEE
    
    total = tuition_amt + inst_amt + act_amt + cap_amt
    balance = total - scholar_amt

def display_results():
    dashes = '--------------------------------------------------'
    d_dashes = '=================================================='
    print(dashes)
    print('****** PIEDMONT VIRGINIA COMMUNITY COLLEGE ******')
    print('***********TUITION & FEES RECEIPT****************')
    print('             ' + current_time + '           ')      
    print(dashes)
    print('Number of credits                : ' + str(num_credits))
    print(dashes)
    print('Tuition                          $ ' + format(tuition_amt,'8,.2f'))
    print('Institutional Fee                $ ' + format(inst_amt,'8,.2f'))
    print('Student Activity Fee             $ ' + format(act_amt,'8,.2f'))
    print('Capital Fee                      $ ' + format(cap_amt,'8,.2f'))
    print('Total                            $ ' + format(total,'8,.2f'))
    print('Scholorship                      $ ' + format(scholar_amt,'8,.2f'))
    print(d_dashes)
    print('Balance Due                      $ ' + format(balance,'8,.2f'))
    print(dashes)
    print('*Capital Fee only applies to out-of-state students')

######### call on main program to execute ###########

main()

