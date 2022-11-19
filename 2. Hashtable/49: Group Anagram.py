class Solution:
    def groupAnagrams(self, strs:[str]):
        hashmap = {}
        for item in strs:
            keys = "".join(sorted(item))
            if keys not in hashmap:
                hashmap[keys] = [item]
            else:
                hashmap[keys].append(item)
                # print(hashmap)
        # print(hashmap.values())
        return list(hashmap.values())

if __name__ == '__main__':
    a = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(a.groupAnagrams(strs))
        


                