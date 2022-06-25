class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        if not mat: return 0
        if len(mat) * len(mat[0]) != r * c: return mat

        res = [[0]*c for _ in range(r)]
        for x in range (r*c):
            res[x//c][x%c] = mat[x//len(mat[0])][x%len(mat[0])] 
        return res

if __name__ == '__main__':
    a = Solution()
    n=[[1,2],[3,4]]
    r=1
    c=4
    print(a.matrixReshape(n,r,c))