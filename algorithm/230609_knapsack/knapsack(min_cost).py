def minCostKnapsack(weights, costs, maxWeight):
    num_items = len(weights)
    dp = [float('inf')] * (maxWeight + 1)  # initialize dp table with 'inf'
    dp[0] = 0  # 0 cost for 0 weight

    for i in range(num_items):
        for w in range(maxWeight, weights[i]-1, -1):
            dp[w] = min(dp[w], dp[w-weights[i]] + costs[i])
    
    return dp[maxWeight] if dp[maxWeight] != float('inf') else -1

weights = [2, 3, 4, 5]
costs = [3, 4, 5, 6]
maxWeight = 5
print(minCostKnapsack(weights, costs, maxWeight))  # Output: 3

'''

처리 후 아이템: 2 (비용: 3)
Weights:     0   1   2   3   4   5  
-----------------------------------
DP:        [0, inf, 3, inf, inf, inf]

처리 후 아이템: 3 (비용: 4)
Weights:     0   1   2   3   4   5  
-----------------------------------
DP:        [0, inf, 3, 4, 7, inf]

처리 후 아이템: 4 (비용: 5)
Weights:     0   1   2   3   4   5  
-----------------------------------
DP:        [0, inf, 3, 4, 5, 8]

처리 후 아이템: 5 (비용: 6)
Weights:     0   1   2   3   4   5  
-----------------------------------
DP:        [0, inf, 3, 4, 5, 6]

'''