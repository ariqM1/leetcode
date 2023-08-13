class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            print(i, subset)
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include i in subset
            subset.append(nums[i])
            dfs(i + 1)

            # decision to not include nums[i] in subset
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res 