import csv
import os
filepath = r"PayBank\Resources\budget_data.csv"
total_months = 1
Total_profit_loss = []
Net_Changes= []
low_change = 0
high_change = 0
with open(filepath,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skipping the header
    Header_row = next(csvreader)
    #skipping the first row to use its value for calculating the net changes of first month
    first_row = next(csvreader)
    prev_net = int(first_row[1])
    Total_net = int(first_row[1])
    for row in csvreader:
        #calculationg the total months and the total net
        total_months += 1
        Total_net = int(row[1]) + Total_net

        #calculating the changes
        changes = int(row[1]) - prev_net
        Net_Changes.append(changes)
        prev_net = int(row[1])

        #calculating greatest decrease
        if low_change > changes:
          low_change = changes
          low_month = row[0] 
          #calculating greatest increase
        if high_change < changes:
           high_change = changes
           high_month = row[0]  
 #calculating the Average Change       
avgchanges = round(sum(Net_Changes)/len(Net_Changes), 2)
 #printing the results in terminal   
print(f"Total Months {total_months}")
print(f"Total ${Total_net}")
print(f"Average Change ${avgchanges}")
print(f"Greatest Increase in Profits: {high_month} (${high_change})")
print(f"Greatest Decrease in Profits: {low_month} (${low_change})")
#writing into the text file:
textpath = r"PayBank\analysis\bank.txt"
with open (textpath,'w') as f:
   f.write("Financial Analysis\n")
   f.write("......................\n")
   f.write(f"Total Months: {total_months}\n")
   f.write(f"Total: {Total_net}\n")
   f.write(f"Average Change: {avgchanges}\n")
   f.write(f"Greatest Increase in Profits: {high_month} $({high_change})\n")
   f.write(f"Greatest Decrease in Profits: {low_month} $({low_change})\n")