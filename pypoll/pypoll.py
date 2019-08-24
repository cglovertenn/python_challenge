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
    khanvote = 0
    corrvote = 0
    livote = 0
    toolvote = 0
    for row in csv:
        votes = row[2]
        total += 1
        if "Khan" in votes:
            khanvote = khanvote + 1
        if "Correy" in votes:
            corrvote = corrvote + 1
        if "Li" in votes:
            livote = livote + 1
        if "O'Tooley" in votes:
            toolvote = toolvote + 1
    
    total = khanvote + corrvote + livote + toolvote
    khan_pct = round((khanvote/total), 2)
    corr_pct = round((corrvote/total), 2)
    li_pct = round((livote/total, 2)
    .tool_pct = round((toolvote/total, 2)
    return [total, khanvote, corrvote, livote, toolvote, khan_pct, corr_pct, li_pct, .tool_pct]

    
# Set source file path
election_data_csv = os.path.join("election_data.csv")

# Open source file
with open(election_data_csv, 'r') as file:

# Read source file and print results
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    analysis = datafetch(csvreader)

#print results
print(f"""
Election Results
-------------------------
Total Votes: {analysis[0]}
-------------------------
Khan: {analysis[5]}% ({analysis[1]})
Correy: {analysis[6]}% ({analysis[2]})
Li: {analysis[7]}% ({analysis[3]})
O'Tooley: {analysis[8]}% ({analysis[4]})
-------------------------
Winner: Khan
-------------------------
""")


# Set output file path
## data_output = os.path.join("pypoll_output.csv")

# Save and print to text file
## with open(data_output, "w", newline="") as csvfile:
    ## writer = csv.writer(csvfile)
    ## writer.writerow()