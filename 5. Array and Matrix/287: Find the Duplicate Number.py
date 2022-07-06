class Solution:
    def findDuplicate(self, nums) -> int:
        l , r = 1, len(nums)
        while l<r:
            mid = l+(r-l)//2
            counter = 0
            for num in nums:
                if num <= mid:
                    counter+=1

            if counter > mid:
                r = mid
            else:
                l = mid+1
        return l
if __name__ == '__main__':
    a = Solution()
    n = [1,3,4,2,2]
    print(a.findDuplicate(n))
                    

        # slow , fast = 0 , 1
        # res = 0
        # while slow < fast and fast<= len(nums):
        #     if nums[slow] != nums[fast]:
        #         # print(slow)
        #         print(fast)

        #         fast +=1
        #         if fast == len(nums)-1:
        #             slow+=1
        #             fast = slow+1
        #     else:
        #         return nums[slow]