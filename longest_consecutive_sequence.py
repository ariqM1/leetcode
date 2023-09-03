class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        window = set(nums)
        maxLength = 0

        for n in window:
            if (n - 1) not in window:
                length = 1
                while (n + length) in window:
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength
