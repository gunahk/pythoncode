#4)Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for item in range(7):
	if(item%3 == 0 ):
		continue
	else:
		print(f'{item}')