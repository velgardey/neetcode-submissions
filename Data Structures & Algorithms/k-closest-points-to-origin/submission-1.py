class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for [x, y]  in points:
            dist = (x**2) + (y**2)
            res.append([dist, x, y])
        heapq.heapify(res)
        result = []
        for i in range(k):
            dist, x, y = heapq.heappop(res)
            result.append([x, y])
        return result