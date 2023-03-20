# n = int(input())

# arr = list(map(int, input().split()))
# dp = [0] * n

# for i in range(n):
#     max_n = arr[i]
#     count = 1
#     for j in range(i,n):
#         if arr[j] > max_n:
#             max_n = arr[j]
#             count += 1
#     dp[i] = count
    
# print(max(dp))

n = int(input())

arr = list(map(int, input().split()))
dp = [0] * 10000

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] <dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))