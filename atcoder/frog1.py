N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = abs(arr[1] - arr[0])
for i in range(2, N):
    dp[i] = min((dp[i - 1] + abs(arr[i - 1] - arr[i])), (dp[i - 2] + abs(arr[i - 2] - arr[i])))
print(dp[N - 1])
