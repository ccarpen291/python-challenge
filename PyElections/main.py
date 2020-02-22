#Rice University Homework #2 -- Python!
#By: Colby Carpenter
#Feb. 17, 2020
#Please call or email for confirmations or help
#ColbyCarpenter@gmail.com
#504-430-4464

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#This is for sorting dictionaries
import operator
from collections import OrderedDict
csvpath = os.path.join('Homework_03-Python-Challenge_Instructions_PyElections_Resources_houston_election_data.csv')
candidates ={}
rowcounter = 0
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
    for row in csvreader:
        key = row[0]
        candidates[key]=0
        rowcounter += 1
#        print(row)
#now that we have gone through the loop once, to identify all of the candidates the second loop will tally up the counts
with open(csvpath,newline='',encoding='utf-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#Commented out the CSV reader
#    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
 #This is the header, have commented it out becasue I don't want to see the data anymore
#    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        key = row[0]
        value = candidates[key]
        value +=1
        candidates[key] = value
#        print(row)
#This sorts the dictionary by highest to lowest, if you wanted it to be lowest to high you would remove the reverse = true
dd = OrderedDict(sorted(candidates.items(), key=lambda x:x[1],reverse=True))
print(" ")

f=open("output.txt","w+")

print("Houston Mayoral Election Results")
f.write("Houston Mayoral Election Results"+"\n")

print("-----------------------------------------")
f.write("-----------------------------------------"+"\n")

print(f"Total Cast Votes: {rowcounter}")
f.write(f"Total Cast Votes: {rowcounter}"+"\n")

print("-----------------------------------------")
f.write(f"-----------------------------------------"+"\n")

for key in dd:
#    print(key,dd[key])
    print(f"{key}: {round(dd[key]/rowcounter*100,2)}% ({dd[key]})")
    f.write(f"{key}: {round(dd[key]/rowcounter*100,2)}% ({dd[key]})"+"\n")
print("-----------------------------------------")
f.write("-----------------------------------------"+"\n")
numbercounter=1
for key in dd:
    if numbercounter == 1:
        print(f"1st Advancing Candidate: {key}")
        f.write(f"1st Advancing Candidate: {key}"+"\n")
    elif numbercounter == 2:
        print(f"2nd Advancing Candidate: {key}")
        f.write(f"2nd Advancing Candidate: {key}"+"\n")
    numbercounter +=1
f.close()
print(" ")
print("Check the output.txt file for results you can take with you!")