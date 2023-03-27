# Python = structured + object-oriented
# A) Class B) Object C) Inheritance D) Polymorphism E) Constructor F) Method
# Class = Employee   Object = scott, john, merry
# Class  = Animal  Object = dog, horse, elephant
# Class is a collection of variables(attribute) and methods(behaviour)
# Class is a blueprint
# Class is a logical entity
# Class does not occupy space in the memory

# Object is a instance of a class
# Object is a physical entity
# Object occupy certain amount of space in the memory
# For one class, we can create multiple object
# Objects are independent

# Function vs Method:
# Function = We can create without a class.
# Method = Create inside the class

# Example 1 : How to create class

# class MyClass:
#     def myfun(self):  # method   self : means belongs to current class
#         pass  # none
#
#     def display(self,name):  # method
#         print(name)
#
#
# # Create object
# mc1 = MyClass()
#
# # Access method from the object
# mc1.myfun()
# mc1.display("Scott")


# 2 types of method we can define within the class :
# A) Instance Method = We can call only through object
# B) Static Method = We can directly call using class

# Self is working different in the instance & static methods
# In the instance method self means it is representing to the class
# In the static method self means one parameter

# Example 2 : Make a method static using @staticmethod annotation

# class MyClass:
#     def m1(self):
#         print("This is instance method")
#
#     @staticmethod
#     def m2(self, name):
#         print(self, name)
#
#
# obj1 = MyClass()
#
# # Instance method access through the objects
# obj1.m1() # This is instance method
#
# obj1.m2("Hello","Merry") # This is not a standard way  # Hello Merry
#
# # Static method access through the class name not through the objects
# MyClass.m2("Hello","John") # Hello John

# Example 3 : How to create class variable and how to access class variable

# class MyClass:
#     a, b = 10, 20  # Class variable
#
#     def add(self):
#         print(self.a + self.b)  # Access class variable
#
#     def mul(self):
#         print(self.a * self.b)
#
#
# obj1 = MyClass()
# obj1.add()  # 30
# obj1.mul()  # 200

# Example 4 : Combination of local, global and class variable
# i, j = 15, 25  # global variable
#
#
# class MyClass:
#     a, b = 10, 20  # class variable
#
#     def add(self, x, y):
#         print(x + y)  # x, y are local variable  300
#         print(self.a + self.b)  # a, b are class variable 30
#         print(i + j)  # i, j are the global variable 40
#
#
# obj1 = MyClass()
# obj1.add(100, 200)

# Example 5 : if the local,global,class variable name same then how to access global variable
# a, b = 15, 25  # global variable
#
#
# class MyClass:
#     a, b = 10, 20  # class variable
#
#     def add(self, a, b):
#         print(a + b)  # x, y are local variable  300
#         print(self.a + self.b)  # a, b are class variable 30
#         print(globals()['a'] + globals()['b'])  # a, b are the global variable 40
#
#
# obj1 = MyClass()
# obj1.add(100, 200)

# Example 6 : One class can have multiple objects
# class MyClass:
#
#     def display(self, name):
#         print("This is display method")
#         print(name)
#
#
# obj1 = MyClass()
# obj1.display("Merry")
#
# obj2 = MyClass()
# obj2.display("John")

# Method and Constructor :
# Method :
# A) Give any name
# B) Return the value/s
# C) Method can take the arguments / parameters
# D) We can to use object to invoke the methods

# Constructor:
# A) Constructor name is fixed : def __init__(self)
# B) Constructor will not return anny value
# C) Constructor can take arguments/ parameters
# D) Constructor will be called at the time of object creation itself

# Example 7 : Constructor Example

# class MyClass:
#     def __init__(self):
#         print("this is constructor")
#
#     def m1(self):
#         print("Hello")
#
#     def m2(self, x, y):
#         return x + y
#
#
# obj1 = MyClass()  # invoke constructor automatically
# obj1.m1()  # method we have call explicitly by using objects
# print(obj1.m2(10, 20))  # 30

# Example 8: Parameterized constructor
#
# class MyClass:
#     name = "Ram"
#
#     def __init__(self, name):
#         print(self.name)
#         print(name)
#
#
# obj1 = MyClass("David")  # Passing parameter to the constructor

# Example 9 : Req: Emp class  # constructor : eid,ename,sal  # Method: display() print eid,ename,sal
# class Employee:
#     def __init__(self, eid, name, sal):  # local variable (parameterized constructor)
#         self.eid = eid
#         self.name = name  # converting local variable to class variable using self keyword
#         self.sal = sal
#
#     def display(self):
#         print(self.eid, self.name, self.sal)
#
#
# e1 = Employee(102, "Merry", 58000)
# e1.display()

# class Employee:
#
#     def __init__(self, eid, ename,sal):   # local variable (parameterized constructor)
#         self.eid = eid
#         self.ename = ename  # converting local variable to class variable using self keyword
#         self.sal = sal
#
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
#
# obj1 = Employee(101,"Sagar",80000)
# obj1.display() # 101 Sagar 80000
#
# obj2 = Employee(102,"Merry",90000)
# obj2.display() # 102 Merry 90000

# Example 10 : Req: Emp class  # constructor : eid,ename,sal  # constructor:  print eid,ename,sal

# class Employee:
#
#     def __init__(self, eid, ename,sal):   # local variable (parameterized constructor)
#         self.eid = eid
#         self.ename = ename  # converting local variable to class variable using self keyword
#         self.sal = sal
#
#     def __str__(self):
#         # return self.ename
#         return (self.eid,self.ename,self.sal) # TypeError: __str__ returned non-string (type tuple)
#
# obj1 = Employee(101,"Sagar",80000)
# print(obj1)
