#Election Results

print("Election Results")
print("----------------------------")

import os
import csv


#creates path to resource file
electiondata_csv = os.path.join('Resources', 'election_data.csv')

#open file and read csv
with open(electiondata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',' )
#skip header
    csv_header = next(csvreader)

#The total number of votes cast
    total_votes_cast = len([index for index in csvreader])
    print(f"Total Votes: {total_votes_cast}")