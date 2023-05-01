# Name: Andrew Vida
# Prog Purpose: This program reads a comma-delimited data file into a LIST of smaller lists.
#   The data for each student is appended to a list with six data fields:
#   Position 0 is last name, 1 is first name, 2 is Homework, 3 is Midterm exam, 4 is Final exam.
#   The group of student lists in the larger "outer" list
#   The resulting report is sent to an output file.

import datetime
current_time = str(datetime.datetime.now()).split('.')[0]

stu = []
student_file = "students.csv"
out_file = "stu_report.txt"

def main():
    read_data_file()
    calculate_grades()
    create_report_file()

def read_data_file():
    datafile = open(student_file, "r") #The "r" indicates this is a READ file
    lines = datafile.readlines() #Read the entire file into a variable called lines
    for i in lines:
        stu.append(i.split(",")) #Split the data by commas and add each section to the list
    datafile.close()
    
def calculate_grades():
    global average, totA, totB, totC, totD, totF
    totA = totB = totC = totD = totF = 0
    gradestotal = 0

    for i in range(len(stu)):
        hw = int(stu[i][2])    #Last name is pos. 0, first name is pos. 1, so homework is pos. 2
        midex = int(stu[i][3])   #Midterm exam is in position 3
        stu[i][4] = stu[i][4][:-1]  #Remove the \n from the final exam string (end of the input line)
        finex = int(stu[i][4])  #Final exam is in pos. 4
        sum_grades = hw + midex + finex
        finalgr = sum_grades / 3
        gradestotal += finalgr  #Add the grade to the total for calculating the average
        stu[i].append(finalgr)

        if finalgr >= 90:
            lettergrade = "A"
            totA += 1
        elif finalgr >= 80:
            lettergrade = "B"
            totB += 1
        elif finalgr >= 70:
            lettergrade = "C"
            totC += 1
        elif finalgr >= 60:
            lettergrade = "D"
            totD += 1
        else:
            lettergrade = "F"
            totF += 1
        stu[i].append(lettergrade)

    average = gradestotal / len(stu)

def create_report_file():
    line = "\n***************************************************************"
    repfile = open(out_file, "w")
    repfile.write("\n************************ CSC 230 Grade Report *****************")
    repfile.write("\nReport Date/Time          : " + str(current_time))
    repfile.write("\nTotal number of students  : " + str(len(stu)))
    repfile.write("\nAverage student grade     : " + format(average, '5,.2f'))
    repfile.write("\nTotal number of A grades  : " + str(totA))
    repfile.write("\nTotal number of B grades  : " + str(totB))
    repfile.write("\nTotal number of C grades  : " + str(totC))
    repfile.write("\nTotal number of D grades  : " + str(totD))
    repfile.write("\nTotal number of F grades  : " + str(totF))
    repfile.write(line)
    repfile.write("\nNAME                    HW\tMID\tFIN\tFinal Grade")
    repfile.write(line)
    for i in range(len(stu)):
        sname = '{0:<18}'.format(stu[i][0] + ', ' + stu[i][1])
        hw = str(stu[i][2])
        midex = str(stu[i][3])
        finex = str(stu[i][4])
        fingrade = format(stu[i][5],'6,.2f')
        repfile.write("\n" + sname + "\t" + hw + "\t" + midex + "\t" + finex + "\t" + fingrade + " " + stu[i][6])
    repfile.write(line)
    repfile.close()
    print("Open this file to view the Grades Report:  " + out_file)
                
#    for i in range(len(stu)):
#            sum_grades = stu[i]['hw'] + stu[i]['mid_exam'] + stu[i]['fin_exam']
#            stu[i]['fin_grade'] = sum_grades / 3

#            finalgr = stu[i]['fin_grade']
#            if finalgr >= 90:
#                lettergrade = 'A'
#            elif finalgr >= 80:
#                lettergrade = 'B'
#            elif finalgr >= 70:
#                lettergrade = 'C'
#            elif finalgr >= 60:
#                lettergrade = 'D'
#            else:
#                lettergrade = 'F'
#           stu[i]['ltr_grade'] = lettergrade

                
#def print_grade_report():
#    print("************************ CSC 230 Grade Report ******************")
#    print("NAME                    HW\tMID\tFIN\tFinal Grade")
#    for i in range(len(stu)):
#        sname = '{0:<18}'.format(stu[i]['name'])
#        hw = str(stu[i]['hw'])
#        midex = str(stu[i]['mid_exam'])
#       finex = str(stu[i]['fin_exam'])
#        fingrade = format(stu[i]['fin_grade'],'6,.2f')
#       print(sname + "\t" + hw + "\t" + midex + "\t" + finex + "\t" + fingrade + "\t" + stu[i]['ltr_grade'])

main()
