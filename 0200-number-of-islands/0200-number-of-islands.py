class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                dfs(r, c+1)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r-1, c)
        
        islands = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands+=1
        
        return islands