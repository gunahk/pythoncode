#check a list is empty or not.

inputString = input('Enter the  item (by comma(,)):')

if (len(inputString) == 0 ):
	print('There is no item to display')
else:
	inputSplint = inputString.split(',')
	print(f'Entered list is {inputSplint}')