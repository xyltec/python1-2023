def get_best_value_package(costs: list[int], values: list[int], max_total_cost: int) -> int:
    n = len(costs)
    dp = [[0] * (max_total_cost + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_total_cost + 1):
            if costs[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j - costs[i-1]])

    return dp[n][max_total_cost]
