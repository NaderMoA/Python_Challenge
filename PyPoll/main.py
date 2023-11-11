import csv
import math
filepath = r"PyPoll\Resources\election_data.csv"
total_vote = 1
candidates = []
candid_1 = 1
candid_2 = 0
candid_3 = 0
Election =[]

with open (filepath, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    header = next(csvreader)
    first_row = next(csvreader)
    candid = first_row[2]
    
    candidates.append(candid)
    for vote in csvreader:
        total_vote +=1
        if (candid != vote[2]) and (vote[2] not in candidates): 
            candidates.append(vote[2])

    
        if candidates[0] == vote[2]:
            candid_1 +=1
        elif candidates[1] == vote[2]:
            candid_2 +=1
        else:
            candid_3 +=1


percent_candid_1 = round(((candid_1)/total_vote)*100, 3)
percent_candid_2 = round(((candid_2)/total_vote)*100, 3)
percent_candid_3 = round(((candid_3)/total_vote)*100, 3)
Election.append(float(percent_candid_1))
Election.append(float(percent_candid_2))
Election.append(float(percent_candid_3))
#identifying the percentage of the winner votes
win = max(Election)


#identifying the candidate who won
num = 0
for nom in Election:
 if win == nom:
  Winer = candidates[num]
 else:
    num +=1



print(f"Total Votes: {total_vote}")
print(f"{candidates[0]}: {percent_candid_1}% ({candid_1})")
print(f"{candidates[1]}: {percent_candid_2}% ({candid_2})")
print(f"{candidates[2]}: {percent_candid_3}% ({candid_3})")
print(f"Winner: {Winer}")