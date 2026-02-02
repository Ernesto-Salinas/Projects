import say_hi
say_hi.say_hi()

import os
print("Current working director:", os.getcwd())

import sys
file_name = 'projects/phsc/intro-to-computer-programing-python/lesson-8.3/py/test.txt'
try:
   with open(file_name, "r") as test_file:
      for line in test_file:
          print(line)
except:
    print('Could not open {}.'.format(file_name))
    sys.exit(1)