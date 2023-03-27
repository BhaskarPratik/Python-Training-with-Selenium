# Approach 1 :
# import A
# import B
#
# obj1 = A.Animal()
# obj1.display()
#
# obj2 = B.Bird()
# obj2.display()

# Approach 2 :
from A import Animal
from B import Bird

obj1 = Animal()
obj1.display()

obj2 = Bird()
obj2.display()