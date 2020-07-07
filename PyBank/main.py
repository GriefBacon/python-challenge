# Task: create python script to analyze records and calculate the following
    # Total number of months
    # Net total of "profit/losses" over total period
    # Average of changes in "profit/losses" over total period
    # Greatest increase in profits (date & amount) over total period
    # Greatest decrease in losses (date & amount) over total period

# import OS functions

import os

# import csv functions and file

import csv
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# define the variables
months = []
profit_or_loss_change = []

total_months = 0
total_profit = 0
previous_month_profit = 0
current_month_profit = 0
profit_change = 0

# open & read csv
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # read header
    csv_header = next(csvfile)

    # read through rows
    for row in csv_reader:
        # count months
        total_months += 1

        # total "profit/losses" over total period
        current_month_profit = int(row[1])
        total_profit += current_month_profit
        if (total_months == 1):
            previous_month_profit = current_month_profit
            continue
        else:

            # show change in profit
            profit_change = current_month_profit - previous_month_profit

            # append month to months[]
            months.append(row[0])

            # append profit change to profit_or_loss_change
            profit_change.append(profit_or_loss_change)

            # make current month previous month for next loop
            previous_month_profit = current_month_profit

    # make sum & average of changes
    sum_profit = sum(profit_or_loss_change)
    average_profit = round(sum_profit/(months - 1), 2)

    # show highest and losest profit changes in over total period
    highest_change = max(profit_or_loss_change)
    lowest_change = min(profit_or_loss_change)

    # show row for highest and lowest changes
    highest_month = profit_or_loss_change.index(highest_change)
    lowest_month = profit_or_loss_change.index(lowest_change)

    # give best and worst month
    best_month = months[highest_month]
    worst_month = months[lowest_month]

# print out summary
print("------------------------------------")
print("-------CSV Financial Analysis-------")
print("------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit: ${total_profit}")
print(f"Average profit change: ${average_profit}")
print(f"Greatest increase in profit: {best_month} (${highest_change})")
print(f"Greatest decrease in profit: {worst_month} (${lowest_change})")

# export to text file

export_file = os.path.join("analysis", "output_data.txt")
with open(export_file, "w") as output_file:

    output_file.write("------------------------------------")
    output_file.write("-------CSV Financial Analysis-------")
    output_file.write("------------------------------------")
    output_file.write(f"Total Months: {total_months}")
    output_file.write(f"Total Profit: ${total_profit}")
    output_file.write(f"Average Change: ${average_profit}")
    output_file.write(f"Greatest increase in profit: {best_month} (${highest_change})")
    output_file.write(f"Greatest decrease in profit: {worst_month} (${lowest_change})")