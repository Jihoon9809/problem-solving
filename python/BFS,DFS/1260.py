from collections import deque

n, m, v = map(int,input().split())

board = [[0]*(n+1) for _ in range(n+1)]
vist = [False]*(n+1)

for _ in range(m):
    x, y = map(int,input().split())
    board[x][y] = 1
    board[y][x] = 1

def dfs(st):
    vist[st] = True
    print(st, end = ' ')
    for i in range(1,n+1):
        if board[st][i] == 1 and not vist[i] :
            dfs(i)

def bfs(st):
    vist[st] = False
    q = deque()
    q.append(st)
    while q :
        st = q.popleft()
        print(st, end = ' ')
        for i in range(1,n+1):
            if vist[i] and board[st][i] == 1:
                q.append(i)
                vist[i] = False

dfs(v)
print()
bfs(v)
