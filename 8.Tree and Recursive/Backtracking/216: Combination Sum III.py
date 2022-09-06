class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backtrack(nums, index, n, res):
            if n < 0: return 
            elif index ==k and n==0:
                self.res.append(res)
                return

            for i in range(len(nums)):
                if len(nums) < k-index: continue  
                backtrack(nums[i+1:], index+1, n-nums[i], res+[nums[i]])
            return

        self.res = []
        backtrack(list(range(1,10)), 0, n, [])
        return self.res

