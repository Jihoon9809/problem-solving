from collections import deque

n1, n2 = map(int,input().split())

arr = [[] for _ in range(n1+1)]
vist = [False] * (n1+1)

for _ in range(1,n2):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(v):
    q = deque()
    q.append(v)

    while q:
        x = q.popleft()
        if not vist[x]:
            vist[x] =True
            for i in arr[x]:
                q.append(i)

count = 0
for i in range(1, n1+1):
    if not vist[i]:
        bfs(i)
        count += 1

print(count)
