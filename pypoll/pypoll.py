# Import modules
import os
import csv

# Write functions to accomplish:
## Total number of votes
## List canditates who received votes
## Percentage of total votes for each candidate
## Total votes per candidate
## Election winner based on most votes
def datafetch(csv):
    totalvotes = 0
    candidates = 0
    vote_pct = 0
    candidate_votes = 0
    candidate_winner = 0
    voter_id = None
    for row in csv:
        voter_id = int(row[0])
        candidate = (row[2])
        if candidate is not None:
            totalvotes = candidate
    return [totalvotes]


# Set source file path
election_data_csv = os.path.join("election_data.csv")

# Open source file
with open(election_data_csv, 'r') as file:

# Read source file and print results
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    analysis = datafetch(csvreader)

print ({analysis[0]})


# Set output file path
## data_output = os.path.join("pypoll_output.csv")

# Save and print to text file
## with open(data_output, "w", newline="") as csvfile:
    ## writer = csv.writer(csvfile)
    ## writer.writerow()

