import csv
import os
csvpath=os.path.join("resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    total_vote=0
    candidates=[]
    


    for row in csvreader:
        
        total_vote+=1
        if row[2] not in candidates:
            candidates.append(row[2])

    
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)
    candidates0_vote=0 
    candidates1_vote=0
    candidates2_vote=0
    candidates3_vote=0  
    for row in csvreader:
        if row[2]==candidates[0]:
            candidates0_vote+=1
            candidates0_percent='{:.3%}'.format(candidates0_vote/total_vote)
        if row[2]==candidates[1]:
            candidates1_vote+=1
            candidates1_percent='{:.3%}'.format(candidates1_vote/total_vote)
        if row[2]==candidates[2]:
            candidates2_vote+=1
            candidates2_percent='{:.3%}'.format(candidates2_vote/total_vote)
        if row[2]==candidates[3]:
            candidates3_vote+=1
            candidates3_percent='{:.3%}'.format(candidates3_vote/total_vote)

votes=[candidates0_vote,candidates1_vote,candidates2_vote,candidates3_vote]
zoster=zip(candidates,votes)

winner_vote=0
for candidate, vote in zoster:
    if vote > winner_vote:
        winner_vote=vote
        winner=candidate


print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_vote}")
print("--------------------------")
print(f"{candidates[0]}: {candidates0_percent} ({candidates0_vote})")
print(f"{candidates[1]}: {candidates1_percent} ({candidates1_vote})")
print(f"{candidates[2]}: {candidates2_percent} ({candidates2_vote})")
print(f"{candidates[3]}: {candidates3_percent} ({candidates3_vote})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")
