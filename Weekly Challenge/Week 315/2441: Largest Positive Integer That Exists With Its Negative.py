class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]]+=1
        
        print(hashmap)

        res = -1
        for i in range(len(nums)):
            if nums[i] > res:
                if -nums[i] in hashmap:
                    res = max(res, nums[i])
        
        return res