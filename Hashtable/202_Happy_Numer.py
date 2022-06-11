class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1: return True
        # visited = {}
        visited = set()
        # print (visited)

        while True:
            if n == 1: return True
            elif n in visited: return False
            visited.add(n)
            n = sum(int(nums)**2 for nums in str(n))

        
if __name__ == '__main__':
    a = Solution()
    n = 19
    print(a.isHappy(n))





    



            
