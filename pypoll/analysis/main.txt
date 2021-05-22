import csv
import os
#path to collect data from resources folder
csvpath=os.path.join("resources", "election_data.csv")
#read in the csv file
with open(csvpath) as csvfile:
    #split the data by commas
    csvreader=csv.reader(csvfile, delimiter=",")
    #read the head row first
    csv_header=next(csvreader)
    #set variable
    total_vote=0
    #set list
    candidates=[]
    

#loop through rows
    for row in csvreader:
        #add 1 to total_vote
        total_vote+=1
        #check if row[2] in candidates
        if row[2] not in candidates:
            #append row[2] to candidates
            candidates.append(row[2])

#read in the csv file    
with open(csvpath) as csvfile:
    #split the data by commas
    csvreader=csv.reader(csvfile,delimiter=",")
    #read the head row first
    csv_header=next(csvreader)
    #set variables
    candidates0_vote=0 
    candidates1_vote=0
    candidates2_vote=0
    candidates3_vote=0 
    #loop through rows 
    for row in csvreader:
        #check if row[2] equals to candidates[0]
        if row[2]==candidates[0]:
            #add 1 to candidates0_vote
            candidates0_vote+=1
            #set candidates_percent to candidates0_vote divided by total_vote as percentage with 3 digits after decimal point
            candidates0_percent='{:.3%}'.format(candidates0_vote/total_vote)
            #check if row[2] equals to candidates[1]
        if row[2]==candidates[1]:
            #add 1 to candidates1_vote
            candidates1_vote+=1
            #set candidates1_percent to candidates1_vote divided by total_vote as percentage with 3 digits after decimal point
            candidates1_percent='{:.3%}'.format(candidates1_vote/total_vote)
            #check if row[2] equals to candidates[2]
        if row[2]==candidates[2]:
            #add 1 to candidates2_vote
            candidates2_vote+=1
            #set candidates2_percent to candidates2_vote divided by total_vote as percentage with 3 digits after decimal point
            candidates2_percent='{:.3%}'.format(candidates2_vote/total_vote)
            #check if row[2] equals to candidates[3]
        if row[2]==candidates[3]:
            #add 1 to candidates3_vote
            candidates3_vote+=1
            #set candidates3_percent to candidates3_vote divided by total_vote as percentage with 3 digits after decimal point
            candidates3_percent='{:.3%}'.format(candidates3_vote/total_vote)
#set votes list
votes=[candidates0_vote,candidates1_vote,candidates2_vote,candidates3_vote]
#combine candidates and votes list
zoster=zip(candidates,votes)
#set variable
winner_vote=0
#loop through items in zoster
for candidate, vote in zoster:
    #check if vote is larger than winner_vote
    if vote > winner_vote:
        #set winner_vote to vote
        winner_vote=vote
        #set winner to candidate
        winner=candidate

#print statements
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
