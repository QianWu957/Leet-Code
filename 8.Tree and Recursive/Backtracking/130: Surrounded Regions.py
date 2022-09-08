class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def backtrack(start_x, start_y):
            visited [start_x][start_y] = True
            for off in offset:
                next_x = start_x + off[0]
                next_y = start_y + off[1]
                if inbound(next_x,next_y) and not visited[next_x][next_y] and board[next_x][next_y] == 'O':
                    backtrack(next_x, next_y)
            return    
        
        
        def inbound(x,y):
            return x<m and x>=0 and y< n and y>=0

        if not board: return 
        m = len(board)
        n = len(board[0])
        offset = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False for _ in range(n)]for _ in range(m)]
        

        for i in range(m):
            if board[i][0] == 'O':
                backtrack(i,0)
            if board[i][n-1] =='O':
                backtrack(i,n-1)
        for j in range(n):
            if board[0][j] == 'O':
                backtrack(0,j)
            if board[m-1][j] =='O':
                backtrack(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and visited[i][j] == False:
                    board[i][j] = 'X'

        """
        Do not return anything, modify board in-place instead.
        """