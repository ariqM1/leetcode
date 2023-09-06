class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True
        if nums[0] == 0:
            return False
        
        dp = [0] * n
        dp[0] = (True, nums[0])
        for i in range(1, n):
            if dp[i-1][1] + (i-1) >= i:
                dp[i] = (True, max(dp[i-1][1] - 1, nums[i]))
            else:
                dp[i] = (False, 0) 
        
        return dp[n-1][0]


        