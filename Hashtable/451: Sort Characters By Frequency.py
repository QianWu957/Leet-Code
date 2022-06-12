class Solution:
    def frequencySort(self, s: str) -> str:
        if not s: return ''

        hashmap = dict.fromkeys(s, 0)
        for char in s:
            hashmap[char] += 1
        # print(hashmap)
        tuple_ = sorted(hashmap.items(), key = lambda kv:(kv[1],kv[0]), reverse= True) 
        # print(tuple_)
        res = []
        for k, v in tuple_:
            for i in range(v):
                res.append(k)
        return ''.join(res)


if __name__ == '__main__':
    a = Solution()
    string = "tree"
    print(a.frequencySort(string))