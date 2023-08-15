from collections import deque

n = int(input())
m = int(input())

board = [[] for _ in range(n+1)]
vist = [0] * (n+1)

cnt = 0

for _ in range(m):
    x,y = map(int,input().split())
    board[x].append(y)
    board[y].append(x)

def dfs(v):
    vist[v] = 1
    for j in board[v]:
        if not vist[j] : dfs(j)

dfs(1)

print(sum(vist)-1)