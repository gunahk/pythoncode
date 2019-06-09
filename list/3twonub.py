my_input=input('enter the numbers that can store in the list  :')
my_list=my_input.split(',')
numlistNoInteger=list(my_list)
numList=[int(i) for i in numlistNoInteger]

if(( numList[0] == numList[1]) or ( numList[1] == numList[2] ) or (numList[0] == numList[2] )):
	print("Two numbers are equal ")

else:
	print("Sum of numbers is ",sum(numList))
