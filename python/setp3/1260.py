from collections import deque

n,l,v = map(int,input().split())

board = [[0]*(n+1) for _ in range(n+1)]
vist = [False]*(n+1)

for _ in range(l):
    x, y = map(int,input().split())
    board[x][y] = 1
    board[y][x] = 1

def dfs(v):
    vist[v] = True
    print(v, end = ' ')
    for i in range(1, n+1):
        if board[v][i] == 1 and not vist[i] : dfs(i)

def bfs(v):
    vist[v] = False
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in range(1,n+1):
            if vist[i] and board[v][i] == 1:
                q.append(i)
                vist[i] = False

dfs(v)
print()
bfs(v)

