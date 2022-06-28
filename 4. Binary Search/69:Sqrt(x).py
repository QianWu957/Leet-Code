class Solution:
    def mySqrt(self, x: int):
        l, r, res= 0, x , 0
        while l <= r:
            mid = (l+r)//2
            if mid * mid <= x:
                res = mid
                l = mid +1
            else:
                r = mid -1
        return res
if __name__ == '__main__':
    a = Solution()
    input = 4
    print(a.mySqrt(input))


        # l, r = 0, x//2+1
        # while l<=r:
        #     m = (l+r) //2
        #     s1 = m ** 2
        #     s2 = (m + 1) ** 2

        #     if s1 < x and s2 > x or s1 == x:
        #         return m
        #     if s2 == x:
        #         return m + 1

        #     if s1 > x:
        #         r = m - 1 
        #     elif s2 < x:
        #         l = m + 1
        # return

        # l, r, res = 0, x, 0
        # mid = l+ (r-l) //2
        # if mid * mid > x:
        #     r = mid -1
        # elif mid * mid < x:
        #     l = mid +1
        # elif mid * mid == res:
        #     return res
        # return res
           
