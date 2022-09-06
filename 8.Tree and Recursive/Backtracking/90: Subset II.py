class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,res):
            self.res.append(res)
            if not nums: return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: continue
                backtrack(nums[i+1:], res+ [nums[i]])
            return

        self.res = []
        nums.sort()
        backtrack(nums,[])
        return self.res

        
        