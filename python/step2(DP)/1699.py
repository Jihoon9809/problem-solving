n = int(input())

arr = [i for i in range(n+1)]

for i in range(2,n+1):
    target = i ** 2
    
    if len(arr) <= target :
        break
    
    arr[target] = 1
    
    for j in range(target+1,n+1):
        arr[j] = min(arr[j],arr[j - target] + arr[target])
        
print(arr[n])