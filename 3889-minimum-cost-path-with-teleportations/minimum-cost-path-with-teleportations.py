class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18
        
        # dist[i][j][t] = min cost to reach (i,j) using t teleports
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0
        
        # Min heap: (cost, i, j, used_teleports)
        pq = [(0, 0, 0, 0)]
        
        # Group cells by value
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        
        # For teleport optimization:
        # next_idx[t] tells how many cells (from sorted list) are already usable
        next_idx = [0] * (k + 1)
        
        while pq:
            cost, i, j, t = heapq.heappop(pq)
            if cost != dist[i][j][t]:
                continue
            
            # Normal moves
            if i + 1 < m:
                nc = cost + grid[i + 1][j]
                if nc < dist[i + 1][j][t]:
                    dist[i + 1][j][t] = nc
                    heapq.heappush(pq, (nc, i + 1, j, t))
            
            if j + 1 < n:
                nc = cost + grid[i][j + 1]
                if nc < dist[i][j + 1][t]:
                    dist[i][j + 1][t] = nc
                    heapq.heappush(pq, (nc, i, j + 1, t))
            
            # Teleport
            if t < k:
                # Activate all cells with value <= grid[i][j]
                while next_idx[t] < len(cells) and cells[next_idx[t]][0] <= grid[i][j]:
                    _, x, y = cells[next_idx[t]]
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][t + 1] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))
                    next_idx[t] += 1
        
        return min(dist[m - 1][n - 1])
        