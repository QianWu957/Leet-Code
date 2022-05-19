class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 2: return True

        def isPalindrome(s, head, tail):
            while head < tail:
                if s[head] == s[tail]:
                    head +=1
                    tail -=1
                    continue
                else: return False
            return True

        head, tail =  0, len(s)-1
        while head < tail:
            if s[head] == s[tail]:
                head +=1
                tail -=1
                continue
            else: 
                return isPalindrome(s, head+1, tail) or isPalindrome(s, head,tail-1)
        return True
    

if __name__ == "__main__":
    a = Solution()
    s = "eeccccbebaeeabebcccee"
    print(a.validPalindrome(s))