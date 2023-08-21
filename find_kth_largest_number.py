from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for num in nums:
            heappush(maxHeap, num)

        while len(maxHeap) > k:
            heappop(maxHeap)

        return maxHeap[0]
