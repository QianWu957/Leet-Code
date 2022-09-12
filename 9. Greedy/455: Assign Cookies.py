class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()

        res = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i+=1
                j+=1
                res+=1
            else:
                j+=1
       
        return res

if __name__ == '__main__':
    a = Solution()
    g = [1,2,3]
    s = [1,1,3]
    print(a.findContentChildren(g,s))
    
