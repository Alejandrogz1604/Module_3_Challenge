#The following code imports the necessary modules for this script.

import csv
import os

#The following code declares a variable which will store our csv file.


election_dataset = os.path.join('..', 'Resources', 'election_data.csv')

#This empty list will contain every individual ballot ID.

ballotID_list = []

#This empty list will contain every individual county.

county_list = []

#This empty list will contain the candidate associated with each individual vote.

candidate_list = []

#This empty list will contain each candidate included in the election.

individual_candidate_list=[]

#This empty list will contain the percentage of the votes that each candidate has secured.

individual_candidate_percent = []

#This empty list will contain the number of votes that each candidate has secured.

individual_candidate_votes = []

##The following block of code will read the CSV file, and append each value in the first column to their corresponding list.

with open(election_dataset, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        ballotID_list.append(int(row[0]))
        county_list.append(row[1])
        candidate_list.append(row[2])
        
#The following loop will append each candidate name based on the following conditions:
#1. Only append a candidate name if it is not equal to the name in the following cell.
#2. Only append a candidate name if it has not already been stored in the lsit.

#These conditions allow us to obtain each candidate name once, and would do so for any amount of candidates.
        
for i in range(len(candidate_list)-1):
    
    if candidate_list[i] != candidate_list[i+1] and candidate_list[i] not in individual_candidate_list:
        individual_candidate_list.append(candidate_list[i])
        
#The following method will convert a numeric value to a percentage with three decimal values.
        
def to_percent (numeric_value):
    numeric_value = float(numeric_value)
    numeric_value = "{:.3%}".format(numeric_value) 
    return numeric_value

#The following code is declaring a variable which stores the total amount of votes.
#The total amount of votes coincides with the length of our ballot ID list.

vote_count = len(ballotID_list)

#The following code involves a nested loop.

#The outer loop will iterate through each individual candidate, and initialize our individual candidate vote varialble to 0.

#The inner loop will add a vote to the counter for each candidate if the ballot coincides with their name.

#This is achieved by iterating through our full candidate vote list, and comparing it to the names of each individual candidate.

#Once our inner loop has iterated, it will store the total votes the corresponding candidate.

#The outer loop will then use the candidate total vote count to calculate their percentage of the total votes.

#Finally, the loop will append their vote percentage, and total votes to their corresponding lists.

for i in range(len(individual_candidate_list)):
    
    individual_vote_count = 0
    
    for j in range(len(candidate_list)):
        
        if individual_candidate_list[i] == candidate_list[j]:
            
            individual_vote_count += 1
            
    candidate_percentage = individual_vote_count/vote_count
            
    individual_candidate_percent.append(to_percent(candidate_percentage))
    individual_candidate_votes.append(individual_vote_count) 
    
#The following code will obtain the candidate with the maximum votes using the "max" function on our individual vote list.

#Then, we wil obtain the index for this maximum vote value.

#Finally, we will obtain the value from this index in the individual candidate list, therefore storing the election winner.
    
candidate_winner = individual_candidate_list[individual_candidate_votes.index(max(individual_candidate_votes))]

#The following statements will print our analysis to the console.

print("Election Results")
print("\n")
print("-" * 30)
print("\n")
print(f"Total Votes: {vote_count}")
print("\n")
print("-" * 30)
print("\n")
print(f"{individual_candidate_list[0]}: {individual_candidate_percent[0]} ({individual_candidate_votes[0]})")
print("\n")
print(f"{individual_candidate_list[1]}: {individual_candidate_percent[1]} ({individual_candidate_votes[1]})")
print("\n")
print(f"{individual_candidate_list[2]}: {individual_candidate_percent[2]} ({individual_candidate_votes[2]})")    
print("\n")
print("-" * 30)
print("\n")
print(f"Winner: {candidate_winner}")

#The following code declares a variable which will store the path of the text file that we will be outputting our analysis to.
#The "with" code block will allow us to edit the above mentioned text file, due to the 'w' (write) indication.
#The write function will output our script to the specified text file.

election_analysis = os.path.join('..', 'election_analysis', 'election_analysis_summary.txt')

with open(election_analysis, 'w') as txt_file:
  
   txt_file.write("Election Results")
   txt_file.write("\n")
   txt_file.write("-" * 30)
   txt_file.write("\n")
   txt_file.write(f"Total Votes: {vote_count}")
   txt_file.write("\n")
   txt_file.write("-" * 30)
   txt_file.write("\n")
   txt_file.write(f"{individual_candidate_list[0]}: {individual_candidate_percent[0]} ({individual_candidate_votes[0]})")
   txt_file.write("\n")
   txt_file.write(f"{individual_candidate_list[1]}: {individual_candidate_percent[1]} ({individual_candidate_votes[1]})")
   txt_file.write("\n")
   txt_file.write(f"{individual_candidate_list[2]}: {individual_candidate_percent[2]} ({individual_candidate_votes[2]})")    
   txt_file.write("\n")
   txt_file.write("-" * 30)
   txt_file.write("\n")
   txt_file.write(f"Winner: {candidate_winner}")
   
 


    

            
            
    
   
   
    
    
        