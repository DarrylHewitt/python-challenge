import os # Import os module to create file path across operating systems
import csv # Import module for reading csv files

csvpath = os.path.join("Resources", "budget_data.csv") # Create a path to the csv file

with open(csvpath) as csvfile: # Open and read the csv file

    budget_data = csv.reader(csvfile, delimiter=',') # Name the file and specify the delimiter

    next(budget_data) # Skip the header row

    # The total number of months included in the dataset and net total amount of "Profit/Losses" over the entire period:
    months = []
    total_profit_loss = 0
    
    for month in budget_data:
        months.append(month[0])
        profit_loss = int(month[1])
        total_profit_loss += profit_loss 

    print("Total Months:", len(months))
    print("Total:", total_profit_loss)

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes:
    csvfile.seek(0) # Reset the file pointer
    next(budget_data) # Skip the header row again
    first_row = next(budget_data) # Assign the first row after the header to a variable

    net_change_list = [] # Create list for every monthly change
    prev_val = int(first_row[1]) # Keep track of the previous value variable by initialising it to the first row

    for j in budget_data: 
        
        net_change = int(j[1]) - prev_val # Subtract the current cell value from the previous value
        prev_val = int(j[1]) # Once calculated, update the previous value to the current cell value
        net_change_list.append(net_change) # Add the calculation to the list
        
    avg_net_change = sum(net_change_list) / len(net_change_list) #Find the average monthly change

    print("Average change:", avg_net_change)

    # Make the two lists the same size by adding a None value to the beginning of the shorter list
    max_length = max(len(months), len(net_change_list))
    months = [None] * (max_length - len(months)) + months 
    net_change_list = [0] * (max_length - len(net_change_list)) + net_change_list

    combined_list = list(zip(months, net_change_list)) # Zip the two lists together
    for month in combined_list:
        print(month)

    max_inc = 0
    max_dec = 0
    max_mon = None
    min_mon = None
   
    for month, profit_loss in combined_list:
        if profit_loss > max_inc:
            max_inc = profit_loss
            max_month = month
        else:
            profit_loss = profit_loss + 1

    print("Greatest Increase in Profits:", max_month, max_inc)

    for month, profit_loss in combined_list:
        if profit_loss < max_dec:
            max_dec = profit_loss
            min_mon = month

    print("Greatest Decrease in Profits:", min_mon, max_dec)        
        

        

    


