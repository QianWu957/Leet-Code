class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            
            if row == n:
                return 1
            else:
                counter = 0
            
            for i in range(n):
                if i not in col and (row+i) not in posDiag and (row-i) not in negDiag:
                    col.add(i)
                    posDiag.add(row+i)
                    negDiag.add(row-i)
                    counter += backtrack(row+1)
                    col.remove(i)
                    posDiag.remove(row+i)
                    negDiag.remove(row-i)
            return counter

        col = set()
        posDiag = set()
        negDiag = set()
        return backtrack(0)
