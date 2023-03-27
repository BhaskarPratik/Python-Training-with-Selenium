# package1 ==> Module1 ==> Display()
# package1 ==> package2 ==> Module2 ==> Show()

# Approach 1:

# import sys
#
# sys.path.append("E:/PythonTraining/Day9/Package1")
# sys.path.append("E:/PythonTraining/Day9/Package1/Package2")
#
# import Module1
# import Module2
#
# Module1.display()  # This is display function from module 1
# Module2.show()  # This is show function from module 2


# Approach 2 :
import sys

sys.path.append("E:/PythonTraining/Day9/Package1")
sys.path.append("E:/PythonTraining/Day9/Package1/Package2")

from Module1 import *
from Module2 import *

display()  # This is display function from module 1
show()  # This is show function from module 2
