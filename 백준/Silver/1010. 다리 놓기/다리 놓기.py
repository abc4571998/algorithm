def bridge(n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = i
    #f(3,4) = f(2,3) + f(2,2) = f(1,2) + f(1,1) + f(1, 1)
    for i in range(2, n+1):
        for j in range(i, m+1):
            for k in range(i-1, j):
                dp[i][j] += dp[i-1][k]
    return dp[n][m]

num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    print(bridge(n,m))