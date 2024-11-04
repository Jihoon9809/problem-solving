시간복잡도 : 1초,
N = 100,000

N = int(input())
arr = list(map(int,input().split()))
total = sum(arr)
res = 0

for target in arr :
    total -= target
    res += total * target

print(res)


1*5,2*5,3*5,4*5,5*5와 15*5 의 값은 같다.
따라서 중첩 반복문을 사용하는 것 보다 위의 코드가 효율적이다.
또한 시간 복잡도를 초과하지 않는다.


백준 : https://www.acmicpc.net/problem/13900
