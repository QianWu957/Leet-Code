class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        ROWS, COLS = len(matrix),len(matrix[0])
        top, bot = 0, ROWS-1
        while top <= bot:
            row = top + (bot-top)//2
            if target > matrix[row][-1]:
                top = row +1
            elif target < matrix[row][0]:
                bot = row -1
            else:
                break

        if not (top<=bot):
            return False
        row = top+(bot-top)//2
        l,r = 0, COLS-1
        while l <= r:
            mid = l+(r-l)//2
            if target < matrix[row][mid]:
                r = mid-1
            elif target > matrix[row][mid]:
                l = mid+1
            else:
                return True
        return False
if __name__ == '__main__':
    a = Solution()
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    t = 3
    print(a.searchMatrix(m,t))








