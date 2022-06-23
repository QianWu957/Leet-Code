class Solution:
    def groupAnagrams(self, strs):
        if not strs: return []
        hashmap = {}
        for i in range(len(strs)):
            alist = [0]*26
            for j in range(len(strs[i])):
                alist[ord(strs[i][j]) - ord('a')] +=1
            atuple = tuple(alist)
            if atuple not in hashmap:
                hashmap[atuple] = []
            hashmap[atuple].append(strs[i])
        res = []
        for k, v in hashmap.items():
            res.append(v)
        return res
if __name__ == '__main__':
    a = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(a.groupAnagrams(strs))
        


                