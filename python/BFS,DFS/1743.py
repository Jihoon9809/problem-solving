from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m, k = map(int,input().split())

vist = [[False] * (m) for _ in range(n)]
res = []

for _ in range(k):
    x,y = map(int,input().split())

    vist[x-1][y-1] = True
    
for i in range(n):
    for j in range(m):
        if vist[i][j] :

            q = deque()     
            q.append([i,j])
            vist[i][j] = False
            cnt = 0
            
            while q :
                x, y = q.popleft()
                cnt += 1
                for c in range(4):
                    nx,ny = dx[c] + x, dy[c] + y
                    if nx < 0 or ny < 0 or nx >= n or ny >= m : continue
                    if not vist[nx][ny] : continue
                    q.append([nx,ny])
                    vist[nx][ny] = False
            res.append(cnt)

res.sort(reverse=True)
print(res[0])



# 3 4 5
# 3 2
# 2 2
# 3 1
# 2 3
# 1 1