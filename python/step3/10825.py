n = int(input())

arr = []

for _ in range(n):
    name,n1,n2,n3 = input().split()
    arr.append((name,int(n1),int(n2),int(n3)))

arr.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))


for name,n1,n2,n3 in arr:
    print(name)
