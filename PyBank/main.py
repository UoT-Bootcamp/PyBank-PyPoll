import os
import csv
# /Users/preeti/Desktop/GIT/Python---Challenge/PyBank/Resources
csvpath = os.path.join("/Users/preeti/Desktop/GIT/Python---Challenge/PyBank/Resources", 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)

    months_num = []

    for row in csvreader:
        months_num.append(row[0])
        # print(row)
    number_of_months = len(months_num)
    #print(number_of_months)



