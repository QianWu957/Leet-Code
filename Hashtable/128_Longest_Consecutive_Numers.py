class Solution:
    def longestConsecutive(self, nums) -> int:
        'Control from element perspective'
        # if not nums: return 0

        # hashmap = {}

        # longest = 0
        # for j in nums:
        #     if j not in hashmap:
        #         hashmap[j] = 'init'
        # for i in range (len(nums)):
        #     if nums[i]-1 not in hashmap:
        #         cur_length = 1
        #         while (nums[i] + cur_length) in hashmap:
        #             cur_length +=1
        #         longest = max(longest, cur_length)
        # return longest

        'Control from index perspective'

        if not nums: return 0
        longest = 0
        hashmap = {}

        print(hashmap)

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 'init'
        print(hashmap)

        for i in range(len(nums)):
            #找到一个合适的开头，如果nums[i]-1存在于hashmap中，那么这个元素就不能作为序列的起点
            if nums[i]-1 not in hashmap:
                length = 1
                
                while nums[i] + length in hashmap:
                    length += 1
                longest = max(length, longest)
        return longest

if __name__ == '__main__':
    a = Solution()
    n = [100,4,200,1,3,2]
    print(a.longestConsecutive(n))