arr = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

# print 10 20 30 40 50 60 70 80 90
for i in range(3):
    for j in range(3):
        print(arr[i][j])

print("")
print("-----------------------------------------")
print("")

# print 90 80 70 60 50 40 30 20 10
for i in range(2, -1, -1):
    for j in range(2, -1, -1):
        print(arr[i][j])

print("")
print("-----------------------------------------")
print("")

# print 30 20 10 60 50 40 90 80 70
for i in range(3):
    for j in range(2, -1, -1):
        print(arr[i][j])

print("")
print("-----------------------------------------")
print("")

# print 10 40 70 20 50 80 30 60 90
for i in range(3):
    for j in range(3):
        print(arr[j][i])