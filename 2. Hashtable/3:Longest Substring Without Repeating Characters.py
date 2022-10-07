class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        hashmap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hashmap:
                hashmap.pop(s[l])
                l+=1
            hashmap[s[r]] =1
            res = max(res, r-l+1)
        return res
