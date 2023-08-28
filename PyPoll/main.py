import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

candidate_data = {}

with open(csvpath) as csvfile:

    election_data = csv.reader(csvfile, delimiter=',')

    results_folder = "C:\\Users\\dhewi\\OneDrive\\Desktop\\Bootcamp\\Week_3\\Week_3_assignment\\python-challenge\\PyPoll\\Analysis"
    results_path = os.path.join(results_folder, "election_results.txt")

    with open(results_path, "w") as file:

        next(election_data)

        file.write("------------------\n")

        file.write("Election Results\n")

        file.write("------------------\n")

        print("------------------")

        print("Election Results")

        print("------------------")


        # The total number of votes cast:

        ballot_count = [] # Declare a ballot count list

        for row in election_data:
            ballot_count.append(row[0]) # Add each ballot count to the list

        total_votes = len(ballot_count) # Assign the length of the list to a variable to use later
         
        file.write(f"Total votes: {total_votes}\n")

        print(f"Total votes: {total_votes}")

        file.write("------------------\n")

        print("------------------")

        csvfile.seek(0) # Reset the file pointer
        next(election_data) # Skip the header row again

        for row in election_data:

            candidate_name = row[2] # Declare a candidate name variable to the candidate column

            if candidate_name in candidate_data: # Check if the candidate is in the dictionary
                candidate_data[candidate_name] += 1 # If they are, then increase their vote count by one
            else:
                candidate_data[candidate_name] = 1 # If they aren't, add them as a key and then start them off with a vote count of one

        for candidate, votes in candidate_data.items(): # Loop through the key value pairs
            percentage = (votes / total_votes) * 100 # Calculate percentage 
            percentage_rounded = round(percentage, 3) # Round the percentage to the required decimal places
            file.write(f"{candidate}: {percentage_rounded}% ({votes})\n")
            print(f"{candidate}: {percentage_rounded}% ({votes})")

        file.write("------------------\n")

        print("------------------")
    
        max_votes = max(candidate_data.values()) # Declare a variable for max votes and perform the max function. We only want to calculate the vote count, so we use .values()
        for candidate, votes in candidate_data.items(): # We use .items() to loop through the values and their keys
            if votes == max_votes: # If the total number of votes for a candidate matches the calculated max vote then ...
                file.write(f"Winner: {candidate}\n") # Declare the winner
                print(f"Winner: {candidate}")

        file.write("------------------\n")

        print("------------------")



