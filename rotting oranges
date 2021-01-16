class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        a = len(grid)
        if a == 0:
            return -1
        b = len(grid[0])
        l = []
        s = [(-1,0),(0,-1),(1,0),(0,1)]
        for i in range(a):
            for j in range(b):
                if grid[i][j] == 2:
                    l.append((i,j,0))
        t = 0
        while l:
            x,y,t = l.pop(0)
            for i,j in s:
                p,q = i+x,j+y
                if 0 <= p < a and 0 <= q < b and grid[p][q] == 1:
                    grid[p][q] = 2
                    l.append((p,q,t+1))
        for i in range(a):
            for j in range(b):
                if grid[i][j] == 1:
                    return -1
        return t
