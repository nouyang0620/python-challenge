# import os module which allows for file path creation across operating systems
import os 

# import module to read csv files
import csv

# set path for file
elect_csv = os.path.join('Resources','election_data.csv')

# open the csv file
with open(elect_csv, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # read the header row first 
    csv_header = next(csvreader)

    # declare variables and lists
    total_votes = 0
    candidate_votes = []
    names = []
    vote_percentage = []
    vote_count = []

    # read each row of data after the header
    for row in csvreader:

        # count votes
        total_votes += 1

        # add candidate votes to list
        candidate_votes.append(row[2])
    
    # from the candidate_votes list
    for name in set(candidate_votes):

        # get the candidate names
        names.append(name)

        # count the votes for each candidate
        x = candidate_votes.count(name)
        vote_count.append(x)

        # get the percent of votes for each candidate
        y = (x/total_votes)*100
        vote_percentage.append(y)

    winner_count = max(vote_count)
    winner = name[vote_count.index(winner_count)]

# output results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")


