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
    total = 0
    kvote = 0
    cvote = 0
    lvote = 0
    tvote = 0
    for row in csv:
        votes = row[2]
        total += 1
        if "Khan" in votes:
            kvote = kvote + 1

    print(kvote)

# Set source file path
election_data_csv = os.path.join("election_data.csv")

# Open source file
with open(election_data_csv, 'r') as file:

# Read source file and print results
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    datafetch(csvreader)
    #analysis = datafetch(csvreader)

#print ({analysis[0]})


# Set output file path
## data_output = os.path.join("pypoll_output.csv")

# Save and print to text file
## with open(data_output, "w", newline="") as csvfile:
    ## writer = csv.writer(csvfile)
    ## writer.writerow()

