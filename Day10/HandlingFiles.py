# Example 1 : Writing data into text-file
# file = open("C:/Users/Mangesh/OneDrive/Desktop/Python-Demo-File/MyFile.txt", 'w')
# file.write("This is my first statement.. \n")
# file.write("This is my first statement.. \n")
# file.write("This is my first statement.. ")
# file.close()
# print("Program Completed")

# Example 2  : Reading data from text-file
# file = open("C:/Users/Mangesh/OneDrive/Desktop/Python-Demo-File/MyFile.txt", 'r')
# print(file.read())
# # print(file.readline())
# file.close()

# Example 3  : Appending data into text file
file = open("C:/Users/Mangesh/OneDrive/Desktop/Python-Demo-File/MyFile.txt", 'a')
file.write("This is my second statement \n")
file.write("This is my second statement \n")
file.write("This is my second statement \n")
file.close()
print("Append data completed")


