class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        counter =0
        res = 0
    
        print(len(nums))
        for i in range(len(nums)):
            if nums[i] == 1:
                counter +=1
                res = max(res,counter)
            else:
                counter = 0
        return res


if __name__ == '__main__':
    a = Solution()
    n = [1,1,0,1,1,1]
    print(a.findMaxConsecutiveOnes(n))