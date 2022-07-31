class Solution:
    def nextGreaterElement(self, nums1, nums2) :
        res = []
        stack = []
        hashmap = {}

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                hashmap[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        print(hashmap)

        # while stack:
        #     hashmap[stack.pop()] =-1
        
        for j in range(len(nums1)):
            if nums1[j] in hashmap:
                res.append(hashmap[nums1[j]])
            else:
                res.append(-1)
        return res
        
if __name__ == '__main__':
    a = Solution()
    n1 = [4,1,2]
    n2 = [1,3,4,2]
    print(a.nextGreaterElement(n1,n2))