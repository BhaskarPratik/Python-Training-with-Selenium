# Inheritance :
# Acquiring all the attributes(variable) and behaviour(methods) from one class to another class is called inheritance.
# class A --> a,b,c  m1() m2() ---> A is a parent of B class  (Base class/Super class)
# class B(A) --> x,y,z  m3() ---> B is child of A class (Sub class / Derived class)

# Objective of inheritance
# 1. Code re-usability
# 2. Avoid duplication

# Types of inheritance
# 1. Single inheritance    ---> One parent and One child
# 2. Multilevel inheritance
# 3. Hierarchy inheritance
# 4. Multiple inheritance

# Polymorphism = One thing can have multiple option

# # Example 1 : Single inheritance (One parent and One child)
#
# class A:
#     def m1(self):
#         print("This is method m1 from class A")
#
#
# class B(A):
#     def m2(self):
#         print("This is m2 method from class B")
#
#
# obj1 = B()
# obj1.m1()  # This is method m1 from class A
# obj1.m2()  # This is m2 method from class B

# Example 2 : Way of single inheritance (One parent and One child)

# class A:
#     a, b = 10, 20
#
#     def m1(self):
#         print(self.a + self.b)
#
#
# class B(A):
#     x, y = 200, 100
#
#     def m2(self):
#         print(self.x - self.y)
#
#
# obj2 = B()
# obj2.m1()  # 30
# obj2.m2()  # 100

# Example 3 : Multilevel inheritance (combination of multiple single inheritance )

# class A:
#     a, b = 10, 20
#
#     def m1(self):
#         print(self.a + self.b)
#
#
# class B(A):
#     x, y = 200, 100
#
#     def m2(self):
#         print(self.x - self.y)
#
#
# class C(B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
#
# obj3 = C()
# obj3.m1()  # 30
# obj3.m2()  # 100
# obj3.m3()  # 10

# Example 4: Hierarchy inheritance (One parent multiple child)
# class A:
#     a, b = 10, 20
#
#     def m1(self):
#         print(self.a + self.b)
#
#
# class B(A):
#     x, y = 200, 100
#
#     def m2(self):
#         print(self.x - self.y)
#
#
# class C(A):
#     i, j = 3, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
#
# obj4 = C()
# obj4.m1()  # 30
# obj4.m3()  # 6
#
# obj5 = B()
# obj5.m1()  # 30
# obj5.m2()  # 100

# Example 5: Multiple Inheritance (Multiple parent one child)
# class A:
#     a, b = 10, 20
#
#     def m1(self):
#         print(self.a + self.b)
#
#
# class B:
#     i, j = 20, 40
#
#     def m2(self):
#         print(self.i - self.j)
#
#
# class C(A, B):
#     x, y = 30, 60
#
#     def m3(self):
#         print(self.x * self.y)
#
# obj6 = C()
# obj6.m1()  # 30
# obj6.m2()  # -20
# obj6.m3()  # 1800

# Example 6: calling parent class method using child class using (super())  ---> (Method overriding)
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
#
#
# class B(A):
#     def m1(self):
#         print("This is m2 method from class B")
#         super().m1()  # This is m1 method from class A
#
#
# obj7 = B()
# obj7.m1()  # This is m2 method from class B
# This is m1 method from class A

# Example 7:
# class A:
#     a, b = 10, 20
#
#
# class B(A):
#     i, j = 100, 200
#
#     def m1(self, x, y):
#         print(x + y)  # local variables 3000
#         print(self.i + self.j)  # class variable 300
#         print(self.a + self.b)  # class variable 30
# obj8 = B()
# obj8.m1(1000,2000)

# Example 8: Overriding variables
# class Parent:
#     name = "Scott"
#
#
# class Child(Parent):
#     name = "Merry"  # overriding the variable value
#
#     def test(self):
#         print(super().name)
#
#
# obj9 = Child()
# print(obj9.name)  # Merry
# obj9.test()  # Scott

# Example 9: Overriding methods
# class Bank:
#     def rateOfIntrest(self):
#         return 0
#
#
# class XBank(Bank):
#     def rateOfIntrest(self):
#         return 10
#
#
# class YBank(Bank):
#     def rateOfIntrest(self):
#         return 12
#
#
# objX = XBank()
# print(objX.rateOfIntrest())  # 10
#
# objY = YBank()
# print(objY.rateOfIntrest())  # 20

# Example 10: overloading (polymorphism)
# class Human:
#     def sayHello(self, name=None):
#         if name is not None:
#             print("Hello", name)
#         else:
#             print("Hello")
#
#
# h = Human()
# h.sayHello("Scott")  # Hello Scott
# h.sayHello()  # Hello

# Example 11: overloading (polymorphism)

# class Calculation:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#
# objcal = Calculation()
# objcal.add()  # 0
# objcal.add(10,20)  # 30
# objcal.add(200,300,500)  # 1000
