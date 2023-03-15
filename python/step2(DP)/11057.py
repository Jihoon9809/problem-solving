n = int(input())

arr = [[0 for col in range(10)]for row in range(n+1)]

for i in range(10):
    arr[1][i] = 1
    
for i in range(2,n+1):
    for j in range(10):
        if i == 0 : arr[i][j] = sum(arr[i-1])
        else :
            temp = 0
            for k in range(j):
                temp += arr[i-1][k]
            arr[i][j] = sum(arr[i-1])-temp
            
            
print(sum(arr[n])%10007)
