class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]
                
        def robbing(nums):
            if len(nums) == 1:
                return nums[0]

            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]

            for i in range(1, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            return dp[n-1]

        # dont rob first house
        first = robbing(nums[1:])
        # dont rob last house
        last = robbing(nums[:-1])

        print(first, last)


        return max(first, last)
        
        