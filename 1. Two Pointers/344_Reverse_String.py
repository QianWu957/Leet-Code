class Solution:
    def reverseString(self, s):
        if not s: return False

        b = str[0]

        s = b[::-1]

    
        return s
    
        # if not s: return []
        # head, tail = 0, len(s)-1

        # while head < tail:
        #     s[head], s[tail] = s[tail],s[head]
        #     head+=1
        #     tail-=1
        #     continue

if __name__ == '__main__':
     a = Solution()
     str = ['aaaaccccccbbbbb']
     print(a.reverseString(str))



"""
Do not return anything, modify s in-place instead.
"""