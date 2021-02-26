import os 
import csv 

budgetcsv = os.path.join("Resources", "budget_data.csv") 

with open (budgetcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header =next(csvfile)
    print(f"Header: {header}")

    # find net amount of profit and loss by creating a list 
    PandL = []
    months = []

    #read through each row of data after header by using append
    for rows in csvreader:
        PandL.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change by creating a list inside the loop 
    difference = []

    #Call len(obj) with obj as an iterable to return the number of items obj contains.
    # set 1 as the indext starts at 1 and stops at the len(PanL) - last row 
    for x in range(1, len(PandL)):
        difference.append((int(PandL[x]) - int(PandL[x-1])))
    
    # calculate average revenue change
    revenue_average = sum(difference) / len(difference)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(difference)
    # greatest decrease in revenue
    greatest_decrease = min(difference)


    # print the Results
    print("Financial Analysis")

    print("....................................................................................")

    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(PandL)))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[difference.index(max(difference))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[difference.index(min(difference))+1]) + " " + "$" + str(greatest_decrease))

# output to a text file

    file = open("analysis/output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(PandL)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[difference.index(max(difference))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[difference.index(min(difference))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()