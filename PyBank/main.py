# Import os module to create file path across operating systems:
import os
# Import module for reading csv files:
import csv

# Create a path to the csv file:
csvpath = os.path.join("Resources", "budget_data.csv")

# Open and read the csv file:
with open(csvpath) as csvfile:

    # Name the file and specify the delimiter:
    budget_data = csv.reader(csvfile, delimiter=',')

    # Read and print header row:
    csv_header = next(budget_data)
    #print(f"CSV Header: {csv_header}")

    # The total number of months included in the dataset:
    month_count = 0
    months = []
    for row in budget_data:
        months.append(row)
    
    print("Total Months:", len(months))

    #month_count = sum(1 for row in budget_data)
    #print(f"Total Months: {month_count}")

    # Read each row of data after the header:
    #for row in budget_data:
        #months = len(list(budget_data))
        #months = months + 1
        #print("Total Months: " + str(months))

    