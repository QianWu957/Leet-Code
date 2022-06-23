class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) :
        N = len(nums1)
        hashmap1 = {}
        hashmap2 = {}
        res = 0
        for num_1 in nums1:
            for num_2 in nums2:
                if (num_1+num_2) not in hashmap1:
                    hashmap1[num_1+num_2] = 0
                hashmap1[num_1+num_2] +=1
                # hashmap1[num_1+num_2] = hashmap1.get(num_1+num_2, 0) + 1
        print(hashmap1)
        
        for num_1 in nums3:
            for num_2 in nums4:
                hashmap2[num_1+num_2] = hashmap2.get(num_1+num_2, 0) + 1
        print(hashmap2)

        for k ,v in hashmap1.items():
            res += hashmap2.get(0-k, 0) * v
        return res


if __name__ == '__main__':
    a = Solution()
    n1 = [1,2]
    n2 = [-2,-1]
    n3 = [-1,2]
    n4= [0,2]
    print (a.fourSumCount(n1,n2,n3,n4))