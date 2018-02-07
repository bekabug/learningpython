x = int(input("Give me a number: "))
num = int(input("Give me another number: "))
check = int(input("Give me one more number: "))
y = x % 2
if y == 0:
    print("You get a cupcake!")
elif y !=  7:
    print("You get a smoothie!")
else:
    print("You get quiche!")
utensil = num % check
if utensil == 0:
    print("And you have to eat it with a straw!")
elif utensil == 3:
    print("And you have to eat it with a spoon!")
elif utensil == 9:
    print("And you have to eat it with a your hands!")
else:
    print("And you have to eat it with chopsticks!")
