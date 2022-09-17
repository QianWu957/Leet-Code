class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        ptr_s, ptr_t = 0, 0

        while ptr_s <= len(s)-1 and ptr_t <= len(t)-1:
            if s[ptr_s] == t[ptr_t]:
                ptr_s+=1
            ptr_t+=1
            
        if ptr_s == len(s):
            return True
        else:
            return False