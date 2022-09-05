class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtrack(nums, comb):
            if not nums and comb not in self.res:
                self.res.append(comb)
                return
            
            
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], comb + [nums[i]])
            return
        backtrack(nums,[])
        return self.res
