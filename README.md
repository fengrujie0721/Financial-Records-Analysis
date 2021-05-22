# python-challenge pybank pypoll
Creat a Python script for analyzing the financial records of a company. The dataset is composed of two columns: Date and Profit/Losses. Give a set of financial data called budget_data.csv.



![image](https://user-images.githubusercontent.com/79819331/119210088-6b103c00-ba78-11eb-852b-2827e0ac5be9.png)

create a Python script that analyzes the records to calculate each of the following:


The total number of months included in the dataset


The net total amount of "Profit/Losses" over the entire period


Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


The greatest increase in profits (date and amount) over the entire period


The greatest decrease in losses (date and amount) over the entire period

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
