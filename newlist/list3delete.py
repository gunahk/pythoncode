#2)Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
inputStr=input('Enter the values with (space) : ')
inputSplit = inputStr.split(' ')
inputNum= [int(i) for i in inputSplit]
number=len(inputNum)
for item in range(number):
	inputNum.pop(2)
	print('After Remving third item',inputNum)
	if (len(inputNum) <= 3):
		break
for i in range(3):
	inputNum.pop(0)
	print('Removing first item',inputNum)


