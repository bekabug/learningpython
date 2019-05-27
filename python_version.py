'''spit out the python version'''
import platform
THE_VERSION = platform.python_version()
print(THE_VERSION)
if THE_VERSION <= '3':
    print('uh oh. you\'re running', platform.python_version())
else:
    print('yay! you\'re running ', platform.python_version())
print('This requires Python3')
