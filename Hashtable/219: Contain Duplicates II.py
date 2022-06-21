class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums: return False
        hashset = set()
        for i in range(len(nums)):
            # print(hashset)
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
            if len(hashset)>k:
                hashset.remove(nums[i-k])
        return False
if __name__ == '__main__':
    a = Solution()
    n = [1,2,3,1]
        # hashset = {}
        # for i in range(len(nums)):
        #     # print(hashset)
        #     if nums[i] not in hashset:
        #         hashset[nums[i]] = 0
        #     else:
        #         return True
            
        #     print(len(hashset))
        #     if len(hashset)>k:
        #         hashset.pop(nums[i-k])
            
        # return False

        # # if len(nums) == len(set(nums)):
        # #     return False
        
        # # for i in range (len(nums)):
        # #     for j in range(i+1,len(nums)):
        # #         if i!=j and nums[i] == nums[j] and j-i <=k:
        # #             return True
        # # return False