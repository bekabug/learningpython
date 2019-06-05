'''write a program that
1. generates a random list of intergers,
2. requests user input of a list of intergers,
3. compares the lists and,
4. outputs the similar numbers in the 2 lists'''

import random
RAND_INT = random.sample(range(1, 100), 8)
USER_NUM = input('Hi! Give me 8 random numbers separated by commas: ')
USER_INT = USER_NUM.split(',')
USER_INT = [int(x) for x in USER_NUM]
print('My numbers are', RAND_INT)
print(USER_INT)
MATCHES = set(RAND_INT) & set(USER_INT)
print("Our common numbers are", MATCHES)
