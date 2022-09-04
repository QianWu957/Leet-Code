class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        letter = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res = []
        def backtracking(index,curStr):
            if index >= len(digits):
                res.append(curStr)
                return
        
            for i in letter[digits[index]]:
                backtracking(index+1,curStr+i)
            return
        backtracking(0,'')

        return res
      