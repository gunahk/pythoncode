from datetime import date

recentYear  = int(input('Enter the year of recent in formate (YYYY)	: '))
recentMonth = int(input('Enter the month of recent in formate (MM)	: '))
recentDate  = int(input('Enter the date of recent in formate (DD)	: '))

oldYear     = int(input('Enter the year of old in formate (YYYY)		: '))
oldMonth    = int(input('Enter the month of old in formate (MM) 		: '))
oldDate     = int(input('Enter the date of old in formate (DD) 		: '))

greatYear = date(recentYear,recentMonth,recentDate)
lessYear = date(oldYear,oldDate,oldDate)
Result = greatYear - lessYear
print(f'Number of days is {Result.days}')