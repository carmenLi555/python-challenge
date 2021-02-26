import os 
import csv

pollfile = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv") 

# create a list for both voter and who they vote for 
votes = []
voteFor = []

with open(pollfile,'r') as file:
    reader = csv.reader(file)
    next(reader)
    
    # add the row into the lists 
    for row in reader:
        votes.append(row[0])
        voteFor.append(row[2])

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(votes)}")
print("-------------------------")


# create a list for candidates into classes 
#  get a list of distinct values of candidates in alphabetic order by using sort()
candidates = list(set(voteFor))
candidates.sort()

# get a vote count for each candidate.
candVotes = []
for cand in candidates:
    candVotes.append(voteFor.count(cand))

for i in range(len(candidates)):
    print(f"{candidates[i]}: {'{:.2%}'.format(candVotes[i]/len(voteFor))} ({candVotes[i]})")

print("-------------------------")
print(f"Winner: {candidates[candVotes.index(max(candVotes))]}")
print("-------------------------\n")

 # output to a text file

file = open("analysis/output.txt","w")

file.write("Election Results" + "\n")

file.write("...................................................................................." + "\n")

file.write(f"Total Votes: {len(votes)}" + "\n")

file.write("...................................................................................." + "\n")

file.write(f"{candidates[1]}: {'{:.2%}'.format(candVotes[1]/len(voteFor))} ({candVotes[1]})" + "\n")

file.write(f"{candidates[0]}: {'{:.2%}'.format(candVotes[0]/len(voteFor))} ({candVotes[0]})" + "\n")

file.write(f"{candidates[2]}: {'{:.2%}'.format(candVotes[2]/len(voteFor))} ({candVotes[2]})" + "\n")

file.write(f"{candidates[3]}: {'{:.2%}'.format(candVotes[3]/len(voteFor))} ({candVotes[3]})" + "\n")


file.write("...................................................................................." + "\n")

file.write(f"Winner: {candidates[candVotes.index(max(candVotes))]}" + "\n")

file.write("...................................................................................." + "\n")

file.close()
