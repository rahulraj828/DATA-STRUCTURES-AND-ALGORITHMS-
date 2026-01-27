import heapq
import math

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list
        # For each edge [u, v, w], we add:
        # 1. Forward edge: u -> v with cost w
        # 2. Backward edge: v -> u with cost 2 * w (representing the switch)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))
        
        # Dijkstra's Algorithm
        # Priority Queue stores tuples of (current_cost, current_node)
        pq = [(0, 0)]
        
        # Distance array to track minimum cost to each node
        min_cost = [math.inf] * n
        min_cost[0] = 0
        
        while pq:
            cost, u = heapq.heappop(pq)
            
            # If we found a shorter path to u already, skip processing
            if cost > min_cost[u]:
                continue
            
            # If we reached the target node
            if u == n - 1:
                return cost
            
            for v, weight in adj[u]:
                new_cost = cost + weight
                if new_cost < min_cost[v]:
                    min_cost[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
                    
        return -1