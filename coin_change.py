class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = amount + 1
        dp = [n] * n
        dp[0] = 0

        for i in range(1, n):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
                    
        if dp[amount] == n:
            return -1
        return dp[amount]
