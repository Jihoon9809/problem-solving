n, p = map(int,input().split())

arr = [n]

while True:
    temp = 0
    for s in str(arr[-1]):
        temp += int(s) ** p
        print(temp)

    if temp in arr:
        print(temp)
        break
    
    arr.append(temp)

print(arr.index(temp))
