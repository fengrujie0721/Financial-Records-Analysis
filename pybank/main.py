
import csv
import os

from dateutil.parser import parse
#path to collect data from resources folder
csvpath=os.path.join("resources","budget_data.csv")
#read in the csv file
with open(csvpath) as csvfile:
    #split the data with commas
    csvreader=csv.reader(csvfile,delimiter=",")
    #read the head row first
    csv_header=next(csvreader)
    #set list
    previous_profit=[]
    month=[]
    #set variables
    total_profit_or_loss=0
    #loop through rows
    for row in csvreader:
        #check if row[0] in month
        if row[0] not in month:
            #append row[0] to month
            month.append(row[0])
            #set monthnumber to length of month
            monthnumber=len(month)      
        total_profit_or_loss+=int(row[1])
        #append integer of row[1] to previous_profit
        previous_profit.append(int(row[1]))
        #remove last value of previous_profit
    previous_profit.pop()
#read in the csv file    
with open(csvpath) as csvfile:
    #split the data with commas
    csvreader=csv.reader(csvfile,delimiter=",")
    #read the head row first
    csv_header=next(csvreader)
    #read the next row after head row
    csv_firstrow=next(csvreader)
    #set list
    after_profit=[]
    time=[]
    change=[]
    #set varibles
    sum_of_change=0
    greatest_increase=0
    greatest_decrease= 0
#loop through rows
    for row in csvreader:
        #append integer of row[1] to after_profit
        after_profit.append(int(row[1]))
        #append row[0] to time
        time.append(row[0])
        #combine after_profit and previous_profit lists
roster=zip(after_profit,previous_profit)
#append after_profit-previous_profit to list of change
for x,y in roster:
    change.append(x-y)
    #combine time and changes lists
roster2=zip(time,change)
#loop through items in roster2
for a,b in roster2:
    #add change to sum_of_change
    sum_of_change+=b
    #check if b is greater than greatest_increase
    if b>greatest_increase:
        #set greatest_increase to b
        greatest_increase=b
        #set greatest_increase_time to a
        greatest_increase_time=a
        #check if b is less than greatest_decrease
    if b<greatest_decrease:
        #set greatest_decrease to b
        greatest_decrease=b
        #set greatest_decrease_time to a
        greatest_decrease_time=a
        #set average_change to sum_of_change divided by length of change and round to 2 digits after decimal point
average_change=round(sum_of_change/len(change),2)

#print statements
print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {monthnumber}")
print(f"Total: ${total_profit_or_loss}")
print(f"Average Change: ${average_change}")  
print(f"Greatest Increase in Profits: {greatest_increase_time} (${greatest_increase})") 
print(f"Greatest Decrease in Profits: {greatest_decrease_time} (${greatest_decrease})")


       
     

    

    
    
    