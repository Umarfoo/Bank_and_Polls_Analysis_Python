import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Declaration of necassary variables for initial calculations for months, total budget & average change
month_counter = 0
total_budget = 0
open_value = 0
total = 0

# Declaration of necassary lists for storing values for average change and their corressponding months
change_list = []
months_list = []

# Declaration of values necassary for greatest profit (grt_profit) and loss (lst_profit) calculations
grt_profit = 0
lst_profit = 0
grt_month = "N/A"
lst_month = "N/A"

# Read the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # To skip the header row
    next(csvreader)

    for row in csvreader:
    
        # Months counter and total budget formula
        month_counter +=1
        total_budget += int(row[1])
            
        # Statement to skip first row while calculating change
        if open_value != 0:
            change = int(row[1]) - open_value
            m_change = str(row[0])
            # Appending to change list and months list
            change_list.append(change)
            months_list.append(m_change)
        
        # To calculate change between closing - opening value
        open_value = int(row[1])

    # Calculation on change list for Total, grt_profit & lst_profit
    for i in change_list:
        total = total + i
        
        if i > grt_profit:
            grt_profit = i
            
        if i < lst_profit:
            lst_profit = i
    
    # Calculation of average of the changes in "Profit/Losses" over the entire period and formatting to two decimal place
    average_change = total/len(change_list)
    avg_formatted = "{:.2f}".format(average_change)

    # Assignment of corresponding months for printing
    grt_month = months_list[change_list.index(grt_profit)]
    lst_month = months_list[change_list.index(lst_profit)]

# Declaration of output variable for printing of results
output = (
    f"```text\n"
    f"Financial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {month_counter}\n"
    f"Total: ${total_budget}\n"
    f"Average  Change: ${avg_formatted}\n"
    f"Greatest Increase in Profits: {grt_month} ($ {grt_profit})\n"
    f"Greatest Decrease in Profits: {lst_month} ($ {lst_profit})\n"
    f"```\n")

# Printing results in terminal
print(output)

# Printing output and creating file
file_to_output = os.path.join("analysis", "budget_analysis.txt")

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)