class Solution:
    def orangesRotting(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        
        rotting, fresh = [],set()
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 2:
                    rotting.append((i,j))
                if grid[i][j] == 1:
                    fresh.add((i,j))
        #print(rotting, fresh)

        timer = 0
        while fresh and rotting:
            newr = []
            for i, j in rotting:
                for (d_r, d_c) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if (i+d_r, j+d_c) in fresh:
                        fresh.remove((i+d_r, j+d_c))
                        newr.append((i+d_r, j+d_c))
            rotting = newr
            timer += 1
        return -1 if fresh else timer

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))