N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(3)]
dp = points[::]
for i in range(N - 2, -1, -1):
    for j in range(2, -1, -1):
        if j == 2:
            dp[i][j] = points[i][j] + max(dp[i + 1][0], dp[i + 1][1])
        elif j == 1:
            dp[i][j] = points[i][j] + max(dp[i + 1][0], dp[i + 1][2])
        else:
            dp[i][j] = points[i][j] + max(dp[i + 1][1], dp[i + 1][2])
print(max(dp[0]))
