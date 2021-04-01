#import the csv file and read it
import os
import csv
import math

csvpath = os.path.join('PyBank','Resources','Python_PyBank_Resources_budget_data.csv')
total_months = 0
total_p_l = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#define and print headers
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#total count of column 0 to get total # of months in the set
    #store as variable "total_months"
    for row in csvreader:
       total_months += 1
#sum of column 2 to get the net total profits/losses
    #store as variable "total_p_l"
       total_p_l += int(row[1])
    print(total_months)
    print(total_p_l)

#calculate average change over time
    #it'll have to be the average of (second month - first month)/total month
    # sum of change divided by total months
    #store average change as "av_change"

#calculate greatest increase month
    #store as a variable
    #find a way to associate greatest inc with month included

#calculate greatest losses month
    #store as a variable
    #find a way to associate greatest loss with month included

#assign report as a def
    #print("Total Months: " + total_months) try str(total_months) if the first way doesn't work
    #print("Total: " + total_p_l)
    #print("Average Change: " + av_change)
    #print("Greatest Increase in Profits: " + row[0] + row[1])
    #print("Greatest Decrease in Profits: " + row[0] + row[1])

#print(report)

#export report as txt file