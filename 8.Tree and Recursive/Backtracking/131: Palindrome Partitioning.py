class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        def backtracking(s,comb):
            if not s:
                self.res.append(comb)
                return

            for i in range(1, len(s)+1):
                if s[:i] != s[:i][::-1]:
                    continue
                backtracking(s[i:], comb+[s[:i]])
            return
        backtracking(s,[])
        return self.res


