n = int(input())

arr = [0] * 10000

for _ in range(n):
    arr.append(int(input()))

# arr = [int(input()) for _ in range(n)]
    
dp = [0]*10000
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2], dp[1])

for i in range(3,n):
    dp[i] = max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i],dp[i-1])
    
print(max(dp))


# 3~6번째 줄을 사용하는 이유는 메모리 사용 측면의 효율을 더하기 위해서 이다.

# append 함수를 이용하여 값을 추가하는 방식은 입력값이 작은 경우 리스트의 크기는 작을 것이다.
# 하지만 이방식은 리스트에 크기를 추가할 때마다 메모리를 재할당하게 되므로,
# 입력값이 매우 큰 경우에는 더 나은 메모리를 사용하게 된다.
# 따라서 입력값이 매우 큰 경우에는 리스트의 크기를 미리 지정하여 메모리를 효율적으로 사용하는 것이 좋다.



