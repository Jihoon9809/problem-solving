n = int(input())

for _ in range(n):
    arr = []
    col = int(input())

    for _ in range(2) :
        arr.append(list(map(int,input().split())))
        
    for i in range(1,col):
        if i == 1:
            arr[0][i] += arr[1][i-1]
            arr[1][i] += arr[0][i-1]    
        else :
            arr[0][i] += max(arr[1][i-1],arr[1][i-2])
            arr[1][i] += max(arr[0][i-1],arr[0][i-2])
            

    print(max(arr[0][col-1],arr[1][col-1]))      
         
