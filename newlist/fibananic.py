#2)Write a Python program to get the Fibonacci series between 0 to 50.
intputNum = int(input('Enter the number upto which u want to print Fibonanic :'))
firstNum=0
secondNum=0
result=1
for item in range(intputNum):
	firstNum=secondNum
	secondNum=result
	result=firstNum+secondNum
	print(firstNum)
	if (secondNum>=intputNum):
		break