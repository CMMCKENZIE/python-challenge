import csv
import os

filename = os.path.join("Resources/election_data.csv")
fileresult = os.path.join("Resources/election_analysis.txt")

total_votes = 0

options = []
candidate_votes = {}

winner_candidate = ""
winning_count = 0

with open(filename) as election_data:
    reader = csv.reader(election_data)
   
    header = next(reader)
   
    for row in reader:
       
        total_votes = total_votes + 1
       
        candidate_name = row[2]
       
        if candidate_name not in options:
           
            options.append(candidate_name)
          
            candidate_votes[candidate_name] = 0
       
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
   
    for candidate in candidate_votes:
       
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
       
        if (votes > winning_count):
            winning_count = votes
            winner_candidate = candidate
       
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
       
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
   









