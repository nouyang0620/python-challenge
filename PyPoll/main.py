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
    winner_count = 0

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

    # get the highest vote count from list
    winner_count = max(vote_count)
    # get the winner name based on the winning count
    winner = names[vote_count.index(winner_count)]

# output results
print("\nElection Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
# print the name, vote percentage, and vote count for each candidate
for i in range(len(names)):
    print(names[i] + ": " + str(round(vote_percentage[i], 3)) + "% (" + str(vote_count[i]) + ")")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

# set path for text file
poll_analysis = os.path.join('analysis','poll_analysis.txt')

# open and write results to text file
with open(poll_analysis,"w") as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(total_votes))
    text.write("\n-------------------------\n")
    # write the name, vote percentage, and vote count for each candidate
    for i in range(len(names)):
        text.write(names[i] + ": " + str(round(vote_percentage[i], 3)) + "% (" + str(vote_count[i]) + ")\n")
    text.write("-------------------------\n")
    text.write("Winner: " + str(winner))
    text.write("\n-------------------------")
    

