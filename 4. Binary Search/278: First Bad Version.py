# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l , r  = 1 , n
        while l<=r:
            mid = l+(r-l)//2
            if isBadVersion(mid):
                r = mid -1

            else:
                l = mid+1

        return l

if __name__ == '__main__':
    a = Solution()
    
    print(a.firstBadVersion())