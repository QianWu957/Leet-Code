class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return 0

        dp = [0 for _ in range(len(nums))]
        # dp 表示当前位置有
        # print(dp)

        dp[0] = 0
        for i in range(1,len(nums)-1):
            # print(dp)
            if nums[i+1] + nums[i-1] == 2*(nums[i]):
                dp[i] = dp[i-1] + 1
        print(dp)
        return sum(dp)