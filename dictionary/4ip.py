inpIP = input('Enter the ip addres (in formate 255.255.255.255): ')
splitIP = inpIP.split('.')
intIP = [ int(item)  for item in splitIP ]
if ( intIP[0] >= 256 ):
	print('This is invalid IP')
elif ( intIP[1] >= 256 ):
	print('This is invalid IP')
elif ( intIP[2] >= 256 ):
	print('This is invalid IP')
elif ( intIP[3] >= 256 ):
	print('This is invalid IP')
else :
	print('This is valid IP')