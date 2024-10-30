#첫 제출
#시간초과
# O(n^3) -> 약 9억번 수행
N,M = map(int,input().split())
arr = []

[arr.append(list(map(int,input().split()))) for _ in range(N)]

K = int(input())
for tk in range(K):
    i,j,x,y = map(int,input().split())
    tsum = 0
    for tx in range(i-1,x):
        for ty in range(j-1,y):
            tsum += arr[tx][ty]
    print(tsum)

# 두번째 제출
# DP구현
# https://velog.io/@seungjae/%EB%B0%B1%EC%A4%80-2167%EB%B2%88-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9-Python-DP
해당 블로그 참고

N,M = map(int,input().split())
arr = []
[arr.append(list(map(int,input().split()))) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

K = int(input())
for k in range(K):
    i,j,x,y = map(int,input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
