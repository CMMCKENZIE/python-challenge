import csv
filename = "Resources/Budget_data.csv"
fields = []
rows = []
 
months = 0
previous_profit_loss=1088983
Total_change=0
greatest_change=0
smallest_change=0
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(int(row[1]))
        print(row[1])
        months = months + 1

        profit_loss= int(row[1])
        change=profit_loss -previous_profit_loss
        print(change)
        if change > greatest_change:
            greatest_change=change
        if change < smallest_change:
            smallest_change=change
        previous_profit_loss=profit_loss
        Total_change=Total_change + change
        
print("Total Months", months)
Total= sum(rows)
print("Total", Total)
print("Average change", Total_change/(months -1))
print("Greatest increase in profits", greatest_change)
print("Greatest decrease in profits", smallest_change)

