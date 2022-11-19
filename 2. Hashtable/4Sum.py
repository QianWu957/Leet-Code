class Solution:
    def fourSum(self, nums, target):

        if not nums or len(nums)<4: return []
        nums.sort()
        res, quad = [],[]

        def kSum (k, start, target):
            if k!=2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue 
                    quad.append(nums[i])
                    kSum(k-1, i+1, target - nums[i])
                    quad.pop()
                return

            left, right = start, len(nums)-1
            while left < right:
                if nums[left] + nums[right] > target:
                    right-=1
                elif nums[left] + nums[right] < target:
                    left+=1
                elif target == nums[left] + nums[right]:
                    res.append(quad + [nums[left],nums[right]])
                    left +=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
        kSum(4,0,target)
        return res
    
if __name__ == '__main__':
    a = Solution()
    n = [1,0,-1,0,-2,2]
    tar = 0
    print(a.fourSum(n,tar))
