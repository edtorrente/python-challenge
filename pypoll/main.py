# Import modules 
import os
import csv

"""Description: In this challenge, you are tasked with helping a small, rural town modernize its vote counting 
process. You will be give a set of poll data called election.csv. The dataset is composed of three columns: 
Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates 
each of the following:

Output:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.
"""

# set path and directory togerther along with data set located in Resources folder
election_data = os.path.join(os.getcwd(), 'Resources', 'election.csv')


# Create a function to calculate percentage of votes
def percentage (candidate, total_votes):
    return 100 * float(candidate)/float(total_votes)


def poll_results(data):
    # Define variables and all counter zeros.
    total_votes = 0; 
    khan = 0; 
    correy = 0; 
    li = 0; 
    otooley = 0; 
    vote_count = 0
    voter_id = [0]  
    candidate = [2]

    # Initiate loop for all variables, in this case, candidates.
    for _ in data:
        # Find total count of votes 
        total_votes = total_votes + 1
    
        # collecting votecounts per candidates.
        candidate = _[2]
        if candidate =="Khan":
           khan = khan + 1
        if candidate =="Correy":
           correy = correy + 1
        if candidate =="Li":
           li = li + 1
        if candidate =="O'Tooley":
           otooley = otooley + 1
                
        # Create a list 
        candidate_vote = {"Khan": khan,"Correy": correy,"Li" :li, "O'Tooley": otooley}
        
    # Find the winner 
    for candidate, name in candidate_vote.items():
        if name > vote_count:
            vote_count = name
            winner = candidate

                
    # Print the results       
    print(f'Election Results'+'\n')
    print(f'-------------------------------'+'\n')
    print(f'Total Votes: {total_votes}'+'\n')
    print(f'-------------------------------'+'\n')
    print(f'Khan: {percentage(khan,total_votes):.3f}%  ({khan})')
    print(f'Correy: {percentage(correy, total_votes):.3f}%  ({correy})')
    print(f'Li: {percentage(li, total_votes):.3f}%  ({li})')
    print(f'O\'Tooley: {percentage(otooley, total_votes):.3f}%  ({otooley})')
    print(f'--------------------------------'+'\n')
    print(f'Winner: {winner} '+'\n')
    print(f'--------------------------------'+'\n')    

    # Set the path for the new file 
    pypoll_output = os.path.join('Analysis', "election_results.txt")    
   
    # Write script to create new file with results 
    with open(pypoll_output, 'w') as new:
        new.write(f'Election Results'+'\n')
        new.write(f'-------------------------------'+'\n')
        new.write(f'Total Votes: {total_votes}'+'\n')
        new.write(f'-------------------------------'+'\n')
        new.write(f'Khan: {percentage(khan,total_votes):.3f}%  ({khan})')
        new.write(f'\nCorrey: {percentage(correy, total_votes):.3f}%  ({correy})')
        new.write(f'\nLi: {percentage(li, total_votes):.3f}%  ({li})')
        new.write(f'\nO\'Tooley: {percentage(otooley, total_votes):.3f}%  ({otooley})')
        new.write(f'\n--------------------------------'+'\n')
        new.write(f'Winner: {winner} '+'\n')
        new.write(f'--------------------------------'+'\n')   


with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    dataheader = next(csvfile)
    poll_results(csvreader)