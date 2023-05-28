import csv
# Open the CSV file using csv.reader()
with open('Resources/budget_data.csv') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Convert the data to integers
    data = [[row[0], int(row[1])] for row in reader]

# Calculate the total months
total_months = len(data)

# Calculate the net total
net_total = sum(row[1] for row in data)

print(data)

# Create an empty list to store the changes in "Profit/Losses"
changes = []
# Loop through the data and calculate the changes in "Profit/Losses" between each cell over the entire period
for i in range(total_months - 1):
    # Calculate the change using subtraction
    change = data[i+1][1] - data[i][1]
    # Append the change to the empty list
    changes.append(change)
# Calculate the average of those changes
average_change = sum(changes) / len(changes)

# Calculate the greatest increase and decrease in profits/losses
max_increase = max(changes)
max_increase_date = data[changes.index(max_increase) + 1][0]
max_decrease = min(changes)
max_decrease_date = data[changes.index(max_decrease) + 1][0]
# Calculate the average change by dividing the net total by the total months
average_change = net_total / total_months
# Print the results using formatted strings and line breaks
print(f'Financial Analysis')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')

# Open a text file for writing
with open("PyBank/analysis/analysis.txt", "w") as txtfile:
    # Write the results using formatted strings and line breaks
    txtfile.write(f'Financial Analysis\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${net_total}\n')
    txtfile.write(f'Average Change: ${average_change:.2f}\n')
    txtfile.write(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})\n')
    txtfile.write(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n')



