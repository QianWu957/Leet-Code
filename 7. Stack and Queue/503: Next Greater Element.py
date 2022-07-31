class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        res = []
        nums1 = nums+nums
        res = [-1]* len(nums1)

        for i in range(len(nums1)):
            while stack and stack[-1][0] < nums1[i]:
                res[stack.pop()[1]] =  nums1[i]
            stack.append((nums1[i],i))

        res = res[:len(nums)]
        return res

if __name__ == '__main__':
    a = Solution()
    n = [5,4,3,2,1]
    print(a.nextGreaterElements(n))