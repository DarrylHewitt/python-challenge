import os # Import os module to create file path across operating systems
import csv # Import module for reading csv files

csvpath = os.path.join("Resources", "budget_data.csv") # Create a path to the csv file

with open(csvpath) as csvfile: # Open and read the csv file

    budget_data = csv.reader(csvfile, delimiter=',') # Name the file and specify the delimiter

    next(budget_data) # Skip the header row

    # The total number of months included in the dataset and net total amount of "Profit/Losses" over the entire period:
    months = []
    total_profit_loss = 0
    
    for i in budget_data:
        months.append(i[0])
        profit_loss = int(i[1])
        total_profit_loss += profit_loss 
        
    print("Total Months:", len(months))
    print("Total:", total_profit_loss)

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes:
    csvfile.seek(0) # Reset the file pointer
    next(budget_data) # Skip the header row again
    first_row = next(budget_data) # Assign the first row after the header to a first_row variable

    net_change_list = [] # Create list for every monthly change
    prev_val = int(first_row[1]) # Keep track of the previous value variable by initialising it to the first row

    for j in budget_data: 
        
        net_change = int(j[1]) - prev_val # Subject the current cell value from the previous value
        prev_val = int(j[1]) # Once calculated, update the previous value to the current cell value
        net_change_list.append(net_change) # Add the calculation to the list

    avg_net_change = sum(net_change_list) / len(net_change_list) #Find the average monthly change
    
    print("Average change:", avg_net_change)



            
    
    


