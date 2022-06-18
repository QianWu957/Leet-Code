class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k < 0:
             return False
        hashmap = {}
        buck_num = 0
        for i in range(len(nums)):
            buck_num = nums[i] // (t+1)
            if buck_num not in hashmap:
                hashmap[buck_num] = nums[i]
            else:
                return True

            if (buck_num - 1) in hashmap and abs(hashmap[buck_num-1] - hashmap[buck_num]) <= t:
                    return True
            if (buck_num + 1) in hashmap and abs(hashmap[buck_num+1] - hashmap[buck_num]) <= t:
                    return True
            hashmap[buck_num] = nums[i]
            if len(hashmap) > k:
                hashmap.pop(nums[i-k]//(t+1))
        return False


        # all_buckets = {}
        # bucket_size = t + 1                     # 桶的大小设成t+1更加方便
        # for i in range(len(nums)):
        #     bucket_num = nums[i] // bucket_size # 放入哪个桶
            
        #     if bucket_num not in all_buckets:  
        #         all_buckets[bucket_num] = nums[i]   # 把nums[i]放入桶中   
        #     else:
        #         return True # 桶中已经有元素了
                  
            
        #     if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t: # 检查前一个桶
        #         return True
            
        #     if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t: # 检查后一个桶
        #         return True
            
        #     # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
        #     if i >= k:
        #         all_buckets.pop(nums[i-k]//bucket_size)
                
        # return False

