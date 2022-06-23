class Solution:
    def reverseVowels(self, s: str) -> str:

        if len(s)<1: return s

        s = list(s)

        head, tail = 0, len(s)-1
        
        vowels = set('aeiouAEIOU')

        while head < tail:
            if s[head] in vowels and s[tail] in vowels:
                s[head],s[tail]= s[tail],s[head]
                head +=1
                tail -=1
            
            elif s[head] in vowels:
                tail -= 1
            
            elif s[tail] in vowels:
                head +=1
            
            else:
                head +=1
                tail-=1
        
        return ''.join(s)

if __name__ == '__main__':
    a = Solution()
    s = 'hello'
    print (a.reverseVowels(s))