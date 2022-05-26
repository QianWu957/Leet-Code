class Solution:
    def moveZeroes(self, nums, t):
        slow, fast = 0,0
        while fast < len(nums):
            if nums[slow] != 0:
                slow +=1
            elif nums[fast] !=0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow +=1
            fast+=1
            # print(n)
        print(t)
        t = 5
        return n

if __name__ == '__main__':
    a = Solution()
    n = [0,1,0,3,12]
    nums =[0,0,0,1,2,3,4,5]
    tt = 4
    print(a.moveZeroes(n, tt))
