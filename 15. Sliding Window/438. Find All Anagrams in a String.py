import collections
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []
        
        # left, right = 0, 0 
        need = len(p)
        res = []

        cnt = collections.Counter(p)
        
        for right in range(len(s)):
            ch = s[right]
            if ch in cnt:
                if cnt[ch] > 0:
                    need -=1
                cnt[ch]-=1


            left = right - len(p)
            if left >=0:
                ch = s[left]
                if ch in cnt:
                    if cnt[ch] >=0:
                        need +=1
                    cnt[ch] +=1
                
            if need ==0:
                res.append(right - len(p) +1)


            
        return res

if __name__ == '__main__':
    a = Solution()
    s = "cbaebabacd"
    p = "abc"
    
    print(a.findAnagrams(s,p))

               
