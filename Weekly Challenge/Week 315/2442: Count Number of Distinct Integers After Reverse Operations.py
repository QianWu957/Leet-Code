class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # return len(set(nums) | set(int(str(x)[::-1]) for x in nums))

        # print(set(int(str(x)[::-1])for x in nums))

        # print(len(set(nums)))

        new_nums = []
        for x in nums:
            new_nums.append(x)
        temp = []
        for i in range(len(nums)):
            reverse = 0
            # print(new_nums)
            while nums[i]:
                digit = nums[i] % 10 
                reverse = reverse * 10 + digit
                nums[i] = nums[i] // 10
            temp.append(reverse)
        for x in temp:
            new_nums.append(x)
      
        return len(set(new_nums))