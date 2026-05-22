class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        r, c = len(grid), len(grid[0])
        islands = 0

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]=='0':
                return
            grid[i][j] = "0"
            for dr, dc in directions:
                dfs(i+dr, j+dc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    islands+=1
        
        return islands
        