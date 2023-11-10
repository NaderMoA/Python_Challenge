import os
import csv
import random
filepath = r"PayBank\Resources\budget_data.csv"
row_count = 0
Total_profit_loss = []
# calculation of the total number of mounth 
with open(filepath,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    Header_row = next(csvreader)

    # for row in csvreader:
    #     row_count = row_count + 1

    for net in csvreader:
        profit_loss = (net[1].split(","))
        Total_profit_loss.append(profit_loss)


Total = sum(Total_profit_loss)
print(Total)


# Total_Months = row_count
# print(Total_Months)      
# Total_profit_loss = profit_loss
# print(Total_profit_loss)

