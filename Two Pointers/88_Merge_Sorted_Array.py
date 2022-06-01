class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        ptr1, ptr2, ptrmid = len(nums1)-len(nums2)-1, len(nums2)-1, len(nums1)-1

        while ptr1 >= 0 and ptr2 >= 0:
            print(ptr1, ptr2, nums1[ptr1], nums2[ptr2])
            if nums1[ptr1] < nums2[ptr2]:
                nums1[ptrmid] = nums2[ptr2]
                ptr2 -= 1
                ptrmid -= 1
            else:
                 nums1[ptrmid] = nums1[ptr1]
                 ptr1 -= 1
                 ptrmid -= 1
        if ptr2 >= 0:
                nums1[:ptr2+1] = nums2[:ptr2+1]

if __name__ == '__main__':
    a = Solution()
    n1 = [1,2,3,0,0,0]
    m = 3
    n2 = [2,5,6]
    n = 3
    print(a.merge(n1,m,n2,n))


      