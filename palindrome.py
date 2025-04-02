#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

f = open("words.txt", "r") #Imports from text file
words = [line.strip() for line in f] #Fuction that calls for a list and strips 
#whitespace for ease of reading
def palindrome(word: str) -> bool: #Def fuction, checking if word is palindrome
    #Removes non-alphabetical characters and makes all lowercase
    cleaned_text = ''.join(char.lower() for char in word if char.isalpha())
    return cleaned_text == cleaned_text[::-1] #Checks if matching forward and reverse
    #[::-1] reverses the string

count = 0 #Starting count at zero

for word in words: #Checks the list to count
    if palindrome(word): #Runs def fuction, checking each word
        count += 1 #Adds one when found

total = count #Storing the count

print(f"There are {total} palindromes in the list.") #Display result
f.close() #Closing file after running