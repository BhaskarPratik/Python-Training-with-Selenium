# pack1 ==> Module1 ==> Display()
#       ==> Module2 ==> Show()
# Access pack1 modules in client Module

# How to access module from another packages module
# Approach 1 :

import sys  # This is predefined in python
sys.path.append("E:/PythonTraining/Day9/Pack1")

# import Module1
# import Module2
#
# Module1.display()  # This is display function from module 1
# Module2.show()  # This is show function from module 2

# Approach 2 :

from Module1 import *
from Module2 import *

display()  # This is display function from module 1
show()  # This is show function from module 2

