# break continue

for x in range(1, 10):
    if x == 5:
        break
    print(x)  # 1,2,3,4,5
print("Program Executed")

for i in range(1, 10):
    if i == 5:
        continue  # skip 5
    print(i)
print("Program Exited")

# skip 8,3,1
for i in range(1, 10):
    if i == 8 or i == 3 or i == 6:
        continue
    print(i)
print("Program Exited")
