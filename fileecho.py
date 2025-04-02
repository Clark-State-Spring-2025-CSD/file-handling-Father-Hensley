#Read in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.
curFile = open("echo.txt") #Imports from text file
#curLine = curFile.readline() #Reads the first line
#curLine = curFile.read() #Reads entire file
for curLine in curFile: #Creates a loop checing each line in the file
    print(curLine) #Prints echo.txt in the terminal

curFile.close() #Closes text file

#print(curLine) #Prints echo.txt in the terminal
