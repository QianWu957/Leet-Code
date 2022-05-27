class Solution:
    def removeElement(self, nums, val):
        if not nums: return 0

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow]!= val:
                slow +=1

            elif nums[fast]!= val:
                nums[slow], nums[fast] = nums[fast],nums[slow]
                slow +=1
            fast+=1
        
        return slow

class answer:
    def numbers(self, nums, interger):
        return nums[ 1:]

if __name__== '__main__':
    a = Solution()
    n = [0,1,2,2,3,0,4,2]
    val = 2
    b = answer()
    print(b.numbers(n, 3))