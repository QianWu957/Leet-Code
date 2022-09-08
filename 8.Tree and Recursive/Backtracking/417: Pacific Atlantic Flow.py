class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def backtrack(start_x, start_y, visited):
            visited[start_x][start_y] = True
            for off in offset:
                next_x = start_x + off[0]
                next_y = start_y + off[1]
                if inboard(next_x, next_y) and not visited[next_x][next_y] and matrix[next_x][next_y] >= matrix[start_x][start_y]:
                    backtrack(next_x,next_y,visited)
            return

        def inboard(x, y):
            return x<m and x>=0 and y<n and y>=0



        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        offset = [(-1,0),(1,0),(0,-1),(0,1)]
        visited1 = [[False for _ in range(n)] for _ in range(m)]
        visited2 = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            if not visited1[i][0]:
                backtrack(i, 0, visited1)
            if not visited2[i][n-1]:
                backtrack(i, n-1, visited2)

        for j in range(n):
            if not visited1[0][j]:
                backtrack(0, j, visited1)
            if not visited2[m-1][j]:
                backtrack(m-1, j, visited2)

        res = []
        for i in range(m):
            for j in range(n):
                if visited1[i][j] and visited2[i][j]:
                    res.append([i,j])
        return res