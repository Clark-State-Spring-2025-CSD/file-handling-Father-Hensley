#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

f = open("numbers.txt", "r") #Imports from text file
numbers = [int(line.strip()) for line in f] #Fuction that calls for a list and strips 
#whitespace for ease of reading

count = len(numbers) #How many entries
total = sum(numbers) #All added together
average = (total / count) #Just the average
highest = max(numbers) #Finds the largest number
lowest = min(numbers) #Finds the smallest number
#Print statements answering in the order listed above
print("Count: ", count)
print("Total: ", total)
print("Average: ", average)
print("Highest: ", highest)
print("Lowest: ", lowest)
f.close() #Closes the text file