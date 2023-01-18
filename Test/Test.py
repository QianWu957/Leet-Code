class Solution:
    def test(self, target:int, nums:[int] ):
        if not target or not nums:
            return 0
        m = len(nums)
        min_ = len(nums) +1
        res = 0
        left = 0
        for right in range(m):
            target -= nums[right]
            while target <=0:
                length = right - left + 1
                if length < min_:
                    min_ = length
                target += nums[left]
                left +=1
                
        if min_ != len(nums) + 1:
            return min_

        else:
            return 0
        
        # =-0-0-0
if __name__ == '__main__':
    a = Solution()
    target = 7
    nums = [7,3,1,2,4,3]
    print(a.test(target, nums))  