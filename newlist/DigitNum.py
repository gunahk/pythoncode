#5)Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
InputNum=int(input('Enter the number to check every digit is even or Not :'))

firstNum=int(InputNum/100)
#print(firstNum)

temp=int(InputNum/10)
SecondNum=int(temp%10)
#print(SecondNum)

thirdNum=int(InputNum%10)
#print(thirdNum)


Num=[firstNum,SecondNum,thirdNum]

if (Num[0] % 2 == 0) :
	if (Num[1] % 2 == 0) :
		if (Num[2] % 2 == 0) :
			print('Even Number with Space is',Num)
		else:
			print(f'{Num[2]} is not Even')	
	else:
		print(f'{Num[1]} is not Even')
else:	
	print(f'{Num[0]} is not Even')
	
	


