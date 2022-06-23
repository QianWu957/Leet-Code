class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not s and not t: return True
        if not s or not t: return False
        if len(s) != len(t): return False


        hashmap_1 = dict.fromkeys(s,0)
        hashmap_2 = dict.fromkeys(t,0)

        for char in s:
            hashmap_1[char] +=1
        
        for char in t:
            hashmap_2[char] +=1

        if hashmap_1 == hashmap_2:
            return True
        
        else:
            return False

if __name__ == '__main__':
    a = Solution()
    s = "cinema"
    t = "iceman"
    print(a.isAnagram(s,t))