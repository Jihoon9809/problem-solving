from collections import deque

t = int(input())

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        n = q.popleft()
        vis[n] = True
        if not vis[arr[n]] :
            q.append(arr[n])


for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    vis = [False] * (n+1)
    vis[0] = True    
    count = 0
    for i in arr:
        if not vis[i] :
            bfs(i)
            count+=1
    print(count)            

