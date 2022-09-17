class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 0

        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                counter+=1
                if i > 1 and i+1< len(nums):
                    if nums[i-2] > nums[i] and nums[i+1]< nums[i-1]:
                        return False

            if counter >1:
                return False
        
        return True