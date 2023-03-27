n = int(input())
arr = []
dp = [0] * n

for  i in range(n):
    arr.append(int(input()))

dp[0] = arr[0]

for i in range(1,n-1):
    if i % 2 == 0:
        dp[i] = dp[i-1]
    else : dp[i] = dp[i-1]+arr[i]

dp[2] = max(arr[i-1],arr[i-2])+arr[2] 

for i in range(4, n,2):
    dp[i] = dp[i-2]+arr[i]

# print(arr)
# print(dp)
print(max(dp[n-3]+arr[n-1], dp[n-2]+arr[n-1]))

