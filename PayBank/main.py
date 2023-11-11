import csv
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
        
avgchanges = round(sum(Net_Changes)/len(Net_Changes), 2)
    
print(f"Total Months {total_months}")
print(f"Total ${Total_net}")
print(f"Average Change ${avgchanges}")
print(f"Greatest Increase in Profits: {high_month} (${high_change})")
print(f"Greatest Decrease in Profits: {low_month} (${low_change})")
