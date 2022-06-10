class Solution:
    def intersection(self, nums1, nums2):
        if not nums1 or not nums2: return []
        res = []
        hashset_1 = set(nums1)
        hashset_2 = set (nums2)

        for i in hashset_1:
            if i in hashset_2:
                res.append(i)
        return res

if __name__ == '__main__':
    a = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(a.intersection(nums1, nums2))


