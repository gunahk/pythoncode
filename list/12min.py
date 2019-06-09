input_Num = input('Enter the three Numbers (with comma(,)) : ')
input_Num_Split = input_Num.split(',')
inputNum = [int(i) for i in input_Num_Split]

print(f'Minimum of given Numbers is {min(inputNum)}')
