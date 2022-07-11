class Solution:
    def findErrorNums(self, nums) ->[int]:
        hashmap = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] +=1
        # print(hashmap)
        # print(nums[-1])
        for k, v in hashmap.items():
            if hashmap[k] != 1:
                res.append(k)
               
        # print(hashmap)
        for i in range(1, len(nums)+1):
            if i not in hashmap:
                missing = i
                res.append(missing)
                    
        return res

if __name__ == '__main__':
    a = Solution()
    n = [1,2,2,4]
    print(a.findErrorNums(n))
        # set_num = set(nums)
        # print(set_num)
        # nums.sort()
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         dul = nums[i]
        # for i in range(1, len(nums)+1):
        #     if i not in set_num:
        #         missing = i
        # return [dul, missing]
       