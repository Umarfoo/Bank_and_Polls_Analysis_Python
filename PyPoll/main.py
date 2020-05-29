import os
import csv

# Path to collect data from the resources folder and export data to text file
poll_csv = os.path.join('Resources', 'election_data.csv')
file_to_output = os.path.join("analysis", "poll_analysis.txt")

# Declaration of necassary variables for initial calculations for votes and candidates name
vote_total = 0
candidate = ""

# Declaration of necassary lists for storing values for candidates and vote calculation
final_list = {}

# Declaration of values necassary for calculation of Winner
winner_votes = 0
winner_name = ""
    
# Read the CSV file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # To skip the header row
    next(csvreader)

    for row in csvreader:
    
        # Row counter to calculate number of votes
        vote_total +=1
        
        # Adding/update candidates and there vote count to dictionary final_list
        candidate = row[2]
        if candidate in final_list:
            final_list[candidate] += 1
        else:
            final_list[candidate] = 1

# For printing inital result in terminal (output part 1)
print(f"```text")
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {vote_total}")
print(f"----------------------------")

# For printing in the text file ouput_1 (output part 1)
output_1 = (
    f"```text\n"
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {vote_total}\n"
    f"----------------------------\n"
    )
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_1)
    
# For printing each candidates in format "Khan: 63.000% (2218231)""
for candidate in final_list:

    # Calculating percentage of candidates vote
    percentage = (final_list[candidate]/vote_total)*100
    percentage_formatted = "{:.3f}".format(percentage)

    print(candidate + ": " + str(percentage_formatted) + "%" + " (" + str(final_list[candidate]) + ")")
    
    # Saving output_2 (output part 2) for text file export
    output_2 = (f"{candidate} : {percentage_formatted}% ({final_list[candidate]})\n")

    # Running function to calculate the number of votes and winner
    if final_list[candidate] > winner_votes:
        winner_votes = final_list[candidate]
        winner_name = candidate
    
    # Appending output file with results
    with open(file_to_output, "a") as txt_file:
        txt_file.write(output_2)

# For printing final output_3 (output part 3)
output_3 = (
    f"----------------------------\n"
    f"Winner: {winner_name}\n"
    f"----------------------------\n"
    f"```\n"
    )
# Printing results in terminal
print(output_3)
# Appending output file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output_3)