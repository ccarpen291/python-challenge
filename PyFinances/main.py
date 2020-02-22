# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#This is for sorting dictionaries
import operator
from collections import OrderedDict
csvpath = os.path.join('Homework_03-Python-Challenge_Instructions_PyFinances_Resources_budget_data.csv')
rowcounter = 0
dictionary = {}
# Method 2: Improved Reading using CSV module
with open(csvpath,newline='',encoding='utf-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#Commented out the csvreader
#    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
 #This is the header, have commented it out becasue I don't want to see the data anymore
 #   print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    totalsum=0
    changes=[]
    change = True
    var1 = 0.0
    var2 = 0.0

    maxprofits=0
    minprofits=0

    for row in csvreader:
        if change == False: #this finds the change between current value and last value 
            var2 = int(row[0])
            changes.append(var2-var1)
            change = True
            if var2-var1 >= maxprofits:
                maxprofits = var2-var1
                maxprofitdate = row[1]
            if var2-var1 <= minprofits:
                minprofits = var2-var1
                minprofitdate = row[1]
        if change == True:
            var1 = int(row[0])
            change = False
        totalsum+=int(row[0]) #this adds all of the items
        key = row[1]
        dictionary[key]=0
        rowcounter += 1
#        print(row) 

monthcounter = 0
for key in dictionary:
    monthcounter += 1

length = len(changes)
total = 0.0
for number in changes:
    total += number
averages = total / length


f=open("output.txt","w+")

print(" ")
f.write(" " + "\n")

print("Financial Analysis")
f.write("Financial Analysis" + "\n")

print("----------------------------")
f.write("----------------------------" +"\n")
print(f"Total Months: {monthcounter}")
f.write(f"Total Months: {monthcounter}" + "\n")

print(f"Total Sum: ${totalsum}")
f.write(f"Total Sum: ${totalsum}" +"\n")

print(f"Average Change: ${round(averages,2)}")
f.write(f"Average Change: ${round(averages,2)}" +"\n")

print(f"Greatest Increase in Profits: {maxprofitdate} (${maxprofits})")
f.write(f"Greatest Increase in Profits: {maxprofitdate} (${maxprofits})" +"\n")

print(f"Greatest Decrease in Profits: {minprofitdate} (${minprofits})")
f.write(f"Greatest Decrease in Profits: {minprofitdate} (${minprofits})" +"\n")

print(" ")

print("Check the same file where you ran this to get an output.txt of the results!  Thanks Much")


def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length