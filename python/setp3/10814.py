import sys
input = sys.stdin.readline

n= int(input())

arr =[]

for _ in range(n):
    num,name = input().split()
    arr.append((int(num), name))

# print(arr)
arr = sorted(arr, key = lambda x: int(x[0]))

for i in arr:
    print(i[0], i[1])
