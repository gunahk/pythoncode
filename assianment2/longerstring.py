FirstString=input('Enter the 1st string:')
SecndString=input('Enter the 2nd string:')
if (len(FirstString) > len(SecndString)):
	print(f'{FirstString} is longest string ')
elif(len(SecndString) > len(FirstString)):
	print(f'{SecndString} is longest string ')
else:
	print(f'{FirstString} and {SecndString} are long string')
