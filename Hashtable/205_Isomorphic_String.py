class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        if len(s) != len(t): return False
        
        mapst, mapts = dict(), dict()
        
        for i in range (len(s)):
            c1,c2 = s[i],t[i]
            if (c1 in mapst and mapst[c1]!=c2) or (c2 in mapts and mapts[c2]!=c1):
                 return False
            else:
                mapst[c1]=c2
                mapts[c2]=c1
        return True

if __name__ == '__main__':
    a = Solution()
    s = "paper"
    t = "title"
    print(a.isIsomorphic(s,t))
         

        
            

        

        


       