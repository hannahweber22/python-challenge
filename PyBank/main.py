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
    #Combine month and year in array, 
    #For the data index in the array (loop through the array),
    #If month or year is not equal to previous then add to list
        #for date_index in 

#The net total amount of Profit/ Loss over the entire period
#float each index in profit_loss then sum all of the floats
    profit_loss_total = sum(float(index) for index in profit_loss)
    print(f"Profit/Loss Net Total Amount {profit_loss_total}")


