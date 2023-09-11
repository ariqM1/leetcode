class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 1
        
        dp = [1] * n
        latest = nums[0]

        for j in range(1, n):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return max(dp)