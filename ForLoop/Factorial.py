#7)Write a program to print all factors of a number
Num=int(input('Enter the number to find Factorial :'))
for item in range(1, Num + 1):
   if Num % item == 0:
	   print(f'{item}, ',end=(''))
print()