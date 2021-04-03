import csv
import os

from dateutil.parser import parse
csvpath=os.path.join("resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)
    previous_profit=[]
    monthnumber=0
    total_profit_or_loss=0
    for row in csvreader:
        total_profit_or_loss+=int(row[1])
               
        monthnumber+=1
        previous_profit.append(int(row[1]))
        #change=int(next(row[1]))-int(row[1])
    previous_profit.pop()
    
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)
    csv_firstrow=next(csvreader)
    after_profit=[]
    time=[]
    change=[]
    sum_of_change=0
    greatest_increase=0
    greatest_decrease= 0

    for row in csvreader:
        after_profit.append(int(row[1]))
        time.append(row[0])
roster=zip(after_profit,previous_profit)
for x,y in roster:
    change.append(x-y)
roster2=zip(time,change)
for a,b in roster2:
    sum_of_change+=b
    if b>greatest_increase:
        greatest_increase=b
        greatest_increase_time=a
    if b<greatest_decrease:
        greatest_decrease=b
        greatest_decrease_time=a
average_change=round(sum_of_change/len(change),2)


print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {monthnumber}")
print(f"Total: ${total_profit_or_loss}")
print(f"Average Change: ${average_change}")  
print(f"Greatest Increase in Profits: {greatest_increase_time} (${greatest_increase})") 
print(f"Greatest Decrease in Profits: {greatest_decrease_time} (${greatest_decrease})")


       
     

    

    
    
    