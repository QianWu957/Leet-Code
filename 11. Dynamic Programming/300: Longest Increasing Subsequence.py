
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return 1
        
        dp = [1] * (len(nums)+1)

        dp[0] = 1

        for i in range(1, len(nums)):
            for j in range (i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)