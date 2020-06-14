#Import os and csv modules
import os
import csv

#Define the path of budget_data.csv file
#csvpath = os.path.join("/Users/preeti/Desktop/GIT/Python---Challenge/PyBank/Resources", 'budget_data.csv')
csvpath = os.path.join("/Users/preeti/Desktop/GIT/Python---Challenge/PyBank/Resources", "budget_data.csv")
#Open the budget_data.csv file in read mode
with open(csvpath, 'r') as csvfile:
    
    #Read the file using delimiter ","
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read the header row first 
    csv_header = next(csvreader)

    #declare an empty list for holding number of months, total profit & losses
    months_num = []
    total_profit_losses = []
    avg_change_profit_losses = []

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
        
    #Set the value of the index of first element in the list 'total_profit_losses'  
    index = 0
    
    #loop till the index is not equal to (length of list - 1)
    while index != (len(total_profit_losses) - 1):
        #calculate the change in profit/losses
        change_profit_losses = total_profit_losses[index + 1]- total_profit_losses[index]
        #update the value of index
        index +=1
        #Append the values in the empty list 'avg_change_profit_losses
        avg_change_profit_losses.append(change_profit_losses)
    #Calculate the average of the change in profit/losses
    average_change_profit_losses = round(sum(avg_change_profit_losses) / len(avg_change_profit_losses), 2)
  




    
    #Print the final result
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {len(months_num)}")
    print(f"Total: ${sum_profit_losses}")
    print(f"Average Change: ${average_change_profit_losses}")


        
        
       
    
  



