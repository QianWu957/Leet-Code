class Solution:
    def twoSum(self, nums, target: int):
        
        hash_map = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hash_map:
                return [hash_map[diff], idx] 
            else:
                hash_map[val] = idx
     # init solution by two pointers
        # if not nums: return None
        # slow, fast = 0, 1
        # while slow < len(nums) and nums[slow] + nums[fast] != target:
        #     fast +=1
        #     if fast == len(nums):
        #         slow +=1
        #         fast = slow+1
        # return [slow, fast]

if __name__ == '__main__':
    a = Solution()
    n = [2,7,11,15]
    t = 9
    print (a.twoSum(n,t))