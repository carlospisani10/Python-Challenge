#import os and write csv path
from statistics import mean
import os
csvpath = os.path.join("CSV", "budget_data_1.csv") 

#Improved Reading using CSV module
import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader delimiter and varaiable
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    csvlist = list(csvreader)

    #list creation, places to store csv "rows" (They are columns!)
    dates = []
    revenues = []

    #run for loop for every row
    for dog in csvlist:
        dates.append(dog[0])
        revenues.append(int(dog[1]))
    
    #create a list for revenue change
    revchange = []

    #run loop through revenues list to find the change revenues from month
    revchange = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
    
    #variables
    max_change = max(revchange)
    big_loss = min(revchange)
    max_date = None

    print(max_change)
    for r in csvlist::
        if r == max_change:
            max_date = i[0]

    print(max_date)
    print(len(dates))
    print(mean(revchange))
    print(max(revchange))
    print(min(revchange))
   
    

 



  
        






    














