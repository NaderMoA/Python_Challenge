import csv
filepath = r"PyPoll\Resources\election_data.csv"
total_vote = 1
candidates = []
candid_1 = 1
candid_2 = 0
candid_3 = 0
Election =[]

with open (filepath, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    #skipping the header row
    header = next(csvreader)
    #skipping the first row to use its valu and compare it the row below it
    first_row = next(csvreader)
    candid = first_row[2]
    #finding the list of all candidates
    candidates.append(candid)
    for vote in csvreader:
        total_vote +=1
        if (candid != vote[2]) and (vote[2] not in candidates): 
            candidates.append(vote[2])

     #finding the number of votes for each candidate
        if candidates[0] == vote[2]:
            candid_1 +=1
        elif candidates[1] == vote[2]:
            candid_2 +=1
        else:
            candid_3 +=1

#calculating the % for each candidate and adding them to a list to later find the max and the winner from the list
percent_candid_1 = round(((candid_1)/total_vote)*100, 3)
percent_candid_2 = round(((candid_2)/total_vote)*100, 3)
percent_candid_3 = round(((candid_3)/total_vote)*100, 3)
Election.append(float(percent_candid_1))
Election.append(float(percent_candid_2))
Election.append(float(percent_candid_3))
#identifying the percentage of the winner votes
win = max(Election)
#identifying the candidate who won by coparing the max % to the vote % of each candidate
num = 0
for nom in Election:
 if win == nom:
  Winer = candidates[num]
 else:
    num +=1
#printging the results in Terminal
print(f"Total Votes: {total_vote}")
print(f"{candidates[0]}: {percent_candid_1}% ({candid_1})")
print(f"{candidates[1]}: {percent_candid_2}% ({candid_2})")
print(f"{candidates[2]}: {percent_candid_3}% ({candid_3})")
print(f"Winner: {Winer}")
#writing the results in text file:
textpath = r"PyPoll\analysis\poll.txt"
with open(textpath, "w") as f:
   f.write("Election Results\n")
   f.write("......................\n")
   f.write(f"Total Votes: {total_vote}\n")
   f.write(f"{candidates[0]}: {percent_candid_1}% ({candid_1})\n")
   f.write(f"{candidates[1]}: {percent_candid_2}% ({candid_2})\n")
   f.write(f"{candidates[2]}: {percent_candid_3}% ({candid_3})\n")
   f.write("......................\n")
   f.write(f"Winner: {Winer}")