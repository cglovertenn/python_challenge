# Import modules
import os
import csv

# Write a function that does:
## Number of months
## Greatest Profit and Month
## Greatest Loss and Month
## Average Change
## Print the stuff
## Net Profit
def getthestuff(csv):
    months = 0
    total = 0
    maxrev = 0
    minrev = 0
    avgchange = 0
    maxmonth = ""
    minmonth = ""
    lastmonth = None
    changes = []
    current_change = 0
    for row in csv:
        current_month = row[0]
        current_pnl = int(row[1])
        total += current_pnl
        months += 1
        if lastmonth is not None:
            current_change = current_pnl-lastmonth
            changes.append(current_change)
        if current_pnl > maxrev:
            maxrev = current_pnl
            maxmonth = current_month
        if current_pnl < minrev:
             minrev = current_pnl
             minmonth = current_month
        if current_change < minrev:
            minrev = current_change
            minmonth = current_month

        lastmonth = current_pnl
    avgchange = sum(changes)/len(changes)
    return [months, total, maxrev, minrev, avgchange, maxmonth, minmonth]

# Set source file path
budget_data_csv = os.path.join("budget_data.csv")

# Open the source file
with open(budget_data_csv, 'r') as file:

# Read the source file
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    analysis = getthestuff(csvreader)

print(f"""
Financial Analysis
-------------------------------
Total Months: {analysis[0]}
Total: ${analysis[1]}
Average Change: ${analysis[4]}
Greatest Increase in Profit: {analysis[5]} ${analysis[2]}
Greatest Decrease in Profit: {analysis[6]} ${analysis[3]}
""")

# Set output file path
# Save the stuff to a text file