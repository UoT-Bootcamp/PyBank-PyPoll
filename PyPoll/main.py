import os
import csv


csvpath = os.path.join("/Users/preeti/Desktop/GIT/Python---Challenge/PyPoll/Resources", "election_data.csv")

total_number_votes = []
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    for row in csv_reader:
        total_number_votes.append (row)

    
