class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = collections.Counter(s1)
        print(counter1)
        l = 0
        r = len(s1)-1

        window = collections.Counter(s2[0:r])

        print(window)
        while r < len(s2):
            window[s2[r]] += 1
            
            if counter1 == window:
                return True
            window[s2[l]]-=1

            if window[s2[l]] == 0:
                del window[s2[l]]
            l+=1
            r+=1
        return False
            
         


        


        
     

















