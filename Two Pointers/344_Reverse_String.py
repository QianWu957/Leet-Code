class Solution:
    def reverseString(self, s: List[str]) -> None:
        if not s: return []
        head, tail = 0, len(s)-1

        while head < tail:
            s[head], s[tail] = s[tail],s[head]
            head+=1
            tail-=1
            continue
    

        """
        Do not return anything, modify s in-place instead.
        """