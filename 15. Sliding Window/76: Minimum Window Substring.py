class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, counteT = {}, {}
        
        for c in t:
            counteT[c] = 1+ counteT.get(c,0)
        
        # print(counteT)
        have, need = 0, len(counteT)
        res, resLen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1+ window.get(s[r],0)
            # print(window)
            if s[r] in counteT and window[s[r]] == counteT[s[r]]:
                have+=1

            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1

                if s[l] in counteT and window[s[l]] < counteT[s[l]]:
                    have -=1
                l+=1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
                
                



            



     