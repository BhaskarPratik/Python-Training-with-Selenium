# Creating String Variables
# Example 1 : ways of creating string variable
# s = "Welcome"
# s = 'welcome'
# s = str('welcome')
# s = str("Welcome")
#
# # creating empty string variable
# name = ""
# name = ''
# name = str()
#
# # Example 2
# # Mutable : can change the value of variable
# # Immutable : can not change the value of variable
#
# str1 = "Welcome"
# print(id(str))
#
# str1 = str1 + "to python"
# print(id(str1))
#
# # Example 3 : + and * with string
#
# str1 = "Welcome"
# print(str1 + " Programming ")  # concatenation / joining

# print(str * 5)  # * is used to print sting value multiple time
#
# # slicing []
# # starting index 0
# # ending index 1
#
# str5 = "Welcome"
# print(str5[1:4])  # elc
# print(str5[2:6])  # lcom
# print(str5[0:6])  # Welcom
# print(str5[1:])   # elcome
#
# print(str5[1:-1]) # elcom   # last 1 character removed
# print(str5[1:-2])  # elco   # last 2 character removed
#
# print(str5[-3:6]) # om

# Example 4 :  ord()  and chr()
# ord() = Returns the ASCII code of the character
# char() = Returns the character represented by ASCII number

# print(ord('A'))  # 65
# print(chr(65))   # A

# Example 5 : max() min() len()

# print(max("ABC"))  # C
# print(min("ABC"))  # A
# print(len("Welcome"))  # 7
#
# # Example 6: in, not in operator  - return true / false
# s='Welcome'
# # print("come" in s) # True
# # print("lome" in s) # False
#
# print("come" not in s) # False
# print("lome" not in s) # True

# Example 7:  String comparison
# print("tim" == "tie")   # False
# print("free" != "freedom") # True
# print("arrow" > "aron")    # True
# print("right" >= "left")   # True
# print("teeth" < "tee")     # False
# print("yellow" <= "fellow") # False
# print("abc" > "") # True

# Example 8: Testing strings   True / False
# s = "Welcome to python"
# print(s.isalnum())  # False
#
# print("Welcome".isalpha())  # True
# print("2021".isdigit())  # True
# print("First Number".isidentifier())  # False
# print(s.islower())  # False
# print("WELCOME".isupper()) # True
# print(" ".isspace()); # True

# Example 9: searching for substring
# s = "Welcome to python"
# print(s.endswith("thon"))  # True
# print(s.startswith("good"))  # False
# print(s.find("come"))  # 3 =  find() will return the position
# print(s.find("become")) # -1  not found
# print(s.count("o"))  # 3  count() returns number of occurrences of substring the string

# Example 10: converting string
# s = "String in PYTHON"
# s1 = s.capitalize();
# print(s1)  # String in python
#
# s2 = s.title()
# print(s2) # String In Python
#
# s3 = s.lower()
# print(s3) # string in python
#
# s4 = s.swapcase()
# print(s4) # sTRING IN python
#
# s5 = s.upper()
# print(s5) # STRING IN PYTHON
#
# s6 = s.replace("in","on")
# print(s6) # Strong on PYTHON

# Example 11: Reverse a string (Interview Question)
# Method 1

s = "welcome"
rev_String = ''
for i in s:
    rev_String = i + rev_String
print("Reversed string is : ",rev_String)          # emoclew

# Method 2 :
# s = "welcome"
# rev_str = s[::-1]
# print(rev_str)  # emoclew
