# Tuple is a collection of ordered and unchangeable
# In python tuples are written with round brackets ().
# Tuples is immutable
# Index start from 0

# If it is immutable below things are not possible
# 1. We cannot  modify existing value
# 2. We cannot append new value
# 3. We cannot insert a new value
# 4. We cannot remove a value

# Example 1: Creating tuple

# myTuple = ("Apple", "Banana", "Cherry")
# print(myTuple)  # ('Apple', 'Banana', 'Cherry')

# Example 2 : Access tuple items
# myTuple = ("Apple", "Banana", "Cherry")
# print(myTuple[1]) # Banana
# print(myTuple[-1]) # Cherry

# Example 3 : Empty tuple
# myTuple = ()

# Example 4 : Range of indexes
# myTuple =("Apple","Banana","Pear","kiwi","Orange", "Mango")
# print(myTuple[2:4]) # ('Pear', 'kiwi')
# print(myTuple[-4:-1]) # ('Pear', 'kiwi', 'Orange')

# Example 5: Changing tuple items
# Indirect process (tuple ---> list(modify)---tuple)
# myTuple = ("Apple", "Banana", "Cherry")
# myList = list(myTuple)
# myList[0]="Orange"
#
# myTuple = tuple(myList)
# print(myTuple) # ('Orange', 'Banana', 'Cherry')

# Example 6: Read tuple items using loop
# myTuple = ("Apple", "Banana", "Cherry","Orange","Mango","Strawberry")
# for i in myTuple:
#     print(i)

# Example 7: Check if the item exist (searching item of tuple )
# myTuple = ("Apple", "Banana", "Cherry","Orange","Mango","Strawberry")
# if "Banana" in myTuple:
#     print("Yes, Banana is present")
# else:
#     print("No,Banana is not present")

# Example 8: tuple length
# myTuple = ("Apple", "Banana", "Cherry","Orange","Mango","Strawberry")
# print(len(myTuple)) # 6

# Example 9: Add items in tuple
# myTuple = ("Apple", "Banana", "Cherry","Orange","Mango","Strawberry")
# myTuple[0] = "Pinapple" # TypeError: 'tuple' object does not support item assignment
# print(myTuple)

# Example 10: Copy tuple
# myTuple = ("Apple", "Banana", "Cherry","Orange","Mango","Strawberry")
# myTuple1 = myTuple
# print(myTuple1)

# Example 11: Removing item from the tuples not possible bcoz is immutable
# myTuple = ("Apple", "Banana", "Cherry","Orange","Mango","Strawberry")
# # myTuple.remove() # invalid AttributeError: 'tuple' object has no attribute 'remove'
# del myTuple
# print(myTuple) # NameError: name 'myTuple' is not defined.

# Example 12: join / combine tuple
tuple1 = (10, 20, 30)
# tuple2 = ('a', 'b', 'c')
tuple2 = (10, 20, 30)
tuple3 = tuple1 + tuple2
print(tuple3)  # (10, 20, 30, 'a', 'b', 'c')

# Example 13 : compare tuple
if tuple1 == tuple2:
    print("Tuples are equal")
else:
    print("Tuples are not equal")
