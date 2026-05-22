class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+ dr, c+dc

                if nr<0 or nc<0 or nr>=rows or nc>=cols:
                    continue
                
                if grid[nr][nc] != 2147483647:
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))

        