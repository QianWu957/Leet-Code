class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def backtrack(grid, start_x, start_y ):
            visited [start_x][start_y] = True

            for off in offset:
                next_x = start_x+ off[0]
                next_y = start_y+ off[1]
                if inbound(next_x, next_y) and not visited[next_x][next_y] and grid [next_x][next_y] =='1':
                    backtrack(grid, next_x, next_y)
            return

        def inbound(x,y):
            return x<m and x>=0 and y< n and y>=0

        if not grid: return 0
        
        m = len(grid)
        n = len(grid[0])
        offset = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0
        # print(existed)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    res+=1
                    backtrack(grid, i, j)
        return res

           