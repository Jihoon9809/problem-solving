# n = int(input())

# arr = list(map(int,input().split()))
# dp = [0]*n

# for i in range(1,n):
#     if arr[i] > -1 or arr[i] + dp[i-1] > 0 : dp[i] = dp[i-1]+arr[i]

# if max(dp) == 0: print(max(arr))
# else : print(max(dp))    
# 수정

n = int(input())

arr = list(map(int,input().split()))

for i in range(1,n):
    arr[i] = max(arr[i], arr[i-1] + arr[i])

print(max(arr))