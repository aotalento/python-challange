# import dependants
import csv
import os

# add file path
BankData = os.path.join("budget_data.csv")

# Set list variables
Profits = []
MonthlyChange = []
Date = []

# Set variables to zero
MonthCount = 0
TotalProfits = 0
Change = 0
StartingProfit = 0

with open(BankData, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    
#    Count the months in the sheet 
    for row in csvreader:
        MonthCount = MonthCount + 1
        
#       Set the date column
        Date.append(row[0])

#     Set the profits column
        Profits.append(row[1])
    
#     Calculate total profits
        TotalProfits = TotalProfits + int(row[1])
    
#     Calculate average change in profits
        FinalProfit = int(row[1])
        Monthly_Change= FinalProfit - StartingProfit
        
        MonthlyChange.append(Monthly_Change)
        
        Change = Change + Monthly_Change
        StartingProfit = FinalProfit
        
        ProfitChanges = round((Change/MonthCount))
        
        GreatestIncrease = max(MonthlyChange)
        IncreaseDate = Date[MonthlyChange.index(GreatestIncrease)]
        GreatestLoss = min(MonthlyChange)
        LossDate = Date[MonthlyChange.index(GreatestLoss)]
        
        
    print("-----------------------------------------------")
    print("              Financial Analysis")
    print("-----------------------------------------------")
    print("Total Months: " + str(MonthCount))
    print("Total Profits: $" + str(TotalProfits))
    print("Average Profit Change: $" + str(ProfitChanges))
    print('Greatest Increase in Profits:' + str(IncreaseDate) +" ($" + str(GreatestIncrease) + ")")
    print('Greatest Loss in Profits:' + str(LossDate) + '($' + str(GreatestLoss) + ')')

    
with open('Financial_Analysis.txt', 'w') as text:
    text.write("-----------------------------------------------\n")
    text.write("              Financial Analysis" + "\n")
    text.write("-----------------------------------------------\n")
    text.write("Total Months: " + str(MonthCount) + "\n")
    text.write("Total Profits: $" + str(TotalProfits) + "\n")
    text.write("Average Profit Change: $" +str(ProfitChanges) + "\n")
    text.write('Greatest Increase in Profits:' + str(IncreaseDate) +" ($" + str(GreatestIncrease) + ")" + "\n")
    text.write('Greatest Loss in Profits:' + str(LossDate) + '($' + str(GreatestLoss) + ')' + "\n")