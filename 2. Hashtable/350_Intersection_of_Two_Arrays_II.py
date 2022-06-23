class Solution:
    def intersect(self, nums1, nums2) :
        if not nums1 or not nums2: return []
        hashmap1 = dict.fromkeys(nums1, 0)
        hashmap2 = dict.fromkeys(nums2, 0)

        for num in nums1:
            hashmap1[num] +=1  #在hashmap1中每个元素出现的次数
        print(hashmap1) 

        for num in nums2:
            if hashmap1.get(num) and hashmap1[num]>0:
                hashmap1[num] -= 1
                hashmap2[num] += 1
            #用hash_1中key出现的次数（val），给hash_2每个对应key的出现次数（val）赋值
        # print(hashmap2)
        res = []
        for k, v in hashmap2.items():
            for _ in range(v):
                res.append(k) # List用append, hashtable用add
        return res

if __name__ == '__main__':
    a = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(a.intersect(nums1,nums2))

