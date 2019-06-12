import csv

import os

PollResultsCsv = os.path.join("election_data.csv")

TotalVotes = 0
Candidates = []
VotesEach = []
VotePercentage = []
EachCandidate = []

with open(PollResultsCsv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    
    for row in csvreader:
        TotalVotes = TotalVotes + 1
        Candidates.append(row[2])
        
        
    for x in set(Candidates):
        EachCandidate.append(x)
        y = Candidates.count(x)
        VotesEach.append(y)
        z = round((y/TotalVotes)*100, 3)
        VotePercentage.append(z)
        
    Winner = max(VotesEach)
    WinnerName = EachCandidate[VotesEach.index(Winner)]
    
    

print("Election Results")
print("-------------------------------")
print("Total Votes: " + str(TotalVotes))
for Each in range(len(EachCandidate)):
    print(EachCandidate[Each] + ": " + str(VotePercentage[Each]) +"% (" + str(VotesEach[Each])+ ")")
print("-------------------------------")
print("Winner:" + str(WinnerName))
print("-------------------------------")


with open("Results.txt", "w") as text:
    text.write("Election Results\n")
    text.write("-------------------------------\n")
    text.write("Total Votes: " + str(TotalVotes) + "\n")
    for Each in range(len(EachCandidate)):
        text.write(EachCandidate[Each] + ": " + str(VotePercentage[Each]) +"% (" + str(VotesEach[Each])+ ")\n")
    text.write("-------------------------------\n")
    text.write("Winner:" + str(WinnerName) + "\n")
    text.write("-------------------------------\n")