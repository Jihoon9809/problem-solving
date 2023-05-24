n = int(input())

arr = []
arr.append(1)
arr.append(1)
arr.append(1)

for i in range(3,100):
    arr.append(arr[i-3]+arr[i-2])

for i in range(n):
    n2 = int(input())
    print(arr[n2 - 1])
