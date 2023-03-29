n = int(input())
arr = []
dp = [0] * n

for  i in range(n):
    arr.append(int(input()))


if len(arr) <= 2:
    print(sum(arr))
    
else :
    dp[0] = arr[0]    
    dp[1] = arr[1]+dp[0]
    
    for i in range(2,n):
        dp[i] = max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])
    
    print(dp[n-1])
