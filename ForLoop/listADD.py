#1)Write a Python program to insert a given string at the beginning of all items in a list.

inputString=input('Enter the string (by ","'') : ')
intputAdd = input('Enter the string which you want to add  : ')
inpSplitString=inputString.split(',')
listString = list(inpSplitString)
print('The output is :')
for item in  range(len(listString)):
	print(listString[item] + intputAdd)