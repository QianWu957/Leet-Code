class solution:
    def q1(self, nums):
        if not nums:
            return 0

        i = 0
        j = 1
        res = 0
        while i < len(nums) or j < len(nums):
            # print(i, j)
            if i < len(nums) and nums[i] <= 100 and nums[i] >= -100:
                res += nums[i]
            i += 2
            if j< len(nums) and nums[j] <= 100 and nums[j] >= -100:
                res -= nums[j]
            j += 2
        return res

if __name__ == '__main__':
    a = solution()
    nums = [-2,234,-100,-99,5,19,5,7,3,8]
    print(a.q1(nums))