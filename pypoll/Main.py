#Import dependants
import csv
import os

PollResultsCsv = os.path.join("election_data.csv")

# Define lists
TotalVotes = 0
Candidates = []
VotesEach = []
VotePercentage = []
EachCandidate = []

with open(PollResultsCsv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    
    #Loop through 
    for row in csvreader:
        TotalVotes = TotalVotes + 1
        Candidates.append(row[2])
        
    #Select out individual candidates    
    for i in set(Candidates):
        EachCandidate.append(i)
        #Count the number of times they come up
        j = Candidates.count(i)
        VotesEach.append(j)
        #Solve for vote percentage
        k = round((j/TotalVotes)*100, 3)
        VotePercentage.append(k)
        
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