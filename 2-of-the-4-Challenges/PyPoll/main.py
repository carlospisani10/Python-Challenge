#import os and write csv path
import os
from collections import Counter

csvpath = os.path.join("CSV", "election_data_2.csv") 

#Import csv
import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader delimiter and varaiable
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

   #lists
    voterid = []
    county = []
    candidate = []
    
    #run for loop for every row
    for dog in csvreader:
        voterid.append(dog[0])
        county.append(dog[1])
        candidate.append(dog[2])
    
    #find a unique set of canditates, and the total vote. Counter is a neat command
    can_set = set(candidate)    
    tot_vote = len(voterid)
    cnt = Counter(candidate)

    #create a list with the unique names
    names = []
    
    for row in can_set:  
        names.append(row)


    #Print the Total Votes

    print("Results for Election")
    print("Total number of votes:" + str(tot_vote))
    print(names)



    #create a loop that prints the vote count and vote percentage for each 
    print(tot_vote)
    print(names)
    print(cnt)
    
   
 
 

      

        
        

       
 