# calling function from calculator module.

# Example 1 :How to call the function from one module to another module

# Approach 1 :
# import CalculatorModule
#
# CalculatorModule.add(150, 250)  # 400
# CalculatorModule.multi(5, 4)  # 20

# Approach 2:
# from CalculatorModule import add, multi
#
# add(350, 350)  # 700
# multi(8, 4)  # 32

# Approach 3 :
from CalculatorModule import *
 
add(450, 260)  # 710
multi(7, 3)  # 21
