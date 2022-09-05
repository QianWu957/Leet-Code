class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtracking(nums,comb):
            if not nums:
                self.res.append(comb)
                return

            for i in range(len(nums)):
                backtracking(nums[:i]+nums[i+1:], comb+ [nums[i]])
            return
        backtracking(nums,[])
        return self.res

        
