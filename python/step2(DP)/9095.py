n = int(input())

arr = [0] * 12

arr[1] = 1
arr[2] = 2
arr[3] = 4
arr[4] = 7

for i in range(5,12):
    arr[i] = arr[i-3] +arr[i-2]+arr[i-1]

for i in range(n):
    n2 = int(input())
    print(arr[n2])