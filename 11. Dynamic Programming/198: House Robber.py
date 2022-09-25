class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        if len(nums) < 2:
            return nums[0]

        dp = [0]* len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            # dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            dp[i] = nums[i] + max(dp[:i-1])
        
        return max(dp[-1],dp[-2])
        # return max(dp[-1])


