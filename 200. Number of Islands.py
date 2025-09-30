
class Solution(object):
    """
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
    """
    def numIslands(self, grid):
        islands = 0
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands+=1
                    self.clearIsland(grid,i,j)
        return islands
                
    def clearIsland(self,grid,i,j):
        if j < len(grid[0])-1: # Right
            if grid[i][j+1] == '1':
                grid[i][j] = '0'
                self.clearIsland(grid,i,j+1)
        if j > 0:
            if grid[i][j-1] == '1': # Left
                grid[i][j] = '0'
                self.clearIsland(grid,i,j-1)
        if i < len(grid)-1:
            if grid[i+1][j] == '1': # Down
                grid[i][j] = '0'
                self.clearIsland(grid,i+1,j)
        if i > 0:
            if grid[i-1][j] == '1': # Up
                grid[i][j] = '0'
                self.clearIsland(grid,i-1,j)
        grid[i][j] = '0'