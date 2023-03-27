# Global Variable = The variable create outside the function are called global-variable
# Global variable can be access everywhere

# Local Variable =  The variable create inside the function are called local-variable
# Local variable can be access within the function

# Example 1:
global_var = 20  # Global-Variable


def func():
    local_var = 10  # local_var
    print(local_var)
    print(global_var)


func()

# print(local_var)  # NameError: name 'local_var' is not defined.  local variable
# print(global_var) # 20 Global variable

# Example 2 :
# xy = 100  # global var
#
#
# def cool():
#     xy = 200  # local var
#     print(xy)
#
#
# cool()  # 200

# Example 3 : Using global variable in local variable and update value

# xy = 100  # global var


# def cool():
#     # global xy = 200  # invalid syntax
#     global xy
#     xy = 200  # global var
#     print(xy)
#
#
# cool()  # 200
# print(xy)  # 200

# Example 4:

# a = 100
#
#
# def func():
#     global a
#     a = 500
#     print(a)
#
#
# func()  # 500
# print(a)  # 500

# Example 5:
# There is no need to declare global variable outside the function
# You can declare them global inside the function - global

# def myfunc():
#     global b
#     b = 100
#     print(b)
#
#
# myfunc() # 100
# print(b) # 100 able to access b it is global variable
