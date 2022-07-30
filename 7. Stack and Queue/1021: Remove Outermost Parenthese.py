class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = []
        
        # for char in s:
        #     if char == '(':
        #         stack.append(char)
        #         if len(stack) > 1:
        #             res.append(char)
        #         else: continue
        #     elif char == ')': 
        #         stack.pop()
        #         if len(stack) >0: 
        #             res.append(char)
        #         else:
        #             continue
        # return ''.join(res)

        for c in s:
            if c == ')':
                stack.pop()
            if stack:
                res.append(c)
            if c == '(':
                stack.append(c)
        return ''.join(res)

if __name__ == '__main__':
    a = Solution()
    n = "(()())(())"
    print(a.removeOuterParentheses(n))

        

        