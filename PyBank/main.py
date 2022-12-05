import os
import csv

read_path = os.path.join('Resources', 'budget_data.csv')
write_path = os.path.join('analysis', 'results.txt')

profit_loss = []
increase_decrease = {}
net_total = 0

# open budget_data.csv file
with open(read_path, 'r', encoding='utf') as readfile:
    # read file
    csv_reader = csv.reader(readfile, delimiter=',')
    # skip header row
    csv_header = next(csv_reader)
    # loop over data
    for data in csv_reader:
        # find total profit/loss
        net_total += int(data[1])
        # add data to empty_list
        profit_loss.append(data)
# find total months using len function
total_months = len(profit_loss)
# find change by subtracting the first value from the last value in empty_list
change = int(profit_loss[-1][1])-int(profit_loss[0][1])
# find average change and round to 2 decimal places
average_change = round(change/(total_months-1), 2)

for n in range(total_months-1):
    # populate dict with month as key and increase/decrease in P/L as values
    increase_decrease[profit_loss[n+1][0]] = int(profit_loss[n+1][1])-int(profit_loss[n][1])
# find max value in dict        
max_value = max(increase_decrease.values())
# find key of max value in dict
max_key = max(increase_decrease, key=increase_decrease.get)
# find min value in dict
min_value = min(increase_decrease.values())
# find key of min value in dict
min_key = min(increase_decrease, key=increase_decrease.get)
# print results to terminal
print('Financial Analysis\n')
print('-----------------------------\n')
print(f'Total Months: {total_months}\n')
print(f'Total: ${net_total}\n')
print(f'Average Change: ${average_change}\n')
print(f'Greatest Increase in Profits: {max_key} ({max_value})\n')
print(f'Greatest Decrease in Profits: {min_key} ({min_value})')
# open results.txt file
with open(write_path, 'w', encoding='utf') as writefile:
    results = ['Financial Analysis\n',
                '-----------------------------\n',
                f'Total Months: {total_months}\n',
                f'Total: ${net_total}\n',
                f'Average Change: ${average_change}\n',
                f'Greatest Increase in Profits: {max_key} ({max_value})\n',
                f'Greatest Decrease in Profits: {min_key} ({min_value})']
    # write results to file
    writefile.writelines(results)
