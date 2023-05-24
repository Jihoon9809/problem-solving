import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n) :
    n2 = int(input())
    arr.append(n2)
    
arr = sorted(arr)

for i in arr:
    print(i)
    
    
    