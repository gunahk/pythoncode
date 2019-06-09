from datetime import date

greatYear = input('Enter the date of recent in formate (YYYY,MM,DD)')
lessYear  = input('Enter the date of old in formate (YYYY,MM,DD ): ')
greatYear = (int(item)  for item in greatYear)
greatYear = (int(item)  for item in lessYear)
print(greatYear)
greatYear = date(greatYear)
lessYear = date(lessYear)
Result = greatYear - lessYear
print('Number of days is {Result.days}')