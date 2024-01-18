#Lines 3-6 importthe necessary modules for this script

import os
import csv
import statistics

#Line 10 is declaring a variable and defining it as the csv file containing the data
#that we will be analyzing.

budget_dataset = os.path.join('..', 'Resources', 'budget_data.csv')

#num_months is an empty list that will contain the number of months within our dataset.

num_months = []

#monthly_profit is an empty list that will contain the profit or loss obtained each month.

monthly_profit = []

#monthly_change is an empty list that will contain the monthly variance in profit or loss.

monthly_change = []




#The following block of code will read the CSV file, and append each value in the first column to "num months" & second colum to "monthly_profit"

with open(budget_dataset, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)
    first_row =next(csvreader)
    
    
    for row in csvreader:
        
        num_months.append(row[0])
        monthly_profit.append(int(row[1]))
        

#The following loop will calculate the monthly variance in profit, and append the value to the "monthly_change" list.
        
for i in range(len(monthly_profit)-1):
        
    monthly_change.append(monthly_profit[i+1]-monthly_profit[i])
    
#The following line of code declares a variable that will store the total profit.

#This was calculated by using the sum function, which adds all the values within our "monthly_change" profit list.  

total_profit = sum(monthly_profit)

#The following variable will store the average monthly change.

#This is calculated by calling the "mean" method within the "statistics" module.

average_monthly_profit = statistics.mean(monthly_change)

#The following code declares two variables storing our largest profit, and loss.
#These values are obtained by calling the "max" and "min" function on tthe "monthly_change" list.
    
max_monthly_gain = max(monthly_change)
max_monthly_loss = min(monthly_change)

#The following code uses the "index" function to obtain the list index of our max and min profit/loss values.
#Since the profit and month lists indices are aligned, we are able to plug the index number into our month list.

max_increase_month = num_months[1 + monthly_change.index(max_monthly_gain)]
max_loss_month = num_months[1 + monthly_change.index(max_monthly_loss)] 

#The following method takes in a numeric value, and formats it to a monetary value,  

def int_to_mon (numeric_value):
    numeric_value = float(numeric_value)
    numeric_value = "${:,.2f}".format(numeric_value)
    return numeric_value 

#The following statements will print our analysis to the console.

print("Financial Analysis")
print("\n")
print('-' * 30)
print("\n")
print(f"Total Months: {len(num_months)}") 
print("\n")
print(f"Total Profit: {int_to_mon(total_profit)}")
print("\n")
print(f"Average Change: {int_to_mon(average_monthly_profit)}")
print("\n")
print(f"Greatest Increase in Profits: {max_increase_month} ({int_to_mon(max_monthly_gain)})")
print("\n")
print(f"Greatest Decrease in Profits: {max_loss_month} ({int_to_mon(max_monthly_loss)})")

#The following code declares a variable which will store the path of the text file that we will be outputting our analysis to.
#The "with" code block will allow us to edit the above mentioned text file, due to the 'w' (write) indication.
#The write function will output our script to the specified text file.

financial_analysis = os.path.join('..', 'Financial_Analysis_Summary','financial_analysis_summary.txt')

with open(financial_analysis, 'w') as txt_file:
    
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write('-' * 30)
    txt_file.write("\n")
    txt_file.write(f"Total Months: {len(num_months)}") 
    txt_file.write("\n")
    txt_file.write(f"Total Profit: {int_to_mon(total_profit)}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: {int_to_mon(average_monthly_profit)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: {max_increase_month} ({int_to_mon(max_monthly_gain)})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: {max_loss_month} ({int_to_mon(max_monthly_loss)})")

    
        
 
        


    


    


    

