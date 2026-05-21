class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, x-y)
            
        heapq.heappush(heap, 0)
        return abs(heap[0])
        
