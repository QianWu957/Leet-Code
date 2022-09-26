class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)


        dp = [0] * (len(nums)-1)

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)-1):
            dp[i] = nums[i] + max(dp[:i-1])
        
        res = max(dp[-1],dp[-2])


        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])
        for i in range(2, len(nums)-1):
            dp[i] = nums[i+1] + max(dp[:i-1])
        
        return max(res, dp[-1],dp[-2])
            



        