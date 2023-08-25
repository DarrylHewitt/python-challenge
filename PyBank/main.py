# Import os module to create file path across operating systems:
import os
# Import module for reading csv files:
import csv

# Create a path to the csv file:
csvpath = os.path.join("Resources", "budget_data.csv")

# Open and read the csv file:
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and print header row:
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header:
    for row in csvreader:
        print(row)