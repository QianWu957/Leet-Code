class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(index, row):

            if index == n:
                self.res.append(generateboard(n, row))
                return

            for i in range(n):
                if not col[i] and not diag1[index+i] and not diag2[index-i+n-1]:
                    col[i] = True
                    diag1[index+i] = True
                    diag2[index-i+n-1] = True
                    row.append(i)
                    backtrack(index+1,row)
                    col[i] = False
                    diag1[index+i] = False
                    diag2[index-i+n-1] = False
                    row.pop()
            return

        def generateboard(n,row):
            board = [['.' for _ in range(n)]for _ in range(n)]
            for i in range(len(row)):
                board[i][row[i]] = 'Q'
            return [''.join(board[i]) for i in range(len(board))]


        self.res = []
        col = [False for _ in range(n)]
        diag1 = [False for _ in range(2*n-1)]
        diag2 = [False for _ in range(2*n-1)]
        backtrack(0,[])
        return self.res

         