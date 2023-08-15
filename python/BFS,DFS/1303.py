from collections import deque

n, m = map(int,input().split())

board = []
vist = [[False]*n for _ in range(m)]

w_count,b_count = 0,0


x_dir = [-1,1,0,0]
y_dir = [0,0,-1,1]


for i in range(n):
    temp = list(input())
    board.append(temp)



for i in range(n):
    for j in range(m):
        if board[i][j] == 'W' and vist[i][j] == False:
            q = deque()
            q.append((i,j))
            vist[i][j] = True
            temp_count = 1

            while q:
                x,y = q.popleft()
                for i in range(4):
                    nx_dir = x + x_dir[i]
                    ny_dir = y + y_dir[i]

                    if nx_dir < 0 or ny_dir < 0 or nx_dir >= n or ny_dir >= m : continue
                    if board[nx_dir][ny_dir] != 'W' or vist[nx_dir][ny_dir] != False : continue

                    temp_count += 1
                    q.append((nx_dir,ny_dir))
                    vist[nx_dir][ny_dir] = True

            w_count += temp_count**2

        if board[i][j] == 'B' and vist[i][j] == False:
            q = deque()
            q.append((i,j))
            vist[i][j] = True
            temp_count = 1

            print(i,j)

            while q:
                x,y = q.popleft()
                for i in range(4):
                    nx_dir = x + x_dir[i]
                    ny_dir = y + y_dir[i]

                    if nx_dir < 0 or ny_dir < 0 or nx_dir >= n or ny_dir >= m : continue
                    if board[nx_dir][ny_dir] != 'B' or vist[nx_dir][ny_dir] != False : continue

                    temp_count += 1
                    q.append((nx_dir,ny_dir))
                    vist[nx_dir][ny_dir] = True

            b_count += temp_count**2
print(w_count,b_count)
print(vist)

# print(board)
# print(check)