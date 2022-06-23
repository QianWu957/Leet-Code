class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        print(nums)
        for i , v in enumerate(nums):
            if i >0 and v == nums[i-1]:
                continue
            left , right = i+1, len(nums)-1 # v从最后一个重复的数开始算
            while left < right:
                threesum = v + nums[left] + nums[right]
                if threesum > 0:
                    right -=1
                elif threesum < 0:
                    left+=1
                else:
                    res.append([v, nums[left], nums[right]])
                    left +=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
        return res


if __name__ == '__main__':
    a = Solution()
    input = [-1,0,1,2,-1,-4]
    print(a.threeSum(input))