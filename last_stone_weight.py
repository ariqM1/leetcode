class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for stone in stones:
            heapq.heappush(minHeap, -stone)
        
        while len(minHeap) > 1:
            x, y = heapq.heappop(minHeap), heapq.heappop(minHeap)
            x, y = -x, -y
            if x-y > 0:
                heapq.heappush(minHeap, -(x-y))
        heapq.heappush(minHeap, 0)
        return abs(minHeap[0])