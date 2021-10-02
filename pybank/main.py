import os
import csv

"""Description: create a Python script for analyzing the financial records of your 
company. You will give a set of financial data called budget_data.csv. The dataset is composed of 
two columns: Date and Profit/Losses. 

Ouput:
The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period
"""


#read in data
budget_data = os.path.join(os.getcwd(), 'Resources', 'budget.csv')
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    data_head = next(csvreader)
    
    #must create empty lists to store values
    total_number_months = []
    total_amount_profit_losses = []
    change_amount_profit_losses = []
    
    # going to through the empty lists and begin appending
    for row in csvreader:
        total_number_months.append(row[0])
        total_amount_profit_losses.append(int(row[1]))
    for _ in range(len(total_amount_profit_losses)-1):
        change_amount_profit_losses.append(total_amount_profit_losses[_ + 1]- total_amount_profit_losses[_]) 
        


#finding the maxixum and minimum using statistical functions inherent in python

growth = max(change_amount_profit_losses)
decline = min(change_amount_profit_losses)

#begin the counter for profit growth or decline

monthly_profit_growth = change_amount_profit_losses.index(max(change_amount_profit_losses)) + 1
monthly_profit_decline = change_amount_profit_losses.index(min(change_amount_profit_losses)) + 1

# printing the output to a folder named, "analysis".

budget_data_output = os.path.join(os.getcwd(), 'analysis', 'budget_analysis.txt')
with open(budget_data_output, "w") as new:
    new.write("Finacial Analysis")
    new.write("\n")
    new.write("--------------------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(total_number_months)}")
    new.write("\n")
    new.write(f"Total: ${sum(total_amount_profit_losses)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_amount_profit_losses)/len(change_amount_profit_losses),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {total_number_months[monthly_profit_growth]} (${(str(growth))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {total_number_months[monthly_profit_decline]} (${(str(decline))})")
    

    
#print statements 

print("Finacial Analysis")
print("--------------------------------------")
print(f"Total Months:{len(total_number_months)}")
print(f"Total: ${sum(total_amount_profit_losses)}")
print(f"Average Change: {round(sum(change_amount_profit_losses)/len(change_amount_profit_losses),2)}")
print(f"Greatest Increase in Profits: {total_number_months[monthly_profit_growth]} (${(str(growth))})")
print(f"Greatest Decrease in Profits: {total_number_months[monthly_profit_decline]} (${(str(decline))})")     