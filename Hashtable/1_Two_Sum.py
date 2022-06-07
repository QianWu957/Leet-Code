class Solution:
    def twoSum(self, nums, target: int):
        
        hash_map = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hash_map:
                return [hash_map[diff], idx] 
            else:
                hash_map[val] = idx

if __name__ == '__main__':
    a = Solution()
    n = [2,7,11,15]
    t = 9
    print (a.twoSum(n,t))