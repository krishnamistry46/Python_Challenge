#Challenge 1: PyBank Financial Analysis
#--------------------------------------------------------------------------------------------------------------------

# In this challenge, objective is to develop a Python script to analyze company's financial records. 
#The dataset we'll be working with is called budget_data.csv, comprising two columns: Date and Profit/Losses.

#--------------------------------------------------------------------------------------------------------------------

# Script should perform the following calculations:

# Determine the total number of months included in the dataset.
# Calculate the total net amount of profit or loss over the entire period.
# Compute the average change in profit or loss between months throughout the period.
# Identify the greatest increase in profits, including the corresponding date and amount.
# Identify the greatest decrease in losses, including the corresponding date and amount.

#--------------------------------------------------------------------------------------------------------------------

# An example output might resemble the following:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

#====================================================================================================================

# Importing the modules OS and CSV

import os
import csv

# Set path to CSV file
budget_data_path = os.path.join( 'Resources', 'budget_data.csv')

# # Initialize variables
total_months = 0
net_profit = 0
change = {}
greatest_increase_month = ""
greatest_decrease_month = ""

# Open and read CSV file
with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip header row

    #for row in csvreader:
       # print(row)

    # Loop through each row in the CSV file
    for row in csvreader:
        total_months += 1
        net_profit += int(row[1])

        # Calculate change in profit from month to month
        if total_months > 1:
            current_change = int(row[1]) - prev_month
            change[row[0]] = current_change
            
            # Track greatest increase and decrease in profits
            if current_change > change.get(greatest_increase_month, 0):
                greatest_increase_month = row[0]
            elif current_change < change.get(greatest_decrease_month, 0):
                greatest_decrease_month = row[0]
        
        prev_month = int(row[1])  # Store previous month's profit for next iteration

# Calculate average change
average_change = sum(change.values()) / len(change) if change else 0

# Format output
results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_profit}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_month} (${change.get(greatest_increase_month, 0)})
Greatest Decrease in Profits: {greatest_decrease_month} (${change.get(greatest_decrease_month, 0)})"""

# Print results
print(results)

# Write results to a text file
output_path = os.path.join('..', 'PyBank', 'Resources', 'Result_pybank.txt')
with open(output_path, "w") as output_file:
    output_file.write(results)




