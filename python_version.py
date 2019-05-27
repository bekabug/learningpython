'''checks for Python3'''
import platform
THE_VERSION = platform.python_version()

if THE_VERSION <= '3':
    print('uh oh. you\'re running ' + THE_VERSION)
else:
    print('yay! you\'re running', THE_VERSION)
print('This requires Python3')
