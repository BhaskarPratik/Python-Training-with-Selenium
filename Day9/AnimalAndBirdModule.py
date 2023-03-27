# Example 2 : Same function in 2 modules
# Approach 1:

# import AnimalModule
# import BirdModule
#
# AnimalModule.fly()
# AnimalModule.color()
#
# BirdModule.fly()
# BirdModule.color()

# Approach 2:

from AnimalModule import *

fly()
color()

from BirdModule import *

fly()
color()
