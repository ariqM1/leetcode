class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            distance = math.sqrt((point[0]*point[0]) + (point[1] * point[1]))
            heappush(minHeap, (distance, point))
        
        res = []
        while k > 0:
            answer = heappop(minHeap)[1]
            res.append(answer)
            k -= 1

        return res        