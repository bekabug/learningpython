import datetime
d = datetime.datetime.today()
thisyear = int(d.year)
            
birthyear = int(input("What year were you born: "))
age = thisyear - birthyear
yearsto100 = 100 - age

print("You will be", age, "this year")
print("You will be 100 in", yearsto100, "years")

print("In", yearsto100, "years, the year will be", birthyear + 100)
