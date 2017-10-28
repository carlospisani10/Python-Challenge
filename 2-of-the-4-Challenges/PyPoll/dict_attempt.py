#Pypoll

# Dependencies
import csv

# Files to load and output (Remember to change these)
file_to_load = "election_data_2.csv"
file_to_output = "computations/election_results.txt"

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as poll_data:
    reader = csv.DictReader(poll_data)

    #create an empy list to store your dictionary 
    dict_list = []

    #run for loop to append data into your dictionary
    for row in reader:
        dict_list.append(row)

    #sort list by 'Candidate'
    dict_list = sorted(dict_list, key=lambda k: k['Voter ID'])

    
    print(dict_list)
      