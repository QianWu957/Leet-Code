class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(nums, index, res):
            if index >= k:
                self.res.append(res)
                return
            
            for i in range(len(nums)):
                if len(nums) < k-index: continue
                backtrack(nums[i+1:], index+1,res+[nums[i]])
            return

        self.res = []
        backtrack(list(range(1,n+1)), 0 , [])
        return self.res