
# count from 1-10 using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# count from 1-10 using a for loop
for i in range(1,11):
    print(i)


# count backwards from 10 using a while loop
i = 10
while i > 0:
    print(i)
    i -= 1

# count backwards from 10 using a for loop
for i in range(10, 0, -1):
    print(i)


arr = [10,20,30,40,50,60,70,80,90]

# print each index and element in the array
for i in range(len(arr)):
    print(i, arr[i])