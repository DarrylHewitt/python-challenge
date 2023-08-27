import os # Import os module to create file path across operating systems
import csv # Import module for reading csv files

csvpath = os.path.join("Resources", "budget_data.csv") # Create a path to the csv file

with open(csvpath) as csvfile: # Open and read the csv file

    budget_data = csv.reader(csvfile, delimiter=',') # Name the file and specify the delimiter

    next(budget_data) # Skip the header row

    print("Financial Analysis")
    
    print("---------------------")

    # The total number of months included in the dataset and net total amount of "Profit/Losses" over the entire period:
    mths = []
    net_profit_loss = 0
    
    for mth in budget_data:
        mths.append(mth[0])
        profit_loss = int(mth[1])
        net_profit_loss += profit_loss 

    print("Total Months:", len(mths))
    print(f"Total: ${net_profit_loss}")

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes:
    csvfile.seek(0) # Reset the file pointer
    next(budget_data) # Skip the header row again
    first_row = next(budget_data) # Assign the first row after the header to a variable

    mth_change_list = [] # Create list for every monthly change
    prev_mth_val = int(first_row[1]) # Initialise a previous value variable to the first row
    
    for j in budget_data: 
        
        mth_change = int(j[1]) - prev_mth_val # Calculate a monthly change by subtracting the current cell value from the previous value
        prev_mth_val = int(j[1]) # Once calculated, update the previous value to the current cell value
        mth_change_list.append(mth_change) # Add the calculation to the list
        
    avg_mthly_change = sum(mth_change_list) / len(mth_change_list) # Find the average monthly change
    avg_mthly_change_rounded = round(avg_mthly_change, 2) # Round the number to two decimal places

    print(f"Average change: ${avg_mthly_change_rounded}")

    # Make the two lists the same size by adding a 0 value to the beginning of the shorter list
    # (There should be no change attributed to 'Jan-10', because there is no previous month to compare it to)
    max_length = max(len(mths), len(mth_change_list))
    mths = [None] * (max_length - len(mths)) + mths 
    mth_change_list = [0] * (max_length - len(mth_change_list)) + mth_change_list

    combined_list = list(zip(mths, mth_change_list)) # Zip the two lists together
    for mth in combined_list:
        print(mth)

    # Initialise variables for min/max:
    max_inc = 0
    max_dec = 0
    max_mon = None
    min_mon = None
   
    # Use the for loop to find and return the greatest increase and corresponding date:
    for mth, profit_loss in combined_list:
        if profit_loss > max_inc:
            max_inc = profit_loss
            max_mth = mth
        else:
            profit_loss = profit_loss + 1

    print(f"Greatest Increase in Profits: {max_mth} (${max_inc})")

    # Use the for loop to find and return the greatest decrease and corresponding date:
    for mth, profit_loss in combined_list:
        if profit_loss < max_dec:
            max_dec = profit_loss
            min_mon = mth
        else: 
            profit_loss = profit_loss + 1

    print(f"Greatest Decrease in Profits: {min_mon} (${max_dec})")        
        

        

    


