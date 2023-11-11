import os
import csv
import random
filepath = r"PayBank\Resources\budget_data.csv"
total_months = 1
Total_profit_loss = []
Net_Changes= []
low_change = 0
high_change = 0
with open(filepath,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    Header_row = next(csvreader)
    first_row = next(csvreader)
    prev_net = int(first_row[1])
    Total_net = int(first_row[1])
    for row in csvreader:
        
        total_months += 1
        Total_net = int(row[1]) + Total_net
        
        changes = int(row[1]) - prev_net
        if low_change > changes:
          low_change = changes
          low_month = row[0] 
        if high_change < changes:
           high_change = changes
           high_month = row[0]  
        prev_net = int(row[1])
        Net_Changes.append(changes)
    
    avgchanges = round(sum(Net_Changes)/len(Net_Changes), 2)
    
print(f"Total Months {total_months}")
print(f"Total ${Total_net}")
print(f"Average Changes ${avgchanges}")
print(f"Greatest Increase in Profits: {high_month} (${high_change})")
print(f"Greatest Decrease in Profits: {low_month} (${low_change})")






