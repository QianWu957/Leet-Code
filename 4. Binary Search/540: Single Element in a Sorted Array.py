class Solution:
    def singleNonDuplicate(self, nums) -> int:
        l , r = 0 , len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if (nums[mid]!= nums[mid-1]) and (nums[mid]!= nums[mid+1]):
                return nums[mid]
            
            if (mid%2==0 and nums[mid+1] == nums[mid])or(mid%2==1 and nums[mid]==nums[mid-1]):
                l = mid +1
            else:
                r = mid -1
        return nums[l]

if __name__ == '__main__':
    a = Solution()
    input = [1,1,2,3,3,4,4,8,8]
    print(a.singleNonDuplicate(input))

        # l, r = 0 , len(nums)-1
        # while l < r:
        #     m = l +(r-l) // 2

        #     if (nums[m] != nums[m+1])and(nums[m] != nums[m-1]):
        #         return nums[m]

        #     if ( m%2 == 0 and nums[m+1]==nums[m]) or ( m%2 == 1 and nums[m-1]==nums[m]):
        #         l = m +1
        #     else:
        #         r = m-1
        # return nums[l]

       