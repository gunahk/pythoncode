heightFeet= input('Enter the height (in feet.inches) :')
height_Feet_NonInteger = heightFeet.split('.')
heightFI = [int(i) for i in height_Feet_NonInteger]

heightFI[0] = heightFI[0] * 12
heightFI[1] =  heightFI[1] * 2.54
print(f'Height in Centi Meter is {sum(heightFI)}' )