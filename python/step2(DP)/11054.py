n = int(input())

arr = list(map(int,input().split()))
dp1 = [1] * n
dp2 = [1] *n
for i in range(1,n):
    for j in range(i):
        if arr[j] > arr[i] and dp1[j] >= dp1[i]:
            dp1[i] = dp1[j] +1
        if arr[j] 
print(max(dp))