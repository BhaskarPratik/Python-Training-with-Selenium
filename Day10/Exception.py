# Exception Handling: Exception is an event which will cause program termination

# Example 1:
# print("This is staring point of program")
# print("This is staring point of program")
# print("This is staring point of program")
# try:
#     print(x)
# except:
#     print("Exception occurred")
# print("This is ending point of program")
# print("This is ending point of program")
# print("This is ending point of program")

# Example 2 :
# print("This is staring point of program")
# print("Program in progress")
# try:
#     print(10 / 5)  # 2.0
# except ZeroDivisionError:
#     print("Exception occurred...handled...")  # skip this statement because no exception is occurred
# print("Program completed...")


# Example 3 : (Multiple Except Block)  --> try,except,else,finally
# try:
#     num1, num2 = 10,5
#     result = num1 / num2
#     print("result is :", result)
# except ZeroDivisionError:
#     print("Throw ZeroDivisionError exception")
# except SyntaxError:
#     print("Thrown syntax error exception")
# except:
#     print("Exception Handled")
# else:
#     print("No Exception Occurred")
# finally:
#     print("Always Execute")
#

# Example 4 : Raising our own exception
def enterage(num):
    if num < 0:
        raise ValueError("Only integers are allowed")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


print("Checking number is even or odd by calling function..")
num = -5
try:
    enterage(num)
except ValueError:
    print("Value error exception occurred and handled")
print("Program completed")
