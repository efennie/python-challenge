#import the csv file and read it
import os
import csv
import math

csvpath = os.path.join('PyBank','Resources','Python_PyBank_Resources_budget_data.csv')
total_months = 0
total_p_l = 0
net_change_list = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#define and print headers
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#total count of column 0 to get total # of months in the set
    #store as variable "total_months"
    for row in csvreader:
        date[row[0]] = ("profit_loss"[row[1]])
        print(date)