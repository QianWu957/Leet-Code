from asyncio import FastChildWatcher
from cgitb import reset


class Solution:
    def checkPossibility(self, nums, k) :
        # counter = 0

        # for i in range(1,len(nums)):
        #     if nums[i] < nums[i-1]:
        #         counter+=1
        #         if i > 1 and i+1< len(nums):
        #             if nums[i-2] > nums[i] and nums[i+1]< nums[i-1]:
        #                 return False

        #     if counter >1:
        #         return False
        
        # return True

        slow, fast = 0, 1
        equal = 0
        res = 0
        tem_sum = nums[slow] + nums[fast]
        while fast < len(nums)-1 and slow < len(nums)-1:
            if nums[slow] > k:
                slow +=1
                fast = slow+1
            elif nums[slow] == k:
                equal +=1
                slow +=1
                fast = slow+1
            while tem_sum < k and fast < len(nums)-1:
                fast+=1
                tem_sum = tem_sum + nums[fast]
            res+=1
            slow = fast
        
        if equal >= 1:
            return res+1
        else:
            return res
    
if __name__ == '__main__':
    a = Solution()
    m = [1,8,3,4,5,6]
    k = 6 
    print(a.checkPossibility(m,k))


             