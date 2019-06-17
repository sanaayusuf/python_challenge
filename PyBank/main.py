import csv

csvpath="./budget_data.csv"
with open (csvpath,"r") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    header=next(readCSV)
    dates = []
    profit_losses = []
    for row in readCSV:
        date = row[0]
        profit_loss= row[1]
        dates.append(date)
        profit_losses.append(float(profit_loss))

        
    print(len(dates))
    print(sum(profit_losses))