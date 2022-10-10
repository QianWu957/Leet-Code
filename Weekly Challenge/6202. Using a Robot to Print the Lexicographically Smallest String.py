class Solution:
    def robotWithString(self, s: str) -> str:
       
        st = []
        alpha = ord("a")
        print(alpha)
        res = []
        hashmap = {}
        for i in range(len(s)):
            if ord(s[i]) not in hashmap:
                hashmap[ord(s[i])] = 1
            else:
                hashmap[ord(s[i])]+=1

        for i in range(len(s)):
            st.append(s[i])
            hashmap[ord(s[i])]-=1
            while alpha < ord("z") and (alpha not in hashmap or (alpha in hashmap and hashmap[alpha] == 0)):
                alpha +=1

            while st and chr(alpha) >= st[-1]:
                res.append(st.pop())
        
        return "".join (res)
            
            

