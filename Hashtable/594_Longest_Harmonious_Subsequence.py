class Solution:
    def findLHS(self, nums) -> int:
        if not nums: return 0
        if len(nums) < 2: return 0

        hashmap = {}
        for key in nums:
            if key in hashmap:
                hashmap[key]= hashmap.get(key,0)+1
            else:
                hashmap[key] =1
            # if key not in hashmap:
            #     hashmap[key] = 1
            # else:
            #     hashmap [key] +=1
        res = 0
        
        for k, v in hashmap.items():
            if hashmap.get(k+1,0) !=0:
                res = max(res, hashmap[k+1]+hashmap[k])
        return res
            
if __name__ == '__main__':
    a = Solution()
    n = [1,3,2,2,5,2,3,7]
    print(a.findLHS(n))


        # if not nums: return 0
        # if len(nums)<2: return 0

        # hashmap = {}
        # for key in nums:
        #     if key not in hashmap:
        #         hashmap[key] = 1
        #     else:
        #         hashmap[key] +=1
        # #     hashmap[num] = hashmap.get(num, 0) + 1
        # # print(hashmap)
        # res = 0 
        # for k, v in hashmap.items():
        #     if hashmap.get(k+1, 0) != 0:
        #         res = max(res, hashmap.get(k+1)+v)
        # return res