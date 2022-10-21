class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:

        # return any(i + int(str(i)[::-1]) == num for i in range(0, num + 1))
        # n = num // 2
        # for i in range(n,num+1):
        #     temp = int(str(i)[::-1])
        #     if temp + i == num:
        #         return True
        # return False

        # if num == 0:
        #     return True

        for n in range(num//2,num):
            reverse = int((str(n)[::-1]))
            if n + reverse == num:
                return True
            
        return False