class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = 1
        prefix_list = [1] * n

        for i in range(n):
            prefix_list[i] = prefix
            prefix *= nums[i]
            

        print(prefix_list)

        suffix = 1
        suffix_list = [1] * n

        for i in range(n-1, -1, -1):
            suffix_list[i] = suffix
            suffix *= nums[i]


        res = [1] * n
        for i in range(n):
            res[i] = prefix_list[i] * suffix_list[i]
        
        return res

