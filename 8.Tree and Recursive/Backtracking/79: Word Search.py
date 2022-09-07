class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(index, start_x, start_y):
            if index == len(word)-1:
                return board[start_x][start_y] == word[index]
            if board[start_x][start_y] != word[index]:
                return False
            visited[start_x][start_y] = True
            for off in offset:
                next_x = start_x + off[0]
                next_y = start_y + off[1]
                if inbound(next_x,next_y) and not visited[next_x][next_y]:
                    if backtrack(index+1, next_x, next_y): return True
            visited [start_x][start_y] = False
            return False


        def inbound(x,y):
            return x < m and x>=0 and y < n and y >=0         

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        offset = [(-1,0),(1,0),(0,1),(0,-1)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(0, i, j):
                        return True
        return False
                    

                




       