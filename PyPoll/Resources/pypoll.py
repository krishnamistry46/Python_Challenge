# Challenge 2: PyPoll

#====================================================================================================================================

# This challenge involves analyzing voting data from an election. Here are the key tasks to accomplish:

# Determine the total number of votes cast: Simply sum up all the votes.
# Compile a list of all candidates who received votes: Find the unique names from the third column (index 2) of the data.
# Calculate the percentage of votes each candidate received:
# For each unique candidate, calculate the total number of votes they received.
# Divide this total by the overall number of votes cast (from step 1), then multiply by 100.
# Determine the total number of votes each candidate received: Obtain from the previous step.
# Identify the winner of the election based on the popular vote: The candidate with the highest number of votes wins.
# Remember to use version control with git to submit this assignment

#========================================================================================================================================

# Resource used: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/.
# For writing the text, also utilize the same loop.
# Resource used: https://www.geeksforgeeks.org/python-get-unique-values-list/.

#=====================================================================================================================================

# Note to Self:

#he CSV file is opened using a with statement, ensuring it's properly closed after reading.
# Used dict.get() method to simplify vote counting for each candidate.
# Used items() to iterate over key-value pairs in candidate_votes.
# Formatted percentage votes using f-strings for better readability.
# Simplified finding the winner using the max() function with the key argument.
# Combined some operations to improve readability and efficiency.
# Applied consistent naming conventions and formatting throughout the code.

import os
import csv

# Variables initialization
total_votes = 0
candidate_votes = {}

# Path to CSV file
election_data_path = os.path.join('Resources', 'election_data.csv')

# Open CSV file and calculate total votes
with open(election_data_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)  # Read and skip header
    for row in csvreader:
        total_votes += 1
        candidate = row[2]  # Candidate name
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1  # Increment candidate votes count

# Election results string
results = f"""Election Results
--------------------------
Total Votes: {total_votes}
--------------------------
"""

# Calculate and add candidate vote total and percent of vote
for candidate, votes in candidate_votes.items():
    percent_vote = round((votes / total_votes) * 100, 3)
    results += f"{candidate}: {percent_vote:.3f}% ({votes})\n"

# Find the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Add winner to results
results += f"""--------------------------
Winner: {winner}
--------------------------
"""

# Print results to the terminal
print(results)

# Path for output file
output_path = os.path.join('..', 'PyPoll', 'Resources', 'Result_pypoll.txt')

# Write results to output file
with open(output_path, "w") as output_file:
    output_file.write(results)
