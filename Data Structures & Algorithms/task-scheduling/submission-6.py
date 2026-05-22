class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)
        q = deque()
        t = 0

        while heap or q:
            t += 1

            if not heap:
                t = q[0][1]
            else:
                count = 1 + heapq.heappop(heap)
                if count < 0:
                    q.append([count, t + n])
            
            if q and q[0][1] == t:
                heapq.heappush(heap, q.popleft()[0])

            
        return t