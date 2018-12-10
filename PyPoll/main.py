import os
import csv



PyPollcsv = os.path.join("Pypoll.csv")

#Set Variables and Lists

count = 0
canlist = []
unique_can = []
v_count = []
v_percent = []

#Open CSV file
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#Count the variables in the csv file and add it to total count this is the total votes, add row two to canlist to get the canidates in a list  
    for row in csvreader:
        
        count = count + 1
        
        canlist.append(row[2])
# Make the varables for the math then put the varibles in the formula 
# set = makes a unique set and sorted sorts them alphabetically unique can will now have each canidate once 
    for x in sorted(set(canlist)):
        unique_can.append(x)
        
        y = canlist.count(x) #Set the variable to count the amount of variables in canlist
        v_count.append(y)   #Add this to vote count for each canidate and make y the total votes for a canidate
        
        z = (y/count)*100     #make vote percenteage 
        v_percent.append(z)   
      
    winning_vote_count = max(v_count)
    winner = unique_can[v_count.index(winning_vote_count)]
    
#Get printing
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_can)):
            print(unique_can[i] + ": " + str(round(v_percent[i])) +"% (" + str(v_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


# Could not figure out how to print results to a new file. I do not beleive we went over this in class. Ask TA's for help as this is probably important.
# Ther is probably a less loop instensive way of doing this with dictionaries but I couldn't figure it out. Would probably make code more efficient.