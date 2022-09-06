class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, res):
            self.res.append(res)
            if not nums:return
                
            for i in range(len(nums)):
                print(i,nums)
                backtrack(nums[i+1:], res + [nums[i]])
            return
        self.res = []
        backtrack(nums,[])
        return self.res 