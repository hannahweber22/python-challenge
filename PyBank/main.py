
import os
import csv

#create lists for date and profit/loss
date = []
profit_loss = []
month = []
year = []

#creates path to resource file
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')

#open file and read csv
with open(budgetdata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',' )
#skip header
    csv_header = next(csvreader)
#loop through each row in each column and put in list (creating list for each column)
    for row in csvreader:
        date.append(row[0])
        split_date = row[0].split("-")
        month.append(split_date[0])
        year.append(split_date[1])
        profit_loss.append(row[1])

#The total number of months included in the dataset
    #add to the total month list for each index in the date list if the index is not already in total month list
    
    total_month_count = 0
    total_month_list = []
    for index in date:
        if index not in total_month_list:
            total_month_list.append(index)
            total_month_count = total_month_count + 1  
    
#The net total amount of Profit/ Loss over the entire period
    #float each index in profit_loss then sum all of the floats
    profit_loss_total = sum(float(index) for index in profit_loss)
    

#The changes in Proft/ Loss over the entire period, and the average of those changes
    
    #find the changes month to month and determine if they are profits or losses; additionally, add the changes to a list
    change_list = []

    for location in range(1, len(profit_loss)):
        if profit_loss[location] < profit_loss[location - 1]:
            loss = abs(float(profit_loss[location]) - float(profit_loss[location - 1])) * -1
            change_list.append(loss)
        else:
            profit = abs(float(profit_loss[location]) - float(profit_loss[location - 1])) 
            change_list.append(profit)


    #find total change in profit_loss and determine if it is a profit or loss
    if float(profit_loss[0]) > float(profit_loss[-1]):   
        total_change = abs(float(profit_loss[0]) - float(profit_loss[-1])) * -1
    else:
        total_change = abs(float(profit_loss[0]) - float(profit_loss[-1])) 

    #find average of changes over period dividing the change between the first and last profit_loss values by length of profit_loss changes
    average_change = total_change/ len(change_list)
    
 #The greatest increase in profits (data and amount) over the entire period
    great_increase_profit = max(change_list)
    great_increase_index = change_list.index(great_increase_profit) + 1
    great_increase_date = date[great_increase_index]

#The greatest decrease in profits (date and amount) over the entire period
    great_decrease_profit = min(change_list)
    great_decrease_index = change_list.index(great_decrease_profit) + 1
    great_decrease_date = date[great_decrease_index]

#Create variables with analysis results and insert variables in a list to be looped through to print/ write results
    #assign variables to analysis results to be printed and written
    Finanical_Analysis = "Financial Analysis"
    Dash = "----------------------------"
    Total_Months = f"Total months: {total_month_count}"
    Profit_Loss_Total = f"Total: ${profit_loss_total: .0f}"
    Average_Change = f"Average Change: ${average_change: .2f}"
    Greatest_Increase = f"Greatest Increase in Profits: {great_increase_date} (${great_increase_profit: .0f})"
    Greatest_Decrease = f"Greatest Decrease in Profits: {great_decrease_date} (${great_decrease_profit: .0f})"

    #create list of analysis for printer
    analysis_list = [Finanical_Analysis, Dash, Total_Months, Profit_Loss_Total, Average_Change, Greatest_Increase, Greatest_Decrease]

 #Print analysis results to terminal
    #Loop through the analysis list and print analysis results to terminal   
    for printer in analysis_list:
        print(printer)

#Print analysis to text file in analysis folder
#create path to write the txt to 
output_path = os.path.join("analysis", "main.txt")

#open file and write to file
with open(output_path, 'w') as file:
    #loop through the analysis_list and write to file
    for writer in analysis_list:
        file.writelines(writer)
        file.write("\n")
