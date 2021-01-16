class Solution:
    def search(self, i, j, rows, cols, grid):
        if i >= rows or i < 0:
            return
        if j >= cols or j < 0:
            return
        if grid[i][j] != "1":
            return
        
        grid[i][j] = "0"
        
        self.search(i + 1, j, rows, cols, grid)
        self.search(i - 1, j, rows, cols, grid)
        self.search(i, j + 1, rows, cols, grid)
        self.search(i, j - 1, rows, cols, grid)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.search(i, j, rows, cols, grid)
                    
        return num_islands
