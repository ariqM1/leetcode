class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        r, c = (len(coins)+1), (amount+1)
        dp = [[0] * c for i in range(r)]

        for row in range(r):
            dp[row][0] = 1

        for row in range(r):
            for col in range(c):
                if row - 1 >= 0:
                    dp[row][col] = dp[row-1][col]
                    if col - coins[row-1] >= 0:
                        dp[row][col] += dp[row][col - coins[row-1]]
    
        return dp[len(coins)][amount]