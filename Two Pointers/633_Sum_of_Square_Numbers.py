from math import sqrt
class Solution:
    def judgeSquareSum(self, numbers, c: int):

        if c < 0: return False
        #assert c >= 0 
        head, tail = 0, int(sqrt(c))
        
        # print(111111111)
        while head <= tail:
            _sum = head **2 + tail **2
            if _sum < c:
                head += 1

            elif _sum > c:
                tail -= 1 
        
            else:
                return True
            print(head, tail, _sum, c)
        return False 

if __name__ == "__main__":

    a = Solution()

    numbers = [1,2,4,6,8,10]
    c = 101
    print(a.judgeSquareSum(numbers,c))

