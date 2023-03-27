# List is a collection which is ordered and changeable.
# In python list are written in square brackets [].
# List is mutable.
# Index start from 0

# Example 1: how to create list
# myList1 = ["Apple", "Banana", "Orange", "Cherry"]
# myList2 = [10, 20, 30, 40]
# myList3 = ["Apple", 10, "Banana", 20, "Orange", 30]
# myList = list()  # empty list
# print(myList1)
# print(myList2)
# print(myList3)
# print(myList)

# Example 2: Accessing item from the list
# myList1 = ["Apple", "Banana", "Orange", "Cherry"]
# print(myList1[1]) # Banana
# print(myList1[3]) # Cherry
# print(myList1[-1]) # Cherry
# print(myList1[-3]) # Banana

# Example 3: Range of indexes
# myList2 = ["Apple", "Banana", "Orange", "Cherry", "Kiwi", "Watermelon"]
# print(myList2[2:5])  # ['Orange', 'Cherry', 'Kiwi']
#
# print(myList2[-4:-1])  # ['Orange', 'Cherry', 'Kiwi']

# Example 4: how to change item in the list
# myList3 = ["Apple", "Banana", "Orange", ]
# print(myList3)  # ['Apple', 'Banana', 'Orange']
#
# myList3[0] = "Kiwi"
# print(myList3) # ['Kiwi', 'Banana', 'Orange']

# Example 5: how to read item using loop statement
# myList4 = ["Apple", "Banana", "Orange", "Cherry", "Kiwi", "Watermelon"]
# for i in myList4:
#     print(i)

# Example 6 : Check item is existed in the list or not
# myList5 = ["Apple", "Banana", "Orange", "Cherry", "Kiwi", "Watermelon"]
# if "Apple" in myList5:
#     print("Yes, Apple is present")
# else:
#     print("No, Apple is not present")

# Example 7 : list length
# myList6 =["Apple", "Banana", "Orange", "Cherry", "Kiwi", "Watermelon"]
# print(len(myList6)) # 6

# Example 8 : Add items append() insert()
# myList7 =["Apple", "Banana", "Orange", "Cherry", "Kiwi", "Watermelon"]
# myList7.append("Pear") # adding new item at the end of the list
# print(myList7) # ['Apple', 'Banana', 'Orange', 'Cherry', 'Kiwi', 'Watermelon', 'Pear']
#
# myList7.insert(1,"Strawberry") # add item somewhere in the middle of the list based on the index
# print(myList7) # ['Apple', 'Strawberry', 'Banana', 'Orange', 'Cherry', 'Kiwi', 'Watermelon', 'Pear']

# Example 9 : remove item from the list -: pop(), del(), clear()
# pop()
# myList8 = ["Apple", "Banana", "Orange"]
# myList8.pop(1)
# print(myList8)  # ['Apple', 'Orange']

# del
# myList8 = ["Apple", "Banana", "Orange"]
# del myList8[2]
# print(myList8) # ['Apple', 'Banana']

# clear()
# myList8 = ["Apple", "Banana", "Orange"]
# myList8.clear()  # It will clear all the item from the list
# print(myList8)

# Example 10 : copy list

# Approach 1 : using list() function
# myList9 = ["Apple", "Banana", "Orange"]
# myList10 = list(myList9)
# print(myList9)  # ['Apple', 'Banana', 'Orange']
# print(myList10)  # ['Apple', 'Banana', 'Orange']

# Approach 2: copy()
# myList11 = ["Apple", "Banana", "Orange"]
# myList12 = myList11.copy()
# print(myList11) # ['Apple', 'Banana', 'Orange']
# print(myList12) # ['Apple', 'Banana', 'Orange']

# Example 11 : combine/ join list

# using + operator
# myList13 = ['a', 'b', 'c']
# myList14 = [1, 2, 3]
# myList15 = myList13 + myList14
# print(myList15)  # ['a', 'b', 'c', 1, 2, 3]

# using looping statement
# myList13 = ['a', 'b', 'c']
# myList14 = [1, 2, 3]

# for i in myList14:
#     myList13.append(i)
# print(myList13) # ['a', 'b', 'c', 1, 2, 3]

# using extend()
# myList13 = ['a', 'b', 'c']
# myList14 = [1, 2, 3]
# myList13.extend(myList14)
# print(myList13) # ['a', 'b', 'c', 1, 2, 3]

# Example 12 : Compare list
myList13 = ['a', 'b', 'c']
myList14 = [1, 2, 3]
# myList14 = ['a', 'b', 'c']
if myList13 == myList14:
    print("List is equal")
else:
    print("List is not equal")

