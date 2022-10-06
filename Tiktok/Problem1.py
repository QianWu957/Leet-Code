
#選擇題 BCD
#選擇題 n-1

class Solution:
    def boringArray(self, a, b) -> int:
        

        def stringToList(string):
            listRes = [int(x) for x in string.split(' ')]
            # listRes = [int(x) for x in str(listRes)]
            return listRes
        a_list = stringToList(a)
        b_list = stringToList(b)

        print(a_list)
        print(b_list)

        a_list.sort()
        b_list.sort()

        for i in range(len(a_list)):
            if a_list[i] == b_list[i] or a_list[i]+1 == b_list[i]:
                continue
            else:
                return False
        return True
        

        # hashmap = {}

        # for i in range(len(b_list)):
        #     if b_list[i] not in hashmap:
        #         hashmap[b_list[i]] = 1
        #     else:
        #         hashmap[b_list[i]] +=1
        # print(hashmap)

        # for i in range(len(a_list)):
        #     if a_list[i] in hashmap:
        #         del hashmap[a_list[i]]
        # print(hashmap)

        # for i in range(len(a_list)):
        #     if a_list[i] +1 not in hashmap:
        #         return False
        # return True


if __name__ == '__main__':
    i = Solution()
    a = "1 2 3 4 5" 
    b = "1 2 3 4 6"
    print(i.boringArray(a,b))
