arr = [
    [1,12,-3],
    [17,0,-21],
    [-7,45,-10]
]

# print the even numbers
for i in range(3):
    for j in range(3):
        if arr[i][j] % 2 == 0:
            print(arr[i][j])

print("")
print("-----------------------------------------")
print("")

# print the positive numbers
for i in range(3):
    for j in range(3):
        if arr[i][j] > 0:
            print(arr[i][j])

print("")
print("-----------------------------------------")
print("")


# print matrix transposed
for i in range(3):
    for j in range(3):
        print(arr[j][i])

print("")
print("-----------------------------------------")
print("")
