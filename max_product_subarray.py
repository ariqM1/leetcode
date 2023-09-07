class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        res = nums[0]
        currMin, currMax = 1, 1

        for i in nums:
            temp = currMax * i
            currMax = max(currMax * i, currMin * i, i)
            currMin = min(temp, currMin * i, i)
            res = max(res, currMax)

        return res
        