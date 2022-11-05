# import os module which allows for file path creation across operating systems
import os 

# import module to read csv files
import csv

# set path for file
budget_csv = os.path.join('Resources','budget_data.csv')

# open the csv file
with open(budget_csv, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # read the header row first 
    csv_header = next(csvreader)

    # declare variables and lists
    total_months = 0
    net_total = []
    monthly_change = []
    date = []

    
    # read each row of data after the header
    for row in csvreader:

        # count the months
        total_months += 1

        # add dates to list
        date.append(row[0])

        # add values from profits and losses to list
        net_total.append(int(row[1]))



    # loop through each row of profits and losses
    for i in range(len(net_total)-1):

        # get the difference between each row and add to list
        monthly_change.append(net_total[i+1]-net_total[i])

    # get greatest increase and decrease values from list
    greatest_increase = max(monthly_change)
    greatest_decrease = min(monthly_change)

    # get the matching month for the greatest increase and decrease values
    increase_month = date[monthly_change.index(greatest_increase)+1]
    decrease_month = date[monthly_change.index(greatest_decrease)+1]


# calculate and output results
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", total_months)
print("Total: $" + str(sum(net_total)))
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: " + str(increase_month) + " ($" + str(greatest_increase) + ")")
print(f"Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(greatest_decrease) + ")")

# set path for text file
financial_analysis = os.path.join('analysis','financial_analysis.txt')

# open and write results to text file
with open(financial_analysis,"w") as text:
    text.write("Financial Analysis")
    text.write("\n----------------------------")
    text.write("\nTotal Months: " + str(total_months))
    text.write("\nTotal: $" + str(sum(net_total)))
    text.write(f"\nAverage Change: $" + str(round(sum(monthly_change)/len(monthly_change),2)))
    text.write(f"\nGreatest Increase in Profits: " + str(increase_month) + " ($" + str(greatest_increase) + ")")
    text.write(f"\nGreatest Decrease in Profits: " + str(decrease_month) + " ($" + str(greatest_decrease) + ")")


