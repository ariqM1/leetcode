class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minimum = float('inf')
        while l < r:
            mid = (l + r) // 2
            minimum = min(minimum, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return min(minimum, nums[l])
