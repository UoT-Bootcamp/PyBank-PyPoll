#Import os and csv modules
import os
import csv

#Define the path of budget_data.csv file
csvpath = os.path.join("/Users/preeti/Desktop/GIT/Python---Challenge/PyBank/Resources", 'budget_data.csv')

#Open the budget_data.csv file in read mode
with open(csvpath, 'r') as csvfile:
    
    #Read the file using delimiter ","
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read the header row first 
    csv_header = next(csvreader)

    #declare an empty list for holding number of months, total profit & losses
    months_num = []
    total_profit_losses = []

    # Read each row of data after the header
    for row in csvreader:

        #Append months in the empty list 'months_num'
        months_num.append(row[0])
        #Append profit/losses in the empty list 'total_profit_losses'
        total_profit_losses.append(row[1])
        #convert element of the list 'total_profit_losses' from string to integer
        total_profit_losses = [int(num) for num in total_profit_losses]
        #Calculate sum of all the elements in the list 'total_profit_losses'
        sum_profit_losses = sum(total_profit_losses)
    
    #Print the final result
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {len(months_num)}")
    print(f"Total: ${sum_profit_losses}")


        
        
       
    
  



