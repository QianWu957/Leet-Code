class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums: return None
        slow, fast = 0,0

        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow +=1
                nums[slow] = nums[fast]
            fast +=1
        return slow +1

class another:
    def gan(slef,nums,integers):
        


if __name__ == '__main__':
    a = Solution()
    b = another
    array = [1,1,1,1,2,2,2,3,4,5,6,6,6,7,8,8,8,9]
    print(b.gan(a.removeDuplicates(array))