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

#Create variables with analysis results and insert variables in a list to be looped through to print/ write results
    #for each candidate loop through the candidates and structure their information: then add to a list
    info_list = []
    for each_candidate in candidate_names:
        index = candidate_names.index(each_candidate)
        info = f"{candidate_names[index]}: {candidate_percentages[index]: .3f}% ({candidate_count[index]})"
        info_list.append(info)

    #assign variables to analysis results to be printed and written
    Election_Results = "Election Results"
    Dash = "----------------------------"
    Total_Votes = f"Total Votes: {total_votes_cast}"
    Candidate_Info = info_list
    Winner = f"Winner: {winner}"

    #create list of analysis for printer
    analysis_list = [Election_Results, Dash, Total_Votes, Dash, Candidate_Info, Dash, Winner]

 #Print analysis results to terminal   
    for printer in analysis_list:
        #if the printer comes upon the Candidate Info list then loop through the Candidate Info list and write to file
        if printer == Candidate_Info:
            for special_writer in Candidate_Info:
                print(special_writer)
        else: 
            print(printer)


#Print analysis to text file in analysis folder
#create path to write the txt to 
output_path = os.path.join("analysis", "main.txt")

#open file and write to file
with open(output_path, 'w') as file:
    #loop through the analysis_list and write to file
    for writer in analysis_list:
        #if the writer comes upon the Candidate Info list then loop through the Candidate Info list and write to file
        if writer == Candidate_Info:
            for special_writer in Candidate_Info:
                file.writelines(special_writer)
                file.write("\n")
        else: 
            file.writelines(writer)
            file.write("\n")
    

