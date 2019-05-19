FirstNum=input('Enter the 1st num : ')
SecondNum=input('Enter the 2nd num : ')
ThirdNum=input('Enter the 3rd num : ')
if (FirstNum>SecondNum):
	if(ThirdNum>FirstNum):
		print(f"order is {SecondNum},{FirstNum}.{ThirdNum}")
	elif(SecondNum>ThirdNum):
		print(f"order is {ThirdNum},{SecondNum}.{FirstNum}")
	else:
		print(f"order is {SecondNum},{ThirdNum}.{FirstNum}")
elif(FirstNum<SecondNum):
	if(ThirdNum>SecondNum):
		print(f"order is {FirstNum},{SecondNum}.{ThirdNum}")
	elif(ThirdNum<FirstNum):
		print(f"order is {ThirdNum},{FirstNum}.{SecondNum}")
	else:
		print(f"order is {FirstNum},{ThirdNum}.{SecondNum}")
elif(FirstNum==SecondNum):
	if(FirstNum==ThirdNum):
		print(f"order is {SecondNum},{FirstNum}.{ThirdNum}")
	elif(ThirdNum>FirstNum):
		print(f"order is {SecondNum},{FirstNum}.{ThirdNum}")
	elif(ThirdNum<FirstNum):
		print(f"order is {ThirdNum},{FirstNum}.{SecondNum}")
