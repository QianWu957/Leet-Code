class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        
       if not matrix: return False
       i , j = 0, len(matrix[0])-1

       while (i <=len(matrix)-1 and j >= 0):
           if matrix[i][j] == target:
               return True

           elif matrix[i][j] > target:
               j -=1
           
           elif matrix[i][j] < target:
               i+=1

       return False   

if __name__ == '__main__':
    a = Solution()
    m = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    t = 5
    print(a.searchMatrix(m,t))

        # combine = sum(matrix,[])

        # combine.sort()
    

        # l,r = 0, len(combine)-1
        # while l<=r:
        #     mid = l+(r-l)//2

        #     if target < combine[mid]:
        #         r = mid-1
        #     elif target > combine[mid]:
        #         l = mid+1
        #     elif target == combine[mid]:
        #         return True
        # return False