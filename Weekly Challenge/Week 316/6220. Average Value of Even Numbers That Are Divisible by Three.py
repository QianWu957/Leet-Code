class Solution:
    def averageValue(self, nums: List[int]) -> int:
        counter = 0
        res = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] % 3 == 0:
                counter +=1
                res +=nums[i]
        if counter!= 0:
            return int(res / counter)
        else:
            return 0
       
                
        # return ans if counter!=0 else 0