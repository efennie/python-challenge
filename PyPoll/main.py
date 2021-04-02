#import dependencies
import os
import csv

votes_cast = 0
all_candidates = set()
votes_for_khan = 0
votes_for_correy = 0  
votes_for_otooley = 0
votes_for_li = 0
compare_votes = []

#create path and import csv file and read the file
csvpath = os.path.join('PyPoll', 'Resources', 'Python_PyPoll_Resources_election_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 

#define and print headers
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#calculate the total number of votes cast
    for row in csvreader:
        votes_cast += 1
        previous_row = row[2]

#create a complete set of candidates who received votes
        all_candidates.add(row[2])
        
        #calculate the total number of votes candidate won
        if row[2] == "Khan":
            votes_for_khan += 1

        elif row[2] == "Correy":
            votes_for_correy += 1

        elif row[2] == "Li":
            votes_for_li += 1

        else:
            votes_for_otooley += 1

    print(votes_cast)
    print(all_candidates)
    print(f"Li: {votes_for_li}")
    print(f"Khan: {votes_for_khan}")
    print(f"O'Tooley: {votes_for_otooley}")
    print(f"Correy: {votes_for_correy}")

    #if previous_row in candidate_list != candidate_list:
    #candidate_list.add(previous_row)

#calculate the percentage of the total vote each candidate won
votes_li_dec = (votes_for_li) / (votes_cast)
votes_khan_dec = (votes_for_khan) / (votes_cast)
votes_otooley_dec = (votes_for_otooley) / (votes_cast)
votes_correy_dec = (votes_for_correy) / (votes_cast)

votes_li_percent = "{:.0%}".format(votes_li_dec)
votes_khan_percent = "{:.0%}".format(votes_khan_dec)
votes_otooley_percent = "{:.0%}".format(votes_otooley_dec)
votes_correy_percent = "{:.0%}".format(votes_correy_dec)

#determine the winner of the election based on popular vote 
# & print "Winner: " + their name
#compare_votes.append(votes_for_correy)
#print(compare_votes)

print("Election Results:")
print("---------------------")
print(f"Khan: {votes_khan_percent} ({votes_for_khan})")
print(f"Correy: {votes_correy_percent} ({votes_for_correy})")
print(f"Li: {votes_li_percent} ({votes_for_li})")
print(f"O'Tooley: {votes_otooley_percent} ({votes_for_otooley})")
print("---------------------")
print(f"Total votes cast: {votes_cast}")
print("---------------------")
#print(f"Winner: {}")