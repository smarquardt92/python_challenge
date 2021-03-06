import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
output_file = "Resources/budget_analysis.txt"

months = 0
total_revenue = 0

prev_rev = 0
change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue_changes = []

# Read Files
with open(csvpath) as revenue_data:
    reader = csv.DictReader(revenue_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        months = months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        # print(row)

        # Keep track of changes
        change = int(row["Profit/Losses"]) - prev_rev
        # print(revenue_change)

        # Reset the value of prev_revenue to the row I completed my analysis
        prev_rev = int(row["Profit/Losses"])
        # print(prev_revenue)

        # Determine the greatest increase
        if (change > greatest_increase[1]):
            greatest_increase[1] = change
            greatest_increase[0] = row["Date"]

        if (change < greatest_decrease[1]):
            greatest_decrease[1] = change
            greatest_decrease[0] = row["Date"]

        # Add to the revenue_changes list
        revenue_changes.append(int(row["Profit/Losses"]))

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    
    # Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: ", str(months))
    print("Total Revenue: $", str(total_revenue))
    print("Average Change: $", str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: ", str(greatest_increase[0]), " ($",  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: ", str(greatest_decrease[0]), " ($",  str(greatest_decrease[1]) + ")")
    

    with open(output_file, "w") as txt_file:
        txt_file.write("Total Months: " + str(months))
        txt_file.write("\n")
        txt_file.write("Total Revenue: " + "$" + str(total_revenue))
        txt_file.write("\n")
        txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
        txt_file.write("\n")
        txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
        txt_file.write("\n")
        txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")