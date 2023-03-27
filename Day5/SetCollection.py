# Set: set is a collection which is unordered and un-indexed.
# In python sets are written with curly brackets {}
# Set is a mutable

# Example 1: Create set
# mySet = {"Apple", "Banana", "Cherry"}
# print(mySet) # {'Banana', 'Cherry', 'Apple'}  # unordered

# Example 2: Accessing item from the set (only through loop)
# mySet = {"Apple", "Banana", "Cherry"}
# for i in mySet:
#     print(i)

# Example 3: Value exist or not in the set
# mySet = {"Apple","Banana","Cherry"}
# print("Banana" in mySet) # True
# print("Banana1" in mySet) # False

# if "Banana" in mySet:
#     print("Yes,Banana is present")
# else:
#     print("No, Banana is not present")

# Example 4: Adding items to set = add() update()
# add() = add only single item
# update() = add multiple item
# mySet = {"Apple", "Banana", "Cheery"}
# mySet.add("Orange")
# print(mySet) # {'Cheery', 'Apple', 'Orange', 'Banana'}

# mySet.update(["Kiwi", "Pear", "Grapes"])
# print(mySet)  # {'Banana', 'Cheery', 'Pear', 'Grapes', 'Kiwi', 'Apple'}

# Example 5 : Find number of item in set = len()
# mySet = {'Apple', 'Banana', 'Cherry', 'Grapes', 'Pear'}
# print(len(mySet))  # 5

# Example 6 : Remove item = remove() discard()
# mySet = {'Apple', 'Banana', 'Cherry'}
# mySet.remove("Banana")
# print(mySet)  # {'Cherry', 'Apple'}

# mySet.remove("xyz")
# print(mySet)  # KeyError: 'xyz'

# mySet.discard("Apple")
# print(mySet)  # {'Banana', 'Cherry'}

# mySet.discard("xyz")
# print(mySet)  # {'Banana', 'Cherry', 'Apple'}  = >  Not throw any error

# Example 7 : clear all items from set
# mySet = {'Apple', 'Banana', 'Cherry', }
# # mySet.clear()
# # print(mySet)  # set()
#
# del mySet
# print(mySet)  # NameError: name 'mySet' is not defined

# Example 8 : Joining 2 sets  = union() update()
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)  # {1, 2, 'c', 'b', 3, 'a'}

set1.update(set2)
print(set1)  # {1, 2, 'b', 'c', 'a', 3}


