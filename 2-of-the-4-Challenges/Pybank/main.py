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
    max_month = None
    loss_month = None


   
   #nested for loop to iterate the values in revenues within the csv list iteration
    #for row in csvlist:
        #for i in range(len(revenues)-1):
            #if revenues[i+1] - revenues[i] == max_change:
                #max_month = row[0]
    
    #for row in csvlist:
        # for i in range(len(revenues)-1):
            #if revenues[i+1] - revenues[i] == big_loss:
                #print(revenues[i+1] - revenues[i])
                #loss_month = row[0]
   
    # external rev value, maybe none to start
    #for row in csvlist:
        # if none
            # set external revenue val
            # skip rest of loop, go to next iteration
        # if diff == big loss
            # do stuff
        # store current rev val in external rev val
    
#check to see if variable is done
    
    initial_val = None
    for row in csvlist:
        if initial_val is None:
            initial_val = int(row[1])
            print(initial_val)
            continue
        if int(row[1]) - initial_val == big_loss:
            loss_month = row[0]
        intial_val = int(row[1])

    initial_val2 = None
    for row in csvlist:
        if initial_val2 is None:
            initial_val2 = int(row[1])
            continue
        if int(row[1]) - initial_val == max_change:
            max_month = row[0]
            intial_val = int(row[1])
    
    print(loss_month)
    print(max_month)
        

            
    

    
   

    #print all values required
    #print(len(dates))
    #print(mean(revchange))
    #print(f"The biggest loss {big_loss}")
    #print(max_month)
    #print(loss_month)
    #print(max_change)
   #
    

 

  
        






    














