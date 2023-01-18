class Solution:
    def groupAnagrams(self, strs:[str]):
        hashmap = {}
        for item in strs:
            keys = "".join(sorted(item))
            if keys not in hashmap:
                hashmap[keys] = [item]
            else:
                hashmap[keys].append(item)
      
        comb = list(hashmap.values())
        # print(list(hashmap.values()))
        
        for i in range(len(comb)):
            if len(comb[i]) > 1:
                return 11111
            else:
                return -1
        # return list(hashmap.values())

if __name__ == '__main__':
    a = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(a.groupAnagrams(strs))
        


                