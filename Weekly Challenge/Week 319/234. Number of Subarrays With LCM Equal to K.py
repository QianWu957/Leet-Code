class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            l = 0
            for j in range(i,len(nums)):
                l = lcm(l, nums[j])
                if l == k:
                    res +=1
        
        return res