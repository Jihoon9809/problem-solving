n = int(input())

dicts = {}

for _ in range(n):
    n1 = int(input())
    if n1 in dicts:
        dicts[n1] += 1
    else:
        dicts[n1] = 1

res = sorted(dicts.items(), key= lambda x:(-x[1],x[0]))

print(res[0][0])
