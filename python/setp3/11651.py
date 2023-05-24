n = int(input())

arr = []

for i in range(n):
    n1,n2 = map(int,input().split())
    arr.append([n1,n2])

arr.sort(key=lambda x: (x[1],x[0]))

for i in arr:
    print(i[0],i[1])