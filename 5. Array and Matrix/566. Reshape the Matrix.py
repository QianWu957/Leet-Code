class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat: return 0
        if len(mat) * len(mat[0]) != r * c: return mat

        res = [[0]*c for _ in range(r)]
        for x in range (r*c):
            res[x//c][x%c] = mat[x//len(mat[0])][x%len(mat[0])] 
        return res
    