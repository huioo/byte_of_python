import os
import sys
sys.path.append(os.path.dirname(__file__))


import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)
print('Module name is', mymodule.__name__)
