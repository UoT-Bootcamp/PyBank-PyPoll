#Import the modules
import os
import csv

#Define the path
csvpath = os.path.join("/Users/preeti/Desktop/GIT/Python---Challenge/PyPoll/Resources", "election_data.csv")

#set an empty list and dictionaries
total_number_votes = []
candidate = {}
percent_votes = {}
winner = []

#Open the csv file
with open(csvpath) as csvfile:

    #Read the csv file
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    #loop through the rows in the csv file
    for row in csv_reader:
        
        #Append the rows in the empty list 'total_number votes'
        total_number_votes.append(row)

        #set the key in the dictionary
        key_name = row[2]
        
        #Check whether the key is not in the dictionary 'candidate', if it is then...
        if key_name not in candidate:
            
            #set the value of the key to 0
            candidate[key_name]= 0
        #increase the value of the key each time it encounter the key
        candidate[key_name] += 1
        #calculate the total number of votes
        total_votes = len(total_number_votes)
        #calculate the percent of votes and round the number
        percent_calc = round((candidate[key_name] / total_votes) * 100, 3)
        #format the above calculation to 3 decimal places
        
        #assign the percent of votes of each candidates to their key
        percent_votes[key_name] = percent_calc
        # format_percent = format(percent_calc, '.3f')
    
        #calculate the maximum of all votes
        all_values = percent_votes.values()
        max_value = max(all_values)

    #calculate the name of the candidate who got maximum percentage of vote 
    for name, percentage in percent_votes.items():
        if percentage == max_value:
            winner_name = name

#print the final output   
print("Election Results\n")
print("------------------------------\n")
print("Total Votes: " + str(total_votes) + "\n")
print("------------------------------\n")


for new_name, percentage_of_votes in sorted(percent_votes.items(), key=lambda item:item[1], reverse =True):
    
    print(str(new_name) + ": " + str(percentage_of_votes) + "% (" + str(candidate[new_name]) + ")" + "\n")   
print("------------------------------\n")
print("Winner: " + winner_name + "\n")
print("------------------------------")

#write to a output to a new .txt file
x = open(os.path.join("/Users/preeti/Desktop/GIT/Python---Challenge/PyPoll/Analysis", "PyPoll.txt"), 'w')

x.write("Election Results\n")
x.write("------------------------------\n")
x.write("Total Votes: " + str(total_votes) + "\n")
x.write("------------------------------\n")
for new_name, percentage_of_votes in sorted(percent_votes.items(), key=lambda item:item[1], reverse =True):
    x.write(str(new_name) + ": " + str(percentage_of_votes) + "% (" + str(candidate[new_name]) + ")" + "\n")
x.write("------------------------------\n")
x.write("Winner: " + winner_name + "\n") 
x.write("------------------------------") 