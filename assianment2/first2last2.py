InputString=input('Enter the string: ')
if(len(InputString)>=2):
	print('the new string is',InputString[:2]+InputString[-2:])
else:
	print('empty string')
