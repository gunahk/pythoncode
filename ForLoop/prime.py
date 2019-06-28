#6)Write a program to check if a number is prime number
inputNum=int(input('Enter the Number to check number is even or Not :'))
iteration = 1
for item in range(1,inputNum):
	if (inputNum%item == 0):
		iteration = iteration + 1	
if(iteration<=2):
	print(f'{inputNum} is Prime')
else:
	print(f'{inputNum} is  Not Prime')