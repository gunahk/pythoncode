input_Time_String = input('Enter the Time in (HH : MM : SEC): ')
input_Time_Split = input_Time_String.split(':')
inputTime = [int(i) for i in input_Time_Split]

if((inputTime[0]>23) or (inputTime[1]>60)):
	print('Invalit input time')
else:
	inputTime[0] = inputTime[0] * 60 * 60
	inputTime[1] = inputTime[1] * 60
	print(f'The total time in seconds is {sum(inputTime)}')