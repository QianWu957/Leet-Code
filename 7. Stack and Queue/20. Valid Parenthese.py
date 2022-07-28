class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in hashmap:
                stack.append(char)

            else:
                if not stack or hashmap[stack.pop()] != char:
                    return False
        if not stack:
            return True
        else:
            return False
                 

            
            
                

      