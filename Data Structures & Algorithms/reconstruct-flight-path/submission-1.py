class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets):
            graph[src].append(dst)
        itinerary = []
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop(0)
                dfs(next_airport)
            itinerary.append(airport)
        dfs("JFK")
        return itinerary[::-1]