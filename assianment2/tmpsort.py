FirstNum=input('Enter the 1st ')
SecondNum=input('Enter the 2nd ')
ThirdNum=input('Enter the 3rd ')
if(FirstNum>SecondNum) :
	temp=FirstNum
	FirstNum=SecondNum
	SecondNum=temp
if(SecondNum>ThirdNum) :
	temp=SecondNum
	SecondNum=ThirdNum
	ThirdNum=temp
if(FirstNum>SecondNum) :
	temp=FirstNum
	FirstNum=SecondNum
	SecondNum=temp
print('Sorted Number is',FirstNum,SecondNum,ThirdNum)
