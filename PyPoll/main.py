import os
import csv

candidate = []
voter_id = []

#creates path to resource file
electiondata_csv = os.path.join('Resources', 'election_data.csv')

#open file and read csv
with open(electiondata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',' )
#skip header
    csv_header = next(csvreader)

#loop through csv reader and create candidate list
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])

#The total number of votes cast
    #Create a list of the indexes in the csvreader and take the length of the list
    total_votes_cast = len([index for index in voter_id])


#A complete list of candidates who received votes

    #Make a list of the candidates who received votes
    candidate_count = []
    candidate_names = []
    for name in candidate:
        if name not in candidate_names:
            candidate_names.append(name)


    print(candidate_names)

#The percentage of votes each candidate won
    #For each candidate, go through the candidate list and count how many times each person received a vote        
    for each_person in candidate_names:
        count = 0
        for line in candidate:
            if each_person == line:
                count = count + 1
        candidate_count.append(count)

    #Calculate the number of votes each candidate won divided by the total number of votes cast
    
    candidate_percentages = [(each_total / total_votes_cast) * 100 for each_total in candidate_count]

#The total number of votes each candidate won
    candidate_count

#The winner of the election based on popular vote
    great_vote_index = candidate_count.index(max(candidate_count))
    winner = candidate_names[great_vote_index]

#Print analysis to terminal
    #Election Results
    print("Election Results")
    print("----------------------------")
    #Total Votes
    print(f"Total Votes: {total_votes_cast}")
    print("----------------------------")
    #Candidate: Candidate's Percentage of Votes (Candidate's Total Number of Votes)
    for each_candidate in candidate_names:
        index = candidate_names.index(each_candidate)
        print(f"{candidate_names[index]}: {candidate_percentages[index]: .3f}% ({candidate_count[index]})") 
    print("----------------------------")
    #Winner
    print(f"Winner: {winner}")
