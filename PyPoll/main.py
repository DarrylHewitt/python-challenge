import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:

    election_data = csv.reader(csvfile, delimiter=',')

    next(election_data)

    print("Election Results")

    print("------------------")

    ballot_count = []

    for ballot in election_data:
         ballot_count.append(ballot[0])

    print(f"Total votes:", (len(ballot_count)))

    print("------------------")