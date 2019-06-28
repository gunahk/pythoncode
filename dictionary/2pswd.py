intStr= input('Enter the password :')
print(f'Enter password length is {len(intStr)}')
if (len(intStr) <= 6 and  len(intStr) >= 16 ) :
	print('Enter password length is notfine')
elif (intStr != [a-z]):
	print('Enter password atleast one lower case Alphabet ')
elif (intStr != [A-Z]):
	print('Enter password atleast one upper case Alphabet ')
elif (intStr != [0-9]):
	print('Enter password atleast one digit ')
else:
	print('Valid password')
