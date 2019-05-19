InputString=input('Enter the string:')
if(len(InputString)>=3):
	if(InputString[-3:]=='ing'):
		print('The new string is',InputString+'ly')
	else:
		print('The new string is ',InputString+'ing')
else:
	print('no change in string ',InputString)
