'''Get the time'''
import datetime
THE_TIME = datetime.datetime.now()
print("Current date and time: ")
print(THE_TIME.strftime("%A, %B %d, %Y at %I:%M:%S %p"))
