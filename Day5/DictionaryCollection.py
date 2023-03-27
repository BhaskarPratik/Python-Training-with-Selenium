# Dictionary : Dictionary is a collection which is unordered, changeable (mutable) and indexed
# In python dictionaries are written with curly brackets {}, and they have keys and values.

# Example 1 : Create dictionary
# myDic = {101: "x", 102: "y", 103: "z"}
# print(myDic)  # {101: 'x', 102: 'y', 103: 'z'} # unordered

# Example 2 : Access item from the dictionary
# myDic = {
#     "Brand": "Tata",
#     "Model": "Punch",
#     "Year": 2021
# }
# print(myDic["Brand"])  # Tata
# print(myDic["Model"])  # Punch
#
# # using get()
#
# x = myDic.get("Year")
# print(x)
# print(myDic.get("Brand"))

# Example 3: Change value in dictionary
# myDic = {
#     "Brand": "Tata",
#     "Model": "Punch",
#     "Year": 2021
# }
# print(myDic)  # {'Brand': 'Tata', 'Model': 'Punch', 'Year': 2021}
# myDic["Year"] = 2023 # New value
# print(myDic)  # {'Brand': 'Tata', 'Model': 'Punch', 'Year': 2023}

# Example 4: reading items from dictionary using loop
# myDic = {
#     "Brand": "Tata",
#     "Model": "Punch",
#     "Year": 2021
# }

# for i in myDic:
#     print(i)  # prints only key from dictionary
#
# for i in myDic:
#     print(myDic[i])  # prints only value from dictionary

# for i in myDic.values():
#     print(i)

# for x,y in myDic.items():
#     print(x,y)  # print keys along with value

# Example 5: check key is exist in dictionary or not
# myDic = {
#     "Brand": "Tata",
#     "Model": "Punch",
#     "Year": 2021
# }
# if "Model" in myDic:
#     print("Exist")
# else:
#     print("Not exist")

# print("Model" in myDic)  # True

# Example 6: find no of items in dictionary len()
# myDic = {
#     "Brand": "Tata",
#     "Model": "Punch",
#     "Year": 2021
# }
# print(len(myDic)) # 3

# Example 7: Adding items to dictionary
# myDic = {
#     "Brand": "Tata",
#     "Model": "Punch",
#     "Year": 2021
# }
# myDic["color"] = "Black"
# print(myDic)

# Example 8 : Remove item from dictionary = pop(), del, clear()
# myDic = {
#     "Brand": "Tata",
#     "Model": "Punch",
#     "Year": 2021
# }
# myDic.pop("Year")
# print(myDic)  # {'Brand': 'Tata', 'Model': 'Punch'}

# del myDic["Model"]
# print(myDic)  # {'Brand': 'Tata', 'Year': 2021}

# del myDic
# print(myDic)  # NameError: name 'myDic' is not defined

# myDic.clear()
# print(myDic)  # {}

# Example 9: Copying dictionary
myDic1 = {
    "Brand": "Tata",
    "Model": "Punch",
    "Year": 2021
}

# without using copy()
# myDic2 = myDic1
# print(myDic2)  # {'Brand': 'Tata', 'Model': 'Punch', 'Year': 2021}

# using copy()
myDic2= myDic1.copy()
print(myDic2)  # {'Brand': 'Tata', 'Model': 'Punch', 'Year': 2021}

