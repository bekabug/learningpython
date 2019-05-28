'''print the number of years to your 100th birthday'''
import datetime
THE_DATE = datetime.datetime.today()
THIS_YEAR = int(THE_DATE.year)
BIRTH_YEAR = int(input('What year were you born: '))
AGE = THIS_YEAR - BIRTH_YEAR
YEARSTO100 = 100 - AGE

print('You will be', AGE, 'this year')
print('You will be 100 in', YEARSTO100, 'years')

print('In', YEARSTO100, 'years, the year will be', BIRTH_YEAR + 100)
