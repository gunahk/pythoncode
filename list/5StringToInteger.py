#parse a string to Float or Integer


input_Num= input('Enter the Numbers [0-9] (by comma(,)):')
input_Num_splint = input_Num.split(',')
print(f'Input in string is {input_Num_splint}') 

ResNum = [int(float(i)) for i in  input_Num_splint]

print(f'Input in integer is {ResNum}')