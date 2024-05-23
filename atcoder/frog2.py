N, K = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * N
for i in range(1, N):
    dp[i] = float('inf')
    for j in range(max(0, i - K), i):
        dp[i] = min(dp[i], dp[j] + abs(arr[j] - arr[i]))
print(dp[N - 1])
