# Two types of arguments / parameters we can pass the function  1.Positional arguments 2.Keyword arguments
# Example 1 :
# def func(i, j):
#     print(i, j)
#
#
# func(10, 20)  # positional arguments
# func(j=20, i=10)  # Keyword arguments

# Example 2 : Default value assigned to positional arguments

# def func(i, j=10):
#     print(i, j)
#
#
# func(100,200)  # positional argument 100 200
# func(100)  # 100 10

# Example 3 : Keyword arguments

# def greetings(name, greetmsg):
#     print(greetmsg + " " + name)
#
#
# greetings(name="John", greetmsg="Hello")  # Keyword arguments Hello John
# greetings(greetmsg="Hello", name="Nick")  # Keyword arguments Hello Nick

# Example 4 : Combination of positional and keyword arguments

# def func(a, b, c):
#     print(a, b, c)


# func(10, 20, 30)  # 10 20 30 positional arguments
# func(c=30, b=20, a=10)  # 10 20 30 keyword arguments
# func(15, b=35, c=45)  # 15 35 45  combination of positional and keyword arguments
# func(35, b=45,15 ) # This is wrong positional argument must appear before keyword argument
# func(10, 30, b=20)  # Logical error = func() got multiple values for argument 'b'


# Example 5 : Function can return multiple value

def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


# print(largest(200, 10)) # (200, 10)
# print(largest(10,300)) # (300, 10)

result = largest(200,100)
print(result)  # (200, 100)

print(type(result)) # <class 'tuple'>
