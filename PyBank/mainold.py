# initialize variables to hold integer, strings, lists
Tot_Month = 0
Tot_Profit_Loss = 0
Profit_Loss_Now = 0
Profit_Loss_Past = 0
Profit_Loss_Chg = 0
Delta_Profit = [[]]
Profit_Loss = [[]]
Month_Count = 0
ValueString = [[]]   # create empty string
Dictionary = {'Profit/Loss':[], 'Month_Count': 0, 'Delta_Profit': []}

# Import csv file
import csv

file_name = "Resources/budget_data.csv"

# Open the Budget_Data.csv
with open(file_name, newline='') as csvfile:
    csvreader = csv.reader(csvfile)    # Read each line of Data as row

    for row in csvreader:
        Date = row[0]   # first element is Date
        Profit_Loss_Now = int(row[1])   # Second element is Profit Loss now
        Tot_Month += 1   # third element is total months
        Delta_Profit = PL_Now - PL_Past # change in profit and loss each month
        #print(Date, ' Profit/Loss:',PL_Now, ' Month_Count:', Month_Count,' Delta_Profit:',Delta_Profit)  #Calculate change in Profit loss
        PL_Past = int(row[1])   # show me PL
    Profit_Loss.append(Profit_Loss)
    Month_Count.append(Month_Count)
    Delta_Profit.append(Delta_Profit)
    Max_P = max(Delta_Profit)
    Min_P = min(Delta_Profit)
    Sum_P = sum (Delta_Profit)
    Tot_Month = (Month_Count)


    print('Max Profit:  ', Max_P)           # Find greatest increase
    print('Min Profit:  ', Min_P)           # Find greatest decrease
    Avg_P = (Value / int(Tot_Month))        # Calculate average month to month change
    print('Value of Stock:  ', Value)

output_file = "Resources/budget_output.csv"
with open(output_file, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(Date + ',' + PL_Now + ',' + Tot_Month + ',' + PL_Chg)



