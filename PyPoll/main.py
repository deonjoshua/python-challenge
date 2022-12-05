import os
import csv

read_path = os.path.join('Resources', 'election_data.csv')
write_path = os.path.join('analysis', 'results.txt')

total_votes = 0
candidate_options = []
candidate_votes = {}
# open election_data.csv file
with open(read_path, 'r', encoding='utf') as readfile:
    # read file
    csv_reader = csv.reader(readfile, delimiter=',')
    # skip header row
    csv_header = next(csv_reader)
    # loop over data
    for row in csv_reader:
        # find total votes
        total_votes += 1
        # store candidate_name on each iteration
        candidate_name = row[2]
        # check if candidate_name is NOT in candidate_options list and append name to list and set vote counter to 0
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # find total votes per candidate by adding 1 to the candidate_name keys in candidate_votes dictionary on each iteration
        candidate_votes[candidate_name] += 1
# create a list of total votes per candidate
values_list = list(candidate_votes.values())
# create a list of candidate names
keys_list = list(candidate_votes.keys())
# find percentage of total votes per candidate
percentage1 = round(values_list[0]/total_votes*100,3)
percentage2 = round(values_list[1]/total_votes*100,3)
percentage3 = round(values_list[2]/total_votes*100,3)
# find index of highest total votes
winner_index = values_list.index(max(values_list))
# find winning candidate using above index
winner = keys_list[winner_index]
# print results to terminal
print('Election Results\n')
print('--------------------------\n')
print(f'Total Votes: {total_votes}\n')
print('--------------------------\n')
print(f'{keys_list[0]}: {percentage1}% ({values_list[0]})\n')
print(f'{keys_list[1]}: {percentage2}% ({values_list[1]})\n')
print(f'{keys_list[2]}: {percentage3}% ({values_list[2]})\n')
print('--------------------------\n')
print(f'Winner: {winner}\n')
print('--------------------------\n')
# open results.txt file
with open(write_path, 'w', encoding='utf') as writefile:
    results = ['Election Results\n',
                '--------------------------\n',
                f'Total Votes: {total_votes}\n',
                '--------------------------\n',
                f'{keys_list[0]}: {percentage1}% ({values_list[0]})\n',
                f'{keys_list[1]}: {percentage2}% ({values_list[1]})\n',
                f'{keys_list[2]}: {percentage3}% ({values_list[2]})\n',
                '--------------------------\n',
                f'Winner: {winner}\n',
                '--------------------------\n']
    # write results to file
    writefile.writelines(results)