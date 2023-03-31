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
        month_list = month.append(split_date[0])
        year_list = year.append(split_date[1])
        profit_loss.append(row[1])

#The total number of months included in the dataset
    #add to the total month list for each index in the date list if the index is not already in total month list
    
    total_month_count = 0
    total_month_list = []
    for index in date:
        if index not in total_month_list:
            total_month_list.append(index)
            total_month_count = total_month_count + 1  
    
    print(total_month_count)

#The net total amount of Profit/ Loss over the entire period
    #float each index in profit_loss then sum all of the floats
    profit_loss_total = sum(float(index) for index in profit_loss)
    print(f"Profit/Loss Net Total Amount {profit_loss_total}")

#The changes in Proft/ Loss over the entire period, and the average of those changes



