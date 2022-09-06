class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, res):
            if target <  0: return
            if target == 0:
                self.res.append(res)
                return

            for i in range(len(candidates)):
                backtrack(candidates[i:], target-candidates[i], res+[candidates[i]])
            return

        self.res = []
        backtrack(candidates, target , [])
        return self.res