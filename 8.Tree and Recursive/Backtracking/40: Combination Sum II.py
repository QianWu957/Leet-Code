class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates,target,res):
            if target < 0: return
            elif target == 0:
                self.res.append(res)
                return

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]: continue
                backtrack(candidates[i+1:], target-candidates[i], res+[candidates[i]])
            return
        self.res = []
        candidates.sort()
        backtrack(candidates, target, [])
        print(candidates)
        return self.res
