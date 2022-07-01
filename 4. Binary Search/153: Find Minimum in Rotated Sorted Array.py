class Solution:
    def findMin(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        if nums[-1] > nums[0]: return nums[0]
        l ,r = 0, len(nums)-1
        
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[mid] > nums[-1]:
                l = mid+1

            elif nums[mid] < nums[-1]:
                r = mid-1   

if __name__ == '__main__':
    a = Solution()
    n = [3,4,5,1,2]
    print(a.findMin(n))

