import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')


with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    rows = []
    totalnet = 0
    months=[]
    pl=[]
    change = []
    
    totalchange = 0

    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            rows.append(row)

    totalmonths = len(rows)
    for i in rows:
        totalnet = totalnet + int(i[1])
        pl.append(int(i[1]))
        months.append(i[0])

    plmonths = months[1:]

    for i in range(0,len(pl)-1):
        diff = int(pl[i+1])-int(pl[i])
        change.append(diff)
    
    months_change = list(zip(plmonths,change))
    
    for i in change:
        totalchange = totalchange + i

    avgmonthlychange = round((totalchange/(totalmonths-1)),2)
    
    greatestincrease = max(change)
    greatestdecrease = min(change)

    for i in months_change:
        if greatestincrease == i[1]:
            grtinc="Greatest Increase in Profits: "+ i[0] + " ($" + str(i[1]) + ")"
        if greatestdecrease ==i[1]:
            grtdec="Greatest Decrease in Profits: "+ i[0] + " ($" + str(i[1]) + ")"    
    
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${totalnet}")
    print(f"Average Change: ${avgmonthlychange}")
    print(grtinc)
    print(grtdec)

  
    

