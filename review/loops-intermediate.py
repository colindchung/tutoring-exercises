arr = [32, 12, 45, 17, 4, -1, 9, -7, 33]

# print all numbers greater that 10
for i in arr:
    if i > 10:
        print(i)

print("")
print("-----------------------------------------")
print("")

# print all even odd numbers in the array
for i in arr:
    if i % 2 == 1:
        print(i)

print("")
print("-----------------------------------------")
print("")

# multiply each number in the array by 2 and print
for i in range(len(arr)):
    arr[i] *= 2

for i in arr:
    print(i)