class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        # hashmap = {}
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if hashmap.get(j-i) is None:
        #             hashmap[j-i] = matrix[i][j]
        #             print(hashmap[j-i])
        #         else:
        #             if hashmap[j-i] != matrix[i][j]:
        #                 return False
        # return True
        row = len(matrix)
        col = len(matrix[0])

        for i in range (row-1):
            for j in range (col-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

if __name__ == '__main__':
    a = Solution()
    n =  [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print(a.isToeplitzMatrix(n))         
 