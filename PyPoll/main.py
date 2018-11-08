import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

candidates = []
khan = 0
correy=0
li=0
otooley=0
with open(csvpath, newline='')as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    rows = []
    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            rows.append(row)

totalvotes = len(rows)

for i in rows:
    if i[2] not in candidates:
        candidates.append(i[2])
for i in rows:
    if i[2] == candidates[0]:
        khan +=1
    elif i[2] == candidates[1]:
        correy +=1
    elif i[2] == candidates[2]:
        li +=1
    elif i[2] == candidates[3]:
        otooley +=1

def votepercentage(candidate):
    percentage = round(((candidate/totalvotes)*100),2)
    return (f"{percentage}%")

khanpercentage = votepercentage(khan)
correypercentage = votepercentage(correy)
lipercentage = votepercentage(li)
otooleypercentage = votepercentage(otooley)

votes=[khan,correy,li,otooley]
votes_candidates = list(zip(votes,candidates))

mostvotes = max(votes_candidates)
winner = mostvotes[1]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
print(f"Khan: {khanpercentage} ({khan})")
print(f"Correy: {correypercentage} ({correy})")
print(f"Li: {lipercentage} ({li})")
print(f"O'Tooley: {otooleypercentage} ({otooley})")
print("-------------------------")
