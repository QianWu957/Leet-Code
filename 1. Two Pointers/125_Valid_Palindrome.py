class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 1:
             return True

        head, tail = 0, len(s)-1
        while head < tail:
            if s[head].isalnum() and s[tail].isalnum():
                if s[head].lower() == s[tail].lower():
                    head +=1
                    tail -=1
                    continue
                else:
                    return False
            elif s[head].isalnum(): tail -=1
            elif s[tail].isalnum(): head +=1
            else:
                head +=1
                tail -=1
        return True

if __name__ == '__main__':
    a = Solution()
    s = "A man, a plan, a canal: Panama"
    print(a.isPalindrome(s))

