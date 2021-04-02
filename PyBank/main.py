#import the csv file and read it
import os
import csv
import math

csvpath = os.path.join('PyBank','Resources','Python_PyBank_Resources_budget_data.csv')
total_months = 0
total_p_l = 0
change_list = []
previous_row = 0
change = 0
month_money_list = []

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

       change = int(row[1]) - previous_row
       previous_row = int(row[1])
       change_list.append(change)
       month_money_list.append(row[0])

       
#get the initial value out
    change_list.pop(0)
    month_money_list.pop(0)

    #net_monthly_avg = sum(change_list) / (total_months - 1)
    #calculate average change over time
    net_monthly_avg = round(sum(change_list) / len(change_list), 2)
    
    #print(net_monthly_avg)
    #print(total_months)
    #print(total_p_l)
    #print(net_monthly_avg)

#calculate greatest increase month
    #store as a variable
    #find a way to associate greatest inc with month included
min_loss = min(change_list)
find_the_min_loc = change_list.index(min_loss)
last_min = month_money_list[find_the_min_loc]

#calculate greatest losses month
    #store as a variable
    #find a way to associate greatest loss with month included

max_gains = max(change_list)
find_the_max_loc = change_list.index(max_gains)
last_max = month_money_list[find_the_max_loc]

#run report
print("Total Months: " + str(total_months))
print("Total: " + str(total_p_l))
print("Average Change: $" + str(net_monthly_avg))
print("Greatest Increase in Profits: $" + str(max_gains) + " during " + str(last_max))
print("Greatest Decrease in Profits: $" + str(min_loss) + " during " + str(last_min))


#export report as txt file
output_path = os.path.join('PyBank', 'analysis', 'analysis.txt')

with open(output_path, "w") as output_file:
    
    output_str = (
        f"Total Months: {total_months}\n"
        f"Total: {total_p_l}\n"
        f"Average Change: ${net_monthly_avg}\n"
        f"Greatest Increase in Profits: ${max_gains} {last_max}\n"
        f"Greatest Decrease in Profits: ${min_loss} during {last_min}\n"
    )
    output_file.write(output_str)