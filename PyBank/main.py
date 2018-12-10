import os
import csv
#Create the csv path
csvpath = os.path.join('Pybankresources.csv')
 



#open the csv path


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #convert CSV to variables? or is it something else? is it just a list? pretty sure dictionaries have multiple variables assigned to an element and this is just a list but Ask TA's about {} and [] and if these would be considered lists.
    profit = []
    date = []
    profit_change = []

    for row in csvreader:
        profit.append(float(row[1]))
        date.append(row[0])

    #Create the heading and print 
    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months:", len(date))
    print("Total Profit: $", sum(profit))

# create a new loop for the advanced stuff using the dictionaries(not by going to the csv file for every answer you idiot)
    for rows in range (1, len(profit)):   #WHY does it have to be a range here? also why does it have to be 1 instead of zero? Ask TA's 
        profit_change.append(profit[rows] - profit [rows-1]) #this loop will look at the difference between one line and the next. The -1 after rows looks at the one before the current element the loop is on. Then add the difference to the dictionary.
        # append does not sum variables like you thought it adds them to a list one row at a time. 
        #new variable created to figure out the average now that the difference dictionary is created we can work with it instead of the csv file directly (you idiot)
        avg_profit_change = sum(profit_change)/len(profit_change) #you need to remember to use variables, lists, dictionaries etc. more often.
        
        max_profit_change = max(profit_change) #study base functions more. flashcards or look up a quizlet. 

        min_profit_change = min(profit_change)

        #Now find using the max and min find the date associated with those rows and turn it into a new variable/string

        max_profit_change_date = str(date[profit_change.index(max(profit_change))]) #okay so this allows us to print the date of the max string by finding where in the date variable it matches the profit change and then specifically the max or min profit change. Ask TA's to eleborate on the uses of the .index 
        min_profit_change_date = str(date[profit_change.index(max(profit_change))])
# now bring it all together with print
    print("Average Profit Change: $", round(avg_profit_change))
    print("Greatest Increase in Profit:", max_profit_change_date,"($", max_profit_change,")")
    print("Greatest Decrease in Profit:", min_profit_change_date, "($", min_profit_change, ")")


    
   
