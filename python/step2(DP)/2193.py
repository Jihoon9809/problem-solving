n = int(input())

arr = [[0 for i in range(2)]for i in range(n+1)]

arr[1][1] = 1

arr[2][1] = 1

for i in range(3,n+1):
    for j in range(2):
        arr[i][j] = arr[i-1][j] + arr[i-2][j]
        
print(arr[n][0] + arr[n][1])

